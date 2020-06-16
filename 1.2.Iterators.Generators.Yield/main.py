
#    1. Iterator Class


import json
import md5hash


class Iterator:

    def __init__(self, file):
        self.count = -1
        with open(file, encoding='utf-8') as f:
            self.data = json.load(f)

    def __iter__(self):
        return (self)

    def __next__(self):
        self.count += 1
        if self.count < len(self.data):
            country_name = self.data[self.count]['name']['common']
            link = country_name + ' - ' + 'https://en.wikipedia.org/wiki/' + country_name
            with open('countries.txt', 'a', encoding='utf-8') as f:
                f.writelines(link + '\n')
        else:
            raise StopIteration

"""
2. Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
"""
def generator_hash(file):
    with open(file, encoding='utf8') as f:
        for l in f.readlines():
            print(l.strip())

generator_hash('countries.txt')



country_list = Iterator('countries.json')

for item in country_list:
    next(country_list)
