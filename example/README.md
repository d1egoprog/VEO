# Usage Guide for the Volcano Event Ontology (VEO)

## Introduction

This guide explains how to integrate and utilize the Volcano Event Ontology (VEO) in your projects. VEO is designed to represent seismic events, their characteristics, and related data such as geographic and temporal details.

## Prerequisites

To use VEO in your project, ensure the following:
- A triple store (e.g., Apache Jena, Blazegraph) or an ontology editor (e.g., Protégé) is installed.
- Familiarity with RDF, OWL, and SPARQL is recommended.
- An RDF library for your chosen programming language is helpful (e.g., RDFLib for Python, Jena for Java).

## Loading the Ontology

### 1. Using Protégé

1. Open Protégé.
2. Click **File > Open from URL**.
3. Enter the VEO ontology URL: `http://www.github.com/d1egoprog/VEO`
4. Load and explore the ontology.

### 2. Using a Triple Store

1. Import the ontology into your triple store via the SPARQL endpoint or admin interface.
2. Run SPARQL queries to interact with the ontology.

## Usage Example

Here’s an example illustrating how to use VEO to represent a volcanic event:

``` Turtle
@prefix veo: <http://example.org/veo#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix geo1: <http://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix time: <http://www.w3.org/2006/time#> .

veo:Event_123 a veo:VolcanoTectonic ;
    veo:eventID "EVT123" ;
    veo:timestamp "2024-11-20T10:30:00Z"^^xsd:dateTime ;
    veo:magnitude 4.8 ;
    veo:depth 12.5 ;
    veo:occurredAt geo1:Location_1 ;
    veo:hasAlertLevel veo:AlertLevel_High .

geo1:Location_1 a geo1:SpatialThing ;
    geo1:lat "37.75"^^xsd:decimal ;
    geo1:long "-122.68"^^xsd:decimal .
```

## SPARQL Query Examples

Run some queries over the Knowledge Graph 

### Loading the Knowledge Graph 

To load the knowledge graph into a Python environment, you can use the rdflib library, which supports the TTL format.

### Example 1: Retrieve All Events and Their Magnitudes

``` SPARQL
PREFIX veo: <http://www.github.com/d1egoprog/VEO/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?event ?magnitude
WHERE {
  ?event a veo:Event ;
         veo:magnitude ?magnitude .
}
```

### Example 2: Find Stations Hosting Sensors

``` SPARQL
PREFIX veo: <http://www.github.com/d1egoprog/VEO/>
PREFIX sosa: <http://www.w3.org/ns/sosa/>

SELECT ?station ?sensor
WHERE {
  ?station veo:isComposedBy ?sensor .
}
```

### Predefined Queries

Some specific and prepared queries are in the [Query folder](queries/), they cam be executed using the prepared [script](query_sparql.py)

## Best Practices

- **Namespace Management:** Use standard prefixes to ensure clarity in SPARQL queries.
- **Documentation:** Keep your usage examples updated to assist new users.
- **Validation:** Regularly validate your data using tools like SHACL to ensure conformance to VEO.