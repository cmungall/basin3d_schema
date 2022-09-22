

CREATE TABLE "AbsoluteCoordinate" (
	vertical_extent TEXT, 
	horizontal_position TEXT, 
	PRIMARY KEY (vertical_extent, horizontal_position)
);

CREATE TABLE "AltitudeCoordinate" (
	encoding_method VARCHAR(9), 
	value FLOAT, 
	distance_units VARCHAR(6), 
	type VARCHAR(8), 
	resolution FLOAT, 
	datum VARCHAR(6), 
	PRIMARY KEY (encoding_method, value, distance_units, type, resolution, datum)
);

CREATE TABLE "Coordinate" (
	representative TEXT, 
	absolute TEXT, 
	PRIMARY KEY (representative, absolute)
);

CREATE TABLE "DataSource" (
	id_prefix TEXT, 
	credentials TEXT, 
	name TEXT, 
	id TEXT, 
	location TEXT, 
	PRIMARY KEY (id_prefix, credentials, name, id, location)
);

CREATE TABLE "DepthCoordinate" (
	encoding_method VARCHAR(9), 
	value FLOAT, 
	distance_units VARCHAR(6), 
	type VARCHAR(8), 
	resolution FLOAT, 
	datum VARCHAR(3), 
	PRIMARY KEY (encoding_method, value, distance_units, type, resolution, datum)
);

CREATE TABLE "Feature" (
	feature_type TEXT, 
	description TEXT, 
	name TEXT, 
	id TEXT, 
	observed_property_variables TEXT, 
	PRIMARY KEY (feature_type, description, name, id, observed_property_variables)
);

CREATE TABLE "GeographicCoordinate" (
	type VARCHAR(21), 
	datum VARCHAR(5), 
	x FLOAT, 
	y FLOAT, 
	units TEXT, 
	PRIMARY KEY (type, datum, x, y, units)
);

CREATE TABLE "HorizontalCoordinate" (
	type VARCHAR(21), 
	datum VARCHAR(5), 
	x FLOAT, 
	y FLOAT, 
	PRIMARY KEY (type, datum, x, y)
);

CREATE TABLE "MeasurementTimeseriesTVPObservation" (
	feature_of_interest_type VARCHAR(15), 
	result_quality VARCHAR(17), 
	utc_offset INTEGER, 
	feature_of_interest TEXT, 
	observed_property TEXT, 
	phenomenon_time TEXT, 
	id TEXT, 
	type VARCHAR(26), 
	aggregation_duration VARCHAR(6), 
	time_reference_position VARCHAR(6), 
	statistic TEXT, 
	observed_property_variable TEXT, 
	unit_of_measurement TEXT, 
	result_points TEXT, 
	PRIMARY KEY (feature_of_interest_type, result_quality, utc_offset, feature_of_interest, observed_property, phenomenon_time, id, type, aggregation_duration, time_reference_position, statistic, observed_property_variable, unit_of_measurement, result_points)
);

CREATE TABLE "MonitoringFeature" (
	feature_type TEXT, 
	description TEXT, 
	name TEXT, 
	id TEXT, 
	observed_property_variables TEXT, 
	related_sampling_feature_complex TEXT, 
	shape TEXT, 
	coordinates TEXT, 
	related_party TEXT, 
	description_reference TEXT, 
	utc_offset INTEGER, 
	PRIMARY KEY (feature_type, description, name, id, observed_property_variables, related_sampling_feature_complex, shape, coordinates, related_party, description_reference, utc_offset)
);

CREATE TABLE "Observation" (
	feature_of_interest_type VARCHAR(15), 
	result_quality VARCHAR(17), 
	utc_offset INTEGER, 
	feature_of_interest TEXT, 
	observed_property TEXT, 
	phenomenon_time TEXT, 
	id TEXT, 
	type VARCHAR(26), 
	PRIMARY KEY (feature_of_interest_type, result_quality, utc_offset, feature_of_interest, observed_property, phenomenon_time, id, type)
);

CREATE TABLE "ObservedProperty" (
	datasource_variable TEXT, 
	observed_property_variable TEXT, 
	sampling_medium TEXT, 
	datasource_description TEXT, 
	datasource TEXT, 
	PRIMARY KEY (datasource_variable, observed_property_variable, sampling_medium, datasource_description, datasource)
);

CREATE TABLE "ObservedPropertyVariable" (
	basin3d_id TEXT, 
	units TEXT, 
	categories TEXT, 
	full_name TEXT, 
	PRIMARY KEY (basin3d_id, units, categories, full_name)
);

CREATE TABLE "Person" (
	email TEXT, 
	last_name TEXT, 
	institution TEXT, 
	first_name TEXT, 
	role TEXT, 
	PRIMARY KEY (email, last_name, institution, first_name, role)
);

CREATE TABLE "RelatedSamplingFeature" (
	role TEXT, 
	related_sampling_feature_type TEXT, 
	related_sampling_feature TEXT, 
	PRIMARY KEY (role, related_sampling_feature_type, related_sampling_feature)
);

CREATE TABLE "RepresentativeCoordinate" (
	representative_point TEXT, 
	vertical_position TEXT, 
	representative_point_type VARCHAR(20), 
	PRIMARY KEY (representative_point, vertical_position, representative_point_type)
);

CREATE TABLE "SamplingFeature" (
	feature_type TEXT, 
	description TEXT, 
	name TEXT, 
	id TEXT, 
	observed_property_variables TEXT, 
	related_sampling_feature_complex TEXT, 
	PRIMARY KEY (feature_type, description, name, id, observed_property_variables, related_sampling_feature_complex)
);

CREATE TABLE "SpatialSamplingFeature" (
	feature_type TEXT, 
	description TEXT, 
	name TEXT, 
	id TEXT, 
	observed_property_variables TEXT, 
	related_sampling_feature_complex TEXT, 
	shape TEXT, 
	coordinates TEXT, 
	PRIMARY KEY (feature_type, description, name, id, observed_property_variables, related_sampling_feature_complex, shape, coordinates)
);

CREATE TABLE "TimeValuePair" (
	timestamp TEXT, 
	value TEXT, 
	PRIMARY KEY (timestamp, value)
);

CREATE TABLE "VerticalCoordinate" (
	encoding_method VARCHAR(9), 
	value FLOAT, 
	distance_units VARCHAR(6), 
	type VARCHAR(8), 
	datum TEXT, 
	resolution FLOAT, 
	PRIMARY KEY (encoding_method, value, distance_units, type, datum, resolution)
);
