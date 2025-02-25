CREATE TABLE year (
    "id_year" INTEGER,
    "year_name" TEXT,
    PRIMARY KEY ("id_year")
);

CREATE TABLE exam_type (
    "id_type" INTEGER,
    "exam_type" TEXT,
    PRIMARY KEY ("id_type")
);

CREATE TABLE questions (
    "id" INTEGER,
    "year" INTEGER,
    "exam_subject" INTEGER,
    "question" TEXT,
    "option_1" TEXT,
    "option_2" TEXT,
    "option_3" TEXT,
    "option_4" TEXT,
    "option_5" TEXT,
    "correct_option" TEXT,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("year") REFERENCES "year"("id_year"),
    FOREIGN KEY ("exam_subject") REFERENCES "exam_type"("id_type"),
);