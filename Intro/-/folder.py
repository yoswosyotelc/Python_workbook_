
text ='sample text to save \\n new Line!'
# \\n is ... for new line
##
print(text)
##
##savefile= open('examplefile.txt','w')

#to save file on the desk top follow
##savefile= open('C:\\Users\\user\\Desktop\\examplefile.dwg','w')
##savefile= open('C:\\Users\\user\\Desktop\\examplefile.txt','w')
##
##here for number b/n 1-10... then
##make the range(1,10)
##savefile= open('C:\\Users\\user\\Desktop\\Newfolder\\0'+j+'_html_css\\index.html','w')

##226

##here for number b/n 10- final ... then
##make the range(10,final)
##savefile= open('C:\\Users\\user\\Desktop\\Newfolder\\'+j+'_html_css\\index.html','w')

# C:\\Users\\user\\yotelc\\Java workbook\\java exercise\\w3resource\\solved\\1Basics
# 'D:\\DesignDetaill&Qty\\dsn_wobk_pk\\bdg workbook\\_MathCAD\\_mCAD workbook\\Math_Challenge\\1HighSchoolMath\\\\java_files\B&IA\\0'+a+'_chapter\\src\\Ex'+a+'.'+j+'.java'
##D:\\DesignDetaill&Qty\\dsn_wobk_pk\\bdg workbook\\_MathCAD\\_mCAD workbook\\Math_Challenge\\1HighSchoolMath\\mcdCAD\B&IA\\05_chapter

#C:\\Users\\user\\yotelc\\Java workbook\\java exercise\\pgm by Doing\\solution\\src
i=1
# g=2
for i in range(100,227):
    j=str(i)
    # a=str(g)
    savefile= open('C:\\Users\\user\\yotelc\\Java workbook\\java exercise\\pgm by Doing\\solution\\src\\solu'+j+'.java','w')
    savefile.write(text)
    savefile.close()



##"C:\\\Users\\user\\Desktop\\_HTML5&CSS3_4\\01_html_css"
# open(name[, mode[, buffering]]) 
# name
# The file name of the with path specified...


# modes
# 'w'_______ for writing
# 'r'_______ for reading

# buffering ...// optional
