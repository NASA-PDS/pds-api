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

For specific discipline node search, there are node-specific endpoints available giving access to products of one node, for example:

.. code-block::
   :substitutions:

    https://pds.nasa.gov/api/search-geo/|search_user_guide_api_version|/

Where ``geo`` is the **Node ID**

The **Node IDs** are:

=============  ========================================
Node ID        Node Name
=============  ========================================
atm            Atmospheres
en             Engineering
geo            Geosciences
img            Imaging
naif           Navigation and Ancillary Information
ppi            Planetary Plasma Interactions
rms            Ring-Moon Systems
sbnumd         Small Bodies, Comets
sbnpsi         Small Bodies, Asteroids/Dust
=============  ========================================

The main use cases, to search, crawl products or resolve a product identifier are given in the following sections.

Search Products
----------------

Request Example
~~~~~~~~~~~~~~~~~~~~

Search for the 10 latest collections which processing level is "Raw":

.. code-block:: bash
   :substitutions:

   curl --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/collections' \
       --data-urlencode 'limit=10' \
       --data-urlencode 'q=(pds:Primary_Result_Summary.pds:processing_level eq "Raw")'




Request Template
~~~~~~~~~~~~~~~~~~

The requests template is a follow:

.. code-block:: http
   :substitutions:

   GET https://pds.nasa.gov/api/search/|search_user_guide_api_version|/{product_class}[?[{query-parameter}={query-parameter-value}]*]

Where `product_class` is one of:

* **products**: search among all classes of products (observational products, collections, bundles...)
* **collections**: search among products which class is product_collection
* **bundles**: search among products which class is product_bundle

The concept of product class is derived from the `PDS4 standard <https://pds.nasa.gov/datastandards/documents/im/current/index_1I00.html>`_.

Query Detailed Syntax
~~~~~~~~~~~~~~~~~~~~~~

Query Parameters
..................

The query parameters are:

====================  =========================================================================================================================================================================================================================== ====================
 **Query Parameter**  **Description**                                                                                                                                                                                                             **Example**
====================  =========================================================================================================================================================================================================================== ====================
 q                    (Optional, string) Query string you wish to parse and use for search. See `query string syntax`_                                                                                                                            q=target_name eq "Mars"
 keyword              (Optional, string) String used for text search on title and description of the PDS4 labels                                                                                                                                  keyword=insight
 fields               (Optional, array of strings) Array of fields you wish to return.                                                                                                                                                            fields=lid,pds:Time_Coordinates.pds:start_date_time
 start                (Optional, integer, default=0) The search result to start with in the returned records. For instance, start=10 will return records 10-19. Useful for pagination of the results.                                             start=100
 limit                (Optional, integer, default=100) The number of records/results to return.                                                                                                                                                   limit=100
 sort                 (Optional, string, default=LIDVID) Field to sort on and whether it should be sorted ascending (ASC) or descending (DESC). `fieldName asc` or `fieldName desc`. There can be several sort parameters (order is important).   sort=lidvid asc, pds:Time_Coordinates.pds:start_date_time desc
 summary-only         (Optional, boolean, default=False) When true, only the summary of the results is returned, not the individual results                                                                                                       true
====================  =========================================================================================================================================================================================================================== ====================

`q` and `fields` use PDS4 `Fields Dot Notation`_

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
* **{literal value}** is either a string between ``"`` (double quotes) or a numerical value (float or integer). Wildcards (\*, ?) are supported in strings.

======================= =========================== ============
 **Operator**            **Description**            **Example**
======================= =========================== ============
 *Comparison Operators*
 eq                      Equal                       target\_name **eq** "Mars"
 ne                      Not equal                   target\_name **ne** "Saturn"
 gt                      Greater than                pds:Time\_Coordinates.pds:start\_date\_time **gt** 2001-05-10T00:00:00Z
 ge                      Greater than or equal       pds:Time\_Coordinates.pds:start\_date\_time **ge** 2001-05-10T00:00:00Z
 lt                      Less than                   pds:Time\_Coordinates.pds:start\_date\_time **lt** 2020-06-01T00:00:00Z
 le                      Less than or equal          pds:Time\_Coordinates.pds:start\_date\_time **le** 2020-06-01T00:00:00Z
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

is equivalent to:

.. code-block:: bash
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/{lid}/latest


All Versions
..............

If you want to retrieve **all** the versions of a product, the request is:

.. code-block:: bash
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/{lid}/all


The `all` and `latest` suffixes apply also to all the crawling end-points which description follows.


Crawl a Data Set Hierarchy
--------------------------

For a given product with identifier `lidvid1`, you can browse its parent products or children.


If the Product ‘lidvid1’ Is a Bundle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get its **collections**:

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/bundles/lidvid1/collections[/[all|latest]]


For example, run:

.. code-block:: bash
   :substitutions:

   curl --get 'https://pds.nasa.gov/api/search/|search_user_guide_api_version|/bundles/urn:nasa:pds:insight_rad::2.1/collections' \
       --header 'Accept: application/json'


Get its **observational products**:

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/bundles/lidvid1/products[/[all|latest]]


If the Product ‘lidvid1’ Is a Collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get its **bundle**:

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/collections/lidvid1/bundles[/[all|latest]]

Get its **observational products**:

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/collections/lidvid1/products[/[all|latest]]


If the Product ‘lidvid1’ Is an Observational Product
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get its **bundle**:

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/lidvid1/bundles[/[all|latest]]

Get its **collection**:

.. code-block::
   :substitutions:

   https://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/lidvid1/collections[/[all|latest]]




