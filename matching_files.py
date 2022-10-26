import csv
from pathlib import Path
import xml.etree.ElementTree as ET


def read_csv(folder, csv_file):
    p = Path.cwd()
    with open(p / folder / csv_file) as f:
        # csv_reader = csv.reader(f, delimiter=',')
        # users_lst = list(csv_reader)[1:]
        csv_dict_reader = csv.DictReader(f, delimiter=',')
        users_lst_of_dicts = list(csv_dict_reader)
    # for row in users_lst_of_dicts:
    #     print(row)
    return users_lst_of_dicts


def read_xml(folder, xml_file):
    p = Path.cwd()
    with open(p / folder / xml_file) as f:
        tree = ET.parse(f)
    root = tree.getroot()
    # print("root: ", root.tag)

    users_list = []
    for user in root.findall('./user/users/user'):
        # print(user.tag, user.attrib)
        user_data = user.attrib.copy()
        for field in user:
            user_data[field.tag] = field.text
            # print(" ", field.tag, field.text)
        users_list.append(user_data)

    # for item in users_list:
    #     print(item)
    return users_list


def collect_users_data(folder, csv_file, xml_file):
    users_from_csv = read_csv(folder, csv_file)
    users_from_xml = read_xml(folder, xml_file)

    for usr in users_from_csv:
        print(usr)

    for usr in users_from_xml:
        print(usr)


if __name__ == '__main__':
    folder = 'source_files'
    csv_file = "test_task.csv"
    xml_file = "test_task.xml"

    collect_users_data(folder, csv_file, xml_file)
