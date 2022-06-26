from src.app import db
from sqlalchemy import text


def delete_last_inserted(table_name):
    get_sql = text("SELECT * FROM " + table_name + " ORDER BY id DESC LIMIT 1;")
    inserted_id = db.engine.execute(get_sql).fetchone()[0]
    remove_sql = text("DELETE FROM " + table_name + " WHERE id = '" + inserted_id + "'")
    db.engine.execute(remove_sql)
