import openpyxl
book = openpyxl.Workbook()
sheet = book.active
data = open('data1.txt')
row = 1
for i in data.readlines():
    print(i)
    sheet[row][0].value = i
    row += 1



book.save('my_book.xlxs')
book.close()
data.close()