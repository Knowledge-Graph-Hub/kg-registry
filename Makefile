# Makefile for KG-Registry site
#
# This file contains commands for validating and generating
# configuration files for the KG-Registry website.
# The `util/` directory contains additional scripts
# called from this Makefile.
# It is intended to be run on a Unix system (Linux, Mac OS X)
# **before** the site is built using
# [Jekyll](http://jekyllrb.com).
#
# Software requirements:
#
# - [GNU Make](http://www.gnu.org/software/make/)
# - [Apache Jena](https://jena.apache.org/download/)
# - [Python 3](https://www.python.org/downloads/)
# - [PyYAML](http://pyyaml.org/wiki/PyYAML)
# - [SPARQLWrapper](https://pypi.python.org/pypi/SPARQLWrapper)
#
# Run `make` in this directory to update all generated files
# (i.e. the default `all` task).
# Make does its best to detect changes and run only the required tasks,
# but sometimes it helps to delete the target files first by running `make clean`
#
# WARNING: Makefiles contain significant tab characters!
# Before editing this file, ensure that your editor is not set up to convert tabs
# to spaces, and then use tabs to indent recipe lines.


### Configuration

RUN = poetry run

# All resource .md files
# Note this includes pages for individual products, too
# Those are used to build their own pages but are not included in
# the main registry table
RESOURCES := $(shell find resource -type f -name '*.md')

# Path to the source KG-Registry schema
SOURCE_SCHEMA = src/kg_registry/kg_registry_schema/schema/kg_registry_schema.yaml

# Path to the generated KG-Registry schema docs
SCHEMA_DOC_DIR = docs/schema

# Path to the generated KG-Registry schema directory
SCHEMA_DIR = src/kg_registry/kg_registry_schema

### Main Tasks
.PHONY: all pull_and_build test pull clean

all: _config.yml registry/kgs.ttl refresh-schema

# This is minimal for now, but
# will be expanded to include other docs
# requiring dynamic updates
docs: schema-docs

pull:
	git pull

pull_and_build: pull all

test: reports/metadata-grid.html _config.yml tox

integration-test: test valid-purl-report.txt

# Remove and/or revert all targets to their repository versions
clean:
	rm -Rf registry/kgs.nt registry/kgs.ttl registry/kgs.yml sparql-consistency-report.txt jenkins-output.txt valid-purl-report.txt valid-purl-report.txt.tmp _site/ tmp/ reports/
	git checkout _config.yml registry/kgs.jsonld registry/kgs.ttl registry/kgs.yml

