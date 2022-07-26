General API Conventions
=======================

Reference Documents
---------------------

Several websites and documents were used as references for designing
this API and the accompanying guidelines, including:

1.  `Open API Initiative <https://www.openapis.org/>`_

2.  `Open APIs Specification <http://spec.openapis.org/oas/v3.0.2>`_

3.  `Microsoft API Guidelines <https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md>`_

4.  `Microsoft API Design Best Practices <https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design>`_

5.  `NASA Earth Data APIs <https://earthdata.nasa.gov/collaborate/open-data-services-and-software/api>`_

6.  `Google Custom Search REST API <https://developers.google.com/custom-search/v1/using_rest>`_

7.  `EPN-TAP <https://arxiv.org/pdf/1407.5738.pdf>`_

8.  `Earth Data Common Metadata Repository (CMR) <https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html>`_

9.  `Swagger for Developing API Spec <https://swagger.io/>`_

10. `Open Search <https://en.wikipedia.org/wiki/OpenSearch>`_

11. `Library of Congress Search/Retrieval by URL <http://www.loc.gov/standards/sru/sru-2-0.html>`_

12. `PDS OPUS API <https://opus.pds-rings.seti.org/apiguide.pdf>`_

13. `PDS Imaging Atlas API <https://pds-imaging.jpl.nasa.gov/tools/atlas/api/>`_

14. `OGC Environmental Data Retrieval <https://github.com/opengeospatial/ogcapi-environmental-data-retrieval>`_

General Applicable Open API Conventions
---------------------------------------

Specification Standard
**********************

The API complies with Open API 3.0.


Restful Principles
------------------

Resources
*********

Resources are coded as URI (e.g. `http://domain/api/pets`). Resources
should be nouns (verbs are bad)

Verbs
*****

Users interact with resources through `HTTP request
verbs <https://assertible.com/blog/7-http-methods-every-web-developer-should-know-and-how-to-test-them>`_.
The PDS API uses GET and POST:

-   GET is relevant to get resource representation from the API when the extraction criteria is simple.

-   POST, in a read-only context, is relevant to provide the API with complex request criteria.

Future iterations of the API will transform it to be an `idempotent
REST API <https://restfulapi.net/idempotent-rest-apis/>`_, utilizing
GET, PUT, DELETE, HEAD, OPTIONS and TRACE HTTP methods.

Resource Representation
***********************

When a HTTP request verb (e.g. GET, POST, etc.) is applied to a resource
(e.g. `http://domain/api/pets`) he/she gets a resource representation.

Many flavors of representations are possible to be
returned from a single resource. For example: subsets of a whole,
formats, versions, etc...

The resource representation should be self-described as much as
possible.

They should be wrapped in envelopes which prevent from vulnerabilities
linked to the direct access to json arrays in javascript code (see
`https://haacked.com/archive/2008/11/20/anatomy-of-a-subtle-json-vulnerability.aspx/ <https://haacked.com/archive/2008/11/20/anatomy-of-a-subtle-json-vulnerability.aspx/>`_).
A response with this format is fine:

.. code-block:: json

    {
       "summmary": {"..."},
       "data": ["..."]
    }


Other Conventions
-----------------

Beyond the OpenAPI standard, there are multiple options regarding
general design of an API. We primarily use the following source which is
very complete and not too dogmatic:
`https://www.moesif.com/blog/api-guide/api-design-guidelines/ <https://www.moesif.com/blog/api-guide/api-design-guidelines/>`_

Some peer web API specifications are also considered as references for
the design for the PDS API specification:

-   `ESDIS Common Metadata Repository API <https://earthdata.nasa.gov/collaborate/open-data-services-and-software/api/cmr-api>`_
-   `OGC environment data retrieval <http://docs.opengeospatial.org/DRAFTS/19-086.html>`_

URL Resource Naming: Case
*************************

`Kebab-case <https://en.wiktionary.org/wiki/kebab_case>`_ (lower
case and hyphens ‘-’ used to fill the spaces in) is used for url
resource naming.

For example:

-   \`discipline-nodes\` in http://pds.nasa.gov/api/references/0.1/discipline-nodes

(for the rationale see this `stackoverflow discussion <https://stackoverflow.com/questions/10302179/hyphen-underscore-or-camelcase-as-word-delimiter-in-uris>`_

URL Resource Naming: Plural vs Singular
***************************************

Resources are named plural or singular depending on the use case.

Plural are used when the resources is a collection the user will subset
from, for example \`/pets/scooby-doo\` or \`/planets/mars\` or
‘/users/user-id’ or ‘collections?q=...’’

Singular are used when the resource is accessed as one. For example
‘/profile’ to access the profile of the current user.

See this `post <https://medium.com/@atomaka/single-and-plural-rails-routes-for-the-same-resource-330d985b6595>`_ for more details.

URL Resource Naming: API Versioning
***********************************

The API will have versions and the deployed versions are likely to be
heterogeneous in the PDS system.

Two options have been considered to manage versions (see
`https://restfulapi.net/versioning/ <https://restfulapi.net/versioning/>`_ :

-   Version in the URL, e.g. pds.nasa.gov/api/search/1.0/

-   Content negotiation headers (e.g. Accept: application/vnd.example+json;version=1.0)

To keep things as simple as possible, content negotiation will not be
used for version management. A server API implementation will implement
a single version of the API definition.

However:

-   We advise to use the version in the URL of the API when it is deployed, although it is not part of the API definition.

-   The version is mandatory in the resource representations (result of a request)


Pagination/Sort
---------------

The query parameters for pagination are:

+-----------+---------------------------------------------------------------+
| Parameter | Description                                                   |
+===========+===============================================================+
| start     | Index of first item returned in the response                  |
+-----------+---------------------------------------------------------------+
| limit     | Maximum number of item expected in the response               |
+-----------+---------------------------------------------------------------+

See
`https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/ <https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/>`_
