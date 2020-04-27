from arcpy.sa import *
arcpy.env.workspace="D:\\MRT\\data\\tif\\input"
#覆盖
outFolder = "D:\\MRT\\data\\tif\\input"
arcpy.CheckOutExtension("spatial")
env.overwriteOutput=1

#将路径下的文件存在变量f里
g = os.walk(r"D:\\MRT\\data\\tif\\input")
f = []
for path,dir_list,file_list in g:
    for file_name in file_list:
        print(os.path.join(path, file_name) )
        f.append(os.path.join(path, file_name))
rlist = arcpy.ListRasters(f)
rasterList = arcpy.ListRasters("*", "tif")

#  文件夹内栅格图片列表操作
for inRaster in rasterList:
        outName = os.path.join(outFolder,str(inRaster))
        outSetNull=SetNull(inRaster,inRaster,"VALUE=-3000")
        outSetNull.save(outName)

# 最大值合成
rasterList = arcpy.ListRasters("*", "tif")
for inRaster in rasterList:
      outCellStatistics = CellStatistics(inRaster, "MAXIMUM", "DATA")
#去除边界值-32768
outCellStatisticsNull=SetNull(outCellStatistics,outCellStatistics,"VALUE=-32768")
outCellStatisticsNull.save("D:\\MRT\\data\\tif\\input\\MAXMUM.tif")