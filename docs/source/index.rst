Overview
========

PDS is willing to develop restful web APIs for different applications (so far, registry, dois).

The PDS API base urls are provided under the following pattern:

    https://pds.nasa.gov/api/<application>/<version>

For example: https://pds.nasa.gov/api/doi/0.2/


Specifications:
===============

Each published version of NASA PDS APIs is documented here:

.. toctree::
   :maxdepth: 1

   specifications/registry-v1.0.0-SNAPSHOT
   specifications/doi-v0.2

API implementations
===================

Registry
--------

- Server: https://github.com/NASA-PDS/registry-api
- Client: https://github.com/NASA-PDS/pds-api-client

DOI
---

- Server: https://github.com/NASA-PDS/doi-service/
- Client (UI): https://github.com/NASA-PDS/doi-ui/
- Client (react component): to be completed


Support:
========

.. toctree::
   :maxdepth: 1

   support/contact.rst
   support/contribute.rst





