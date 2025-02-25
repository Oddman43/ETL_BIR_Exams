import sqlite3


path: str = "bir_warehouse.db"


years = [x for x in range(2004, 2025, 1)]
exam_type = ["bir", "fir", "qir", "mir"]


year_table: str = """
CREATE TABLE year (
    "id_year" INTEGER,
    "year_name" TEXT,
    PRIMARY KEY ("id_year")
);
"""

exam_table: str = """
CREATE TABLE exam (
    "id_type" INTEGER,
    "exam_type" TEXT,
    PRIMARY KEY ("id_type")
);
"""

questions_table: str = """
CREATE TABLE questions (
    "id" INTEGER,
    "exam_year" INTEGER,
    "exam_subject" INTEGER,
    "question" TEXT,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("exam_year") REFERENCES "year"("id_year"),
    FOREIGN KEY ("exam_subject") REFERENCES "exam"("id_type"),
);
"""

questions_options_table: str = """
CREATE TABLE questions_options (
    "question_id" INTEGER,
    "option_num" INTEGER,
    "option_text" TEXT,
    "is_correct" BOOLEAN,
    PRIMARY KEY ("question_id", "option_num"),
    FOREIGN KEY ("question_id") REFERENCES "questions"("id")
);
"""


with sqlite3.connect(path) as sql_db:
    cur = sql_db.cursor()
    cur.execute(year_table)
    cur.execute(exam_table)
    cur.execute(questions_table)
    cur.execute(questions_options_table)
    sql_db.commit()
    # for year in years:
    #     query_1: str = "INSERT INTO year (year_name) VALUES(?)"
    #     cur.execute(query_1, (year))
    #     sql_db.commit()
    # for e_type in exam_type:
    #     query_2: str = "INSERT INTO exam (exam_type) VALUES(?)"
    #     cur.execute(query_2, (e_type))
    #     sql_db.commit()
