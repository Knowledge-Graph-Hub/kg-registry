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

### Main Tasks
.PHONY: all pull_and_build test pull clean

all: _config.yml registry/kgs.ttl 

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

# reports/principles:
# 	mkdir -p $@


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

# Use SPARQL queries to Wikidata to enrich the
# OBO operations committee metadata file
.PHONY: update-operations-metadata
update-operations-metadata:
	python -m obofoundry update-operations-metadata

### OBO Dashboard

# This is the Jenkins job
# The reports will be archived

dashboard: build/dashboard.zip

# Build directories
build:
	mkdir -p $@
build/resource:
	mkdir -p $@

# reboot the JVM for Py4J
reboot:
	bash ./util/reboot.sh

# This version of ROBOT includes features for starting Py4J
# This will be changed to ROBOT release once feature is released
#.PHONY: build/robot.jar
build/robot.jar: | build
	curl -o $@ -Lk \
	https://build.obolibrary.io/job/ontodev/job/robot/job/py4j/lastSuccessfulBuild/artifact/bin/robot.jar

# This version of ROBOT includes features for removing external axioms to create 'base' artefacts
# This will be removed once this feature is released
#.PHONY: build/robot-foreign.jar
build/robot-foreign.jar: | build
	curl -o $@ -Lk \
	https://build.obolibrary.io/job/ontodev/job/robot/job/562-feature/lastSuccessfulBuild/artifact/bin/robot.jar

# Generate the initial dashboard results file
# ALWAYS make sure nothing is running on port 25333
# Then boot Py4J gateway to ROBOT on that port
# reports/dashboard.csv: registry/kgs.yml | \
# reports/robot reports/principles build/resource build/robot.jar build/robot-foreign.jar
# 	make reboot
# 	./util/principles/dashboard.py $< $@ --big false

# reports/big-dashboard.csv: reports/dashboard.csv
# 	make reboot
# 	./util/principles/dashboard.py registry/kgs.yml $@ --big true

# # Combine the dashboard files
# reports/dashboard-full.csv: reports/dashboard.csv reports/big-dashboard.csv registry/kgs.yml
# 	./util/principles/sort_tables.py $^ $@

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

# output of central OBO build
# See FAQ for more details, and also README.md
jenkins-output.txt:
	wget http://build.berkeleybop.org/job/simple-build-obo-all/lastBuild/consoleFull -O $@

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

include kg.Makefile
