import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
tuple(sheet['A1':'C3']) #Get all cells from a1 to c3

for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')

list(sheet.columns)[1] #get second columns cells

for cellObj in list(sheet.columns)[1]:
    print(cellObj.value)