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
    for target_year, info_list in info_year_dict.items():
        if year <= target_year:
            max_rows = (info_list[0] * info_list[1]) + info_list[0]
            break
    if year >= 2021:
        max_rows = 1050
    return max_rows, f"clean_{save_name_dict[topic]}_{year}.csv"
