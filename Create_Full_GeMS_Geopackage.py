from pygeopkg.core.geopkg import GeoPackage
from pygeopkg.core.srs import SRS
from pygeopkg.core.field import Field
from pygeopkg.shared.enumeration import GeometryType, SQLFieldTypes
from crs_dictionary import coordinate_systems_dict
import GeMS_basic_feature_classes
from srs_dictionary import srs_dict

def get_coord_sys(coord_sys_input):
    return coordinate_systems_dict.get(coord_sys_input)
def get_fields(feature_class):
    return GeMS_basic_feature_classes.GeMS_basic_feature_class_fields.get(feature_class)
def create_geopackage(gpkg_name, coord_sys):
    gpkg = GeoPackage.create(gpkg_name, flavor=coord_sys)
    return gpkg
def get_srs(coord_sys):
    return srs_dict.get(coord_sys_input)
def create_map_unit_polys():
    gpkg.create_feature_class('MapUnitPolys', srs, fields=get_fields("MapUnitPolys"), shape_type=GeometryType.multi_polygon)
def create_contact_and_faults():
    gpkg.create_feature_class('ContactsAndFaults', srs, fields=get_fields("ContactsAndFaults"), shape_type=GeometryType.multi_linestring)
def create_desc_map_units():
    gpkg.create_table('DescriptionOfMapUnits', fields=get_fields("DescriptionOfMapUnits"),description='')
def create_data_sources_table():
    gpkg.create_table('DataSources', fields=get_fields("DataSources"),description='')
def create_glossary_table():
    gpkg.create_table('Glossary', fields=get_fields("Glossary"),description='')
def create_generic_points():
    gpkg.create_feature_class('GenericPoints', srs, fields=get_fields("GenericPoints"), shape_type=GeometryType.multi_point)
def create_generic_samples():
    gpkg.create_feature_class('GenericSamples', srs, fields=get_fields("GenericSamples"), shape_type=GeometryType.multi_point)
def create_orientation_points():
    gpkg.create_feature_class('OrientationPoints', srs, fields=get_fields("OrientationPoints"), shape_type=GeometryType.multi_point)
def create_geochron_points():
    gpkg.create_feature_class('GeochronPoints', srs, fields=get_fields("GeochronPoints"), shape_type=GeometryType.multi_point)
def create_stations_points():
    gpkg.create_feature_class('Stations', srs, fields=get_fields("Stations"), shape_type=GeometryType.multi_point)
def create_geologic_lines():
    gpkg.create_feature_class('GeologicLines', srs, fields=get_fields("GeologicLines"), shape_type=GeometryType.multi_linestring)
def create_cartographic_lines():
    gpkg.create_feature_class('CartographicLines', srs, fields=get_fields("CartographicLines"), shape_type=GeometryType.multi_linestring)
def create_iso_value_lines():
    gpkg.create_feature_class('IsoValueLines', srs, fields=get_fields("IsoValueLines"), shape_type=GeometryType.multi_linestring)
def create_map_unit_lines():
    gpkg.create_feature_class('MapUnitLines', srs, fields=get_fields("MapUnitLines"), shape_type=GeometryType.multi_linestring)
def create_map_unit_points():
    gpkg.create_feature_class('MapUnitPoints', srs, fields=get_fields("MapUnitPoints"), shape_type=GeometryType.multi_point)
def create_map_unit_overlay_polys():
    gpkg.create_feature_class('MapUnitOverlayPolys', srs, fields=get_fields("MapUnitOverlayPolys"), shape_type=GeometryType.multi_polygon)
def create_overlay_polys():
    gpkg.create_feature_class('OverlayPolys', srs, fields=get_fields("OverlayPolys"), shape_type=GeometryType.multi_polygon)
def create_data_source_polys():
    gpkg.create_feature_class('DataSourcePolys', srs, fields=get_fields("DataSourcePolys"), shape_type=GeometryType.multi_polygon)
def create_repurposed_symbols_table():
    gpkg.create_table('RepurposedSymbols', fields=get_fields("RepurposedSymbols"),description='')
def create_cmu_map_unit_polys():
    gpkg.create_feature_class('CMUMapUnitPolys', srs, fields=get_fields("CMUMapUnitPolys"), shape_type=GeometryType.multi_polygon)
def create_cmu_lines():
    gpkg.create_feature_class('CMULines', srs, fields=get_fields("CMULines"), shape_type=GeometryType.multi_linestring)
def create_cmu_points():
    gpkg.create_feature_class('CMUPoints', srs, fields=get_fields("CMUPoints"), shape_type=GeometryType.multi_point)
def create_misc_map_info():
    gpkg.create_table('MiscellaneousMapInformation', fields=get_fields("MiscellaneousMapInformation"),description='')
def create_layer_list():
    gpkg.create_table('LayerList', fields=get_fields("LayerList"),description='')
def create_standard_lithology():
    gpkg.create_table('StandardLithology', fields=get_fields("StandardLithology"),description='')
def create_fossil_points():
    gpkg.create_feature_class('FossilPoints', srs, fields=get_fields("FossilPoints"), shape_type=GeometryType.multi_point)
def create_photo_points():
    gpkg.create_feature_class('PhotoPoints', srs, fields=get_fields("PhotoPoints"), shape_type=GeometryType.multi_point)


geopkg_location = input("Output workspace: ")
gpkg_name_input = input("Name of new geopackage: ")
gpkg_name = geopkg_location + '/' + gpkg_name_input + '.gpkg'
coord_sys_input = input("Coordinate reference system (EPSG or ESRI number): ")
coord_sys = get_coord_sys(coord_sys_input)

if int(coord_sys_input) < 102629:
    organization = 'EPSG'
else:
    organization = 'ESRI'

gpkg = GeoPackage.create(gpkg_name, flavor=coord_sys)
srs = SRS(get_srs(coord_sys), organization, int(coord_sys_input), coord_sys)

create_map_unit_polys()
create_contact_and_faults()
create_desc_map_units()
create_data_sources_table()
create_glossary_table()
create_generic_points()
create_generic_samples()
create_orientation_points()
create_geochron_points()
create_stations_points()
create_geologic_lines()
create_cartographic_lines()
create_iso_value_lines()
create_map_unit_lines()
create_map_unit_points()
create_map_unit_overlay_polys()
create_overlay_polys()
create_data_source_polys()
create_repurposed_symbols_table()
create_cmu_map_unit_polys()
create_cmu_lines()
create_cmu_points()
create_misc_map_info()
create_layer_list()
create_standard_lithology()
create_fossil_points()
create_photo_points()