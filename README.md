# basin3d_schema

EXPERIMENTAL rendering of basin3d as [linkml](https://linkml.io/linkml/)

## Website

* [https://cmungall.github.io/basin3d_schema](https://cmungall.github.io/basin3d_schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (generated: do not edit these)
    * [jsonschema](jsonschema/) - JSON schema, for validating JSON documents
    * [sqlschema](sqlschema/) - SQL DDL (CREATE TABLE statements)
    * [jdonld](jsonld/) - JSON-LD Contexts
    * [shacl](shacl/) - SHACL shape definitions (for RDF validation)
* [src/](src/) - source files (edit these)
    * [basin3d_schema](src/basin3d_schema)
        * [schema](src/basin3d_schema/schema) -- LinkML schema (edit this)
        * [datamodel](src/basin3d_schema/datamodel) -- Generated pydantic datamodel
* [tests](tests/) - python tests

## Usage

```bash
pip install basin3d_schema
```

(^^ may not work if this is a new repo)

### Creating Objects

Creating objects via generated Pydantic model:

```python
from basin3d_schema.datamodel.models import Observation, MonitoringFeature, Coordinate, AbsoluteCoordinate, \
    GeographicCoordinate

geo_coord = GeographicCoordinate(x=-5, y=20)
ft = FeatureTypeEnum.WATERSHED
feat = MonitoringFeature(description="test",
                         coordinates=Coordinate(absolute=AbsoluteCoordinate(horizontal_position=[geo_coord])))
obs = Observation(feature_of_interest=feat,
                  feature_of_interest_type=ft)
print(obs.json(exclude_unset=True, indent=True))
```

Generates:

```json
{
 "feature_of_interest": {
  "description": "test",
  "coordinates": {
   "absolute": {
    "horizontal_position": [
     {
      "x": -5.0,
      "y": 20.0
     }
    ]
   }
  }
 }, 
  "feature_of_interest_type": "WATERSHED"
}
```

### Validating Objects

Pydantic auto-validates by default

E.g:

```python
ac = AbsoluteCoordinate(horizontal_position=geo_coord)
```

raises an exception as a list is expected

### Vocabularies

See the [generated enums page](https://cmungall.github.io/basin3d_schema/#enumerations)

The generated Python looks like:

```python
class TimeFrequencyEnum(str, Enum):
    
    YEAR = "YEAR"
    MONTH = "MONTH"
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"
    SECOND = "SECOND"
```

The underlying schema is more granular:

```yaml
enums:
  TimeFrequencyEnum:
    permissible_values:
      YEAR:
        meaning: UO:0000036 ## year
        unit:
          ucum_code: a
      MONTH:
        meaning: UO:0000035 ## month
        unit:
          ucum_code: mo
      DAY:
        meaning: UO:0000033 ## day
        unit:
          ucum_code: d
      HOUR:
        meaning: UO:0000032 ## hour
        unit:
          ucum_code: h
      MINUTE:
        meaning: UO:0000031 ## minute
        unit:
          ucum_code: min
      SECOND:
        meaning: UO:0000010 ## second
        unit:
          ucum_code: s
```

The additional metadata gives *interoperability hooks*

But using these is just like any normal Python enum

```python
Time(aggregation_duration=TimeFrequencyEnum.MONTH)
```

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

- `make all`: make everything
- `make deploy`: deploys site

</details>

## Credits

this project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
