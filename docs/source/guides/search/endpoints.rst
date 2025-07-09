Query Syntax
============

.. Warning::
   Since our servers are not fully populated with all PDS data sets, the examples presented in this user guide may return empty results or 404 (Not Found) errors. If there is a data set you would like added, please contact the `PDS Help Desk <mailto:pds-operator@jpl.nasa.gov>`_ for assistance.

.. Note::
   curl command line tool is used to request the API in this documentation. curl is available in many operating systems by default. If not, you can get curl from https://curl.se/ or using a package management tool specific to your operating system (brew, apt, ...).

Endpoints
---------

The URLs for performing GET requests for searching PDS data are as follows.

The **base URL** of the PDS Search API, for search across all the PDS nodes, is:

.. code-block::
   :substitutions:

    https://pds.nasa.gov/api/search/|search_user_guide_api_version|/

The main use cases, to search, crawl products or resolve a product identifier are given in the following sections.

Search Products
----------------

Request Examples
~~~~~~~~~~~~~~~~~~~~

Get the list of properties which describe the products, which criteria you can search against:

.. code-block:: bash
   :substitutions:

    curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/properties'


Search for products which processing level is "Raw", using the property "pds:Primary_Result_Summary.pds:processing_level" found before, get 10 results:

.. code-block:: bash
   :substitutions:

   curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products' \
       --data-urlencode 'limit=10' \
       --data-urlencode 'q=(pds:Primary_Result_Summary.pds:processing_level eq "Raw")'




Request Template
~~~~~~~~~~~~~~~~~~

The requests template is a follow:

.. code-block:: http
   :substitutions:

   GET /api/search/|search_user_guide_api_version|/classes/{product_class}[?[{query-parameter}={query-parameter-value}]*] HTTP/1.1
   Host: pds.nasa.gov

The list of `product_class` proposed by the API can also be found from URL:

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/classes



The concept of product class is derived from the `PDS4 standard <https://pds.nasa.gov/datastandards/documents/im/current/index_1I00.html>`_.


Query Detailed Syntax
~~~~~~~~~~~~~~~~~~~~~~

Query Parameters
..................

The query parameters are:

====================  =========================================================================================================================================================================================================================== ====================
 **Query Parameter**  **Description**                                                                                                                                                                                                             **Example**
====================  =========================================================================================================================================================================================================================== ====================
 q                    (Optional, string) Query string you wish to parse and use for search. See `query string syntax`_                                                                                                                             q=target_name eq "Mars"
 keywords             (Optional, string) String used for text search on title and description of the PDS4 labels                                                                                                                                   keyword=insight
 fields               (Optional, array of strings) Array of fields you wish to return.                                                                                                                                                             fields=pds:Time_Coordinates.pds:start_date_time
 sort                 (Optional, array of strings) Array of fields you wish to sort by, mandatory when search-after is used                                                                                                                        sort=ops:Harvest_Info.ops:harvest_date_time
 search-after         (Optional, string or number) For pagination, the page will start from the value of the field selected in `sort`.                                                                                                             search-after=2024-01-23T22:53:30.402453Z
 limit                (Optional, integer, default=100) The number of records/results to return. By specifying a value of 0 only the summary of the results is returned, not the individual results.                                                limit=100
 facet-fields         (Optional, array of strings) fields which are faceted: in summary, the count of the unique value used for the fields is given.                                                                                               product_class,ops:Harvest_Info.ops:node_name
 facet-limit          (Optional, integer) maximum number of unique values counted for all faceted fields. Default is 10.                                                                                                                           20
====================  =========================================================================================================================================================================================================================== ====================

`q`, `fields` and `facet-fields` use PDS4 `Fields Dot Notation`_

Query String Syntax
...................

An example of query syntax (`q` query parameter) is:

For example:

.. code-block::

   ((pds:Primary_Result_Summary.pds:processing_level eq "Raw") and not (ops:Data_File_Info.ops:file_size ge 8942))

The query syntax follows the rules:

.. code-block::

   {query} = {comparison}|{group}

   {comparison} = {field} {comparison operator} {literal value}

   {group} = [not] ({comparison} [[and|or] {group}])


