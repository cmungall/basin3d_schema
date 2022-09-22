"""Data model test."""
import os
import glob
import unittest
from pathlib import Path

from basin3d_schema.datamodel.core import Observation, MonitoringFeature, Coordinate, AbsoluteCoordinate, \
    GeographicCoordinate, FeatureTypeEnum, MeasurementTimeseriesTVPObservation, TimeFrequencyEnum, HorizontalCoordinate, \
    HorizontalCoordinateDatumEnum, HorizontalCoordinateTypeEnum
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from linkml_runtime.utils.introspection import package_schemaview

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")
SCHEMA_DIR = Path(os.path.join(ROOT, "src", "basin3d_schema", "schema"))

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))

class TestInstrospection(unittest.TestCase):
    """Test using SchemaView."""

    def test_introspection(self):
        sv = SchemaView(str(SCHEMA_DIR / "core.yaml"))
        for en in sv.all_enums():
            e = sv.get_enum(en)
            for pv in e.permissible_values.values():
                print(f"{en}: {pv.text} :: {pv.meaning}")



