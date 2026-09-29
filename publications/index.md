---
title: Publications
nav:
  order: 2
  tooltip: Papers, chapters, and proceedings
---

# {% include icon.html icon="fa-solid fa-scroll" %}Publications

Journal articles, book chapters, and conference proceedings from the lab, with PDFs where available. See also our [technical reports]({{ "publications/tech-reports" | relative_url }}) and [conference presentations]({{ "publications/presentations" | relative_url }}).

**DISCLAIMER**

<sub><sup> *The electronic documents here are posted to improve dissemination of scholarly and technical work on a noncommercial basis. Copyright and all rights therein are maintained by the authors or by other copyright holders, notwithstanding that their works are posted here electronically. It is understood that all persons downloading this information will adhere to the terms and constraints invoked by each item's copyright. These works may not be reposted without the explicit permission of the copyright holder.* </sup></sub>

{% include section.html %}

{% include search-box.html %}

{% include search-info.html %}

## Journal articles and chapters

{% include list.html data="citations" component="citation" filters="type: ^(article|chapter)$" %}

{% include section.html %}

## Conference proceedings

{% include list.html data="citations" component="citation" filters="type: ^proceedings$" %}
