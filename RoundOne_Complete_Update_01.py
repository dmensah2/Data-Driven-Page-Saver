#----------------------------------------------------------------------------#
# Name:        Round One
# Author:      Deidre Mensah
# Created:     01/02/2020
# Description:  Takes location input from user to create and save new Round One map
#----------------------------------------------------------------------------#
#import arcpy to access esri python module
import arcpy, os
arcpy.env.overwriteOutput = True

arcpy.env = r"C:\GIS\Research\Projects\Tenant\Q-R\RoundOne"

mxd = arcpy.mapping.MapDocument(r"C:\GIS\Research\Projects\Tenant\Q-R\RoundOne\01_Demo_DD_5-10-15-20.mxd")
dataFrame = arcpy.mapping.ListDataFrames(mxd)[0]
pageAddress = mxd.dataDrivenPages.pageRow.Address
pageState = mxd.dataDrivenPages.pageRow.State
in_keyID = raw_input("Enter your keyIDs: ")

#Gets user input of IDs for locations and then creates a data driven page series based off entry
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.name == "Mask":
        lyr.definitionQuery ="keyID IN " + str(in_keyID)
        Extent = lyr.getExtent(True) # visible extent of layer
        dataFrame.extent = Extent
        arcpy.RefreshActiveView() # redraw the map
        dataFrame.scale = 320000 #sets scale after map refresh
        mxdName = os.path.join(r"C:\GIS\Research\Projects\Tenant\Q-R\RoundOne\01_" + str(pageAddress) + "_" + str(pageState) + ".mxd")
        mxd.saveACopy(mxdName)
        new_mxd = arcpy.mapping.MapDocument(mxdName)
        for pageNum in range(1, new_mxd.dataDrivenPages.pageCount + 1):
            new_mxd.dataDrivenPages.currentPageID = pageNum
            pageAddress = new_mxd.dataDrivenPages.pageRow.Address
            pageState = new_mxd.dataDrivenPages.pageRow.State
            new_mxdName = os.path.join(r"C:\GIS\Research\Projects\Tenant\Q-R\RoundOne\01_" + str(pageAddress) + "_" + str(pageState) + ".mxd")
            print new_mxdName + " has been saved"
            new_mxd.saveACopy(new_mxdName)
        del new_mxd
        arcpy.Delete_management(mxdName)
del mxd

print "process complete"