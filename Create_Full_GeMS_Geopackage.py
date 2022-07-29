import os, winsound, time, sys
from crs_dictionary import coordinate_systems_dict
import GeMS_basic_feature_classes
from srs_dictionary import srs_dict

try:
    from pygeopkg.core.geopkg import GeoPackage
    from pygeopkg.core.srs import SRS
    from pygeopkg.core.field import Field
    from pygeopkg.shared.enumeration import GeometryType, SQLFieldTypes
except ModuleNotFoundError:
    print("Installing missing modules, please wait...\n")
    # get pip if missing
    if sys.platform == 'win32':
        os.system('python get-pip.py')
    if sys.platform == 'darwin' or sys.platform == 'os2':
        os.system('sudo easy_install pip')

    # install pygeopkg
    if sys.platform == 'linux':
        os.system('pip3 install pygeopkg')
    elif sys.platform == 'win32':
        os.system('pip install pygeopkg')

    else:
        os.system('pip install pygeopkg')

def get_coord_sys(coord_sys_input):
    return coordinate_systems_dict.get(coord_sys_input)


def get_save_folder():
    geopkg_loc_usr_input = input("Enter folder path to save geopackage to: ")
    if os.path.isdir(geopkg_loc_usr_input) == True:
        return geopkg_loc_usr_input
    else:
        winsound.Beep(600, 500)
        print("Invalid path!")
        get_save_folder()


def check_coord_sys():
    coord_sys_input = input("Coordinate reference system (EPSG or ESRI number): ")
    if coord_sys_input in coordinate_systems_dict:
        return coord_sys_input
    else:
        print("Unknown coordinate system, please enter valid coordinate system")
        check_coord_sys()

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
def create_map_unit_overlay_lines():
    gpkg.create_feature_class('MapUnitOverlayLines', srs, fields=get_fields("MapUnitOverlayLines"), shape_type=GeometryType.multi_linestring)
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
def create_geochem_points():
    gpkg.create_feature_class('GeochemPoints', srs, fields=get_fields("GeochemPoints"), shape_type=GeometryType.multi_point)
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


list_of_feature_classes = ['MapUnitPolys', 'ContactsAndFaults', 'MapUnitOverlayLines', 'DescriptionOfMapUnits', 'DataSources',\
'Glossary', 'GenericPoints', 'GenericSamples', 'OrientationPoints', 'GeochronPoints', 'GeochemPoints', 'Stations', 'GeologicLines',\
'CartographicLines', 'IsoValueLines', 'MapUnitLines', 'MapUnitPoints', 'MapUnitOverlayPolys', 'OverlayPolys', 'DataSourcePolys',\
'RepurposedSymbols', 'CMUMapUnitPolys', 'CMULines', 'CMUPoints', 'MiscellaneousMapInformation', 'miscmapinformation', 'miscellaneousmapinfo',\
'miscmapinfo', 'LayerList', 'StandardLithology', 'FossilPoints', 'PhotoPoints']

list_of_crs = ['NAD83 UTM Zone 1N: 26901', 'NAD83 UTM Zone 2N: 26902', 'NAD83 UTM Zone 3N: 26903', 'NAD83 UTM Zone 4N: 26904', 'NAD83 UTM Zone 5N: 26905',\
'NAD83 UTM Zone 6N: 26906', 'NAD83 UTM Zone 7N: 26907', 'NAD83 UTM Zone 8N: 26908', 'NAD83 UTM Zone 9N: 26909', 'NAD83 UTM Zone 10N: 26910', 'NAD83 UTM Zone 11N: 26911',\
'NAD83 UTM Zone 12N: 26912', 'NAD83 UTM Zone 13N: 26913', 'NAD83 UTM Zone 14N: 26914', 'NAD83 UTM Zone 15N: 26915', 'NAD83 UTM Zone 16N: 26916', 'NAD83 UTM Zone 17N: 26917', 'NAD83 UTM Zone 18N: 26918',\
'NAD83 UTM Zone 19N: 26919', 'NAD83 UTM Zone 20N: 26920', 'WGS84 UTM Zone 1N: 32601', 'WGS84 UTM Zone 2N: 32602', 'WGS84 UTM Zone 3N: 32603', 'WGS84 UTM Zone 4N: 32604', 'WGS84 UTM Zone 5N: 32605',\
'WGS84 UTM Zone 6N: 32606', 'WGS84 UTM Zone 7N: 32607', 'WGS84 UTM Zone 8N: 32608', 'WGS84 UTM Zone 9N: 32609', 'WGS84 UTM Zone 10N: 32610', 'WGS84 UTM Zone 11N: 32611', 'WGS84 UTM Zone 12N: 32612', 'WGS84 UTM Zone 13N: 32613',\
'WGS84 UTM Zone 14N: 32614', 'WGS84 UTM Zone 15N: 32615', 'WGS84 UTM Zone 16N: 32616', 'WGS84 UTM Zone 17N: 32617', 'WGS84 UTM Zone 18N: 32618', 'WGS84 UTM Zone 19N: 32619', 'WGS84 UTM Zone 20N: 32620']

