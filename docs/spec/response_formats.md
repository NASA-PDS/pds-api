
DRAFT

# Response formats review


DRAFT

## Response wrappers for search queries:

Choose one among the following

### Current Response:

```json
{
  "summary": {},
  "data": []
}
```


### JSON API

see https://jsonapi.org/

```json
{
  "meta": {},
  "data": [] or {},
  or "errors": [],
}
```

### Google Search API

```json
{
  "responseData": {},
  "results": []
}
```

### PREFERRED

Freely inspired by CMR, see https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html

MIME type: `application/pds4+json` ?

```json
{
  "meta": {},
  "items": []
}

```


## Description Formats

The following format will be wrapped, nested in the above specification or on their own for single results as for LIDVID resolver.

Each of the following format are supported.

### KVP Response

MIME type: `application/kvp+json`

For users who know what they want:

```json
{
   "Product_Bundle.Identification_Area.logical_identifier": "urn:nasa:pds:insight_cameras",
   ...

}
```

### Short JSON Response:

MIME type: `application/json`

For users who want a structured response without knowing of PDS4 model

```json
{
  "id": "urn:nasa:pds:izenberg_pdart14_meap:data_eetable::2.0",
  "type": "Product_Collection",
  "title": "Izenberg PDART 2014 MESSENGER Advanced Products Energetic Electrons Table Collection",
  "start_date_time": "2011-03-25T00:00:00Z",
  "stop_date_time": "2015-04-30T00:00:00Z",
  "investigations": [
      {
          "id": "urn:nasa:pds:context:investigation:mission.messenger",
          "href": "http://localhost:8080/products/urn:nasa:pds:context:investigation:mission.messenger"
      }
  ],
  "observing_system_components": [
      {
          "id": "urn:nasa:pds:context:instrument_host:spacecraft.mess",
          "href": "http://localhost:8080/products/urn:nasa:pds:context:instrument_host:spacecraft.mess"
      },
      {
          "id": "urn:nasa:pds:context:instrument:ns.mess",
          "href": "http://localhost:8080/products/urn:nasa:pds:context:instrument:ns.mess"
      }
  ],
  "targets": [
      {
          "id": "urn:nasa:pds:context:target:planet.mercury",
          "href": "http://localhost:8080/products/urn:nasa:pds:context:target:planet.mercury"
      }
  ],
  "metadata": {
      "creation_date_time": "2016-04-08T00:00:00Z",
      "update_date_time": "2016-04-08T00:00:00Z",
      "version": "2.0",
      "label_url": "/Users/loubrieu/Documents/pds/registry/v11400.patched/dph_example_archive/data_eetable/collection_eetable_inventory.xml"
  }
}

```



###Full response (application/pds4+json)

For users who only trust the genuine original information:


```json
  {
    "id": "urn:nasa:pds:insight_cameras::7.0",
    "meta": {
      "file_size": 34534,
      "checksum": "fhfghx1224f"
    },
    "additional_meta": {
      "opus:": { ... }
      "analyst_notebook" : { ... }
      "dataCite" : { ... }
    },
    "pds4": {
       "Product_Bundle": {
          "Identification_Area": {
             "logical_identifier": "urn:nasa:pds:insight_cameras",
             "version_id": "7.0",
             "title": "InSight Cameras Bundle",
             "information_model_version": "1.11.1.0",
             "product_class": "Product_Bundle",
             "Citation_Information": {
                "author_list": "R. Deen, H. Abarca, P. Zamani, J.Maki",
                "publication_year": "2019",
                "description": "InSight Cameras Experiment Data Record (EDR) and Reduced Data Record (RDR) Data Products"
             }
          },
          "Context_Area": {
             "comment": "Observational Intent",
             "Time_Coordinates": {
                "start_date_time": "2020-07-05T14:15:07.441Z",
                "stop_date_time": "2020-10-05T02:02:53.219Z"
             },
             "Primary_Result_Summary": {
                "purpose": "Science",
                "processing_level": "Raw",
                "Science_Facets": {
                   "wavelength_range": "Visible",
                   "domain": "Surface",
                   "discipline_name": "Imaging"
                }
             },
             "Investigation_Area": {
                "name": "Insight",
                "type": "Mission",
                "Internal_Reference": {
                   "lid_reference": "urn:nasa:pds:context:investigation:mission.insight",
                   "reference_type": "bundle_to_investigation"
                }
             },
             "Observing_System": {
                "Observing_System_Component": [
                   {
                      "name": "Insight Lander",
                      "type": "Spacecraft",
                      "Internal_Reference": {
                         "lid_reference": "urn:nasa:pds:context:instrument_host:spacecraft.insight",
                         "reference_type": "is_instrument_host",
                         "comment": "Reference to the Insight spacecraft."
                      }
                   },
                   {
                      "name": "Insight Context Camera",
                      "type": "Instrument",
                      "Internal_Reference": {
                         "lid_reference": "urn:nasa:pds:context:instrument:icc.insight",
                         "reference_type": "is_instrument",
                         "comment": "Reference to the InSight Context Camera instrument onboard the InSight spacecraft."
                      }
                   },
                   {
                      "name": "Insight Deployment Camera",
                      "type": "Instrument",
                      "Internal_Reference": {
                         "lid_reference": "urn:nasa:pds:context:instrument:idc.insight",
                         "reference_type": "is_instrument",
                         "comment": "Reference to the InSight Deployment Camera instrument onboard the InsSight spacecraft."
                      }
                   }
                ]
             },
             "Target_Identification": {
                "name": "Mars",
                "type": "Planet",
                "Internal_Reference": {
                   "lid_reference": "urn:nasa:pds:context:target:planet.mars",
                   "reference_type": "document_to_target",
                   "comment": "Reference to the Planet - Mars target"
                }
             }
          },
          "Bundle": {
             "bundle_type": "Archive",
             "description": "This Bundle contains InSight camera data."
          },
          "Bundle_Member_Entry": [
             {
                "lid_reference": "urn:nasa:pds:insight_cameras:browse",
                "member_status": "Primary",
                "reference_type": "bundle_has_browse_collection"
             },
             {
                "lid_reference": "urn:nasa:pds:insight_cameras:calibration",
                "member_status": "Primary",
                "reference_type": "bundle_has_calibration_collection"
             },
             {
                "lid_reference": "urn:nasa:pds:insight_cameras:data",
                "member_status": "Primary",
                "reference_type": "bundle_has_data_collection"
             },
             {
                "lid_reference": "urn:nasa:pds:insight_cameras:document",
                "member_status": "Primary",
                "reference_type": "bundle_has_document_collection"
             },
             {
                "lid_reference": "urn:nasa:pds:insight_cameras:miscellaneous",
                "member_status": "Primary",
                "reference_type": "bundle_has_document_collection"
             },
             {
                "lid_reference": "urn:nasa:pds:insight_cameras:xml_schema",
                "member_status": "Primary",
                "reference_type": "bundle_has_schema_collection"
             }
          ],
          "_xmlns": "http://pds.nasa.gov/pds4/pds/v1",
          "_xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
          "_xsi:schemaLocation": "http://pds.nasa.gov/pds4/pds/v1 https://pds.nasa.gov/pds4/pds/v1/PDS4_PDS_1B10.xsd"
       }
    }
  }
]
}
```


# Alternate Formats

Candidates for implementation in the PDS API, as extensions, for interoperability purpose.

- schema.org/ datasets
- EPN-TAP
- PDAP
- Dublin-Core
- json-ld
- …
