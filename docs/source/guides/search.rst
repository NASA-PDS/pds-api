Search API User Guide
=====================

.. attention::
   The PDS Search API (https://pds.nasa.gov/api/search/) will be down will be down for maintenance for 2-3 weeks beginning May 6, 2024 at 8am Pacific Time. Limited functionality will be released as it becomes available. Apologies for the inconvenience. Please contact the PDS Help Desk if you have any questions.

.. note::

   The current guide is based on the PDS Search API version |search_user_guide_api_spec_version|

.. Warning::
   Since our servers are not fully populated with all PDS data sets, the examples presented in this user guide may return empty results or 404 (Not Found) errors. If there is a data set you would like added, please contact the `PDS Help Desk <mailto:pds-operator@jpl.nasa.gov>`_ for assistance.


The PDS Search API provides endpoints:

* to **search** for bundles, collections and any PDS products with advanced search queries.
* to **browse** the archive hierarchically downward (e.g. collection's products) or upward (e.g. bundles containing products),
* to **resolve** an identifier (lid or lidvid) and retrieve the product label and data where ever it is in the Planetary Data System.

For an introduction to the Search API and what it's capable of, checkout these slides and a presentation given at the 2022 PSIDA conference:
* Slides: https://www.cosmos.esa.int/documents/6109777/9316710/X03+-+Padams+-+NASA_Planetary_Data_System_Search_API.pdf
* Presentation Recording: https://www.cosmos.esa.int/web/psida-2022/-/x03

These pages provide a user guide for the PDS Search API.

.. toctree::
   :maxdepth: 3

   search/quickstart
   search/endpoints
   search/responses
   search/tutorials
   API Full Reference <https://nasa-pds.github.io/pds-api/specifications/search-v1.1.0-redoc.html>
   Links <search/links>
