import pytest

from src.quiz_solutions import (
    climb_stairs,
    is_palindrome_phrase,
    majority_element,
    max_subarray_sum,
    roman_to_int,
)


def test_majority_element_examples():
    assert majority_element([3, 3, 4]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2


def test_majority_element_edge_duplicates():
    assert majority_element([1, 1, 1, 2, 3, 1, 4]) == 1


def test_is_palindrome_phrase_examples():
    assert is_palindrome_phrase("A man, a plan, a canal: Panama") is True
    assert is_palindrome_phrase("race a car") is False


def test_is_palindrome_phrase_varied_characters():
    assert is_palindrome_phrase(".,") is True
    assert is_palindrome_phrase("No 'x' in Nixon") is True


def test_climb_stairs_examples():
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3


def test_climb_stairs_larger():
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89


def test_roman_to_int_examples():
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994


def test_roman_to_int_single_values():
    assert roman_to_int("III") == 3
    assert roman_to_int("IX") == 9


def test_max_subarray_sum_examples():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([1]) == 1


def test_max_subarray_sum_all_negative():
    assert max_subarray_sum([-8, -3, -6, -2, -5, -4]) == -2


def test_invalid_inputs_raise():
    with pytest.raises(ValueError):
        majority_element([])
    with pytest.raises(ValueError):
        climb_stairs(0)
    with pytest.raises(ValueError):
        roman_to_int("")
    with pytest.raises(ValueError):
        max_subarray_sum([])
