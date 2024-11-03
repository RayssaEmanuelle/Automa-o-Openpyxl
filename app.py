import openpyxl

book = openpyxl.load_workbook("Cursoss.xlsx")
cursos_page = book["Cursos"]

for rows in cursos_page.iter_rows(min_row=2):
    for cell in rows:
        print(cell.value)