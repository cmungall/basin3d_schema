"""Data model test."""
import os
import glob
import unittest

from basin3d_schema.datamodel.models import Observation, MonitoringFeature, Coordinate, AbsoluteCoordinate, \
    GeographicCoordinate, FeatureTypeEnum

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))

class TestDataModel(unittest.TestCase):
    """Test datamodel."""

    def test_model(self):
        """Observation test."""
        geo_coord = GeographicCoordinate(x=-5, y=20)
        ft = FeatureTypeEnum.WATERSHED
        feat = MonitoringFeature(description="test",
                                 coordinates=Coordinate(absolute=AbsoluteCoordinate(horizontal_position=[geo_coord])))
        obs = Observation(feature_of_interest=feat,
                          feature_of_interest_type=ft)
        print(obs)
        print(obs.json(exclude_unset=True, indent=True))

    def test_validation(self):
        geo_coord = GeographicCoordinate(x=-5, y=20)
        # passing scalars instead of objects
        with self.assertRaises(Exception) as e:
            obs = Observation(feature_of_interest=5)
        # passing single valued instead of lists
        with self.assertRaises(Exception) as e:
            ac = AbsoluteCoordinate(horizontal_position=geo_coord)
