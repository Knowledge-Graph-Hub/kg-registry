DB = ../../semantic-sql/db

DYNAMIC = neo reacto sgd swisslipid uniprot hgnc drugbank ecosim drugcentral

all: $(patsubst %,ontology/%.md,$(DYNAMIC))

ontology/%.md:
	runoak -i $(DB)/$*.db ontology-metadata --all -O md > $@.tmp && mv $@.tmp $@
