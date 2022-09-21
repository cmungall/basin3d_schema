

CREATE TABLE "AbsoluteCoordinate" (
	vertical_extent TEXT, 
	horizontal_position TEXT, 
	PRIMARY KEY (vertical_extent, horizontal_position)
);

CREATE TABLE "AltitudeCoordinate" (
	distance_units TEXT, 
	type TEXT, 
	resolution FLOAT, 
	encoding_method TEXT, 
	value FLOAT, 
	datum TEXT, 
	PRIMARY KEY (distance_units, type, resolution, encoding_method, value, datum)
);

CREATE TABLE "Coordinate" (
	absolute TEXT, 
	representative TEXT, 
	PRIMARY KEY (absolute, representative)
);

CREATE TABLE "DataSource" (
	name TEXT, 
	id TEXT, 
	credentials TEXT, 
	id_prefix TEXT, 
	location TEXT, 
	PRIMARY KEY (name, id, credentials, id_prefix, location)
);

CREATE TABLE "DepthCoordinate" (
	distance_units TEXT, 
	datum TEXT, 
	type TEXT, 
	resolution FLOAT, 
	encoding_method TEXT, 
	value FLOAT, 
	PRIMARY KEY (distance_units, datum, type, resolution, encoding_method, value)
);

CREATE TABLE "Feature" (
	description TEXT, 
	name TEXT, 
	feature_type TEXT, 
	observed_property_variables TEXT, 
	id TEXT, 
	PRIMARY KEY (description, name, feature_type, observed_property_variables, id)
);

CREATE TABLE "GeographicCoordinate" (
	datum TEXT, 
	x FLOAT, 
	y FLOAT, 
	type TEXT, 
	units TEXT, 
	PRIMARY KEY (datum, x, y, type, units)
);

CREATE TABLE "HorizontalCoordinate" (
	datum TEXT, 
	x FLOAT, 
	y FLOAT, 
	type TEXT, 
	PRIMARY KEY (datum, x, y, type)
);

CREATE TABLE "MonitoringFeature" (
	description TEXT, 
	name TEXT, 
	feature_type TEXT, 
	observed_property_variables TEXT, 
	id TEXT, 
	related_sampling_feature_complex TEXT, 
	coordinates TEXT, 
	shape TEXT, 
	utc_offset INTEGER, 
	related_party TEXT, 
	description_reference TEXT, 
	PRIMARY KEY (description, name, feature_type, observed_property_variables, id, related_sampling_feature_complex, coordinates, shape, utc_offset, related_party, description_reference)
);

CREATE TABLE "Observation" (
	feature_of_interest TEXT, 
	id TEXT, 
	result_quality VARCHAR(17), 
	type TEXT, 
	feature_of_interest_type VARCHAR(15), 
	phenomenon_time TEXT, 
	observed_property TEXT, 
	utc_offset INTEGER, 
	PRIMARY KEY (feature_of_interest, id, result_quality, type, feature_of_interest_type, phenomenon_time, observed_property, utc_offset)
);

CREATE TABLE "ObservedProperty" (
	datasource TEXT, 
	datasource_variable TEXT, 
	sampling_medium TEXT, 
	observed_property_variable TEXT, 
	datasource_description TEXT, 
	PRIMARY KEY (datasource, datasource_variable, sampling_medium, observed_property_variable, datasource_description)
);

CREATE TABLE "ObservedPropertyVariable" (
	units TEXT, 
	full_name TEXT, 
	basin3d_id TEXT, 
	categories TEXT, 
	PRIMARY KEY (units, full_name, basin3d_id, categories)
);

CREATE TABLE "Person" (
	email TEXT, 
	role TEXT, 
	first_name TEXT, 
	institution TEXT, 
	last_name TEXT, 
	PRIMARY KEY (email, role, first_name, institution, last_name)
);

CREATE TABLE "RelatedSamplingFeature" (
	related_sampling_feature_type TEXT, 
	related_sampling_feature TEXT, 
	role TEXT, 
	PRIMARY KEY (related_sampling_feature_type, related_sampling_feature, role)
);

CREATE TABLE "RepresentativeCoordinate" (
	representative_point TEXT, 
	representative_point_type TEXT, 
	vertical_position TEXT, 
	PRIMARY KEY (representative_point, representative_point_type, vertical_position)
);

CREATE TABLE "SamplingFeature" (
	description TEXT, 
	name TEXT, 
	feature_type TEXT, 
	observed_property_variables TEXT, 
	id TEXT, 
	related_sampling_feature_complex TEXT, 
	PRIMARY KEY (description, name, feature_type, observed_property_variables, id, related_sampling_feature_complex)
);

CREATE TABLE "SpatialSamplingFeature" (
	description TEXT, 
	name TEXT, 
	feature_type TEXT, 
	observed_property_variables TEXT, 
	id TEXT, 
	related_sampling_feature_complex TEXT, 
	coordinates TEXT, 
	shape TEXT, 
	PRIMARY KEY (description, name, feature_type, observed_property_variables, id, related_sampling_feature_complex, coordinates, shape)
);

CREATE TABLE "VerticalCoordinate" (
	distance_units TEXT, 
	datum TEXT, 
	type TEXT, 
	resolution FLOAT, 
	encoding_method TEXT, 
	value FLOAT, 
	PRIMARY KEY (distance_units, datum, type, resolution, encoding_method, value)
);
