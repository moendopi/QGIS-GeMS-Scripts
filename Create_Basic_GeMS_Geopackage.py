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

# for some reason trying to execut these commands from a function causes problems with create_geopackage()'s flavor argument and I don't know why
def create_basic_GeMS_geopackage(gpkg_name, coord_sys):
    gpkg = create_geopackage(gpkg_name, flavor=coord_sys)

    srs = SRS(get_srs(coord_sys), organization, int(coord_sys_input), coord_sys)
     
    contacts_and_faults = gpkg.create_feature_class('ContactsAndFaults', srs, fields=get_fields("ContactsAndFaults"), shape_type=GeometryType.multi_linestring)
    desc_map_units = gpkg.create_table('DescriptionOfMapUnits', fields=get_fields("DescriptionOfMapUnits"),description='')
    data_sources = gpkg.create_table('DataSources', fields=get_fields("DataSources"),description='')
    glossary_table = gpkg.create_table('Glossary', fields=get_fields("Glossary"),description='')


geopkg_location = input("Output workspace: ")
gpkg_name_input = input("Name of new geopackage: ")
gpkg_name = geopkg_location + '/' + gpkg_name_input + '.gpkg'
coord_sys_input = input("Coordinate reference system (EPSG or ESRI number): ")
coord_sys = get_coord_sys(coord_sys_input)

if int(coord_sys_input) < 102629:
    organization = 'EPSG'
else:
    organization = 'ESRI'

#create_basic_GeMS_geopackage(gpkg_name, coord_sys)

gpkg = GeoPackage.create(gpkg_name, flavor=coord_sys)


srs = SRS(get_srs(coord_sys), organization, int(coord_sys_input), coord_sys)

contacts_and_faults = gpkg.create_feature_class('ContactsAndFaults', srs, fields=get_fields("ContactsAndFaults"), shape_type=GeometryType.multi_linestring)
desc_map_units = gpkg.create_table('DescriptionOfMapUnits', fields=get_fields("DescriptionOfMapUnits"),description='')
data_sources = gpkg.create_table('DataSources', fields=get_fields("DataSources"),description='')
glossary_table = gpkg.create_table('Glossary', fields=get_fields("Glossary"),description='')
