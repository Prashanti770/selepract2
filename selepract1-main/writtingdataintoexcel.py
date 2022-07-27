import openpyxl

path="C:\Prashanti M\data2.xlsx"

workbook=openpyxl.load_workbook(path)
sheet=workbook.active #if only one sheet is there

for r in range(1,5): #4rows will be created
    for c in range(1,4): #3 columns will be created
        sheet.cell(row=r,column=c).value="itcrats"

workbook.save(path) #to save the written data

