
Search API Cookbook
+++++++++++++++++++

Recipes for various search scenarios using the PDS Search API.

.. Note::
   curl command line tool is used to request the API in this documentation. curl is available in many operating systems by default. If not, you can get curl from https://curl.se/ or using a package management tool specific to your operating system (brew, apt, ...).

Search For Product Versions
===========================

Recipes for searching for the latest version of a product, or all versions of a product, including superseded versions.

.. Warning::
   Since our servers are not fully populated with all PDS data sets, the examples presented in this user guide may return empty results or 404 (Not Found) errors. If there is a data set you would like added, please submit a request to the `PDS Help Desk <https://pds.nasa.gov/?feedback=true>`_ for assistance.


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

   curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products' \
       --data-urlencode 'limit=10' \
       --data-urlencode 'q=(pds:Primary_Result_Summary.pds:processing_level eq "Raw")'


Search Observational Products by Target
----------------------------------------

Search for all Observational Products targeting Bennu:

**Query:** ``(ref_lid_target eq "urn:nasa:pds:context:target:asteroid.101955_bennu")``

.. code-block:: bash
   :caption: curl command
   :substitutions:

   curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products' \
     --data-urlencode 'q=(ref_lid_target eq "urn:nasa:pds:context:target:asteroid.101955_bennu")'


Search by Reference
-------------------

Search all products which are referring to a given LID:

.. code-block:: bash
   :caption: curl command
   :substitutions:

    curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products' \
        --data-urlencode 'limit=200' \
        --data-urlencode 'q=((pds:Internal_Reference.pds:lid_reference eq "urn:nasa:pds:context:investigation:mission.orex") or (pds:Internal_Reference.pds:lid_reference like "urn:nasa:pds:context:investigation:mission.orex::*"))' | json_pp



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

We assume you know the identifier of the product you are working with but a couple are provided in the examples below. 


Search for a Product's Collection DOI
*************************************

Run the following request to get the DOI associated with the collection the observational product `urn:nasa:pds:compil-comet:nuc_properties:description::1.0` belongs to:

.. code-block:: bash
   :caption: curl command
   :substitutions:

    curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:vg1-saturn-pos-hgcoords-96sec:data-spice:spice-hg::1.0/member-of' \
        --data-urlencode 'fields=pds:Citation_Information.pds:doi' \
        --header 'Accept: application/kvp+json'

.. _DOI collection request result:

You will get the following result:

.. code-block:: json

    {
        "summary" : {
            "q": "",
            "hits": 1,
            "took": 125,
            "start": 0,
            "limit": 100,
            "sort": [],
            "properties": ["pds:Citation_Information.pds:doi"]
        },
        "data": [
            {
               "pds:Citation_Information.pds:doi":"10.17189/1522962"
            }
        ]
    }

Note that you might not find any DOI at the collection level, in this case you can try to get the DOI from the bundle.

Search for a Product's Bundle DOI
*********************************

To get the DOI associated with the bundle the observational product `urn:nasa:pds:insight.spice:document:spiceds::1.0` belongs to:

.. code-block:: bash
   :caption: curl command
   :substitutions:

    curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight.spice:document:spiceds::1.0/member-of/member-of' \
        --data-urlencode 'fields=pds:Citation_Information/pds:doi' \
        --header 'Accept: application/kvp+json'

.. _DOI bundle request result:

You will get the following result:

.. code-block:: json

    {
        "summary" : {
            "q": "",
            "hits": 2,
            "took": 135,
            "start": 0,
            "limit": 100,
            "sort": [],
            "properties": [
                "pds:Citation_Information.pds:doi"
            ]
        },
        "data": [ 
            { },
            {
                "pds:Citation_Information.pds:doi": "10.17189/1517566"
            }
        ]
    }


How to Find the PDS Product Associated with a DOI
-------------------------------------------------

To get the PDS product metadata associated with a the DOI `10.17189/1517568`:

.. code-block:: bash
    :substitutions:

    curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products' \
        --data-urlencode 'q=(pds:Citation_Information.pds:doi eq "10.17189/1522962")' \
        --header 'Accept: application/json'

You will get a JSON response of the PDS products (any class of product, for example collections or bundles) which have referenced the given DOI.

You can get the result in different format using content negociation with the Accept header parameter.

Search by Time Range
--------------------

For example, as a user I need to find the Voyager 1 PWS Spectrum Analyzer CDF files covering March of 1979 so I can make a plot.

Here is one of the XML files, rendered: https://search-pdsppi.igpp.ucla.edu/ditdos/viewFile?id=pds://PPI/voyager1.pws.sa/data/1979/vg1pws_lr_19790105_v5.20.xml .

To build this query, we can search by the instrument and time range:

.. code-block:: bash

   ((pds:Time_Coordinates.pds:start_date_time ge "1979-03-01T00:00:00.000Z") and
      (pds:Time_Coordinates.pds:start_date_time lt "1979-04-01T00:00:00.000Z") and
      (ref_lid_instrument eq "urn:nasa:pds:context:instrument:vg1.pws"))

Do query that using curl, it would look like this:

.. code-block:: bash
    :substitutions:

    curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products' \
         --data-urlencode 'q=((pds:Time_Coordinates.pds:start_date_time ge "1979-03-01T00:00:00.000Z") and ' \
         --data-urlencode '(pds:Time_Coordinates.pds:start_date_time lt "1979-04-01T00:00:00.000Z") and ' \
         --data-urlencode '(ref_lid_instrument eq "urn:nasa:pds:context:instrument:vg1.pws"))' \
         --header 'Accept: application/json'


**Looking for more recipes? Or have some useful recipes of your own?** Checkout the `PDS API Discussion Board <https://github.com/NASA-PDS/pds-api/discussions>`_ or contact the `PDS Help Desk <mailto:pds-operator@jpl.nasa.gov>`_
