"""Data model test."""
import os
import glob
import unittest

from basin3d_schema.datamodel.core import Observation, MonitoringFeature, Coordinate, AbsoluteCoordinate, \
    GeographicCoordinate, FeatureTypeEnum, MeasurementTimeseriesTVPObservation, TimeFrequencyEnum, HorizontalCoordinate, \
    HorizontalCoordinateDatumEnum, HorizontalCoordinateTypeEnum

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))

class TestDataModel(unittest.TestCase):
    """Test datamodel."""

    def test_model(self):
        """Create test objects, serialize, and deserialize"""
        geo_coord = GeographicCoordinate(x=-5, y=20,
                                         datum=HorizontalCoordinateDatumEnum.WGS84,
                                         type=HorizontalCoordinateTypeEnum.GEOGRAPHIC)
        ft = FeatureTypeEnum.WATERSHED
        feat = MonitoringFeature(description="test",
                                 coordinates=Coordinate(absolute=AbsoluteCoordinate(horizontal_position=[geo_coord])))
        obs = MeasurementTimeseriesTVPObservation(feature_of_interest=feat,
                                                  feature_of_interest_type=ft,
                                                  aggregation_duration=TimeFrequencyEnum.MONTH)
        jstr = obs.json(exclude_unset=True, indent=True)
        print(jstr)
        obs2 = MeasurementTimeseriesTVPObservation.parse_raw(jstr)
        self.assertEqual(obs, obs2)

    def test_validation(self):
        geo_coord = GeographicCoordinate(x=-5, y=20)
        # passing scalars instead of objects
        with self.assertRaises(Exception) as e:
            obs = Observation(feature_of_interest=5)
        # passing single valued instead of lists
        with self.assertRaises(Exception) as e:
            ac = AbsoluteCoordinate(horizontal_position=geo_coord)
        # enum validation: here we introduce a deliberate subtle error,
        # adding a space:
        with self.assertRaises(Exception) as e:
            MeasurementTimeseriesTVPObservation(feature_of_interest_type="WATER SHED")
        # enum validation: using the wrong enum
        with self.assertRaises(Exception) as e:
            x = HorizontalCoordinate(type=HorizontalCoordinateDatumEnum.WGS84)

