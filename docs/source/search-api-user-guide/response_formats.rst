PDS Search API Response Formats
================================

Content Negociation
--------------------

A simple style of `content negotiation <https://restfulapi.net/content-negotiation/>`_ is used to
match the format requested by the client and the capability of the
server.

The client can specify the desired response format by including
the HTTP header `Accept`. If no `Accept` header is present in the request,
or if the requested content type is not available, the server will
provide the response in JSON format by default.

The following table provides a list of the supported HTTP Accept header
types:


+------------------------+--------+---------------------------------------------------+
| Accept Header          | Format | Note                                              |
+========================+========+===================================================+
| application/json       | JSON   | Simplified JSON view of the PDS4 metadata label.  |
|                        |        | Contains “flattened” PDS4 properties extracted    |
|                        |        | from the metadata label                           |
+------------------------+--------+---------------------------------------------------+
| application/xml        | XML    | Same as application/json, but in an XML           |
+------------------------+--------+---------------------------------------------------+
| application/           | JSON   | JSON response containing the full PDS4 metadata   |
| vnd.nasa.pds.pds4+json |        | translated to JSON, along with some additional    |
|                        |        | supplemental                                      |
+------------------------+--------+---------------------------------------------------+
| application/           | XML    | Same as application/vnd.nasa.pds.pds4+json,       |
| vnd.nasa.pds.pds4+xml  |        | but in an XML format. This response format        |
|                        |        | contains the original PDS4 labels.                |
+------------------------+--------+---------------------------------------------------+
| application/kvp+json   | JSON   | JSON response containing key-value-pairs for      |
|                        |        | the applicable metadata.                          |
+------------------------+--------+---------------------------------------------------+
| text/csv               | CSV    | Returns a CSV table containing values for the     |
|                        |        | parameters in the request. If no parameters were  |
|                        |        | specified in the request, a default set is        |
|                        |        | returned. The first row of the CSV is a header    |
|                        |        | that describes the values in each column.         |
+------------------------+--------+---------------------------------------------------+
| text/html              | HTML   | JSON response embedded in an HTML body. This      |
|                        |        | format is provided for requests coming from       |
|                        |        | the browers (e.g. Google Chrome) URL bar.         |
+------------------------+--------+---------------------------------------------------+


`application/vnd.nasa.pds.pds4+json` and `application/vnd.nasa.pds.pds4+xml` have been chosen to comply with `RFC6838 <https://datatracker.ietf.org/doc/html/rfc6838>`_

Examples
----------

application/json
~~~~~~~~~~~~~~~~~

The request:

.. code-block:: bash
   :substitutions:

    curl --location --request GET 'http://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight_rad::2.1' --header 'Accept: application/json'

Returns

.. code-block:: json

    {
        "id": "urn:nasa:pds:insight_rad::2.1",
        "type": "Product_Bundle",
        "title": "Mars InSight Lander Radiometer Data Archive",
        "start_date_time": "2018-05-05T00:00:00Z",
        "stop_date_time": "3000-01-01T00:00:00.000Z",
        "investigations": [
            {
                "id": "urn:nasa:pds:context:investigation:mission.insight",
                "href": "http://localhost:8080/products/urn:nasa:pds:context:investigation:mission.insight"
            }
        ],
        "observing_system_components": [
            {
                "id": "urn:nasa:pds:context:instrument_host:spacecraft.insight",
                "href": "http://localhost:8080/products/urn:nasa:pds:context:instrument_host:spacecraft.insight"
            },
            {
                "id": "urn:nasa:pds:context:instrument:radiometer.insight",
                "href": "http://localhost:8080/products/urn:nasa:pds:context:instrument:radiometer.insight"
            }
        ],
        "targets": [
            {
                "id": "urn:nasa:pds:context:target:planet.mars",
                "href": "http://localhost:8080/products/urn:nasa:pds:context:target:planet.mars"
            }
        ],
        "metadata": {
            "label_url": "/data/bundle_insight_rad.xml",
            "update_date_time": "2018-02-01T00:00:00Z",
            "version": "2.1"
        },
        "properties": {
            "pds:Stream_Text.pds:name": [
                "Introduction to the Radiometer Data Bundle"
            ],
            "pds:Modification_Detail.pds:description": [
                "Pre-peer review version",
                "First release",
                "The collections urn:nasa:pds:insight_rad:data_calibrated and urn:nasa:pds:insight_rad:data_derived were added to this bundle with InSight Release 1b.",
                "Changed Observing_System_Component name in this label from RAD to RADIOMETER to match context product name. Expanded Citation_Information description."
            ],
            "..."
            "pds:Investigation_Area.pds:type": [
                "Mission"
            ]
        }
    }


