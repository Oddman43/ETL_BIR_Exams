def compute_expected_rows(year: int, topic: str) -> tuple:
    info_year_dict: dict = {
        2011: [260, 5],
        2014: [235, 5],
        2018: [235, 4],
        2020: [185, 4],
        2021: [210, 4],
    }
    save_name_dict: dict = {
        "BIOLOGÍA": "bir",
        "FARMACIA": "fir",
        "QUÍMICA": "qir",
        "MEDICINA": "mir",
    }
    max_rows: int = 0
    num_questions: int = 0
    for target_year, info_list in info_year_dict.items():
        if year <= target_year:
            max_rows = (info_list[0] * info_list[1]) + info_list[0]
            num_questions = info_list[1]
            break
    if year >= 2021:
        max_rows = 1050
        num_questions = 4
    return (
        max_rows,
        f"clean_{save_name_dict[topic]}_{year}.csv",
        num_questions,
        save_name_dict[topic],
    )


def process_multi_line_str(df):
    i = 0
    while i < len(df) - 1:
        line = df.iloc[i]
        if i < len(df) - 1 and line.endswith("-"):
            df.iloc[i] = df.iloc[i][:-1] + df.iloc[i + 1]
            df = df.drop(i + 1)
            df = df.reset_index(drop=True)
        else:
            i += 1
    n = 0
    while n < len(df) - 1:
        if n + 1 < len(df):
            try:
                int(df.iloc[n + 1][0:1])
                n += 1
            except ValueError:
                df.iloc[n] = df.iloc[n] + " " + df.iloc[n + 1]
                df = df.drop(n + 1)
                df = df.reset_index(drop=True)
        else:
            break
    return df


def fix_incorrect(num_row, df):
    num_row = sorted(num_row, reverse=True)
    for n in num_row:
        df.iloc[n] = df.iloc[n] + df.iloc[n + 1]
        df = df.drop(n + 1)
        df = df.reset_index(drop=True)
    return df
