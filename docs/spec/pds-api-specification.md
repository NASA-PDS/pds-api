
---
title: "PDS API Conventions"
subtitle: "Version 1"
author:
- "PDS API Working Group"
date: 05-12-2022
include-before:
- '`\newpage{}`{=latex}'
---


**Abstract**
============

The Planetary Data System is a federated system of nodes that archive
planetary science data. The PDS Application Programming Interface (API)
is an attempt at provide a consistent interface for sharing archival
data and services across PDS, among planetary archives, and within the
planetary science community. The API is one of the cornerstone
applications for providing an integrated worldwide data services
platform that enables the efficient discovery, dissemination, use and
analysis of internationally sponsored planetary science archives.

The latest released version of this document is currently maintained on
the PDS API Github Repo, and the development version is maintained on
Google Drive. Feedback and comments welcome.

-   Released: [<u>https://github.com/NASA-PDS/pds-api/blob/main/docs/spec/pds-api-specification.md</u>](https://github.com/NASA-PDS/pds-api/blob/main/docs/spec/pds-api-specification.md)

-   In Development: [<u>https://docs.google.com/document/d/16d0MVh48bFLvWsa5-B\_Hy-cby1rGWdnNojWOJpUcOvA/edit?usp=sharing</u>](https://docs.google.com/document/d/16d0MVh48bFLvWsa5-B_Hy-cby1rGWdnNojWOJpUcOvA/edit?usp=sharing)


**PDS Search API**
==================

General Request Details
-----------------------

#### Maximum URL Length

The Maximum URL Lengths supported by the PDS Search API are:

-   For programmatic GET requests - 6,000 characters

-   For web browser access - 2048 characters

Clients using the Search API with query parameters should be careful not
to exceed this limit or they may get an HTTP response of 413 FULL HEAD
due to server or browser performance restrictions. If a client expects
that the query url could be extra long so that it exceeds 6k characters,
they should use the a POST request through the [<u>JSON Request
API</u>](#_hz19fj2debw3) for searching.

Query Syntax
------------

The query string query parameters, *q*, allows a client to filter the
results from an API request. The expression specified with *q* is
evaluated for each resource in the collection, and only items where the
expression evaluates to true are included in the response. Resources for
which the expression evaluates to false or to null, or which reference
properties that are unavailable due to permissions, are omitted from the
response.

The PDS Search API also supports wild cards ? and \*. A search with no
*q* parameter specified will default to *q=\** (search for all possible
records).

Example: return all collections whose start time is prior to June 1,
2020:

```
GET https://pds.nasa.gov/api/search/1.1/collections?
       q=Time_Coordinates.start_date_time LT 2020-06-01T00:00:00Z
```

### Query String Operations

The PDS Search API supports the following minimal set of operations.

| **Operator**           | **Description**       | **Example**                                                                                                               |
|------------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------|
| *Comparison Operators* |                       |                                                                                                                           |
| eq                     | Equal                 | target\_name ***eq*** "Mars"                                                                                                |
| ne                     | Not equal             | target\_name ***ne*** "Saturn"                                                                                              |
| gt                     | Greater than          | Time\_Coordinates.start\_date\_time ***gt*** "2001-05-10T00:00:00Z"                                                         |
| ge                     | Greater than or equal | Time\_Coordinates.start\_date\_time ***ge*** "2001-05-10T00:00:00Z"                                                         |
| lt                     | Less than             | Time\_Coordinates.start\_date\_time ***lt*** "2020-06-01T00:00:00Z"                                                         |
| le                     | Less than or equal    | Time\_Coordinates.start\_date\_time ***le*** "2020-06-01T00:00:00Z"                                                         |
| *Logical Operators*    |                       |                                                                                                                           |
| and                    | Logical and           | target\_name ***eq*** "Mars" ***and*** instrument\_name ***eq*** "hirise"                                                     |
| or                     | Logical or            | target\_name ***eq*** "Mars" ***or*** target\_name ***eq*** "Phobos"                                                          |
| not                    | Logical negation      | ***not*** target\_name ***eq*** "Mars"                                                                                      |
| *Grouping Operators*   |                       |                                                                                                                           |
| ( )                    | Precedence grouping   | ***(***target\_name ***eq*** "Mars" ***or*** target\_name ***eq*** "Phobos"***)*** ***and*** instrument\_name ***eq*** "hirise" |

### Reserved Query Parameters

The following are a table of reserved query parameters that have special
meaning to support search.

| **Query Parameter** | **Description**                                                                                                                                                                                                    | **Example**                                                |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| q                   | (Required, string) Query string you wish to parse and use for search. See Query string syntax.                                                                                                                     | `q=target_name eq "Mars"`                               |
| fields              | (Optional, array of strings) Array of fields you wish to return.                                                                                                                                                   | `fields=lid,Time_Coordinates.start_date_time`           |
| start               | (Optional, integer, default=0) The search result to start with in the returned records. For instance, start=10 will return records 10-19.                                                                          | `start=100`                                                |
| limit               | (Optional, integer) The number of records/results to return. Defaults to 25.                                                                                                                                       | `limit=100`                                                |
| sort                | (Optional, string, default=LIDVID) Field to sort on and whether it should be sorted ascending (ASC) or descending (DESC). `fieldName asc` or `fieldName desc`. There can be several sort parameters (order is important). | `sort=lidvid asc, Time_Coordinates.start_date_time desc` |



### Endpoints

Based upon the PDS API Specification guidelines for [<u>Request URL
Specification</u>](#request-url-specification), the following are the
base URIs for performing GET requests for searching PDS data.

**For collection-level search:**

Search All PDS Data Collections:

```
GET https://pds.nasa.gov/api/search/1.1/collections?{searchTerms}
```

Search Geosciences Node Collections:

```
GET https://pds.nasa.gov/api/search-geo/1.1/collections?{searchTerms}
```

See Query Parameters for more specific examples for various searches
with different parameters.

**For product-level search:**

Template:

```
GET https://{node-hostname}/api/{service}/{pds.api.version}/products?{searchTerms}
```

Examples:

Search All PDS Data Products:

```
GET https://pds.nasa.gov/api/search/1.1/products?{searchTerms}
```

Search Geosciences Node:

```
GET https://pds.nasa.gov/api/search-geo/1.1/products?{searchTerms}
```


See Query Parameters for more specific examples for various searches
with different parameters.

#### Additional Query String Examples

```
/api/search/1.1/collections?q="2018-01-01" LE Time_Coordinates.start_date_time LE "2020-01-01"&start=100&limit=1000

/api/search/1.1/products?q=Observing_System_Component.description EQ "ISSNA" AND (Optical_Filter.filter_name EQ "BL1" OR Optical_Filter.filter_name EQ "GRN")&fields=cassini.spacecraft_clock_start_count
```

POST Request API
----------------

*For now, we may just want the POST request API to be pretty much identical to the GET, except you can embed the Response Format `return_type` in the HTTP header*

*If we wanted to create a Domain Specific Language (DSL), here are some references:*

* *ElasticSearch Query DSL: [<u>https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html</u>](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)*
* *Solr Query DSL: [<u>https://lucene.apache.org/solr/guide/7\_1/json-query-dsl.html</u>](https://lucene.apache.org/solr/guide/7_1/json-query-dsl.html)*
* *ESDIS CMR Example JSON Request API: [<u>https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html\#search-with-json-query</u>](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html#search-with-json-query)*



Response Formats
----------------

~~Working~~ Document: [PDS API - Response Formats](pds-api-response-formats.pdf)


Query Parameters
----------------

Query parameters are the variables used to specify values in a [<u>query
string</u>](https://en.wikipedia.org/wiki/Query_string) or as part of an
API for searching for specific values in a database.

The following are the defined set of common query parameters for PDS
defined as a query model in the PDS4 Information Model.

### Collection-level Search

The initial revision of the query parameters will be based upon the PDS
Common Dictionary Query Model (designed by the Data Design Working Group
(DDWG)), which was intended to enable searching at the ***data
collection level***. Some of the query model parameters may not apply or
will be grouped together, but these are the values that were decided
would be most helpful for searching for a particular data collection.
Below are the attributes of most interest:

-   Product\_Collection.collection\_type**=Data** (ignored in query parameters)
-   Primary\_Result\_Summary.processing\_level
-   Investigation\_Area.type**=Mission** (ignored in query parameters)
-   Science\_Facets.domain
-   Identification\_Area.product\_class**=Product\_Collection** (ignored in query parameters)
-   Science\_Facets.wavelength\_range
-   Primary\_Result\_Summary.purpose**=Science** (ignored in query parameters)
-   Science\_Facets.discipline\_name
-   Time\_Coordinates.start\_date\_time
-   Collection.description
-   Time\_Coordinates.stop\_date\_time
-   Product\_Context.Instrument.type
-   Target\_Identification.name
-   Identification\_Area.logical\_identifier
-   Target\_Identification.type
-   Identification\_Area.version\_id
-   Investigation\_Area.name
-   Science\_Facets.facet1
-   Observing\_System.name
-   Science\_Facets.facet2
-   Observing\_System\_Component.name
-   Primary\_Result\_Summary.description
-   Observing\_System\_Component.type**=Instrument** (ignored in query parameters)
-   Target\_Identification.description
-   Identification\_Area.title
-   system.archive\_status
-   Citation\_Information.keyword
-   Citation\_Information.description

These are all specified in the PDS Common tab of the [<u>PDS Query
Parameters
spreadsheet</u>](https://docs.google.com/spreadsheets/d/1DyEnLz-U2R1Ej4cTVfCCJVCX6YCWoiLUA_m2mSLW6Qk/edit#gid=0).

### Product-level Search

For enabling product-level search, the collection-level search query
model should be extended for each discipline-specific implementation.
For starters, we can simply add parameters we deem useful to the
specification. However, in the end, all query parameters should be
specified in the PDS4 Information Model and the applicable local data
dictionary, either by query model or some other TBD mechanism.

Each discipline node should create a tab or update their applicable tab
in the [<u>PDS Query Parameters
spreadsheet</u>](https://docs.google.com/spreadsheets/d/1DyEnLz-U2R1Ej4cTVfCCJVCX6YCWoiLUA_m2mSLW6Qk/edit#gid=0)
with parameters useful for their specific discipline node or product
search. Ideally attempting to follow the guidelines for specifying query
parameters noted above.





Additional Example Search Scenarios
-----------------------------------

TBD



**PDS REST Web Services supporting the API federation**
=======================================================

OBSOLETE

URN resolver for LIDVID
-----------------------

The PDS has a powerful URN scheme for naming its resources.

The PDS API will provide a service to resolve URN wherever the resource
identified is managed.

Routes
------

The PDS API end-points will be distributed in the PDS system and hosted
by Discipline Nodes and Engineering Nodes.

To act as a federated API system, the API should enable redirection of
clients’ requests to the most appropriate API end-point depending on
user requests.

**Other PDS REST Web Services**
===============================

TBD a more RESTful approach to searching the registry

**Implementation**
==================

OBSOLETE

<img src="media/image2.png" style="width:7.13021in;height:3.61934in" />
-----------------------------------------------------------------------

4 Stages:

* Standard preparation: swaggerHub
* Standard definition: one yml or json file on a github repository
* Standard libraries: python and java standard implementation (client,severs stubs) shared on PYPI and MAVEN artifactory
* Standard implementations, by Engineering Node (demo, validator, core) and Discipline Nodes (actual access).

3.1 Preparation
---------------

The definition of the API is prepared in swaggerhub:
[https://app.swaggerhub.com/apis/PDS_APIs/pds_federated_api](https://app.swaggerhub.com/apis/PDS_APIs/pds_federated_api)  

3.2 Definition
--------------

The definition of the API is published in a yml and json file in a
public github repository.

[<u>https://github.com/NASA-PDS/pds-api-base</u>](https://github.com/NASA-PDS/pds-api-base)

3.3 Libraries
-------------

Libraries in JAVA and PYTHON are generated from the standard definition.

They include client libraries and server stubs.

They are published on PYPI and MAVEN Central Repository.

TO BE DONE, UNDER PROGRESS

3.4 Implementations
-------------------

The foreseen implementations are:

-   Discipline node servers

-   Validator/Demo client

-   Demo server

-   Core server (router/proxy)

They can be in any language but may use the standard libraries, which
should help to comply with the standard AND implement basic behaviours
(route, urn resolution).


**References**
--------------

Portions of these guidelines were adapted from [Microsoft API Guidelines](https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md) licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/)

Appendix A - API Definition and Application Guidelines
======================================================

This appendix is intended for the PDS Node to provide guidelines for
defining and applying the PDS API Spec.

Goals
-----

-   To define a common, ***RESTful API specification*** to be adopted across the PDS.
-   To define a ***common syntax and best practices for defining query parameters***.
-   To define a ***common set of query parameters for top-level search criteria*** with the widest-ranging applicability across all PDS data.
-   To define a set of best practices and processes for extending the common set of query parameters with ***discipline- and node-specific query parameters***.
-   To provide a ***managed central location for describing and documenting all API specification details***, including query parameters, across the entire PDS.

Request URL Specification
-------------------------

Consistency of URI definitions is important for ubiquitous use of APIs
across a federated system. Additionally, it enables the federated system
to integrate as an architecture of [<u>microservice
architecture</u>](https://en.wikipedia.org/wiki/Microservices). The
following is a general guideline for PDS REST API endpoints:

https://{hostname}/api/v{pds.api.version}/{controller}?{searchTerms}

where {hostname} is the web hostname (e.g.
[<u>https://pds.nasa.gov</u>](https://pds.nasa.gov)),

{controller} is some object controller e.g. search, translate, transform

{pds.api.version} is the version of the API being used.

Defining Query Parameters
-------------------------

### Query Parameter Governance

Governance and stewardship over query parameters follows a similar
pattern to the PDS4 Information Model in that it is a tiered governance
model.

<img src="media/image1.png" style="width:4.35938in;height:2.49756in" />

### Defining Query Parameters using Query Models

In order to leverage the PDS4 Information Model for specifying these
parameters, we can use the notion of [*<u>query
models</u>*](https://www.hou.usra.edu/meetings/planetdata2019/pdf/7083.pdf).
Query models are a means for discipline dictionary developers, or
steward, to specify attributes they deem useful for search that they
believe data providers will search by. As the discipline dictionary
steward, they are close to the scientists and have a good understanding
of their user community needs. It makes the most sense for that
information to be specified by those specialists.

To get started, we will use the PDS Common Dictionary query model for
top-level search integration, and then expand to the discipline
dictionaries.

### Query Parameter Formation Specification

The PDS4 Standard is the backbone of the future for the PDS, where
careful consideration has been taken in the naming of all classes and
attributes throughout the information model. Instead of creating our own
names or using legacy PDS3 naming, we should leverage PDS4 as much as
possible.



##### Examples

| **Query Parameter**                             | **XPath**                                         |
|-------------------------------------------------|---------------------------------------------------|
| `Observing_System.description`                   | `//Observation_Area/Observing_System/description` |
| `geom.Camera_Model_Parameters.geom.model_type` | `//geom:Camera_Model_Parameters/geom:model_type` |

####

#### Exceptions and Nuances

There are some exceptions to the query syntax guidelines:

##### 1. Custom Query Parameters



##### 2. Internal / External References

OBSOLETE

Because Internal and External References are inherited throughout
discipline/mission dictionaries, the ancestor class should replace the
parent. In addition, since lid\_reference and lidvid\_reference are both
referring some identifier, we replace those both with id\_reference,
e.g.:

| **Query Parameter**                        | **XPath**                                                            |
|--------------------------------------------|----------------------------------------------------------------------|
| Observing\_System\_Component.id\_reference | //Observing\_System\_Component/Internal\_Reference/lidvid\_reference |
| Observing\_System\_Component.id\_reference | //Observing\_System\_Component/Internal\_Reference/lid\_reference    |
