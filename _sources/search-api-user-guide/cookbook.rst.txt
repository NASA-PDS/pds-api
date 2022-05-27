Search API Cookbook
+++++++++++++++++++

Recipes for various search scenarios using the PDS Search API.

Search For Product Versions
===========================

Recipes for searching for the latest version of a product, or all versions of a product, including superseded versions.

.. Warning::
   Since our servers are not fully populated with all PDS data sets, the examples presented in this user guide may return empty results or 404 (Not Found) errors. If there is a data set you would like added, please contact the `PDS Help Desk <mailto:pds-operator@jpl.nasa.gov>`_ for assistance.


Search the Latest Version of a Product
--------------------------------------

To retrieve the **latest** versions of product ``urn:nasa:pds:mars2020.spice``, the request is:

The request:

.. code-block:: bash
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:mars2020.spice

which is equivalent to:

.. code-block:: bash
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:mars2020.spice/latest


Search for All Versions of a Product
------------------------------------

To retrieve **all** the versions of product ``urn:nasa:pds:mars2020.spice``, the request is:

.. code-block:: bash
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:mars2020.spice/all

----

Search By Specific Metadata
===========================

The following recipes describe some example queries of the Search API using the `q=` query parameter showing some more complex use cases for querying PDS data.

.. Warning::
   Since our servers are not fully populated with all PDS data sets, the examples presented in this user guide may return empty results or 404 (Not Found) errors. If there is a data set you would like added, please contact the `PDS Help Desk <mailto:pds-operator@jpl.nasa.gov>`_ for assistance.


Search by Processing Level
--------------------------

Search for the 10 latest collections which processing level is "Raw":

**Query:** ``(pds:Primary_Result_Summary.pds:processing_level eq "Raw")``

.. code-block:: bash
   :caption: curl command
   :substitutions:

   curl --location --request GET 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/collections?limit=10&q=(pds:Primary_Result_Summary.pds:processing_level eq "Raw")'


Search by Target
----------------

Search for all Observational Products targeting Bennu:

**Query:** ``(ref_lid_target eq "urn:nasa:pds:context:target:asteroid.101955_bennu")``

.. code-block:: bash
   :caption: curl command
   :substitutions:

   curl --location --request GET 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/collections?q=(ref_lid_target eq "urn:nasa:pds:context:target:asteroid.101955_bennu")'

----

Search for DOIs
===============

`Digital Object Identifiers <https://www.doi.org/>`_ are useful to cite the data you are using in your research. DOIs for PDS data are minted for PDS4 Bundles, PDS4 Collections, PDS4 Documents, and PDS3 Data Sets. The level at which the DOI is minted differs from data set to data set.

The following recipes describe how to find a DOI for a particular product or data set in the Search API metadata.

See the [DOI Search](https://pds.nasa.gov/tools/doi/) for an online interface for searching this information.

See the documentation on `Citing PDS Data <https://pds.nasa.gov/datastandards/citing/>`_ for more information on how to use a DOI to cite your data.

.. Warning::
   Since our servers are not fully populated with all PDS data sets, the examples presented in this user guide may return empty results or 404 (Not Found) errors. If there is a data set you would like added, please contact the `PDS Help Desk <mailto:pds-operator@jpl.nasa.gov>`_ for assistance.


How to Find the DOI associated with an Observational Product
------------------------------------------------------------

We assume you know the identifier of the product you are working with. In our example it is: ``urn:nasa:pds:insight_rad:data_derived:hp3_rad_der_00014_20181211_073042::1.0``


Search for a Products Collection DOI
************************************

Run the following request to get the DOI associated with the product's collection:

.. code-block:: bash
    :substitutions:

    curl --location --request GET 'http://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight_rad:data_derived:hp3_rad_der_00014_20181211_073042::1.0/collections?fields=ops:Identifiers/ops:doi' --header 'Accept: application/kvp+json'

.. _DOI request result:

You will get the following result:

.. code-block:: json

    {
        "summary": {
            "q": "",
            "hits": 1,
            "took": 172,
            "start": 0,
            "limit": 100,
            "sort": [],
            "properties": []
        },
        "data": [
            {
               "ops:Identifiers/ops:doi": "10.17189/1517568"
            }
        ]
    }

Note that you might not find any DOI at the collection level, in this case you can try to get the DOI from the bundle.

Search for a Product's Bundle DOI
*********************************

To get the DOI associated with the bundle the observational product `urn:nasa:pds:insight_rad:data_derived:hp3_rad_der_00014_20181211_073042::1.0` belongs to:

.. code-block:: bash
    :substitutions:

    curl --location --request GET 'http://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight_rad:data_derived:hp3_rad_der_00014_20181211_073042::1.0/bundles?fields=pds:Citation_Information/pds:doi&fields=ops:Identifiers/ops:doi' --header 'Accept: application/kvp+json'


You will get the same response as for a :ref:`collection request <Search for a Product's Collection DOI>`


How to Find the PDS Product Associated with a DOI
-------------------------------------------------

To get the PDS product metadata associated with a the DOI `10.17189/1517568`:

.. code-block:: bash
    :substitutions:

    curl --location --request GET 'http://pds.nasa.gov/api/search/|search_user_guide_api_version|/products?q=(ops:Identifiers/ops:doi eq "10.17189/1517568")' --header 'Accept: application/json'

You will get a JSON response of the PDS products (any class of product, for example collections or bundles) which have referenced the given DOI.

You can get the result in different format using content negociation with the Accept header parameter.


**Looking for more recipes? Or have some useful recipes of your own? Checkout the `PDS API Discussion Board <https://github.com/NASA-PDS/pds-api/discussions>`_ or contact the `PDS Help Desk <mailto:pds-operator@jpl.nasa.gov>`_**
