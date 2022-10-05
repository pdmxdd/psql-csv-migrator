from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from declarative_models import Users, Cars, CarsUsers
from queries.selectors import select_all_rows
from transformers.row import to_dict
from writers.table_to_csv import initialize_csv_for_table, write_row_dict_to_csv

USERNAME = "postgres"
PASSWORD = "postgres"
HOST = "127.0.0.1"
PORT = "5555"
DATABASE = "postgres"

def main():
    engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
    session = Session(engine)

    tables = [Users, Cars, CarsUsers]
    
    for t in tables:
        initialize_csv_for_table(t)
        rows = select_all_rows(session, t)
        for row in rows:
            row_dict = to_dict(row)
            write_row_dict_to_csv(t, row_dict)

    session.close()

if __name__ == "__main__":
    main()

