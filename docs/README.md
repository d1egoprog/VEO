# Ontology Documentation: Volcano Event Ontology (VEO)

## Namespaces

The VEO ontology utilizes a combination of well-known and custom namespaces to ensure semantic clarity and interoperability with other ontologies. Below is a list of the namespaces used:

| Prefix | URI                                                 | Description                                                      |
|--------|-----------------------------------------------------|------------------------------------------------------------------|
| dcterms | <http://purl.org/dc/terms/>                        | Dublin Core Metadata Terms for resource description.              |
| geo1    | <http://www.w3.org/2003/01/geo/wgs84_pos#>         | Geo vocabulary for geographical locations.                        |
| owl     | <http://www.w3.org/2002/07/owl#>                   | Web Ontology Language for ontology creation and reasoning.        |
| rdf     | <http://www.w3.org/1999/02/22-rdf-syntax-ns#>      | RDF syntax vocabulary.                                           |
| rdfs    | <http://www.w3.org/2000/01/rdf-schema#>            | RDF Schema vocabulary for structural metadata.                    |
| sosa    | <http://www.w3.org/ns/sosa/>                       | Sensor, Observation, Sample, and Actuator Ontology.               |
| time    | <http://www.w3.org/2006/time#>                     | Temporal ontology for time-based representations.                 |
| vann    | <http://purl.org/vocab/vann/>                      | Vocabulary of a Friend (VANN) for metadata versioning.            |
| veo     | <http://example.org/veo#>                          | Custom namespace for the Volcano Event Ontology.                  |
| xsd     | <http://www.w3.org/2001/XMLSchema#>                | XML Schema for data types.                                       |

## Classes

### `veo:Event`

- **Label**: Event  
- **Comment**: Represents a seismic or volcanic event, encompassing various event types like blasts, earthquakes, and background noise.
- **Subclasses**:  
  - `veo:Blast` - Explosive events such as quarry blasts.  
  - `veo:LongPeriod` - Long-period seismic events often related to volcanic activity.  
  - `veo:Noise` - Seismic background noise.  
  - `veo:VolcanoTectonic` - Earthquakes caused by volcanic or tectonic activity.  

### `veo:Station`  
- **Label**: Station  
- **Comment**: Represents a seismic monitoring station responsible for collecting event data.

### `veo:Instrument`  
- **Label**: Instrument  
- **Comment**: Devices used for measuring seismic activities, typically installed at stations for observation.  
- **Subclasses**: Inherits properties from `sosa:Sensor`.

### `veo:DataPoint`  
- **Label**: Data Point  
- **Comment**: Individual measurement data associated with seismic events.  
- **Subclasses**:  
  - `veo:DataPointArray` - A time series of data points.  
  - `veo:DataPointMatrix` - A collection of data arrays.

### `veo:AlertLevel`  
- **Label**: Alert Level  
- **Comment**: Represents the risk or threat level associated with a volcanic or seismic event.

---

## Properties

### Object Properties

#### `veo:hasStation`  
- **Label**: Has Station  
- **Comment**: Links an event to the monitoring station that observed it.  
- **Domain**: `veo:Event`  
- **Range**: `veo:Station`  
- **Description**: This property connects a seismic or volcanic event to the corresponding station collecting data.

#### `veo:hasInstrument`  
- **Label**: Has Instrument  
- **Comment**: Connects a station with the instruments it utilizes.  
- **Domain**: `veo:Station`  
- **Range**: `veo:Instrument`  
- **Description**: Essential for identifying specific sensors used for data capture.

#### `veo:hasAlertLevel`  
- **Label**: Has Alert Level  
- **Comment**: Indicates the alert level assigned to an event.  
- **Domain**: `veo:Event`  
- **Range**: `veo:AlertLevel`  
- **Description**: Helps define the severity or risk level of the event.

#### `veo:observedBy`  
- **Label**: Observed By  
- **Comment**: Associates a data point with the instrument observing it.  
- **Domain**: `veo:DataPoint`  
- **Range**: `veo:Instrument`  
- **Description**: Tracks which instrument is responsible for capturing specific data points.

#### `veo:occurredAt`  
- **Label**: Occurred At  
- **Comment**: Links an event to its geographical location.  
- **Domain**: `veo:Event`  
- **Range**: `geo1:SpatialThing`  
- **Description**: This property allows the event's spatial context to be recorded and analyzed.

---

### Datatype Properties

#### `veo:eventID`  
- **Label**: Event ID  
- **Comment**: A unique identifier assigned to each event.  
- **Domain**: `veo:Event`  
- **Range**: `xsd:string`  
- **Description**: Serves as a primary identifier for referencing specific events.

#### `veo:timestamp`  
- **Label**: Timestamp  
- **Comment**: Captures the date and time when an event occurred.  
- **Domain**: `veo:Event`  
- **Range**: `xsd:dateTime`  
- **Description**: Useful for temporal analysis and event sequencing.

#### `veo:magnitude`  
- **Label**: Magnitude  
- **Comment**: Indicates the magnitude of a seismic event.  
- **Domain**: `veo:Event`  
- **Range**: `xsd:decimal`  
- **Description**: A quantitative measure of the event's strength.

#### `veo:depth`  
- **Label**: Depth  
- **Comment**: Represents the depth of an event below the surface in kilometers.  
- **Domain**: `veo:Event`  
- **Range**: `xsd:decimal`  
- **Description**: Critical for understanding the event's subsurface origin.

---

## Extended Documentation

### Design Considerations
The VEO ontology is designed with modularity and interoperability in mind, enabling seamless integration with related ontologies and datasets. Its classes and properties follow well-defined ontological principles to ensure clarity and usability across diverse applications, from academic research to disaster management systems.

---

### Use Cases
- **Real-time Event Monitoring**: Use VEO to feed real-time seismic data into monitoring systems.
- **Historical Data Analysis**: Analyze past events for pattern recognition and risk prediction.
- **Geospatial Mapping**: Visualize seismic events on geographical information systems (GIS) using the spatial data model.
