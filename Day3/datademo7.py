import xlrd

def get_data(file_name):
    data = []

    data_file = xlrd.open_workbook(file_name)
    sheet = data_file.sheet_by_index(0)

    for rowid in range(0,sheet.nrows):
        data.append(list(sheet.row_values(rowid,0,sheet.ncols)))

    return data


print(get_data('TestData1.xls'))