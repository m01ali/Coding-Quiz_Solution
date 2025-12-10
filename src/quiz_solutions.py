from __future__ import annotations
from typing import Iterable, List

# Each function adheres to the requirement of accepting input arguments
# and returning the computed output without performing any direct I/O.

# Question 1

def majority_element(nums: List[int]) -> int:
    """Return the value that appears more than ⌊n/2⌋ times.

    Uses the Boyer-Moore majority vote algorithm which guarantees
    linear time and constant space.
    """

    if not nums:
        raise ValueError("nums must not be empty")

    candidate = nums[0]
    votes = 0
    for num in nums:
        if votes == 0:
            candidate = num
            votes = 1
        elif num == candidate:
            votes += 1
        else:
            votes -= 1

    return candidate


# Question 2

def is_palindrome_phrase(s: str) -> bool:
    """Check whether the sanitized phrase is a palindrome.

    Two-pointer technique that skips non-alphanumeric symbols on the fly,
    yielding O(n) time and O(1) extra space.
    """

    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if left < right and s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


# Question 3

def climb_stairs(n: int) -> int:
    """Return the number of distinct ways to reach step n.

    Optimized Fibonacci DP with constant auxiliary space.
    """

    if n <= 0:
        raise ValueError("n must be positive")
    if n <= 2:
        return n

    prev_two, prev_one = 1, 2
    for _ in range(3, n + 1):
        prev_two, prev_one = prev_one, prev_one + prev_two
    return prev_one


_ROMAN_VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


# Question 4

def roman_to_int(s: str) -> int:
    """Convert a Roman numeral string to its integer value."""

    if not s:
        raise ValueError("s must be non-empty")

    total = 0
    i = 0
    while i < len(s):
        value = _ROMAN_VALUES[s[i]]
        if i + 1 < len(s):
            next_value = _ROMAN_VALUES[s[i + 1]]
            if value < next_value:
                total += next_value - value
                i += 2
                continue
        total += value
        i += 1
    return total


# Question 5

def max_subarray_sum(nums: Iterable[int]) -> int:
    """Return the maximum possible subarray sum using Kadane's algorithm."""

    iterator = iter(nums)
    try:
        first = next(iterator)
    except StopIteration as exc:
        raise ValueError("nums must contain at least one element") from exc

    max_sum = current = first
    for num in iterator:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    return max_sum
