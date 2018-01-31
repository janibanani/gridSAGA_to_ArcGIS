# Import system modules
import arcgisscripting, os
  
# Create the Geoprocessor object  
gp = arcgisscripting.create()  
import arcpy  
import os  
import glob  
  
# Pot do datotek ASCII 
filepath = r"D:\LIDARucenje\UvoziVecListov\UvozSAGAvGRID\SGRD\ASCII"  
# Pot za rezultate
outFolder = r"D:\LIDARucenje\UvoziVecListov\UvozSAGAvGRID\SGRD\ASCII\GRID"  
  
ascList = glob.glob(filepath + "/*.asc")  
print ascList
  
for ascFile in ascList:  
    outRaster = outFolder + "/" + os.path.split(ascFile)[1][:-4]
    print outRaster  
    arcpy.ASCIIToRaster_conversion(ascFile, outRaster, "FLOAT")