application/xml
~~~~~~~~~~~~~~~~~~

The request:

.. code-block:: bash
   :substitutions:

   curl --location --request GET 'http://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight_rad::2.1' --header 'Accept: application/xml'

Returns:

.. code-block:: xml

   <PdsProduct xmlns="http://pds.nasa.gov/api">
       <id>urn:nasa:pds:insight_rad::2.1</id>
       <type>Product_Bundle</type>
       <title>Mars InSight Lander Radiometer Data Archive</title>
       <description/>
       <start_date_time>2018-05-05T00:00:00Z</start_date_time>
       <stop_date_time>3000-01-01T00:00:00.000Z</stop_date_time>
       <investigations>
           <investigations>
               <title/>
               <id>urn:nasa:pds:context:investigation:mission.insight</id>
               <href>http://localhost:8080/products/urn:nasa:pds:context:investigation:mission.insight</href>
               <type/>
               <description/>
           </investigations>
       </investigations>
       <observing_system_components>
           <observing_system_components>
               <title/>
               <id>urn:nasa:pds:context:instrument_host:spacecraft.insight</id>
               <href>http://localhost:8080/products/urn:nasa:pds:context:instrument_host:spacecraft.insight</href>
               <type/>
               <description/>
           </observing_system_components>
           <observing_system_components>
               <title/>
               <id>urn:nasa:pds:context:instrument:radiometer.insight</id>
               <href>http://localhost:8080/products/urn:nasa:pds:context:instrument:radiometer.insight</href>
               <type/>
               <description/>
           </observing_system_components>
       </observing_system_components>
       <targets>
           <targets>
               <title/>
               <id>urn:nasa:pds:context:target:planet.mars</id>
               <href>http://localhost:8080/products/urn:nasa:pds:context:target:planet.mars</href>
               <type/>
               <description/>
           </targets>
       </targets>
       <metadata xmlns="">
           <archive_status xmlns="http://pds.nasa.gov/api"/>
           <creation_date_time xmlns="http://pds.nasa.gov/api"/>
           <label_url xmlns="http://pds.nasa.gov/api">/data/bundle_insight_rad.xml</label_url>
           <update_date_time xmlns="http://pds.nasa.gov/api">2018-02-01T00:00:00Z</update_date_time>
           <version xmlns="http://pds.nasa.gov/api">2.1</version>
       </metadata>
       <properties>
           <pds:Stream_Text.pds:name>Introduction to the Radiometer Data Bundle</pds:Stream_Text.pds:name>
           <pds:Modification_Detail.pds:description>Pre-peer review version</pds:Modification_Detail.pds:description>
           ...
           <pds:Investigation_Area.pds:type>Mission</pds:Investigation_Area.pds:type>
       </properties>
   </PdsProduct>


application/vnd.nasa.pds.pds4+json
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The request:

.. code-block:: bash
   :substitutions:

   curl --location --request GET 'http://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight_rad::2.1' --header 'Accept: application/vnd.nasa.pds.pds4+json'


Returns:

