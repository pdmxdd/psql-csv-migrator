def generate_table_header_list(table):
    removes = [
        "__module__",
        "__tablename__",
        "__doc__",
        "_sa_class_manager",
        "__table__",
        "__init__",
        "__mapper__",
        "__mapper_args__",
    ]
    table_headers = list(table.__dict__.keys())
    for remove in removes:
        if remove in table_headers: table_headers.remove(remove)
    return table_headers

