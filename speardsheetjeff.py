import xlrd, xlwt
usersearch = str(input("What is the name of the company?"))
workbook = xlrd.open_workbook('companylist.csv.xlsx', on_demand = True)
worksheet = workbook.sheet_by_index(0)
i = 0
for i in range(worksheet.nrows):
    if usersearch == worksheet.cell(i,1).value:
        print (worksheet.cell(i,0).value)
        i += 1
        g = 1
if g != 1:
    print("Company not found")

