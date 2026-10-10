---
reference_id: DOI:10.1093/bioinformatics/btae560
title: Biomedical knowledge graph-optimized prompt generation for large language models
authors:
- Karthik Soman
- Peter W Rose
- John H Morris
- Rabia E Akbas
- Brett Smith
- Braian Peetoom
- Catalina Villouta-Reyes
- Gabriel Cerono
- Yongmei Shi
- Angela Rizk-Jackson
- Sharat Israni
- Charlotte A Nelson
- Sui Huang
- Sergio E Baranzini
journal: Bioinformatics
year: '2024'
doi: 10.1093/bioinformatics/btae560
content_type: abstract_only
---

# Biomedical knowledge graph-optimized prompt generation for large language models
**Authors:** Karthik Soman, Peter W Rose, John H Morris, Rabia E Akbas, Brett Smith, Braian Peetoom, Catalina Villouta-Reyes, Gabriel Cerono, Yongmei Shi, Angela Rizk-Jackson, Sharat Israni, Charlotte A Nelson, Sui Huang, Sergio E Baranzini
**Journal:** Bioinformatics (2024)
**DOI:** [10.1093/bioinformatics/btae560](https://doi.org/10.1093/bioinformatics/btae560)

## Content

Abstract

Motivation
Large language models (LLMs) are being adopted at an unprecedented rate, yet still face challenges in knowledge-intensive domains such as biomedicine. Solutions such as pretraining and domain-specific fine-tuning add substantial computational overhead, requiring further domain-expertise. Here, we introduce a token-optimized and robust Knowledge Graph-based Retrieval Augmented Generation (KG-RAG) framework by leveraging a massive biomedical KG (SPOKE) with LLMs such as Llama-2-13b, GPT-3.5-Turbo, and GPT-4, to generate meaningful biomedical text rooted in established knowledge.


Results
Compared to the existing RAG technique for Knowledge Graphs, the proposed method utilizes minimal graph schema for context extraction and uses embedding methods for context pruning. This optimization in context extraction results in more than 50% reduction in token consumption without compromising the accuracy, making a cost-effective and robust RAG implementation on proprietary LLMs. KG-RAG consistently enhanced the performance of LLMs across diverse biomedical prompts by generating responses rooted in established knowledge, accompanied by accurate provenance and statistical evidence (if available) to substantiate the claims. Further benchmarking on human curated datasets, such as biomedical true/false and multiple-choice questions (MCQ), showed a remarkable 71% boost in the performance of the Llama-2 model on the challenging MCQ dataset, demonstrating the framework’s capacity to empower open-source models with fewer parameters for domain-specific questions. Furthermore, KG-RAG enhanced the performance of proprietary GPT models, such as GPT-3.5 and GPT-4. In summary, the proposed framework combines explicit and implicit knowledge of KG and LLM in a token optimized fashion, thus enhancing the adaptability of general-purpose LLMs to tackle domain-specific questions in a cost-effective fashion.


Availability and implementation
SPOKE KG can be accessed at https://spoke.rbvi.ucsf.edu/neighborhood.html. It can also be accessed using REST-API (https://spoke.rbvi.ucsf.edu/swagger/). KG-RAG code is made available at https://github.com/BaranziniLab/KG_RAG. Biomedical benchmark datasets used in this study are made available to the research community in the same GitHub repository.