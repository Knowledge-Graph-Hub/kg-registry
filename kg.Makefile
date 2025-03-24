DB = ../../semantic-sql/db

RUN = poetry run
SCHEMA_DIR = src/kg_registry/kg_registry_schema

# ontology/%.md:
# 	runoak -i $(DB)/$*.db ontology-metadata --all -O md > $@.tmp && mv $@.tmp $@

# Schema building targets

$(SCHEMA_DIR)/datamodel/%.py: $(SCHEMA_DIR)/schema/%.yaml
	$(RUN) gen-pydantic $< > $@

$(SCHEMA_DIR)/%.json: $(SCHEMA_DIR)/schema/%.yaml
	$(RUN) gen-json-schema $< > $@

refresh-schema: clean-schema $(SCHEMA_DIR)/datamodel/kg_registry_schema.py $(SCHEMA_DIR)/kg_registry_schema.json _data/schema.yaml

_data/schema.yaml:
	cp $(SCHEMA_DIR)/schema/kg_registry_schema.yaml _data/schema.yaml