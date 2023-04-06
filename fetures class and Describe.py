import arcpy
# from arcpy import env
arcpy.env.workspace=(r"D:\PWD Project\State_Layers")
fc = arcpy.ListFeatureClasses()
for i in fc:
    des= arcpy.Describe(i)
    print(des.name + " : " + des.shapeType) # here describe the Featue type like Point, Line Polygon


