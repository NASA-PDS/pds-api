DOI Recipes
===========

`Digital Object Identifiers <https://www.doi.org/>`_ are useful to cite the data you are using in your research.
They are referenced in the PDS product descriptions.
Here is how to interact with them through the PDS Search API, in a few simple cases.

.. Warning::
  Since our servers are not populated with data yet, the following url might return empty results or 404 (not found) errors.


I Use an Observational Product, I Want to Get a DOI That I Can Use to Cite It
*****************************************************************************

We assume you know the identifier of the product you are working with. In our example it is: `urn:nasa:pds:insight_rad:data_derived:hp3_rad_der_00014_20181211_073042::1.0`

DOIs are usually born by the collection or bundle the product is belonging to.

Search the DOI in the Containing Collection
-------------------------------------------

Run the following request to get the DOI associated with the collection the product belongs to:

.. code-block:: bash
    :substitutions:

    curl --location --request GET 'http://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight_rad:data_derived:hp3_rad_der_00014_20181211_073042::1.0/collections?fields=pds:Citation_Information/pds:doi&fields=ops:Identifiers/ops:doi' --header 'Accept: application/kvp+json'

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
               "pds:Citation_Information/pds:doi": "10.17189/1517568",
               "ops:Identifiers/ops:doi": "10.17189/1517568"
            }
        ]
    }

The DOI can be found in 2 different properties:
    * **pds:Citation_Information/pds:doi**: DOI citation provided by the custodiam node
    * **ops:Identifiers/ops:doi**: DOI citation automatically provided from the `PDS DOI Service <https://pds.nasa.gov/tools/doi/#/search>`_

Note that you might not find any DOI at the collection level, in this case you can try to get the DOI from the bundle.

Search the DOI in the Containing Bundle
-------------------------------------------

To get the DOI associated with the bundle the observational product `urn:nasa:pds:insight_rad:data_derived:hp3_rad_der_00014_20181211_073042::1.0` belongs to:

.. code-block:: bash
    :substitutions:

    curl --location --request GET 'http://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight_rad:data_derived:hp3_rad_der_00014_20181211_073042::1.0/bundles?fields=pds:Citation_Information/pds:doi&fields=ops:Identifiers/ops:doi' --header 'Accept: application/kvp+json'

You will get the same response as for a :ref:`collection request <Search the DOI in the Containing Collection>`


I Found a DOI Citation, I Want to See Its PDS Product Description
*******************************************************************

To get the PDS product description associated with a given DOI (here `10.17189/1517568`):

.. code-block:: bash
    :substitutions:

    curl --location --request GET 'http://pds.nasa.gov/api/search/|search_user_guide_api_version|/products?q=((pds:Citation_Information/pds:doi eq "10.17189/1517568") or (ops:Identifiers/ops:doi eq "10.17189/1517568"))' --header 'Accept: application/json'

You will get a json description of the PDS products (any class of product, for example collections or bundles) which have referenced the given DOI.

You can get the result in different format using content negociation with the Accept header parameter.