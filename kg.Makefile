DB = ../../semantic-sql/db

RUN = poetry run

# ontology/%.md:
# 	runoak -i $(DB)/$*.db ontology-metadata --all -O md > $@.tmp && mv $@.tmp $@
