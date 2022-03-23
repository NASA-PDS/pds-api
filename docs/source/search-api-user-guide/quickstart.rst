Quickstart
==========

The following section provides a quickstart guide to try out the PDS Search API.

Prerequisites
-------------

- curl command line tool (curl is available in many operating systems by default. It not, you can get curl from https://curl.se/ or using a package management tool specific to your operating system).


Steps to Call the PDS Search API with curl
------------------------------------------

1. Open a terminal.


2. Paste the following curl command in the terminal and press Enter. This will call the relevant operation of the selected API Endpoint and show the response in the terminal. ::

    curl -X GET --header 'Accept: application/json' 'https://pds-gamma.jpl.nasa.gov/api/products?limit=5&only-summary=false'


As explained above, you can call the operations of PDS Search API Endpoints using curl commands.

The API endpoints, operations and related curl commands are available in the Swagger UI of the PDS Federated API available
at https://pds-gamma.jpl.nasa.gov/api/swagger-ui.html.


Quickstart Guide to Call the PDS Search API with Python
-------------------------------------------------------

Alternatively, it is possible to use other tools such as Postman and programming languages such as Python to call the
PDS Search API.

The following quickstart guide explains the steps to use the PDS API Python Client to call the PDS Search API.\

https://nasa-pds.github.io/pds-api-client/quickstart/
