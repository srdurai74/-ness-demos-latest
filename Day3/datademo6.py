import csv

def get_data(file_name):
    data_file = open(file_name,'r')
    reader = csv.reader(data_file)

    next(reader) # to skip the header
    data = []
    for rowdata in reader:
        data.append(rowdata)

    return data


print(get_data('testdata.csv'))