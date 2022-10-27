import csv
from pathlib import Path
import xml.etree.ElementTree as ET
import re
from fuzzywuzzy import fuzz, process


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

    for item in data:
        for field in fields:
            if not item[field]:
                data.remove(item)
                break
            else:
                item[field] = re.sub('\(.*\)', "", item[field])  # remove data in parentheses
                item[field] = re.sub('\[.*\]', "", item[field])  # remove data in square brackets
    return data


def match_names(csv_users, xml_users):
    # collecting names for comparing
    names = []
    for xml_user in xml_users:
        name = str(xml_user['first_name'] or '') + str(xml_user['last_name'] or '')
        names.append(name)

    res = []
    for csv_user in csv_users:
        username = csv_user['username'].replace('.', ' ')

        highest = process.extractOne(username, names)

        if highest[1] > 60:
            xml_record = xml_users[names.index(highest[0])]
            names[names.index(highest[0])] = ''
            res.append({**csv_user, **xml_record})
    return res


def collect_users_data(folder, csv_file, xml_file):
    users_from_csv = read_csv(folder, csv_file)
    users_from_xml = read_xml(folder, xml_file)

    users_from_csv_clean = clean_data(users_from_csv, ['username'])
    users_from_xml_clean = clean_data(users_from_xml, ['first_name', 'last_name'])
    #
    # for usr in users_from_csv_clean:
    #     print(usr)

    # print("=========================================================")
    # for usr in users_from_xml_clean:
    #     print(usr)

    matched_data = match_names(users_from_csv_clean, users_from_xml_clean)
    # print("PAIRS:")
    # for pair in pairs:
    #     print(pair)
    return matched_data


if __name__ == '__main__':
    folder = 'source_files'
    csv_file = "test_task.csv"
    xml_file = "test_task.xml"

    complete_user_data = collect_users_data(folder, csv_file, xml_file)
    for record in complete_user_data:
        print(record)
