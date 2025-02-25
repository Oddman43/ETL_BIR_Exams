import pytest
from functions_in_notebook import compute_expected_rows


def test_compute_expected_rows():
    inputs_lst = [2004, 2011, 2012, 2014, 2016, 2018, 2019, 2020, 2021, 2025]
    expected_lst = [
        (1300 + 260, "clean_bir_2004.csv"),
        (1300 + 260, "clean_bir_2011.csv"),
        (1175 + 235, "clean_bir_2012.csv"),
        (1175 + 235, "clean_bir_2014.csv"),
        (940 + 235, "clean_bir_2016.csv"),
        (940 + 235, "clean_bir_2018.csv"),
        (740 + 185, "clean_bir_2019.csv"),
        (740 + 185, "clean_bir_2020.csv"),
        (840 + 210, "clean_bir_2021.csv"),
        (840 + 210, "clean_bir_2025.csv"),
    ]
    for chunk in zip(inputs_lst, expected_lst):
        assert compute_expected_rows(chunk[0], "BIOLOGÍA") == chunk[1]
