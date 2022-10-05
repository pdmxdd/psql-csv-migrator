from sqlalchemy import select

def select_all_rows(session, model):
    return session.execute(select(model)).all()