.. code-block:: json

   {
       "id": "urn:nasa:pds:insight_rad::2.1",
       "meta": {
           "node_name": "PDS_ENG",
           "ops:Label_File_Info": {
               "ops:file_name": "bundle_insight_rad.xml",
               "ops:file_ref": "/data/bundle_insight_rad.xml",
               "ops:creation_date": "2020-01-15T17:40:30Z",
               "ops:file_size": "6805",
               "ops:md5_checksum": "adfd86bbf2573c37d862e27e08f332db"
           },
           "ops:Data_Files": [
               {
                   "ops:file_name": "readme.txt",
                   "ops:file_ref": "/data/readme.txt",
                   "ops:creation_date": "2020-01-03T17:58:09Z",
                   "ops:file_size": "1114",
                   "ops:md5_checksum": "192de32c12437c180a9e14d60fe4b89a",
                   "ops:mime_type": "text/plain"
               }
           ],
           "ops:Tracking_Meta": [
               {
                   "ops:archive_status": "archived"
               }
           ]
       },
       "pds4": {
           "Product_Bundle": {
               "Identification_Area": {
                   "product_class": "Product_Bundle",
                   "Modification_History": {
                       "Modification_Detail": [
                           {
                               "modification_date": "2018-02-01",
                               "description": "Pre-peer review version",
                               "version_id": 0.1
                           },
                           {
                               "modification_date": "2019-04-22",
                               "description": "First release",
                               "version_id": 1
                           },
                           "..."
                       ]
                   },
                   "information_model_version": "1.11.0.0",
                   "logical_identifier": "urn:nasa:pds:insight_rad",
                   "version_id": 2.1,
                   "Citation_Information": {
                       "publication_year": 2018,
                       "description": "The InSight Radiometer data bundle consists of data in three collections:\r\n                data_raw, data_calibrated, and data_derived.\r\n                The bundle also includes the HP3/RAD Software Interface Specification in \r\n                the HP3/RAD document collection.",
                       "author_list": "InSight RAD Science Team",
                       "doi": "10.17189/1517568"
                   },
                   "title": "Mars InSight Lander Radiometer Data Archive"
               },
               "..."
           }
       }
   }

`pds4` property contains a translation in JSON of the PDS4 XML Label.


application/vnd.nasa.pds.pds4+xml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The request:

.. code-block:: bash
   :substitutions:

   curl --location --request GET 'http://pds.nasa.gov/api/search/|search_user_guide_api_version|/products/urn:nasa:pds:insight_rad::2.1' --header 'Accept: application/vnd.nasa.pds.pds4+xml'


Returns:

.. code-block:: xml

   <pds_api:product xmlns:pds_api="http://pds.nasa.gov/api" xmlns:ops="https://pds.nasa.gov/pds4/ops/v1">
       <pds_api:id>urn:nasa:pds:insight_rad::2.1</pds_api:id>
       <pds_api:meta>
           <node_name>PDS_ENG</node_name>
           <ops:Label_File_Info>
               <ops:file_name>bundle_insight_rad.xml</ops:file_name>
               <ops:file_ref>/data/bundle_insight_rad.xml</ops:file_ref>
               <ops:creation_date>2020-01-15T17:40:30Z</ops:creation_date>
               <ops:file_size>6805</ops:file_size>
               <ops:md5_checksum>adfd86bbf2573c37d862e27e08f332db</ops:md5_checksum>
           </ops:Label_File_Info>
           <ops:Data_Files>
               <ops:Data_Files>
                   <ops:file_name>readme.txt</ops:file_name>
                   <ops:file_ref>/data/readme.txt</ops:file_ref>
                   <ops:creation_date>2020-01-03T17:58:09Z</ops:creation_date>
                   <ops:file_size>1114</ops:file_size>
                   <ops:md5_checksum>192de32c12437c180a9e14d60fe4b89a</ops:md5_checksum>
                   <ops:mime_type>text/plain</ops:mime_type>
               </ops:Data_Files>
           </ops:Data_Files>
           <ops:Tracking_Meta>
               <ops:Tracking_Meta>
                   <ops:archive_status>archived</ops:archive_status>
               </ops:Tracking_Meta>
           </ops:Tracking_Meta>
       </pds_api:meta>
       <pds_api:pds4>
           <Product_Bundle
       xmlns="http://pds.nasa.gov/pds4/pds/v1"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://pds.nasa.gov/pds4/pds/v1 https://pds.nasa.gov/pds4/pds/v1/PDS4_PDS_1B00.xsd">
               <Identification_Area>
                   <logical_identifier>urn:nasa:pds:insight_rad</logical_identifier>
                   <version_id>2.1</version_id>
                   <title>Mars InSight Lander Radiometer Data Archive</title>
                   <information_model_version>1.11.0.0</information_model_version>
                   <product_class>Product_Bundle</product_class>
                   <Citation_Information>
                       <author_list>InSight RAD Science Team</author_list>
                       <publication_year>2018</publication_year>
                       <doi>10.17189/1517568</doi>
                       <description>
                   The InSight Radiometer data bundle consists of data in three collections:
                   data_raw, data_calibrated, and data_derived.
                   The bundle also includes the HP3/RAD Software Interface Specification in
                   the HP3/RAD document collection.
               </description>
                   </Citation_Information>
                  ...
               </Identification_Area>
              ...
           </Product_Bundle>
       </pds_api:pds4>
   </pds_api:product>


