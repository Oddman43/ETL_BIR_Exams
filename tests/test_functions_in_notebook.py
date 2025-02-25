import pytest
from functions_in_notebook import compute_expected_rows


def test_compute_expected_rows():
    inputs_lst = [2004, 2011, 2012, 2014, 2016, 2018, 2019, 2020, 2021, 2025]
    expected_lst = [
        (1300 + 260, "bir"),
        (1300 + 260, "bir"),
        (1175 + 235, "bir"),
        (1175 + 235, "bir"),
        (940 + 235, "bir"),
        (940 + 235, "bir"),
        (740 + 185, "bir"),
        (740 + 185, "bir"),
        (840 + 210, "bir"),
        (840 + 210, "bir"),
    ]
    for chunk in zip(inputs_lst, expected_lst):
        assert compute_expected_rows(chunk[0], "BIOLOGÍA") == chunk[1]
