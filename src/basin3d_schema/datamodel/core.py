from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any
from pydantic import BaseModel as BaseModel, Field

metamodel_version = "None"
version = "None"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'
    
class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True, 
                validate_all = True, 
                underscore_attrs_are_private = True, 
                extra = 'forbid', 
                arbitrary_types_allowed = True):
    pass                    


class TimeFrequencyEnum(str, Enum):
    
    YEAR = "YEAR"
    MONTH = "MONTH"
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"
    SECOND = "SECOND"
    
    

class CoordinateUnitEnum(str, Enum):
    
    ScalarDegreeUnit = "ScalarDegreeUnit"
    CompoundDegreeUnit = "CompoundDegreeUnit"
    UNITS_DEC_DEGREES = "UNITS_DEC_DEGREES"
    UNITS_DEC_MINUTES = "UNITS_DEC_MINUTES"
    UNITS_DEC_SECONDS = "UNITS_DEC_SECONDS"
    UNITS_DEGREES_DEC_MINUTES = "UNITS_DEGREES_DEC_MINUTES"
    UNITS_DEGREES_MIN_DEC_SECS = "UNITS_DEGREES_MIN_DEC_SECS"
    UNITS_RADIANS = "UNITS_RADIANS"
    UNITS_GRADS = "UNITS_GRADS"
    
    

class VerticalCoordinateTypeEnum(str, Enum):
    
    ALTITUDE = "ALTITUDE"
    DEPTH = "DEPTH"
    
    

class VerticalCoordinateDistanceEnum(str, Enum):
    
    meters = "meters"
    feet = "feet"
    
    

class VerticalCoordinateEncodingEnum(str, Enum):
    
    EXPLICIT = "EXPLICIT"
    IMPLICIT = "IMPLICIT"
    ATTRIBUTE = "ATTRIBUTE"
    
    

class HorizontalCoordinateTypeEnum(str, Enum):
    
    GEOGRAPHIC = "GEOGRAPHIC"
    PLANAR_GRID = "PLANAR_GRID"
    PLANAR_LOCAL = "PLANAR_LOCAL"
    PLANAR_MAP_PROJECTION = "PLANAR_MAP_PROJECTION"
    LOCAL = "LOCAL"
    
    

class HorizontalCoordinateDatumEnum(str, Enum):
    
    WGS84 = "WGS84"
    NAD83 = "NAD83"
    NAD27 = "NAD27"
    
    

class TimeReferenceEnum(str, Enum):
    
    START = "START"
    MIDDLE = "MIDDLE"
    END = "END"
    
    

class StatisticEnum(str, Enum):
    
    INSTANT = "INSTANT"
    MEAN = "MEAN"
    MIN = "MIN"
    MAX = "MAX"
    TOTAL = "TOTAL"
    
    

class ResultQualityEnum(str, Enum):
    
    CHECKED = "CHECKED"
    UNCHECKED = "UNCHECKED"
    PARTIALLY_CHECKED = "PARTIALLY_CHECKED"
    
    

class FeatureTypeEnum(str, Enum):
    
    REGION = "REGION"
    SUBREGION = "SUBREGION"
    BASIN = "BASIN"
    SUBBASIN = "SUBBASIN"
    WATERSHED = "WATERSHED"
    SUBWATERSHED = "SUBWATERSHED"
    SITE = "SITE"
    PLOT = "PLOT"
    HORIZONTAL_PATH = "HORIZONTAL_PATH"
    VERTICAL_PATH = "VERTICAL_PATH"
    POINT = "POINT"
    
    

class DepthCoordinateDatumEnum(str, Enum):
    
    LS = "LS"
    MSL = "MSL"
    
    

class AltitudeCoordinateDatumEnum(str, Enum):
    
    NGVD29 = "NGVD29"
    NAVD88 = "NAVD88"
    
    

class RepresentativePointEnum(str, Enum):
    
    CENTER_LOCAL_SURFACE = "CENTER_LOCAL_SURFACE"
    UPPER_LEFT_CORNER = "UPPER_LEFT_CORNER"
    UPPER_RIGHT_CORNER = "UPPER_RIGHT_CORNER"
    LOWER_LEFT_CORNER = "LOWER_LEFT_CORNER"
    LOWER_RIGHT_CORNER = "LOWER_RIGHT_CORNER"
    
    

