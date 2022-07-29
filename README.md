# GeMS-Create-Geopackage
A command line Python script to automatically create GeMS compliant geopacackages for QGIS

* For this to run properly you need to install pygeopkg
pip install pygeopkg

Do not run this script in QGIS. As it stands it will not work trying to run the script in QGIS. The sccript prompts for input which will cause the script 
to crash in QGIS. This can be run through an IDE like Visual Studio Code or Geanie, or you can run the script through a terminal session.

This script with prompt the user initally for 3 pieces of information: the path to store the geopackage once created, a name for the geopackage, 
and a coordinate reference system number. Examples would include 26916 for NAD83 UTM Zone 16N or 32603 for WGS84 UTM Zone 3N.

Currently only NAD83 UTM Zones 1 - 20 and WGS84 UTM Zones 1 - 20 are currently available. 

More information on coordinate reference systems can be found at https://spatialreference.org/.
