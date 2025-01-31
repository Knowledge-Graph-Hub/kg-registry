DB = ../../semantic-sql/db

DYNAMIC = neo reacto sgd swisslipid uniprot hgnc drugbank ecosim drugcentral

RUN = poetry run
SCHEMA_DIR = src/kg_registry/kg_registry_schema
all: $(patsubst %,resource/%.md,$(DYNAMIC))

ontology/%.md:
	runoak -i $(DB)/$*.db ontology-metadata --all -O md > $@.tmp && mv $@.tmp $@

# Schema building targets

$(SCHEMA_DIR)/datamodel/%.py: $(SCHEMA_DIR)/schema/%.yaml
	$(RUN) gen-pydantic $< > $@

$(SCHEMA_DIR)/%.json: $(SCHEMA_DIR)/schema/%.yaml
	$(RUN) gen-json-schema $< > $@

refresh-schema: clean-schema $(SCHEMA_DIR)/datamodel/kg_registry_schema.py $(SCHEMA_DIR)/kg_registry_schema.json