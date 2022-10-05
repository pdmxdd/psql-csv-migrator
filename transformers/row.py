def to_dict(row):
    row_dict = row[0].__dict__
    if "_sa_instance_state" in row_dict.keys(): del row_dict["_sa_instance_state"]
    return row_dict
