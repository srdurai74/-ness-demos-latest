import openpyxl
import pytest


def get_data(file_name):
    data = []

    data_file = openpyxl.load_workbook(file_name)
    sheet = data_file.active

    for row in sheet.iter_rows(min_row=2):
        cell_values = []
        for cell in row:
            cell_values.append(cell.value)

        data.append(cell_values)


    return data


# print(get_data('TestData.xlsx'))


@pytest.mark.parametrize("username,password",get_data('TestData.xlsx'))
def test_login(username,password):
    if((username !='Admin') or (password !='admin123')):
        print(username+" "+password+"Failed")
    else:
        print("Test Passed")