import csv
from pathlib import Path
import xml.etree.ElementTree as ET
import re


def read_csv(folder, csv_file):
    p = Path.cwd()
    with open(p / folder / csv_file) as f:
        csv_dict_reader = csv.DictReader(f, delimiter=',')
        users_lst_of_dicts = list(csv_dict_reader)
    return users_lst_of_dicts


def read_xml(folder, xml_file):
    p = Path.cwd()
    with open(p / folder / xml_file) as f:
        tree = ET.parse(f)
    root = tree.getroot()

    users_list = []
    for user in root.findall('./user/users/user'):
        user_data = user.attrib.copy()
        for field in user:
            user_data[field.tag] = field.text
        users_list.append(user_data)

    return users_list


def remove_empty_records(data, fields):
    new_data = list(filter(lambda item: not all((not item[field]) for field in fields),
                           data)
                    )
    return new_data


def clean_data(data, fields):
    data = remove_empty_records(data, fields)
    print("REMOVED EMPTY\n")

    for item in data:
        for field in fields:
            if not item[field]:
                data.remove(item)
                break
            else:
                item[field] = re.sub('\(.*\)', "", item[field])  # remove data in parentheses
                item[field] = re.sub('\[.*\]', "", item[field])  # remove data in square brackets
    return data


def collect_users_data(folder, csv_file, xml_file):
    users_from_csv = read_csv(folder, csv_file)
    users_from_xml = read_xml(folder, xml_file)

    users_from_csv_clean = clean_data(users_from_csv, ['username'])
    users_from_xml_clean = clean_data(users_from_xml, ['first_name', 'last_name'])

    for usr in users_from_csv_clean:
        print(usr)

    print("=========================================================")
    for usr in users_from_xml_clean:
        print(usr)


if __name__ == '__main__':
    folder = 'source_files'
    csv_file = "test_task.csv"
    xml_file = "test_task.xml"

    collect_users_data(folder, csv_file, xml_file)
