# NASA PDS federated API
This repo is the entry point for the NASA PDS federated API specifications.

The specifications are discussed in the PDS Working Group and a first level of specification is shared on google drive.

The formal specification in Open API standard is shared on swaggerHub: https://app.swaggerhub.com/apis/PDS_APIs/pds_federated_api/0.1.dev

Various implementation flavour are also being made available:
- java library: https://github.com/NASA-PDS/pds-api-javalib
- java stub and demo server: https://github.com/NASA-PDS/pds-api-service , deployed on https://pds-gamma.jpl.nasa.gov/api/swagger-ui.html
- python stub service: ithub.com/NASA-PDS/pds-api-pythonlib
- python client: https://github.com/NASA-PDS/pds-api-client

# Documentation is generated in github action workflow on:

https://nasa-pds.github.io/pds-api/


# To generate a POSTMAN test collection

POSTMAN is a popular tool for user friendly test of the web API: https://www.postman.com/

POSTMAN is a standalone desktop application that you first need to download and install: https://www.postman.com/downloads/

To create a test collection for the PDS federated API, follow the stes:

  1. go to import (top-left)
  2. choose Link tab
  3. Use link `https://raw.githubusercontent.com/NASA-PDS/pds-api/master/json-unresolved/swagger.json`
  4. In settings, for request parameter generation, select 'Example', this will assign example values to the API arguments. If you select 'Schema' no value will be assigned.
  5. Create a virtual environment, click the wheel on top-right, then 'Add'
  6. Create constant 'baseUrl' assign value of your root server without trailing /, for example https://pds-gamma.jpl.nasa.gov/api
  7. Make sure your new environment is selected, use top-right drop down menu.
  8. Go to your new collection folder named 'Planetary Data System API', select a request
  9. Adjust the request's parameters, hit 'Send'
  10. You can extend the collection by duplicating and editing existing requests
 

Warning: if you reimport the same specification in the same folder, your manually set parameters will be lost.









