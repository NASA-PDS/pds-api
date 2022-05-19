Overview
========

The PDS API base urls are provided under the following pattern:

.. code-block::

    https://pds.nasa.gov/api/{service}/{version}/{service_path+params}

where:

- ``{service}``: the service such as ‘search’ (i.e. registry), ‘doi’, etc.. This component can have an optional node identifier (e.g. ‘search-geo’). Absence of a node implies EN.
- ``{version}``: the version of the service.
- ``{service_path+params}``: the ReST path for the service, including any query parameters - this is essentially the remaining portion of the URI after the version.

So for example:

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search-geo/|search_user_guide_api_version|/products?limit=10

intends to obtain 10 product entries from the 0.4.2 version of the GEO node’s search (registry).

The API specifications design is driven by the :doc:`PDS API general conventions <general_conventions>`