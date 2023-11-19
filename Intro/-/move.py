import os, shutil
path ="C:\\Users\user\\Desktop\\pt1\\"
moveto="C:\\Users\user\\Desktop\\pt2\\"
files=os.listdir(path)
files.sort()

for f in files:
    src= path+f
    dst= moveto+f
    shutil.move(src,dst)
        