The tag `pds_api:pds4` contains the XML PDS4 label.


application/kvp+xml
~~~~~~~~~~~~~~~~~~~~~

This format is useful when one only need a few fields from the metadata.

The request:

.. code-block:: bash
   :substitutions:

   curl --location --request GET 'http://pds.nasa.gov/api/search/|search_user_guide_api_version|/products?limit=10&fields=lidvid&fields=title' --header 'Accept: application/kvp+json'

Returns:

.. code-block:: json

 {
    "summary": {
        "q": "",
        "hits": 17,
        "took": 55,
        "start": 0,
        "limit": 10,
        "sort": [],
        "properties": [
            "lidvid",
            "title"
        ]
    },
    "data": [
        {
            "lidvid": "urn:nasa:pds:insight_rad:data_derived::7.0",
            "title": "InSight RAD Derived Data Collection"
        },
        {
            "lidvid": "urn:nasa:pds:insight_rad:data_raw::8.0",
            "title": "InSight RAD Raw Data Collection"
        },
        "..."
    ]
}


text/csv
~~~~~~~~~

This format is useful when one only need a few fields from the metadata.

The request:

.. code-block:: bash
   :substitutions:

   curl --location --request GET 'http://pds.nasa.gov/api/search/|search_user_guide_api_version|/products?limit=10&fields=lidvid&fields=title' --header 'Accept: text/csv'

Returns:

.. code-block:: text

   lidvid,title
   "urn:nasa:pds:insight_rad:data_derived::7.0","InSight RAD Derived Data Collection"
   "urn:nasa:pds:insight_rad:data_raw::8.0","InSight RAD Raw Data Collection"
   "urn:nasa:pds:insight_rad:data_derived:hp3_rad_der_00014_20181211_073042::1.0","InSight HP3 Radiometer Experiment Derived Product:hp3_rad_der_00014_20181211_073042"
   ...


Open Data
~~~~~~~~~~~

NOT IMPLEMENTED

See
[<u>https://project-open-data.cio.gov/</u>](https://project-open-data.cio.gov/)
and example of application at
[<u>https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html\#open-data</u>](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html#open-data)


Missing values
----------------

Properties with empty or null values should be dropped from the JSON
response unless the user asked specifically for the field (through
`field` API parameter). In this case the value must be **null**,
without quotes.

**Rationale**

If a property is optional or has an empty or null value, consider dropping the property from the JSON, unless there's a strong semantic reason for its existence (taken from this `discussion <https://softwareengineering.stackexchange.com/questions/285010/null-vs-missing-key-in-rest-api-response>`_)

Following interactions with OGC/EDR specification group: `https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/issues/171\#issuecomment-767805902 <https://github.com/opengeospatial/ogcapi-environmental-data-retrieval/issues/171#issuecomment-767805902>`_

We choose **null** without quotes for missing values of fields explicitly requested by the user.

We conform to EDR specification for this aspect, see
[http://docs.opengeospatial.org/DRAFTS/19-086.html\#req\_edr\_parameters-response</u>](http://docs.opengeospatial.org/DRAFTS/19-086.html#req_edr_parameters-response)

This should not be mistaken for an actual PDS4 value since missing
values in PDS4 labels. are detailed with a nil:reason attribute.