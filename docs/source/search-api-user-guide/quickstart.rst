Quickstart
==========

The following section provides a quickstart guide to try out the PDS Search API.

Prerequisites
-------------

- curl command line tool (curl is available in many operating systems by default. It not, you can get curl from https://curl.se/ or using a package management tool specific to your operating system).


Steps to Call the PDS Search API with curl
------------------------------------------

1) Visit the Swagger UI of the PDS Federated API available at https://pds-gamma.jpl.nasa.gov/api/swagger-ui.html.

2) Expand the preferred endpoints (E.g.: ``Bundles``, ``Collections``, ``Products``) by clicking on them.


3) For example, click on the ``Products``, and then you will see the following operations.

    - GET /products
    - GET /products/{identifier}
    - GET /products/{identifier}/all
    - GET /products/{identifier}/latest


4) Click on the ``GET /products`` and then click on the **Try it out!** button at the end.

5) Copy the curl command just below the **Try it out!** button (in this example the curl command
is ``curl -X GET --header 'Accept: application/json' 'https://pds-gamma.jpl.nasa.gov/api/products?limit=100&only-summary=false'``).

6) Paste the above curl command in the terminal and press Enter. This will call the relevant operation of the selected
API Endpoint and show the response in the terminal.

As explained above, you can call the operations of PDS Search API Endpoints using curl commands.


Quickstart Guide to Call the PDS Search API with Python
-------------------------------------------------------

Alternatively, it is possible to use other tools such as Postman and programming languages such as Python to call the
PDS Search API.

The following quickstart guide explains the steps to use the PDS API Python Client to call the PDS Search API.\

https://nasa-pds.github.io/pds-api-client/quickstart/