* **{field}** follows the `Fields Dot Notation`_ . The available fields can be found in responses `summary` object, `properties` attribute.
* **{comparison operator}** are eq, ne, gt, lt, ge, le
* **{literal value}** is either a string between ``"`` (double quotes) or a numerical value (float or integer).
* Wildcard searching is available with the **like** operator. The wildcarding syntax of the **{literal value}** follows the [OpenSearch Simple Query String](https://opensearch.org/docs/latest/opensearch/query-dsl/full-text/#simple-query-string) convention.
* **{group}** has mandatory parentheses (round brackets) which make any complex query loaded with parentheses, as seen in the example above, don't forget them !

.. warning::
  the ``like`` operator does not work because of a known `bug <https://github.com/NASA-PDS/registry-api/issues/170>`_

======================= =========================== ============
 **Operator**            **Description**            **Example**
======================= =========================== ============
 *Comparison Operators*
 eq                      Equal                       target\_name **eq** "Mars"
 like                    Similar to                  target\_name **like** "mars"
 ne                      Not equal                   target\_name **ne** "Saturn"
 gt                      Greater than                pds:Time\_Coordinates.pds:start\_date\_time **gt** "2001-05-10T00:00:00Z"
 ge                      Greater than or equal       pds:Time\_Coordinates.pds:start\_date\_time **ge** "2001-05-10T00:00:00Z"
 lt                      Less than                   pds:Time\_Coordinates.pds:start\_date\_time **lt** "2020-06-01T00:00:00Z"
 le                      Less than or equal          pds:Time\_Coordinates.pds:start\_date\_time **le** "2020-06-01T00:00:00Z"
 *Logical Operators*
 and                     Logical and                 target\_name **eq** "Mars" **and** instrument\_name **eq** "hirise"
 or                      Logical or                  target\_name **eq** "Mars" **or** target\_name **eq** "Phobos"
 not                     Logical negation            **not** target\_name **eq** "Mars"
 *Grouping Operators*
 ( )                     Precedence grouping         ((target\_name **eq** "Mars" **or** target\_name **eq** "Phobos"**)** **and** ( instrument\_name **eq** "hirise" ))
======================= =========================== ============




Fields Dot Notation
...................

General Case
,,,,,,,,,,,,,

The syntax of the field names use a combination of the PDS4 Information Model and `dot
notation <http://reeborg.ca/docs/oop_py_en/oop.html>`_ representations of
an XML XPaths.

Query parameters will use a combination of an attribute with its parent
class in *all lowercase*:

.. code-block::

   {namespace:parent_class}.{namespace:attribute}

For example:

.. code-block::

    pds:Science_Facets.pds:discipline_name
    pds:Investigation_Area.pds:type

The classes and attributes are defined in the `PDS4 Data Dictionnaries <https://pds.nasa.gov/datastandards/dictionaries/index-1.18.0.0.shtml>`_.

The PDS4 data dictionaries are augmented with a specific  :ref:`ops Namespace` which contains attributes managed by the `PDS Registry <https://nasa-pds.github.io/registry/>`_ in addition to the PDS4 labels attributes.



.. role:: not-implemented


:not-implemented:`NOT IMPLEMENTED`

:not-implemented:`In the event that the {parent\_class}.{attribute} combination does`
:not-implemented:`sufficiently guarantee uniqueness or sufficiency of search when a class`
:not-implemented:`is inherited by multiple classes, additional ancestor classes should be`
:not-implemented:`prepended to the query parameter until sufficient uniqueness is`
:not-implemented:`attained:`

:not-implemented:`{ns:ancestor\_class}.{ns:parent\_class}.{ns:attribute}`

:not-implemented:`If the query parameter grows beyond 3 ancestor classes, a :ref:custom`
:not-implemented:`query parameter <Custom Query Parameters> should be considered.`


:not-implemented:`In the event that multiple attributes are to be grouped together for`
:not-implemented:`search, the parent class should be used as the query parameter:`

:not-implemented:`{ancestor\_class}.{parent\_class}`

Custom Query Parameters
,,,,,,,,,,,,,,,,,,,,,,,,

:not-implemented:`NOT IMPLEMENTED`

:not-implemented:`There are several cases where custom query parameters are preferred over`
:not-implemented:`the Dot Notation, but should only be avoided wherever possible in order`
:not-implemented:`to minimize confusion amongst developers attempting to use the API.`
:not-implemented:`These are also subject to approval by Search Integration Working Group`
:not-implemented:`representative for each node. That member is responsible for providing`
:not-implemented:`those updates to Engineering Node.`

:not-implemented:`Some reasons for custom query parameters:`

:not-implemented:`-   Combination of multiple attribute values into one`

:not-implemented:`-   Special cases where XQuery needs to be used for finding specific values (e.g. instrument/spacecraft described in Observing\_System\_Component class)`

:not-implemented:`-   Custom search fields on non-PDS4 metadata (e.g. image tags, operations note, etc.)`

:not-implemented:`-   Support common search or PDS4 terminology (e.g. target\_name, lidvid)`


Resolve A Product Identifier
-----------------------------

Default Resolution
~~~~~~~~~~~~~~~~~~~~

If you know the lid (for example `urn:nasa:pds:insight_rad`) or lidvid (for example `urn:nasa:pds:insight_rad::2.1`) identifier of a product, you can retrieve its description, whereever it is managed in the PDS system, with the following request:

.. code-block:: bash
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/{identifier}

For example

.. code-block:: bash
   :substitutions:

   curl --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight_rad::2.1' \
       --header 'Accept: application/json'


Search for Latest vs. All Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Latest Version
................

By default, when the identifier is a lid (without a version, for example urn:nasa:pds:insight_rad) only the latest description of the product is returned.

The request:

.. code-block:: bash
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/{lid}


Crawl a Data Set Hierarchy
--------------------------

For a given product with identifier `lidvid1`, you can browse its parent products (member-of) or children (members).

Get the Collections of a Bundle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get its **children** (collections):

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/lidvid1/members

For example, run:

.. code-block:: bash
   :substitutions:

   curl --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight_rad::2.1/members' \
       --header 'Accept: application/json'

The same request can be used to get the observational products or documents of a collection from the collection's lidvid.


Get the Observational Products of a Bundle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/lidvid1/members/members


For example, run:

.. code-block:: bash
   :substitutions:

   curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight_rad::2.1/members/members' \
       --header 'Accept: application/json'


Get the Collection or Bundles of an Observational Product
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get its **parent** (collection):

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/lidvid1/member-of

The same request can be used to get the bundles of a collection from the collection's lidvid.

Get its **grandparent** (bundle):

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/lidvid1/member-of/member-of


For example, run:

.. code-block:: bash
   :substitutions:

   curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight_rad:data_raw:hp3_rad_raw_00004_20181130_085325/member-of/member-of' \
       --header 'Accept: application/json'


Use pagination to get all products matching a request
-------------------------------------------------------

When you're searching for a large number of products, you'll need to use pagination to ensure you receive all the results. Here's how you can do it.

.. Note::
   The pagination parameters (sort, limit, search-after) described in this section are applicable to all the end-points.

To start, let's say you want to get all the members of a collection named "OSIRIS-REX Spectrometer calibrated observations", which identifier is *urn:nasa:pds:orex.ovirs:data_calibrated::11.0*. You can use the following request in a web browser:

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:orex.ovirs:data_calibrated::11.0/members

This request will only give you the first 100 products out of the total available in the collection (in this example, 334,940 products).

To get all the results, you need to use the pagination.

**1. Make the Initial Request:**

Sort the results by the harvest time, which is the time when products were loaded into the registry. You can do this using the *curl* command:

.. code-block:: bash
   :substitutions:

   curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:orex.ovirs:data_calibrated::11.0/members' \
      --header 'Accept: application/json' \
      --data-urlencode 'sort=ops:Harvest_Info.ops:harvest_date_time'

You are getting the first 100 products, members of the collection, sorted by harvest time (time when they were loaded in the registry).

**2. Get the Next Page**

To retrieve the next set of results, you need to get the latest harvest date and time from the previous response. This information is included in the description of the last product returned.

.. code-block:: json

   "ops:Harvest_Info.ops:harvest_date_time": [
      "2023-05-26T05:53:24.611495Z"
   ],


Use this latest harvest date and time as the reference for the next request:

.. code-block:: bash
   :substitutions:

   curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:orex.ovirs:data_calibrated::11.0/members' \
      --header 'Accept: application/json' \
      --data-urlencode 'sort=ops:Harvest_Info.ops:harvest_date_time' \
      --data-urlencode 'search-after=2023-05-26T05:53:24.611495Z'

**3. Iterate Until Completion:**

Keep making requests and updating the *search-after* parameter with the latest harvest date and time until the number of products returned is less than the limit (100 in this case).


**4. Changing Pagination Parameters:**

You can adjust the default limit of 100 products per page using the limit parameter. For example:

.. code-block:: bash
   :substitutions:

   curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:orex.ovirs:data_calibrated::11.0/members' \
      --header 'Accept: application/json' \
      --data-urlencode 'limit=500' \
      --data-urlencode 'sort=ops:Harvest_Info.ops:harvest_date_time' \
      --data-urlencode 'search-after=2023-05-26T05:53:24.611495Z'




.. Note::
   The number of products per page, specified by the limit parameter should be below a few 1000s. If the queries are too demanding for the server, you might experience `504 errors <https://github.com/NASA-PDS/registry-api/discussions/521>`_ . The optimal number of product per page for quicker data retrieval depends on the type of response requested, as shown in statistics on `pagination performances <https://github.com/NASA-PDS/registry-api/issues/552#issuecomment-2389199054>`_.




Get facets for a subset of the PDS archive
-------------------------------------------------------

Faceted search gives you an overview of the results returned by a query. For specified fields, the API response includes a list of the values found in the result set, along with the number of products associated with each value. These are called *facets*.

You can facet on multiple fields.

By default, the API returns the top 10 values (i.e., the most frequently occurring) for each faceted field. This default can be overridden using the `facet-limit` parameter.

The following example retrieves the 100 most referenced investigation and target LIDVIDs across the entire archive:


.. code-block:: bash
   :substitutions:

   curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products' \
      --header 'Accept: application/json' \
      --data-urlencode 'limit=0' \
      --data-urlencode 'facet-fields=ref_lid_investigation,ref_lid_target' \
      --data-urlencode 'facet-limit=100'


You can also apply faceted search to a subset of the PDS archive. The following example lists the most frequently referenced targets associated with the *Ultraviolet Imaging Spectrograph* instrument on the *Cassini Orbiter*, using its LID `urn:nasa:pds:context:instrument:uvis.co`:

.. code-block:: bash
   :substitutions:

   curl -L --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products' \
      --header 'Accept: application/json' \
      --data-urlencode 'limit=0' \
      --data-urlencode 'q=ref_lid_instrument eq "urn:nasa:pds:context:instrument:uvis.co"' \
      --data-urlencode 'facet-fields=ref_lid_target' \
      --data-urlencode 'facet-limit=100' \
      --data-urlencode 'limit=0'