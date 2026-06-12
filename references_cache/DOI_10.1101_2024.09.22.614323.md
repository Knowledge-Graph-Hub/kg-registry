---
reference_id: DOI:10.1101/2024.09.22.614323
title: Building a literature knowledge base towards transparent biomedical AI
authors:
- Yuanhao Huang
- Zhaowei Han
- Xin Luo
- Xuteng Luo
- Yijia Gao
- Meiqi Zhao
- Feitong Tang
- Yiqun Wang
- Jiyu Chen
- Chengfan Li
- Xinyu Lu
- Tiancheng Jiao
- Jiahao Qiu
- Feiyang Deng
- Lingxiao Guan
- Haohong Shang
- Fan Feng
- Thi Hong Ha Vu
- Thomas Bate
- Dongxiang Xue
- Jean-Philippe Cartailler
- Michael Stitzel
- Shuibing Chen
- Marcela Brissova
- Stephen Parker
- Jie Liu
year: '2024'
doi: 10.1101/2024.09.22.614323
content_type: abstract_only
---

# Building a literature knowledge base towards transparent biomedical AI
**Authors:** Yuanhao Huang, Zhaowei Han, Xin Luo, Xuteng Luo, Yijia Gao, Meiqi Zhao, Feitong Tang, Yiqun Wang, Jiyu Chen, Chengfan Li, Xinyu Lu, Tiancheng Jiao, Jiahao Qiu, Feiyang Deng, Lingxiao Guan, Haohong Shang, Fan Feng, Thi Hong Ha Vu, Thomas Bate, Dongxiang Xue, Jean-Philippe Cartailler, Michael Stitzel, Shuibing Chen, Marcela Brissova, Stephen Parker, Jie Liu
**DOI:** [10.1101/2024.09.22.614323](https://doi.org/10.1101/2024.09.22.614323)

## Content

Abstract
As artificial intelligence (AI) continues to advance and scale up in biomedical research, concerns about AI’s trustworthiness and transparency have grown. There is a critical need to systematically bring accurate and relevant biomedical knowledge into AI applications for transparency and provenance. Knowledge graphs have emerged as a powerful tool that integrates heterogeneous knowledge by explicitly describing biomedical knowledge as entities and relationships between entities. However, PubMed, the largest and most comprehensive repository of biomedical knowledge, exists primarily as unstructured text and is under utilized for advanced machine learning tasks. To address the challenge, we developed LiteralGraph, a computational framework to extract biomedical terms and relationships from PubMed literature into a unified knowledge graph. Using this framework, we established the Genomic Literature Knowledge Base (GLKB), which consolidates 14,634,427 biomedical relationships between 3,276,336 biomedical terms from over 33 million PubMed abstracts and nine well-established biomedical repositories. The database is coupled with RESTful APIs and a user-friendly web interface that makes it accessible to researchers for various usages. We demonstrated the broad utility of GLKB towards transparent AI in three distinct application scenarios. In the LLM grounding scenario, we developed a Retrieval Augmented Generation (RAG) agent to reduce LLM hallucination in biomedical question answering. In the hypothesis generation scenario, we elucidated the potential functions of RFX6 in type 2 diabetes (T2D) using the vast evidence from PubMed articles. In the machine learning scenario, we utilized GLKB to provide semantic knowledge in predictive tasks and scientific fact-checking.