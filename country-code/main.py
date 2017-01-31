import csv
import json

import requests


def get_data(name):
    with open(name) as f:
        reader = csv.reader(f)
        results = dict()
        results['n/a'] = 0
        for row in reader:
            if not(len(row)):
                results['n/a'] += 1
            else:
                country_code = row[0]
                if country_code in results:
                    results[country_code] += 1
                else:
                    results[country_code] = 1
        return results


def convert_to_list(data):
    country_list = list()
    for country_code in data:
        country_list.append({
            'code': country_code,
            'count': data[country_code]
        })
    return country_list


def get_country(countries):
    base = 'https://restcountries.eu/rest/v1/alpha/'
    count = 1
    total = len(countries)
    for country in countries:
        print('    getting {0} of {1}'.format(count, total))
        r = requests.get('{0}{1}'.format(base, country['code']))
        if r.status_code is 200:
            country['name'] = r.json()['name']
        else:
            country['name'] = 'n/a'
        count += 1
    return countries


def create_file(file_name, data):
    with open(file_name, 'w') as f:
        for obj in data:
            w = csv.writer(f)
            w.writerow(obj.values())
    return True


if __name__ == '__main__':
    input_file = 'country.csv'
    output_fule = 'data.csv'
    print('get data...')
    country_counts = get_data(input_file)
    print('convert data to list...')
    array = convert_to_list(country_counts)
    print('get country name from api...')
    all_data = get_country(array)
    print('write to csv...')
    create_file(output_fule, all_data)
    print('done!')
