---
activity_status: active
category: DataSource
description: MEDLINE is the National Library of Medicine's premier bibliographic database containing more than 31 million references to journal articles in life sciences with a concentration on biomedicine. A primary component of PubMed, MEDLINE provides indexed citations with Medical Subject Headings (MeSH).
domains:
  - biomedical
  - literature
  - health
homepage_url: https://www.nlm.nih.gov/medline/medline_home.html
id: medline
layout: resource_detail
name: MEDLINE
contacts:
  - category: Organization
    contact_details:
      - contact_type: url
        value: https://www.nlm.nih.gov/
    label: National Library of Medicine
products:
  - category: GraphicalInterface
    description: PubMed web interface providing free access to MEDLINE and other biomedical literature databases
    format: http
    id: medline.pubmed
    name: PubMed
    original_source:
      - medline
    product_url: https://pubmed.ncbi.nlm.nih.gov/
  - category: ProgrammingInterface
    description: Entrez Programming Utilities (E-utilities) API providing programmatic access to PubMed/MEDLINE data
    format: http
    id: medline.eutils
    name: E-utilities API
    original_source:
      - medline
    product_url: https://www.ncbi.nlm.nih.gov/books/NBK25501/
  - category: Product
    description: Annual baseline set of PubMed/MEDLINE citation records in XML format, complete snapshot of database
    format: xml
    id: medline.baseline
    name: Annual Baseline Files
    original_source:
      - medline
    product_url: https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/
  - category: Product
    description: Daily update files with new, revised, and deleted citations in XML format
    format: xml
    id: medline.updates
    name: Daily Update Files
    original_source:
      - medline
    product_url: https://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/
  - category: DocumentationProduct
    description: PubMed DTD documentation with annotations and examples for all XML elements and attributes
    format: http
    id: medline.dtd
    name: PubMed DTD Documentation
    original_source:
      - medline
    product_url: https://dtd.nlm.nih.gov/ncbi/pubmed/doc/out/250101/index.html
synonyms:
  - PubMed
  - MEDLARS
---

# MEDLINE

## Overview

MEDLINE (MEDical Literature Analysis and Retrieval System Online) is the National Library of Medicine's (NLM) premier bibliographic database containing more than 31 million references to journal articles in life sciences, with a concentration on biomedicine. Originally launched as MEDLARS in 1964, MEDLINE is the online counterpart that has become the world's most comprehensive source of life sciences and biomedical bibliographic information.

MEDLINE is a primary component of PubMed, the free literature database developed and maintained by the NLM National Center for Biotechnology Information (NCBI). A distinctive feature of MEDLINE is that records are indexed with NLM Medical Subject Headings (MeSH), a controlled vocabulary for precise searching.

## Data Content

**Coverage**:
- **Citations**: More than 31 million journal article references
- **Time Range**: 1966 to present (with selected pre-1966 coverage via OLDMEDLINE)
- **Journals**: Citations from more than 5,200 worldwide journals
- **Languages**: Approximately 40 languages represented
- **Updates**: New citations added 7 days a week

**Subject Scope**:
- Biomedicine and health (broadly defined)
- Life sciences relevant to health professionals
- Behavioral sciences
- Chemical sciences
- Bioengineering
- Biology, environmental science, marine biology
- Plant and animal science
- Biophysics and chemistry

**Publication Types**:
- Scholarly journals (majority)
- Selected newspapers, magazines, and newsletters
- Most citations include abstracts

## Key Features

- **MeSH Indexing**: All MEDLINE records indexed with Medical Subject Headings
- **Free Access**: No charge or registration required via PubMed
- **Full-Text Links**: Growing number of citations link to free full-text in PubMed Central
- **Publisher Links**: Direct links to journal websites (access depends on publisher requirements)
- **Comprehensive Search**: Advanced search capabilities including clinical queries
- **Quality Selection**: Journals selected through rigorous Literature Selection Technical Review Committee (LSTRC) process

## Access Methods

### Web Interface (PubMed)
- **URL**: https://pubmed.ncbi.nlm.nih.gov/
- **Features**: Basic and advanced search, clinical queries, citation matching
- **Search Tools**: MeSH database integration, search history, email alerts
- **No Cost**: Free access without registration

### Programmatic Access (E-utilities API)
- **Documentation**: https://www.ncbi.nlm.nih.gov/books/NBK25501/
- **Features**: Eight server-side programs for querying Entrez databases
- **Usage**: Quick Start and In-Depth guides available
- **Requirements**: Follow usage guidelines and rate limits

### Data Downloads (FTP)
- **Annual Baseline**: Complete snapshot released once per year
- **Daily Updates**: New, revised, and deleted citations
- **Format**: XML conforming to PubMed DTD
- **Access**: https://ftp.ncbi.nlm.nih.gov/pubmed/
- **License**: Terms and conditions in README.txt

## Data Format

- **Primary Format**: XML (PubMed DTD)
- **DTD Version**: Current version 250101 (January 2025)
- **Documentation**: Complete element and attribute annotations available
- **Download Mode**: Binary mode required for FTP downloads

## Use Cases

1. **Literature Review**: Comprehensive searches for biomedical research
2. **Clinical Decision Support**: Evidence-based medicine queries
3. **Systematic Reviews**: Large-scale evidence synthesis
4. **Text Mining**: Natural language processing of biomedical literature
5. **Database Integration**: Local database creation using baseline and updates
6. **Research Metrics**: Bibliometric and scientometric analyses
7. **Education**: Teaching and learning biomedical information retrieval

## Journal Selection

**Process**: Managed by Literature Selection Technical Review Committee (LSTRC)
- Rigorous review process described at: https://www.nlm.nih.gov/medline/medline_how_to_include.html
- Selection based on scope, quality, editorial standards
- Regular statistics published on newly accepted journals

## Management

**Organization**: National Library of Medicine (NLM)
- Part of National Institutes of Health (NIH)
- U.S. Department of Health and Human Services (HHS)

**Location**: 8600 Rockville Pike, Bethesda, MD 20894

**Technical Maintenance**: National Center for Biotechnology Information (NCBI)

## Related Resources

- **PubMed Central (PMC)**: Free full-text archive
- **MeSH**: Medical Subject Headings controlled vocabulary
- **Bookshelf**: Collection of biomedical books and documents
- **NLM Catalog**: Journal and book catalog

## Updates and Announcements

Subscribe to the utilities-announce listserv for:
- Annual baseline release notifications
- Significant updates and changes
- Technical announcements

## Terms of Use

- **Downloading Data**: Indicates acceptance of terms in README.txt
- **Attribution**: PubMed wordmark and logo are registered trademarks
- **Restrictions**: See FTP README for complete terms and conditions

## Historical Note

MEDLINE evolved from MEDLARS (MEDical Literature Analysis and Retrieval System), which originated in 1964. The transition to online access as MEDLINE revolutionized biomedical literature searching and continues to be the gold standard for life sciences bibliography.

## Support

- **Help**: https://support.nlm.nih.gov/
- **FAQ**: https://pubmed.ncbi.nlm.nih.gov/help/
- **User Guide**: Comprehensive guides and tutorials available
- **Contact**: Via NLM Support Center