class ObservationDatumEnum(str, Enum):
    
    MEASUREMENT_TVP_TIMESERIES = "MEASUREMENT_TVP_TIMESERIES"
    MEASUREMENT = "MEASUREMENT"
    
    

class TimeMetadataMixinReferenceEnum(str, Enum):
    
    START = "START"
    MIDDLE = "MIDDLE"
    END = "END"
    
    

class TimeValuePair(ConfiguredBaseModel):
    """
    Tuple that represents a time value pair.  This will handle timestamp conversion`(timestamp, value)`
    """
    timestamp: Optional[str] = Field(None)
    value: Optional[str] = Field(None)
    


class MeasurementResultMixin(ConfiguredBaseModel):
    """
    Result Mixin: Measurement
    """
    unit_of_measurement: Optional[str] = Field(None)
    result_value: Optional[float] = Field(None)
    


class TimeMetadataMixin(ConfiguredBaseModel):
    """
    Metadata attributes for Observations with a time
    """
    aggregation_duration: Optional[TimeFrequencyEnum] = Field(None)
    time_reference_position: Optional[TimeMetadataMixinReferenceEnum] = Field(None)
    


class MeasurementTimeseriesTVPResultMixin(ConfiguredBaseModel):
    """
    Result Mixin: Measurement Timeseries TimeValuePair
    """
    unit_of_measurement: Optional[str] = Field(None)
    result_points: Optional[List[TimeValuePair]] = Field(default_factory=list)
    


class MeasurementMetadataMixin(ConfiguredBaseModel):
    """
    Metadata attributes for Observations type Measurement
    """
    statistic: Optional[str] = Field(None)
    observed_property_variable: Optional[str] = Field(None)
    


class JSONSerializable(ConfiguredBaseModel):
    """
    Make a Data class serializable to json
    """
    None
    


class ObservedPropertyVariable(JSONSerializable):
    """
    Defining the properties being observed (measured). See http://vocabulary.odm2.org/variablename/ for controlled vocabularyAttributes:- *basin3d_id:* string,- *full_name:* string,- *categories:* List of strings (in order of priority).- *units:* stringSee http://vocabulary.odm2.org/variabletype/ for options, although I think we should have our own list (theirs is a bit funky).
    """
    basin3d_id: Optional[str] = Field(None)
    units: Optional[str] = Field(None)
    categories: Optional[List[str]] = Field(default_factory=list)
    full_name: Optional[str] = Field(None)
    


class ObservedProperty(JSONSerializable):
    """
    Defining the attributes for a single/multiple Observed PropertiesAttributes:- *datasource_variable:* id, e.g., Cs 137 air dose rate car survey campaigns- *observed_property_variable_id:* string, e.g., Cs137MVID- *sampling_medium:* enum (WATER, GAS, SOLID PHASE, OTHER, NOT APPLICABLE)- *datasource:*- *datasource_description:*
    """
    datasource_variable: Optional[str] = Field(None)
    observed_property_variable: Optional[ObservedPropertyVariable] = Field(None)
    sampling_medium: Optional[str] = Field(None)
    datasource_description: Optional[str] = Field(None)
    datasource: Optional[DataSource] = Field(None)
    


class Base(JSONSerializable):
    """
    Base synthesis model class. All classes that extend this are immutable.
    """
    None
    


class RelatedSamplingFeature(Base):
    """
    Class that represents a related sampling feature and its role relative tothe sampling feature to which it is related. Spatial hierarchies of featuresare built by specifying related sampling features.Data model from OGC Observations and Measurements.
    """
    role: Optional[str] = Field(None)
    related_sampling_feature_type: Optional[str] = Field(None)
    related_sampling_feature: Optional[SamplingFeature] = Field(None)
    


class Person(Base):
    
    email: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    institution: Optional[str] = Field(None)
    first_name: Optional[str] = Field(None)
    role: Optional[str] = Field(None)
    


class Observation(Base):
    """
    OGC OM_Observation feature type. This is a parent class to which Mixinsshould be added to create observation types with metadata and result.
    """
    feature_of_interest_type: Optional[FeatureTypeEnum] = Field(None)
    result_quality: Optional[ResultQualityEnum] = Field(None)
    utc_offset: Optional[int] = Field(None)
    feature_of_interest: Optional[MonitoringFeature] = Field(None)
    observed_property: Optional[ObservedProperty] = Field(None)
    phenomenon_time: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    type: Optional[ObservationDatumEnum] = Field(None)
    


