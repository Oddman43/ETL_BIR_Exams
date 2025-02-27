import sqlite3

path: str = "../clean/bir_warehouse.db"
years = [str(x) for x in range(2004, 2025, 1)]
exam_type = ["bir", "fir", "qir", "mir"]

with sqlite3.connect(path) as sql_db:
    cur = sql_db.cursor()
    with open("schema.sql") as schema_sql:
        schema: str = schema_sql.read()
    cur.executescript(schema)
    sql_db.commit()

with sqlite3.connect(path) as sql_db:
    cur = sql_db.cursor()
    for y in years:
        query_1: str = "INSERT INTO year (year_name) VALUES(?)"
        cur.execute(query_1, (y,))
        sql_db.commit()
    for e_type in exam_type:
        query_2: str = "INSERT INTO exam (exam_type) VALUES(?)"
        cur.execute(query_2, (e_type,))
        sql_db.commit()
