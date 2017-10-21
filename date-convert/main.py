import csv
import json

ALL_YEARS = [
    '12', '11', '10', '09', '08', '07',
    '06', '05', '04', '03', '02', '01'
]

def get_data(name):
    years = dict()
    with open(name) as f:
        reader = csv.reader(f)
        for row in reader:
            new_row = row[0].split('-')
            if new_row[0] not in years:
                years[new_row[0]] = list()
            try:
                years[new_row[0]].append(new_row[1])
            except Exception as e:
                print(e)
    return years


def get_counts(data):
    for key in data.keys():
        new_list = list()
        for year in ALL_YEARS:
            new_list.append({year:data[key].count(year)})
        data[key] = new_list
    return data


if __name__ == '__main__':
    input_file = 'dates.csv'
    print('get data...')
    array = get_data(input_file)
    print('count months...')
    all_data = get_counts(array)
    print(all_data)
