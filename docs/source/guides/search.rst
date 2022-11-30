Search API User Guide
=====================

.. note::

   The current guide is based on the PDS Search API version |search_user_guide_api_version|

.. Warning::
   Since our servers are not fully populated with all PDS data sets, the examples presented in this user guide may return empty results or 404 (Not Found) errors. If there is a data set you would like added, please contact the `PDS Help Desk <mailto:pds-operator@jpl.nasa.gov>`_ for assistance.


The PDS Search API provides endpoints:

* to **search** for bundles, collections and any PDS products with advanced search queries.
* to **browse** the archive hierarchically downward (e.g. collection's products) or upward (e.g. bundles containing products),
* to **resolve** an identifier (lid or lidvid) and retrieve the product label and data where ever it is in the Planetary Data System.

These pages provide a user guide for the PDS Search API.

.. toctree::
   :maxdepth: 3

   search/quickstart
   search/endpoints
   search/responses
   search/tutorials
   API Full Reference <https://nasa-pds.github.io/pds-api/specifications/search-v1.1.0-redoc.html>
