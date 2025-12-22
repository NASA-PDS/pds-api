Overview
========

The PDS API base urls are provided under the following pattern:

.. code-block::

    https://pds.nasa.gov/api/{service}/{version}/{service_path+params}

where:

- ``{service}``: the service such as ‘search’ (in registry), ‘doi’, etc..
- ``{version}``: the version of the service.
- ``{service_path+params}``: the ReST path for the service, including any query parameters - this is essentially the remaining portion of the URI after the version.

API entries currently available are:

+----------+-----------+-------------------------+----------------+-----------------+
| service  |  version  |  scope                  | specification  | user's guide    |
+==========+===========+=========================+================+=================+
| search   |  1.5      | search PDS data archive | `search_spec`_ | `search_guide`_ |
+----------+-----------+-------------------------+----------------+-----------------+
| doi      |  0.2      | manage PDS DOIs         | `doi_spec`_    |                 |
+----------+-----------+-------------------------+----------------+-----------------+

.. _search_spec: specifications/search-v1.1.0-redoc.html

.. _doi_spec: specifications/doi-v0.2-redoc.html

.. _search_guide: guides/search.html



So for example:

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search-geo/|search_user_guide_api_version|/products?limit=10

intends to obtain 10 product entries from the 1.1 version of the GEO node’s search (registry).




The API specifications design is driven by the :doc:`PDS API general conventions <general-conventions>`
