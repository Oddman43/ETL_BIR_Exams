CREATE TABLE year (
    "id_year" INTEGER,
    "year_name" TEXT,
    PRIMARY KEY ("id_year")
);

CREATE TABLE exam (
    "id_type" INTEGER,
    "exam_type" TEXT,
    PRIMARY KEY ("id_type")
);

CREATE TABLE questions (
    "id" INTEGER,
    "exam_year" INTEGER,
    "exam_subject" INTEGER,
    "question" TEXT,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("exam_year") REFERENCES "year"("id_year"),
    FOREIGN KEY ("exam_subject") REFERENCES "exam"("id_type")
);

CREATE TABLE questions_options (
    "option_id" INTEGER,
    "question_id" INTEGER,
    "option_num" INTEGER,
    "option_text" TEXT,
    "is_correct" BOOLEAN,
    PRIMARY KEY ("option_id"),
    FOREIGN KEY ("question_id") REFERENCES "questions"("id")
);
