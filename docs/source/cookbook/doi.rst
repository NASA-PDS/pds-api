DOI Recipes
===========

Search for parent collection and return DOI only
************************************************

Call the following API::

  {base_url}/products/{identifier}/collections?fields={field1}&fields={field2}

where

 * {base_url} - Base URL of the API server. For example *http://localhost:8080* or *https://pds-gamma.jpl.nasa.gov/api*.
 * {identifier} - LID or LIDVID of a product, for example *urn:nasa:pds:kaguya_grs_spectra:data_ephemerides:kgrs_ephemerides::1.0*.
 * {field1}, {field2},.. {fieldN} - list of fields to return. DOIs can be stored in following fields:

    * pds:Citation_Information/pds:doi
    * ops:Identifiers/ops:doi

Below is the **curl** example. Note that the URL has to be encoded.

.. code-block:: python

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/products/urn%3Anasa%3Apds%3Akaguya_grs_spectra%3Adata_ephemerides%3Akgrs_ephemerides%3A%3A1.0/collections?limit=100&fields=ops%3AIdentifiers%2Fops%3Adoi&fields=pds%3ACitation_Information%2Fpds%3Adoi&only-summary=false'


Search for parent bundle and return DOI only
********************************************

Call the following API::

  {base_url}/products/{identifier}/bundles?fields={field1}&fields={field2}

where

 * {base_url} - Base URL of the API server. For example *http://localhost:8080* or *https://pds-gamma.jpl.nasa.gov/api*.
 * {identifier} - LID or LIDVID of a product, for example *urn:nasa:pds:kaguya_grs_spectra:data_ephemerides:kgrs_ephemerides::1.0*.
 * {field1}, {field2},.. {fieldN} - list of fields to return. DOIs can be stored in following fields:

    * pds:Citation_Information/pds:doi
    * ops:Identifiers/ops:doi

Below is the **curl** example. Note that the URL has to be encoded.

.. code-block:: python

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/products/urn%3Anasa%3Apds%3Akaguya_grs_spectra%3Adata_ephemerides%3Akgrs_ephemerides%3A%3A1.0/bundles?limit=100&fields=ops%3AIdentifiers%2Fops%3Adoi&fields=pds%3ACitation_Information%2Fpds%3Adoi&only-summary=false'

