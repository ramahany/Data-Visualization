import pandas as pd
import numpy as np


def get_data(file_path):
    data = pd.read_csv(file_path, na_values='?')
    data = check_headers(data)
    return data


def check_headers(data):

    # check first column
    first_column = data.iloc[:, 0]
    # Check if the first column is numeric
    is_numeric = pd.api.types.is_numeric_dtype(first_column)

    # Check for unique and sequential values
    is_unique = first_column.is_unique
    is_sequential = (first_column.sort_values().diff().dropna() == 1).all()

    if is_numeric and (is_unique or is_sequential):
        data = data.drop(data.columns[0], axis=1)

    # check for headers
    first_row = data.columns.values
    header_is_present = False
    if all((isinstance(item, str) and not item.isdigit()) for item in first_row):
        header_is_present = True

    headers = []
    if not header_is_present:
        for i in range(len(first_row)):
            headers.append(f'X{i+1}')
        data.columns = headers

    data.insert(0, 'ID', range(1, len(data) + 1))
    return data




