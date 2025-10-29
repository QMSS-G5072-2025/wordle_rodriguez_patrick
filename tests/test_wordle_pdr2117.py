"""Simple tests for Wordle functions."""

from wordle_pdr2117.wordle_pdr2117 import (
    validate_guess,
    check_guess,
    is_valid_word,
    calculate_game_score,
)


def test_validate_guess_basic():
    """Test that validate_guess accepts valid lowercase words."""
    assert validate_guess("crane") == True
    assert validate_guess("CRANE") == False


def test_check_guess_perfect():
    """Test that check_guess returns all green for perfect match."""
    result = check_guess("crane", "crane")
    assert len(result) == 5
    assert result[0] == ('c', 'green')
    assert result[4] == ('e', 'green')