##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2022
## Author: sara.diamond@duke.edu (for ENV859)
##---------------------------------------------------------------------

#%% Import Packages
import arcpy, sys, os
#Allow arcpy to overwrite output
arcpy.env.overwriteOutput = True

#%% Import a single file as a file object
# Set input variables (Hard-wired)
inputFile = 'V:/ARGOSTracking/ARGOSTracking/data/ARGOSData/1997dg.txt'
outputSR = arcpy.SpatialReference(54002)
outputFC = "V:/ARGOSTracking/ARGOSTracking/scratch/ARGOStrack.shp"

## Prepare a new feature class to which we'll add tracking points
# Create an empty feature class; requires the path and name as separate paramters
outPath,outName = os.path.split(outputFC)
arcpy.CreateFeatureclass_management(outPath, outName, "POINT",'','','',outputSR)

#%% Construct a while loop to iterate through all lines in the datafile
# Open the ARGOS data file for reading
inputFileObj = open(inputFile,'r')

# Get the first line of data, so we can use a while loop
lineString = inputFileObj.readline()

# Start the while loop
while lineString:
    
    # Set code to run only if the line contains the string "Date: "
    if ("Date :" in lineString):
        
        # Parse the line into a list
        lineData = lineString.split()
        
        # Extract attributes from the datum header line
        tagID = lineData[0]
        
        # Extract location info from the next line
        line2String = inputFileObj.readline()
        
        # Parse the line into a list
        line2Data = line2String.split()
        
        # Extract the date we need to variables
        obsLat = line2Data[2]
        obsLon= line2Data[5]
        
        obsDate = lineData[3]
        obsTime = lineData[4]
        obsLC = lineData[7]
        
        # Print results to see how we're doing
        print (tagID,obsDate,obsTime,obsLC,"Lat:"+obsLat,"Long:"+obsLon)
        
    # Move to the next line so the while loop progresses
    lineString = inputFileObj.readline()
    
#Close the file object
inputFileObj.close()
