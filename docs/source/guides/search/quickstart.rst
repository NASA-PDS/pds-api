Quickstart
==========

The following section provides a quickstart guide to try out the PDS Search API.

.. Warning::
   Since our servers are not fully populated with all PDS data sets, the examples presented in this user guide may return empty results or 404 (Not Found) errors. If there is a data set you would like added, please contact the `PDS Help Desk <mailto:pds-operator@jpl.nasa.gov>`_ for assistance.

Prerequisites
-------------

- curl command line tool (curl is available in many operating systems by default. If not, you can get curl from https://curl.se/ or using a package management tool specific to your operating system).


Search With curl
----------------

1. Open a Terminal window (or your favorite command-line application).


2. Get 5 products' metadata from the API in JSON format:

.. code-block:: bash
   :substitutions:

    curl --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products?limit=5' \
        --header 'Accept: application/json'

3. Get 5 products' metadata from the API in XML format:

.. code-block:: bash
   :substitutions:

    curl --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products?limit=5' \
        --header 'Accept: application/xml'


4. To view this in a more readable way, you can pipe the output to a file, or pretty print (on Mac/Unix):

.. code-block:: bash
   
   # Output JSON to a File
   curl ... > my_first_query.json

   # Pretty print JSON
   curl ... | json_pp > my_first_query.json

   # Output XML to a File
   curl ... > my_first_query.xml


More details on how to use the API can be found in the :doc:`endpoints<./endpoints>` .


Search with Python
------------------

Alternatively, it is possible to use other tools such as Postman and programming languages such as Python to call the PDS Search API.

To use the **PDS API Python Client**, you can read this other `Quickstart <https://nasa-pds.github.io/pds-api-client/quickstart>`_

