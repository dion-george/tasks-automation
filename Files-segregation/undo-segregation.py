import os
import shutil
import os.path

currentPath = os.getcwd()
dirs = [d for d in os.listdir() if os.path.isdir(os.path.join( d))]
print (dirs)
slash = "\\"

for x in dirs:
    if(x=="Text" or x=="Data" or x=="Audio" or x=="Video" or x=="3DImage"
    or x=="RasterImage" or x=="VectorImage" or x=="PageLayout" or x=="Spreadsheet"
    or x=="Database" or x=="Executable" or x=="Game" or x=="CAD" or x=="GIS"
    or x=="Web" or x=="Plugin" or x=="Font" or x=="System" or x=="Settings"
    or x=="Encoded" or x=="Compressed" or x=="DiskImage" or x=="Developer" or x=="Backup"
    or x=="Misc" or x=="Other"): 
        oldpath = currentPath + slash + x
        print(oldpath)
        directoryArray = os.listdir(x)
        print (directoryArray)
        for i in directoryArray:
            shutil.move(oldpath + slash + i,currentPath + slash +i)

        shutil.rmtree(oldpath)


