import pytest

from problems.p3110_Score_of_a_String.p3110_Score_of_a_String import Solution

def test_3110_Score_of_a_String():
    
    solution = Solution()
    assert solution.scoreOfString("hello") == 13
    assert solution.scoreOfString("zaz") == 50