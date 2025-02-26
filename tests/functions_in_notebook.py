import pandas as pd


def compute_expected_rows(year: int, topic: str) -> tuple:
    """Computes and returns metadata about the exam for a given year and topic

    Args:
        year (int): The year of the exam
        topic (str): The topic of the exam

    Returns:
        tuple: Contains:
            - max_rows: The expected maximum number of rows in the DataFrame
            - num_options: The number of questions in the exam
            - exam_type_acronym: The acronym for the exam type

    """
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
    num_options: int = 0
    for target_year, info_list in info_year_dict.items():
        if year <= target_year:
            max_rows = (info_list[0] * info_list[1]) + info_list[0]
            num_options = info_list[1]
            break
    else:
        max_rows = 1050
        num_options = 4
    return max_rows, num_options, save_name_dict[topic]


def process_multi_line_str(df: pd.DataFrame) -> pd.DataFrame:
    """Function to handle truncated lines

    Args:
        df (pd.DataFrame): A pandas dataframe

    Returns:
        pd.DataFrame: Returns the DataFrame without truncated lines
    """
    i: int = 0
    while i < len(df) - 1:
        if i < len(df) - 1 and df.iloc[i].endswith("-"):
            df.iloc[i] = df.iloc[i][:-1] + df.iloc[i + 1]
            df = df.drop(i + 1)
            df = df.reset_index(drop=True)
        else:
            i += 1
    n: int = 0
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


def fix_incorrect(num_row: list[int], df: pd.DataFrame) -> pd.DataFrame:
    """Fix the incorrect rows in the DataFrame

    Args:
        num_row (list): List of ids to fix
        df (pd.DataFrame): The DataFrame to fix

    Returns:
        pd.DataFrame: Fixed
    """
    num_row: list = sorted(num_row, reverse=True)
    for n in num_row:
        df.iloc[n] = df.iloc[n] + df.iloc[n + 1]
        df = df.drop(n + 1)
        df = df.reset_index(drop=True)
    return df
