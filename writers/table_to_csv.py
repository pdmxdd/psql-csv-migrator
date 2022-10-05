from csv import DictWriter
from .utilities import generate_table_header_list

def initialize_csv_for_table(table):
    # overwrite file with table header
    filepath = f"data/{table.__tablename__}.csv"
    headers = generate_table_header_list(table)
    with open(filepath, "w") as csvfile:
        writer = DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
    print(f"headers written into {filepath}")

def write_row_dict_to_csv(table, row_dict):
    # appends row_dict to CSV
    filepath = f"data/{table.__tablename__}.csv"
    headers = generate_table_header_list(table)
    with open(filepath, "a") as csvfile:
        writer = DictWriter(csvfile, fieldnames=headers)
        writer.writerow(row_dict)
    print(f"{row_dict} written to {filepath}")
