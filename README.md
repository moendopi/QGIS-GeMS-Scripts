# GeMS-Create-Geopackage
A command line Python script to automatically create GeMS compliant geopackages for QGIS

*** For either of these scripts to run properly you need to install pygeopkg:
<b>pip install pygeopkg</b>

Additionally, the crs_dictinoary.py, srs_dictionary.py, and GeMS_basic_feature_classes.py files need to be in the same folder as 
Create_GeMS_Geopackage.py and/or Create_Full_GeMS_Geopackage.py files to run properly. 

Do not run this script in QGIS. As it stands it will not work trying to run the script in QGIS. The sccript prompts for input which will cause the script 
to crash in QGIS. This can be run through an IDE like Visual Studio Code or Geanie, or you can run the script through a terminal session.

<b>For Create_GeMS_Geopackage</b>

This script will prompt the user initally for 3 pieces of information: the path to store the geopackage once created, a name for the geopackage, 
and a coordinate reference system number. Examples would include 26916 for NAD83 UTM Zone 16N or 32603 for WGS84 UTM Zone 3N.

Currently only NAD83 UTM Zones 1 - 20 and WGS84 UTM Zones 1 - 20 are available. 

More information on coordinate reference systems can be found at https://spatialreference.org/.

Once the intial information is gathered the script will automatically create the geopackage and add the 5 basic feature classes required for a 
GeMS database: MapUnitPolys, ContactsAndFaults, and the three tables DescriptionOfMapsUnits, DataSources, and Glossary.

The user is then prompted to add additional optional feature classes. A list of feature classes is displayed. <b>DO NOT ADD SPACES IN THE FEATURE CLASS NAME. 
DO NOT ADD SPACES.</b> When you have entered all the desired feature classes, type done. The new features will be added to the geopackage. 

If you prefer not to add any aadditional or optional feature classes just type done when prompted for optional feature classes.

<b>For Create_Full_GeMS_Geopackage</b>
This script will require the same three pieces of information from the user, but will not prompt the user with any additional
optional feature classes. It will instead just create a geopackage with all the defined GeMS Features (29 feature classes and tables). 

# Create MapUnitPolys
This take your contact lines and create polygons of the bedrock from them and add the necessary GeMS fields.
*** Note: lines need to being checked that there are no dangle where lines are to intersect. There needs to be a node at the intersection, and the lines must be split at the intersection. These type of error can be checked using the Topology Checker.

# Create MapUnitOverlayPolys
This takes your surficial lines and create surficial polygons. Topology checks mentioned above apply.

# Create OverlayPolys
This take any lines like water boundaries, isograd lines, sinkhole boundaries, etc., and create overlay polygons. Topology checks required. 

# Split Concealed Contacts
This script is useful for running after all ContactsAndFaults are finished. It will find where bedrock ContactsAndFaults intersect with surficial MapUnitOverlayLines (where surficial deposits or water would cover bedrock contact) and splits them. The contacts can then be selected by location where they are covered by surficial units and changed to concealed. One small note that I haven't figure out how to get around is the creation of lots of tiny or 0 length lines. These can be safely deleted. I suspect they are lines created when split on the point of intersection and thus have no length. 