class MeasurementTimeseriesTVPObservation(Observation, MeasurementMetadataMixin, MeasurementTimeseriesTVPResultMixin, TimeMetadataMixin):
    """
    Series of measurement (numerical) observations in TVP format grouped by time (i.e., a timeseries).Anything specified at the group level automatically applies to the individual observation.
    """
    aggregation_duration: Optional[TimeFrequencyEnum] = Field(None)
    time_reference_position: Optional[TimeMetadataMixinReferenceEnum] = Field(None)
    statistic: Optional[str] = Field(None)
    observed_property_variable: Optional[str] = Field(None)
    unit_of_measurement: Optional[str] = Field(None)
    result_points: Optional[List[TimeValuePair]] = Field(default_factory=list)
    feature_of_interest_type: Optional[FeatureTypeEnum] = Field(None)
    result_quality: Optional[ResultQualityEnum] = Field(None)
    utc_offset: Optional[int] = Field(None)
    feature_of_interest: Optional[MonitoringFeature] = Field(None)
    observed_property: Optional[ObservedProperty] = Field(None)
    phenomenon_time: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    type: Optional[ObservationDatumEnum] = Field(None)
    


class AbsoluteCoordinate(Base):
    """
    Absolute coordinate describes the geo-referenced location of a feature.Coordinates match the feature's shape. For example, a curve is a list of points.Currently collections of discrete points describing a feature are supported.
    """
    vertical_extent: Optional[List[AltitudeCoordinate]] = Field(default_factory=list)
    horizontal_position: Optional[List[GeographicCoordinate]] = Field(default_factory=list)
    


class RepresentativeCoordinate(Base):
    """
    Representative coordinates describe the location of a feature by a representative shape / location.For example, a study area may be represented by the center point.The veritical position from a reference position (e.g., height, depth) is also described in this class.Currently representative points are supported. The class is extendable to other forms of representing(e.g., diameter, area, side_length)Representative point types are also expandable as use cases require.
    """
    representative_point: Optional[AbsoluteCoordinate] = Field(None)
    vertical_position: Optional[DepthCoordinate] = Field(None)
    representative_point_type: Optional[RepresentativePointEnum] = Field(None)
    


class Coordinate(Base):
    """
    Top level coordinate class that holds :class:`AbsoluteCoordinate` or :class:`RepresentativeCoordinate`
    """
    representative: Optional[RepresentativeCoordinate] = Field(None)
    absolute: Optional[AbsoluteCoordinate] = Field(None)
    


class VerticalCoordinate(Base):
    """
    The vertical position of the feature (altitudes or depths).The reference frame or system is specified.
    """
    encoding_method: Optional[VerticalCoordinateEncodingEnum] = Field(None)
    value: Optional[float] = Field(None)
    distance_units: Optional[VerticalCoordinateDistanceEnum] = Field(None)
    type: Optional[VerticalCoordinateTypeEnum] = Field(None)
    datum: Optional[str] = Field(None)
    resolution: Optional[float] = Field(None)
    


class DepthCoordinate(VerticalCoordinate):
    """
    A depth vertical position (i.e., the height or depth from the specified reference position)The reference frame or system is specified.
    """
    encoding_method: Optional[VerticalCoordinateEncodingEnum] = Field(None)
    value: Optional[float] = Field(None)
    distance_units: Optional[VerticalCoordinateDistanceEnum] = Field(None)
    type: Optional[VerticalCoordinateTypeEnum] = Field(None)
    datum: Optional[DepthCoordinateDatumEnum] = Field(None)
    resolution: Optional[float] = Field(None)
    


class AltitudeCoordinate(VerticalCoordinate):
    """
    An altitudinal vertical position (i.e., distance from sea level).The reference frame or system is specified. The term'altitude' is used instead of the common term 'elevation' to conform to the terminologyin Federal Information Processing Standards 70-1 and 173.
    """
    datum: Optional[AltitudeCoordinateDatumEnum] = Field(None)
    encoding_method: Optional[VerticalCoordinateEncodingEnum] = Field(None)
    value: Optional[float] = Field(None)
    distance_units: Optional[VerticalCoordinateDistanceEnum] = Field(None)
    type: Optional[VerticalCoordinateTypeEnum] = Field(None)
    resolution: Optional[float] = Field(None)
    


