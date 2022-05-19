Quickstart
==========

The following section provides a quickstart guide to try out the PDS Search API.

Prerequisites
-------------

- curl command line tool (curl is available in many operating systems by default. If not, you can get curl from https://curl.se/ or using a package management tool specific to your operating system).


Call the PDS Search API with curl
------------------------------------------

1. Open a terminal.


2. Get 5 products description from the API:

.. code-block:: bash
   :substitutions:

    curl -X GET --header 'Accept: application/json' 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products?limit=5'

More details on how to use the API can be found in the :doc:`endpoints<./endpoints>` .

Quickstart Guide to Call the PDS Search API with Python
-------------------------------------------------------

Alternatively, it is possible to use other tools such as Postman and programming languages such as Python to call the
PDS Search API.

To use the **PDS API Python Client**, you can read this other `quickstart <https://nasa-pds.github.io/pds-api-client/quickstart>`_