list_of_optional_feature_classes = ['genericpoints', 'genericsamples', 'orientationpoints', 'geochronpoints', 'geochempoints', 'stations', 'geologiclines', 'cartographiclines',\
'isovaluelines', 'mapunitlines', 'mapunitpoints', 'mapunitoverlaypolys', 'mapunitoverlaylines', 'overlaypolys', 'datasourcepolys', 'repurposedsymbols', 'cmumapunitpolys',\
'cmulines', 'cmupoints', 'miscmapinfo', 'miscellaneousmapinformation', 'miscmapinformation', 'miscellaneousmapinfo', 'layerlist', 'standardlithology', 'fossilpoints', 'photopoints']

print("This script will create a GeMS compliant geopackage from user input.")
print("Needed info: path to folder, name of geopackage to be created, geographic coordinate system reference number")
print("MapUnitPolys, ContactsAndFaults, DescriptionofMapUnits, DataSources, and Glossary will automatically created.\n")

# get location to put geopackage
geopkg_location = get_save_folder()
geopkg_location_check = input("\nYou have entered the folder name {}. Is this correct? (y/n) ".format(geopkg_location))
if geopkg_location_check.lower() == 'y':
    pass
elif geopkg_location_check.lower() == '':
    pass
elif geopkg_location_check.lower() == 'n':
    print("Please re-enter the fold path.")
    geopkg_location = get_save_folder()
else: 
    print("Invalid input")
    geopkg_location = get_save_folder()


# get name of geopackage to be created
gpkg_name_input = input("\nName of new geopackage: ")
gpkg_name_input_check = input("\nYou have entered the geopackage name as {}. Is this correct? (y/n) ".format(gpkg_name_input))
if gpkg_name_input_check.lower() == 'y':
    pass
elif gpkg_name_input_check.lower() == '':
    pass
elif gpkg_name_input_check.lower() == 'n':
    print("Please re-enter the fold path.")
    gpkg_name_input = input("Name of new geopackage: ")
else: 
    print("Invalid input. The name will not be changed.")
gpkg_name = geopkg_location + '/' + gpkg_name_input + '.gpkg'

print("The following is a list of available coordinate reference systems. Enter only the 5 digit number.\n")
print(*list_of_crs, sep='\n')

# get coordinate reference system for geopackage layers
coord_sys_input = check_coord_sys()
coord_sys_input_check = input("\nYou have entered the coordinate reference system code: {}. Is this correct? (y/n) ".format(coord_sys_input))
if coord_sys_input_check.lower() == 'y':
    pass
elif coord_sys_input_check.lower() == '':
    pass
elif coord_sys_input_check.lower() == 'n':
    print("Please re-enter the fold path.")
    coord_sys_input = input("Name of new geopackage: ")
else: 
    print("Invalid input. The name will not be changed.")
coord_sys = get_coord_sys(coord_sys_input)


if int(coord_sys_input) < 102629:
    organization = 'EPSG'
else:
    organization = 'ESRI'


gpkg = GeoPackage.create(gpkg_name, flavor=coord_sys)
srs = SRS(get_srs(coord_sys), organization, int(coord_sys_input), coord_sys)


# Basic Automatically created feature classes
create_map_unit_polys()
create_contact_and_faults()
create_desc_map_units()
create_data_sources_table()
create_glossary_table()
create_generic_points()
create_generic_samples()
create_orientation_points()
create_geochron_points()
create_geochem_points()
create_stations_points()
create_geologic_lines()
create_cartographic_lines()
create_iso_value_lines()
create_map_unit_lines()
create_map_unit_points()
create_map_unit_overlay_polys()
create_map_unit_overlay_lines()
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