class Feature(Base):
    """
    A general feature upon which an observation can be made. Loosely after GF_Feature (ISO).
    """
    feature_type: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    observed_property_variables: Optional[List[str]] = Field(default_factory=list)
    


class SamplingFeature(Feature):
    """
    A feature where sampling is conducted. OGC Observation & Measurements SF_SamplingFeature.
    """
    related_sampling_feature_complex: Optional[List[SamplingFeature]] = Field(default_factory=list)
    feature_type: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    observed_property_variables: Optional[List[str]] = Field(default_factory=list)
    


class SpatialSamplingFeature(SamplingFeature):
    """
    A spatially-defined feature where sampling is conducted. OGC Observation & Measurements SF_SpatialSamplingFeature.
    """
    shape: Optional[str] = Field(None)
    coordinates: Optional[Coordinate] = Field(None)
    related_sampling_feature_complex: Optional[List[SamplingFeature]] = Field(default_factory=list)
    feature_type: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    observed_property_variables: Optional[List[str]] = Field(default_factory=list)
    


class MonitoringFeature(SpatialSamplingFeature):
    """
    A feature upon which monitoring is made. OGC Timeseries Profile OM_MonitoringFeature.
    """
    related_party: Optional[List[Person]] = Field(default_factory=list)
    description_reference: Optional[str] = Field(None)
    utc_offset: Optional[int] = Field(None)
    shape: Optional[str] = Field(None)
    coordinates: Optional[Coordinate] = Field(None)
    related_sampling_feature_complex: Optional[List[SamplingFeature]] = Field(default_factory=list)
    feature_type: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    observed_property_variables: Optional[List[str]] = Field(default_factory=list)
    


class DataSource(JSONSerializable):
    """
    Data Source definitionAttributes:- *id:* string (inherited)- *name:* string- *id_prefix:* string, prefix that is added to all data source ids- *location*- *credentials:*
    """
    id_prefix: Optional[str] = Field(None)
    credentials: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    location: Optional[str] = Field(None)
    


class HorizontalCoordinate(Base):
    
    type: Optional[HorizontalCoordinateTypeEnum] = Field(None)
    datum: Optional[HorizontalCoordinateDatumEnum] = Field(None)
    x: Optional[float] = Field(None)
    y: Optional[float] = Field(None)
    


class GeographicCoordinate(HorizontalCoordinate):
    """
    The latitude and longitude which define the position of a point onthe Earth's surface with respect to a reference spheroid.(https://www.fgdc.gov/csdgmgraphical/spref.htm)
    """
    units: Optional[str] = Field(None)
    type: Optional[HorizontalCoordinateTypeEnum] = Field(None)
    datum: Optional[HorizontalCoordinateDatumEnum] = Field(None)
    x: Optional[float] = Field(None)
    y: Optional[float] = Field(None)
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
TimeValuePair.update_forward_refs()
MeasurementResultMixin.update_forward_refs()
TimeMetadataMixin.update_forward_refs()
MeasurementTimeseriesTVPResultMixin.update_forward_refs()
MeasurementMetadataMixin.update_forward_refs()
JSONSerializable.update_forward_refs()
ObservedPropertyVariable.update_forward_refs()
ObservedProperty.update_forward_refs()
Base.update_forward_refs()
RelatedSamplingFeature.update_forward_refs()
Person.update_forward_refs()
Observation.update_forward_refs()
MeasurementTimeseriesTVPObservation.update_forward_refs()
AbsoluteCoordinate.update_forward_refs()
RepresentativeCoordinate.update_forward_refs()
Coordinate.update_forward_refs()
VerticalCoordinate.update_forward_refs()
DepthCoordinate.update_forward_refs()
AltitudeCoordinate.update_forward_refs()
Feature.update_forward_refs()
SamplingFeature.update_forward_refs()
SpatialSamplingFeature.update_forward_refs()
MonitoringFeature.update_forward_refs()
DataSource.update_forward_refs()
HorizontalCoordinate.update_forward_refs()
GeographicCoordinate.update_forward_refs()

