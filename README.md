# basin3d_schema

EXPERIMENTAL rendering of basin3d as linkml

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

See the [generated enums page](basin3d_schema/#enumerations)

```
```

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

- `make all`: make everything
- `make deploy`: deploys site

</details>

## Credits

this project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
