# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# A223.py
# Created on: 2021-09-29 19:24:09.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: A223 <River__line_> <Segments__polygon_> 
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
import arceditor


# Import arcpy module
import arcpy

# Script arguments
River__line_ = arcpy.GetParameterAsText(0)
if River__line_ == '#' or not River__line_:
    River__line_ = "E:\\00_Cloud\\Surfdrive\\Shared\\URC_RS analyses_share\\00_Elaborations_Daniele\\Base\\URC-D_segments.shp" # provide a default value if unspecified

Segments__polygon_ = arcpy.GetParameterAsText(1)
if Segments__polygon_ == '#' or not Segments__polygon_:
    Segments__polygon_ = "E:\\00_Cloud\\Surfdrive\\Shared\\URC_RS analyses_share\\00_Elaborations_Daniele\\Base\\URCD_dambovita_l_2017.shp" # provide a default value if unspecified

# Local variables:
v01_shp = "E:\\00_Cloud\\Surfdrive\\Shared\\URC_RS analyses_share\\00_Elaborations_Daniele\\Indicators\\A.2.2.3\\delete\\01.shp"
river_RS_shp = "E:\\00_Cloud\\Surfdrive\\Shared\\URC_RS analyses_share\\00_Elaborations_Daniele\\Indicators\\A.2.2.3\\river_RS.shp"
Modified_Input_Features = river_RS_shp
sinuosity_Pnt_shp = Modified_Input_Features
sinuosity_shp = "E:\\00_Cloud\\Surfdrive\\Shared\\URC_RS analyses_share\\00_Elaborations_Daniele\\Indicators\\A.2.2.3\\sinuosity.shp"
Modified_Input_Features__2_ = sinuosity_shp

# Process: Intersect
arcpy.Intersect_analysis("'E:\\00_Cloud\\Surfdrive\\Shared\\URC_RS analyses_share\\00_Elaborations_Daniele\\Base\\URC-D_segments.shp' #;'E:\\00_Cloud\\Surfdrive\\Shared\\URC_RS analyses_share\\00_Elaborations_Daniele\\Base\\URCD_dambovita_l_2017.shp' #", v01_shp, "ALL", "", "INPUT")

# Process: Dissolve
arcpy.Dissolve_management(v01_shp, river_RS_shp, "segment", "", "MULTI_PART", "DISSOLVE_LINES")

# Process: Add Geometry Attributes
arcpy.AddGeometryAttributes_management(river_RS_shp, "LENGTH", "METERS", "", "")

# Process: Simplify Line
arcpy.SimplifyLine_cartography(Modified_Input_Features, sinuosity_shp, "POINT_REMOVE", "500 Meters", "RESOLVE_ERRORS", "KEEP_COLLAPSED_POINTS", "CHECK", "")

# Process: Add Geometry Attributes (2)
arcpy.AddGeometryAttributes_management(sinuosity_shp, "LENGTH", "METERS", "", "")