clean-schema:
	rm -Rf src/kg_registry/kg_registry_schema/datamodel/*.py src/kg_registry/kg_registry_schema/*.json

### Directories:

tmp:
	mkdir -p $@

reports:
	mkdir -p $@

reports/robot:
	mkdir -p $@

### Build Configuration Files

# Create the site-wide config file by combining all metadata on resources
#  and combining with site-wide metadata.
#
# Note that anything in _config.yml is accessible to any liquid template via the
# `sites` object - think of it like the global database
#
# (this is somewhat hacky, but concatenating these yamls is safe)
_config.yml: _config_header.yml registry/kgs.yml
	cat $^ > $@.tmp && mv $@.tmp $@

# Sort resources based on the validation (metadata-grid)
registry/kgs.yml: reports/metadata-grid.csv
	./util/sort-resources.py tmp/unsorted-resources.yml $< $@ && rm -rf tmp

# Use a generic yaml->json conversion, but adding a @content
registry/kgs.jsonld: registry/kgs.yml
	./util/yaml2json.py $< > $@.tmp && mv $@.tmp $@

# Use Apache-Jena RIOT to convert jsonld to n-triples
# NOTE: UGLY HACK. If there is a problem then Jena will write WARN message (to stdout!!!), there appears to
#  be no way to get it to flag this even with strict and check options, so we do a check with grep, ugh.
# see: http://stackoverflow.com/questions/20860222/why-do-i-have-these-warnings-with-jena-2-11-0
registry/kgs.nt: registry/kgs.jsonld
	riot --base=http://purl.obolibrary.org/obo/ --strict --check -q registry/context.jsonld $< > $@.tmp && mv $@.tmp $@ && egrep '(WARN|ERROR)' $@ && exit 1 || echo ok

registry/kgs.ttl: registry/kgs.nt
	riot --base=http://purl.obolibrary.org/obo/ --out=ttl $< > $@.tmp && mv $@.tmp $@

### Validate Configuration Files

# generate both a report of the violations and a grid of all results
# the grid is later used to sort the resources on the home page
RESULTS = reports/metadata-violations.tsv reports/metadata-grid.csv
reports/metadata-grid.csv: tmp/unsorted-resources.yml | extract-metadata reports
	./util/validate-metadata.py $< $(RESULTS)

# generate an HTML output of the metadata grid
# TODO: determine where this output belongs
reports/metadata-grid.html: reports/metadata-grid.csv
	./util/create-html-grid.py $< $@

# Extract metadata from each resource .md file and combine into single yaml
# Also create product pages where needed
# and propagate product entries to related resources
tmp/unsorted-resources.yml: $(RESOURCES) | tmp
	./util/extract-metadata.py concat -o $@.tmp $^  && mv $@.tmp $@

# Run validation, including with LinkML validator
extract-metadata: $(RESOURCES)
	./util/extract-metadata.py validate $^

prettify: $(RESOURCES)
	./util/extract-metadata.py prettify $^

# Run tox tests (requires `pip install tox`)
tox:
	tox -e py

##########################
## Metadata Maintenance ##
##########################

# Build directories
build:
	mkdir -p $@
build/resource:
	mkdir -p $@

# Generate the HTML grid output for dashboard
reports/dashboard.html: reports/dashboard-full.csv
	./util/create-html-grid.py $< $@

# Move all important results to a dashboard directory
build/dashboard: reports/dashboard.html
	mkdir -p $@
	mkdir -p $@/assets
	mkdir -p $@/reports
	cp $< $@
	cp -r reports/robot $@/reports
	cp -r assets/svg $@/assets
	rm -rf build/dashboard.zip
	zip -r $@.zip $@

# Clean up, removing files
# We don't want to keep them because we will download new ones each time to stay up-to-date
# Reports are all archived in build/dashboard.zip
clean-dashboard: build/dashboard
	rm -rf build/resource
	rm -rf reports/robot
	rm -rf build/dashboard

# Note this should *not* be run as part of general travis jobs, it is expensive
# and may be prone to false positives as it is inherently network-based
valid-purl-report.txt: registry/kgs.yml
	./util/processor.py -i $< check-urls > $@.tmp && mv $@.tmp $@

sparql-consistency-report.txt: registry/kgs.yml
	./util/processor.py -i $< sparql-compare > $@.tmp && mv $@.tmp $@

reports/%.csv: registry/kgs.ttl sparql/%.sparql
	arq --data $< --query sparql/$*.sparql --results csv > $@.tmp && mv $@.tmp $@

# Generate schema documentation
# and add the frontmatter to each page
schema-docs:
	$(RUN) gen-doc -d $(SCHEMA_DOC_DIR) $(SOURCE_SCHEMA)
	for file in $(SCHEMA_DOC_DIR)/*; do \
		sed -i 's/\.md)/\.html)/g' $$file; \
		sed -i 's/href "..\/\([^"]*\)"/href "\1.html"/g' $$file; \
		echo "---\nlayout: schema_doc\nmermaid: true\n---\n\n$$(cat $$file)" > $$file; \
	done

# Generate the schema files
refresh-schema: clean-schema $(SCHEMA_DIR)/datamodel/kg_registry_schema.py $(SCHEMA_DIR)/kg_registry_schema.json
	cp $(SCHEMA_DIR)/schema/kg_registry_schema.yaml _data/schema.yaml

$(SCHEMA_DIR)/datamodel/%.py: $(SCHEMA_DIR)/schema/%.yaml
	$(RUN) gen-pydantic $< > $@

$(SCHEMA_DIR)/%.json: $(SCHEMA_DIR)/schema/%.yaml
	$(RUN) gen-json-schema $< > $@

include kg.Makefile
