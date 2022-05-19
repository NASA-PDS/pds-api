# Changelog

## [«unknown»](https://github.com/NASA-PDS/pds-api/tree/«unknown») (2022-05-19)

[Full Changelog](https://github.com/NASA-PDS/pds-api/compare/v12.0.1-dev...«unknown»)

**Improvements:**

- Improve linkages from Registry App Docs to API Docs [\#158](https://github.com/NASA-PDS/pds-api/issues/158)

**Other closed issues:**

- Check for typos in OpenAPI spec [\#161](https://github.com/NASA-PDS/pds-api/issues/161)
- document the server - specification - client [\#157](https://github.com/NASA-PDS/pds-api/issues/157)

## [v12.0.1-dev](https://github.com/NASA-PDS/pds-api/tree/v12.0.1-dev) (2022-04-19)

[Full Changelog](https://github.com/NASA-PDS/pds-api/compare/0.4.0...v12.0.1-dev)

**Requirements:**

- As a user, I want to receive error messages when an invalid request is submitted to the API [\#153](https://github.com/NASA-PDS/pds-api/issues/153)
- As a user, I want the API response media types to be compliant with RFC 6838 [\#152](https://github.com/NASA-PDS/pds-api/issues/152)
- As a user, I want to see API stable release specifications [\#139](https://github.com/NASA-PDS/pds-api/issues/139)
- As an API user, I want to get a key-value-pair JSON response [\#134](https://github.com/NASA-PDS/pds-api/issues/134)
- As a user, I want to get the metadata in a pds4+xml response [\#125](https://github.com/NASA-PDS/pds-api/issues/125)
- As an API user, I want a CSV response format option [\#120](https://github.com/NASA-PDS/pds-api/issues/120)
- As a user, I want to clearly see which formats are accepted by the API when a 406 error is raised [\#127](https://github.com/NASA-PDS/pds-api/issues/127)
- As a API manager, I want to restrict access to registered products that should not be publicly accessible [\#106](https://github.com/NASA-PDS/pds-api/issues/106)
- As an API user, I want to specify whether I get the latest or all versions of a product [\#74](https://github.com/NASA-PDS/pds-api/issues/74)
- As an API user, I want to get an XML response [\#66](https://github.com/NASA-PDS/pds-api/issues/66)
- As an API user, I want to get only the fields I explicitly requested [\#65](https://github.com/NASA-PDS/pds-api/issues/65)
- As a developer, I want a continuous deployment of the API available for testing [\#51](https://github.com/NASA-PDS/pds-api/issues/51)

**Improvements:**

- Refactor `meta` section of pds4+json and pds4+xml to use ops namespace [\#154](https://github.com/NASA-PDS/pds-api/issues/154)
- Remove the x-total-count header from the API specification [\#145](https://github.com/NASA-PDS/pds-api/issues/145)
- flesh out the registry repository [\#142](https://github.com/NASA-PDS/pds-api/issues/142)
- Merge unnecessary individual repository [\#140](https://github.com/NASA-PDS/pds-api/issues/140)
- As a user, I want to have a detailed description of the API q parameter syntax [\#137](https://github.com/NASA-PDS/pds-api/issues/137)
- Revise the pds-api README so that it gives a perspective on non search api \(e.g. doi\) from pds [\#136](https://github.com/NASA-PDS/pds-api/issues/136)
- clarify what `keyword` parameter is for [\#133](https://github.com/NASA-PDS/pds-api/issues/133)
- As an API client user, I want to consistently and robustly start local servers for development and testing [\#112](https://github.com/NASA-PDS/pds-api/issues/112)
- Extend application/pds4+json support to all endpoints [\#110](https://github.com/NASA-PDS/pds-api/issues/110)
- Update API endpoints to use `identifier` instead of `lidvid` [\#108](https://github.com/NASA-PDS/pds-api/issues/108)

**Defects:**

- version number invalid according to PEP validation in CI [\#164](https://github.com/NASA-PDS/pds-api/issues/164) [[s.critical](https://github.com/NASA-PDS/pds-api/labels/s.critical)]
- `products/{identifier}` missing properties object in application/json response [\#155](https://github.com/NASA-PDS/pds-api/issues/155) [[s.high](https://github.com/NASA-PDS/pds-api/labels/s.high)]
- pds api not able to search using URL parameters [\#130](https://github.com/NASA-PDS/pds-api/issues/130) [[s.low](https://github.com/NASA-PDS/pds-api/labels/s.low)]
- Changes to API per last tagged release not in SwaggerHub [\#124](https://github.com/NASA-PDS/pds-api/issues/124) [[s.critical](https://github.com/NASA-PDS/pds-api/labels/s.critical)]
- Deployed API + Registry does not contain product metadata for pds4+json response [\#121](https://github.com/NASA-PDS/pds-api/issues/121) [[s.high](https://github.com/NASA-PDS/pds-api/labels/s.high)]

**Other closed issues:**

- Update Specifications documentation to only include latest with link to page with past versions [\#167](https://github.com/NASA-PDS/pds-api/issues/167)
- Disable automated github pages deployment with v1.0 [\#156](https://github.com/NASA-PDS/pds-api/issues/156)
- Update fields parameter definition to note that it does not apply to pds4+json and pds4+xml response formats [\#151](https://github.com/NASA-PDS/pds-api/issues/151)
- Update the swagger web tool from the specification [\#150](https://github.com/NASA-PDS/pds-api/issues/150)
- Update API documentation to have consistent descriptions for the query parameter [\#143](https://github.com/NASA-PDS/pds-api/issues/143)
- create a super registry+api repository [\#123](https://github.com/NASA-PDS/pds-api/issues/123)
- analysis of current workflow, ideas for improvment [\#122](https://github.com/NASA-PDS/pds-api/issues/122)
- \[pds-api\] B12.1 Improve API query handling [\#116](https://github.com/NASA-PDS/pds-api/issues/116)
- Expand API to include latest/all for all endpoints [\#115](https://github.com/NASA-PDS/pds-api/issues/115)

## [0.4.0](https://github.com/NASA-PDS/pds-api/tree/0.4.0) (2021-10-01)

[Full Changelog](https://github.com/NASA-PDS/pds-api/compare/f8aae0969c047bd9da84c5beb6761186bf18d93e...0.4.0)

**Requirements:**

- As an API user, I want to explicitly request the latest version of a product [\#107](https://github.com/NASA-PDS/pds-api/issues/107)
- As an API user, I want to know how long a request took to complete [\#105](https://github.com/NASA-PDS/pds-api/issues/105)
- As a user, I want to receive a JSON response that contains the PDS4 label metadata in JSON format \(application/pds4+json\) [\#101](https://github.com/NASA-PDS/pds-api/issues/101)
- As an API user, I want to be able to use the API for free text search [\#99](https://github.com/NASA-PDS/pds-api/issues/99)
- As an API user, I want to get the latest version of a product, by default [\#96](https://github.com/NASA-PDS/pds-api/issues/96)
- As a user, I want to query for all versions of a product [\#95](https://github.com/NASA-PDS/pds-api/issues/95)
- As an API user, I want to search using URL parameters [\#83](https://github.com/NASA-PDS/pds-api/issues/83)
- As a developer, I never want the label blob to be returned [\#80](https://github.com/NASA-PDS/pds-api/issues/80)
- As an API user, I want to search by a temporal range as an ISO-8601 time interval. [\#72](https://github.com/NASA-PDS/pds-api/issues/72)
- As an API user, I want to know in the response how many hits are returned for an API query. [\#68](https://github.com/NASA-PDS/pds-api/issues/68)
- As an API user, I want to access supplemental metadata from Product\_Metadata\_Supplemental. [\#67](https://github.com/NASA-PDS/pds-api/issues/67)
- As a user, when I request specific fields I want to get records which have at least one of these fields [\#64](https://github.com/NASA-PDS/pds-api/issues/64)
- As an API user, I want to know the Bundle for a given Collection. [\#62](https://github.com/NASA-PDS/pds-api/issues/62)
- As an API user, I want to know the Collection\(s\) for a given Product. [\#61](https://github.com/NASA-PDS/pds-api/issues/61)
- As an API user, I want to know the Bundle for a given Product. [\#60](https://github.com/NASA-PDS/pds-api/issues/60)
- As an API user, I want to know the Product\(s\) that belong to a given Bundle. [\#59](https://github.com/NASA-PDS/pds-api/issues/59)
- As an API user, I want to know the children and ancestors of bundle, collections, and products [\#56](https://github.com/NASA-PDS/pds-api/issues/56)
- As an API user, I want to perform a search using wildcards [\#54](https://github.com/NASA-PDS/pds-api/issues/54)

**Improvements:**

- Disable XML and HTML responses from current registry-api-service implementation [\#91](https://github.com/NASA-PDS/pds-api/issues/91)
- Get investigation area/targets/instruments from external ids [\#52](https://github.com/NASA-PDS/pds-api/issues/52)
- initiate a proposal for the API WG and ENG team [\#49](https://github.com/NASA-PDS/pds-api/issues/49)
- develop a jupyter notebook demo where a user can browse PDS archive from bundle to product data file [\#47](https://github.com/NASA-PDS/pds-api/issues/47)
- Implement content negotiation [\#43](https://github.com/NASA-PDS/pds-api/issues/43)
- Manage field preselection in queries [\#41](https://github.com/NASA-PDS/pds-api/issues/41)
- add lexer to registry api [\#40](https://github.com/NASA-PDS/pds-api/issues/40)
- Initial Federated API implementation [\#35](https://github.com/NASA-PDS/pds-api/issues/35)
- Deploy PDS API v0 \(alpha\) for beta testing [\#34](https://github.com/NASA-PDS/pds-api/issues/34)
- Define initial structure for response format conventions and parameter definition [\#17](https://github.com/NASA-PDS/pds-api/issues/17)
- Define initial set of intra-discipline \(product-level\) search scope [\#14](https://github.com/NASA-PDS/pds-api/issues/14)
- Deploy PDS API v0 \(alpha\) on pds-gamma test server [\#13](https://github.com/NASA-PDS/pds-api/issues/13)
- Initial Query Syntax Lexer Implementation [\#12](https://github.com/NASA-PDS/pds-api/issues/12)
- Streamline testing of API server implementation [\#31](https://github.com/NASA-PDS/pds-api/issues/31)
- Identify a framework to generate python api client from a swagger file [\#11](https://github.com/NASA-PDS/pds-api/issues/11)
- Propose an initial server stub based on swagger output [\#10](https://github.com/NASA-PDS/pds-api/issues/10)
- Design and elicit requirements for PDS API Spec [\#8](https://github.com/NASA-PDS/pds-api/issues/8)
- Assign and iterate over applicable API spec sections with API WG [\#6](https://github.com/NASA-PDS/pds-api/issues/6)
- Define collection-level search parameters [\#5](https://github.com/NASA-PDS/pds-api/issues/5)
- Convert PDS API Spec to Open API [\#4](https://github.com/NASA-PDS/pds-api/issues/4)
- Design initial collection-level search API [\#1](https://github.com/NASA-PDS/pds-api/issues/1)

**Defects:**

- As a n00b paginator, there might be an off-by-1 error in the `limit` parameter [\#73](https://github.com/NASA-PDS/pds-api/issues/73) [[s.medium](https://github.com/NASA-PDS/pds-api/labels/s.medium)]

**Other closed issues:**

- Update Swagger OpenAPI with new `hits` and `took` fields [\#87](https://github.com/NASA-PDS/pds-api/issues/87)
- Propose an acceptable syntax for PDS4 Xpath in json object [\#39](https://github.com/NASA-PDS/pds-api/issues/39)
- Standardize management of empty attributes [\#38](https://github.com/NASA-PDS/pds-api/issues/38)
- Update public PDS API Spec in Github [\#33](https://github.com/NASA-PDS/pds-api/issues/33)
- Deploy PDS API v0 \(beta\) on pds-gamma test server [\#32](https://github.com/NASA-PDS/pds-api/issues/32)
- Document basic adaptation capabilities from pds-api-service [\#26](https://github.com/NASA-PDS/pds-api/issues/26)
- Define required response fields [\#20](https://github.com/NASA-PDS/pds-api/issues/20)
- Define default response fields [\#19](https://github.com/NASA-PDS/pds-api/issues/19)
- Refine format conventions defined by the API WG [\#18](https://github.com/NASA-PDS/pds-api/issues/18)
- Perform trade study on various query language parsers to meet needs of proposed API Spec [\#9](https://github.com/NASA-PDS/pds-api/issues/9)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
