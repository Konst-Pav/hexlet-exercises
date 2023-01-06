#!/usr/bin/env python3
import datetime
from collections import Counter


def get_men_counted_by_year(users):
    years = []
    for user in users:
        if user['gender'] == 'male':
            bday = datetime.datetime.strptime(user.get('birthday'), '%Y-%m-%d')
            years.append(bday.year)
    years_counter = Counter(years).most_common()
    years_dict = {}
    for year in years_counter:
        key, value = year
        years_dict[key] = value
    return years_dict


users = [
    {'name': 'Bronn', 'gender': 'male', 'birthday': '1973-03-23'},
    {'name': 'Reigar', 'gender': 'male', 'birthday': '1973-11-03'},
    {'name': 'Eiegon', 'gender': 'male', 'birthday': '1963-11-03'},
    {'name': 'Sansa', 'gender': 'female', 'birthday': '2012-11-03'},
    {'name': 'Jon', 'gender': 'male', 'birthday': '1980-11-03'},
    {'name': 'Robb', 'gender': 'male', 'birthday': '1980-05-14'},
    {'name': 'Tisha', 'gender': 'female', 'birthday': '2012-11-03'},
    {'name': 'Rick', 'gender': 'male', 'birthday': '2012-11-03'},
    {'name': 'Joffrey', 'gender': 'male', 'birthday': '1999-11-03'},
    {'name': 'Edd', 'gender': 'male', 'birthday': '1973-11-03'},
]


def main():
    print(get_men_counted_by_year(users))
# {1973: 3, 1963: 1, 1980: 2, 2012: 1, 1999: 1}


if __name__ == '__main__':
    main()
