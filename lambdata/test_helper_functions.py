""" Unit tests for Helper Functions """

import pytest
import pandas as pd
import lambdata

from lambdata import null_count, split_dates, rm_outlier, list_2_series

def test_null_count():
    assert isinstance(x, tuple)
    assert isinstance(y, tuple)
    assert isinstance(non_null_count, int)

def test_split_dates():
    assert isinstance(date_series, pd.Series)
    assert 'month' in df.columns()

def test_rm_outlier():
    assert isinstance(iqr, float)

def test_list_2_series():
    assert isinstance(s1, pd.Series)
    assert isinstance(df, pd.DataFrame)