from hypothesis import given, assume
import hypothesis.strategies as st
import sys 
import os 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import (
    reverse_twice,
    is_sorted,
    buggy_sort,
    remove_duplicates,
)

# ✅ Property 1: Reversing twice returns original list
@given(st.lists(st.integers()))
def test_reverse_twice_identity(lst):
    assert reverse_twice(lst) == lst

# ✅ Property 2: Buggy sort should result in sorted list
@given(st.lists(st.integers()))
def test_buggy_sort_sorted_output(xs):
    sorted_xs = buggy_sort(xs)
    assert is_sorted(sorted_xs)

# ✅ Property 3: Idempotency of sort
@given(st.lists(st.integers()))
def test_sort_idempotency(xs):
    sorted_once = sorted(xs)
    sorted_twice = sorted(sorted_once)
    assert sorted_once == sorted_twice

# ✅ Property 4: Remove duplicates has only unique items and is a subset
@given(st.lists(st.integers()))
def test_remove_duplicates_properties(xs):
    result = remove_duplicates(xs)
    assert len(result) == len(set(result))
    assert set(result).issubset(set(xs))

# ✅ Property 5: Length of reversed twice == original
@given(st.lists(st.integers()))
def test_reverse_twice_preserves_length(lst):
    assert len(reverse_twice(lst)) == len(lst)

# ✅ Property 6: Check identity with empty list
def test_reverse_twice_empty_list():
    assert reverse_twice([]) == []
