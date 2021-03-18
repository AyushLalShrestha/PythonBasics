"""
Compares 1st json file with 2nd json file.
Order of elements matter when 2 lists are compared.
Order of elements does not matter when 2 dicts are compared.

Override (edit) method:read_json_rows as per you requirement.
"""

import json
import os

def read_json_rows(fp):
    with open(fp, "r") as fh:
        json_result = json.load(fh)
        return json_result.get('rows', [])


def is_equal_lists(l1, l2):
    if len(l1) != len(l2):
        return False

    for i in range(len(l1)):
        if not is_equal(l1[i], l2[i]):
            return False
    return True


def is_equal_dicts(d1, d2):
    for k1, v1 in d1.items():
        # print(f"{v1} vs. {d2[k1]} == {is_equal(v1, d2[k1])}")
        if not (k1 in d2 and is_equal(v1, d2[k1])):
            return False
    return True


def is_equal(v1, v2):
    if type(v1) != type(v2):
        return False
    elif isinstance(v1, list):
        return is_equal_lists(v1, v2)
    elif isinstance(v1, dict):
        return is_equal_dicts(v1, v2)
    elif isinstance(v1, str):
        return v1.strip() == v2.strip()
    else:
        return v1 == v2


def compare_json(fp1, fp2):
    match_elements = []
    match_count = 0
    unmatch_count = 0
    rows_1 = read_json_rows(fp1)
    rows_2 = read_json_rows(fp2)
    for i, row_1 in enumerate(rows_1):
        for j, row_2 in enumerate(rows_2):
            match = is_equal_dicts(row_1, row_2)
            if match:
                match_count += 1
                match_elements.append((i+1, j+1))
            else:
                unmatch_count += 1
    print(f"Rows in 1st JSON: {len(rows_1)}")
    print(f"Rows in 2nd JSON: {len(rows_2)}")
    print(f"Number of row-matches between two JSON: {match_count}")
    print(f"Number of row-un-matches between two JSON: {unmatch_count}")
    for i,j in match_elements:
        print(f"1st JSON's row {i} == row {j} of 2nd JSON")


if __name__ == '__main__':
    # file1 = "/Users/ayushshrestha/Desktop/bfbbaad1fbd6beb691470ac2d093637d_5f71a6b8e4673a943f493b39.json"
    # file2 = "/Users/ayushshrestha/Desktop/bfbbaad1fbd6beb691470ac2d093637d_5f71a49fe4673a943f493b38.json"
    file1 = os.path.join(os.path.dirname(__file__), "json1.json")
    file2 = os.path.join(os.path.dirname(__file__), "json2.json")
    compare_json(file1, file2)
