# NASA PDS Federated API

This repository is the entry point for the NASA PDS federated API specifications.

PDS is willing to develop restful web APIs for different applications (so far, data search, dois) without a priori limitation of what the API is relevant for.

Each of the applications for which an official PDS API end-point is published should be registered in this repository.

# API specifications available:

- registry (specification discussed in the PDS API Working Group)
- doi

# API entry points

The API entry-points are provided under the following pattern:

    https://pds.nasa.gov/api/<application>/<version>






# API implementations 

## Registry:

Various implementation flavors are available:

-   Java library: https://github.com/NASA-PDS/pds-api-javalib
-   Java official server (alpha version): https://github.com/NASA-PDS/registry-api-service , deployed on https://pds-gamma.jpl.nasa.gov/api/swagger-ui.html
-   Python client: https://github.com/NASA-PDS/pds-api-client


# API Documentation 

The API Documentation is available at: https://nasa-pds.github.io/pds-api/

We also publish [a draft of the PDS API Specification](https://docs.google.com/document/d/16d0MVh48bFLvWsa5-B_Hy-cby1rGWdnNojWOJpUcOvA/edit#heading=h.3pbz9ppxrxvr).


