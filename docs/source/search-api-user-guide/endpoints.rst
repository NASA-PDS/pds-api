PDS Search API Endpoints and Search Terms
=========================================

Endpoints
---------

The base URIs for performing GET requests for searching PDS data are as follows.

**For collection-level search:**

*Template:* ::

    GET https://{node-hostname}/api/{service}/{pds.api.version}/collections?{searchTerms}


*Examples:*

Search All PDS Data Collections: ::

    GET https://pds-gamma.jpl.nasa.gov/api/search/0.1/collections?{searchTerms}

Search Geosciences Node Collections: ::

    GET https://pds-gamma.jpl.nasa.gov/api/search-geo/0.1/collections?{searchTerms}


**For product-level search:**

*Template:* ::

    GET https://{node-hostname}/api/{service}/{pds.api.version}/products?{searchTerms}

*Examples:*

Search All PDS Data Products: ::

    GET https://pds-gamma.jpl.nasa.gov/api/search/0.1/products?{searchTerms}

Search Geosciences Node: ::

    GET https://pds-gamma.jpl.nasa.gov/api/search-geo/0.1/products?{searchTerms}


Search Terms
------------

The following search terms can be passed after the ? sign as shown in the following examples with actual search terms. ::

    GET https://pds-gamma.jpl.nasa.gov/api/search/0.1/collections?q="2018-01-01" le Time_Coordinates.start_date_time le "2020-01-01"&start=100&limit=1000

    GET https://pds-gamma.jpl.nasa.gov/api/search/0.1/products?q=pds:Observing_System_Component.pds:type eq "Spacecraft" and (Optical_Filter.filter_name eq "BL1" or Optical_Filter.filter_name eq "GRN")&fields=cassini.spacecraft_clock_start_count


**Query String Operations**

The PDS Search API supports the following minimal set of operations.

======================= ======================= ============
 **Operator**            **Description**        **Example**
======================= ======================= ============
 *Comparison Operators*                                                                                                                                                   
 eq                      Equal                  target\_name **eq** "Mars"                                                                                                
 ne                      Not equal              target\_name **ne** "Saturn"                                                                                              
 gt                      Greater than           Time\_Coordinates.start\_date\_time **gt** 2001-05-10T00:00:00Z                                                         
 ge                      Greater than or equal  Time\_Coordinates.start\_date\_time **ge** 2001-05-10T00:00:00Z                                                         
 lt                      Less than              Time\_Coordinates.start\_date\_time **lt** 2020-06-01T00:00:00Z                                                         
 le                      Less than or equal     Time\_Coordinates.start\_date\_time **le** 2020-06-01T00:00:00Z                                                         
 *Logical Operators*                                                                                                                                                      
 and                     Logical and            target\_name **eq** "Mars" **and** instrument\_name **eq** "hirise"                                                     
 or                      Logical or             target\_name **eq** "Mars" **or** target\_name **eq** "Phobos"                                                          
 not                     Logical negation       **not** target\_name **eq** "Mars"                                                                                      
 *Grouping Operators*                                                                                                                                                     
 ( )                     Precedence grouping    (target\_name **eq** "Mars" **or** target\_name **eq** "Phobos"**)** **and** instrument\_name **eq** "hirise"
======================= ======================= ============

**Reserved Query Parameters**

The following are a table of reserved query parameters that have special meaning to support search.

====================  ===============
 **Query Parameter**  **Description**                                                                                                                                                                                                     **Example**                                                
====================  ===============
 q                    (Required, string) Query string you wish to parse and use for search. See Query string syntax.                                                                                                                      `q=target_name eq "Mars"`
 fields               (Optional, array of strings) Array of fields you wish to return.                                                                                                                                                    `fields=lid,Time_Coordinates.start_date_time`           
 start                (Optional, integer, default=0) The search result to start with in the returned records. For instance, start=10 will return records 10-19.                                                                           `start=100`                                                
 limit                (Optional, integer) The number of records/results to return. Defaults to 25.                                                                                                                                        `limit=100`                                                
 sort                 (Optional, string, default=LIDVID) Field to sort on and whether it should be sorted ascending (ASC) or descending (DESC). `fieldName asc` or `fieldName desc`. There can be several sort parameters (order is important).  `sort=lidvid asc, Time_Coordinates.start_date_time desc` 
====================  ===============

More details are available at `PDS API Specification </pds-api/docs/build/search-api-user-guide/pds-api-specification.pdf>`_.
