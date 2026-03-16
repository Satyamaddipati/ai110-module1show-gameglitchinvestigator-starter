from logic_utils import check_guess, get_range_for_difficulty, parse_guess

# Bug fix tests
# FIX: Wrote the following 4 tests with agent to test range and hints

def test_normal_range():
    # Normal should return range 1-50
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50


def test_hard_range():
    # Hard should return range 1-100
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100


def test_too_high_gives_go_lower_hint():
    # If guess > secret, hint should say "LOWER"
    result, message = check_guess(60, 50)
    assert result == "wrong"
    assert "LOWER" in message


def test_too_low_gives_go_higher_hint():
    # If guess < secret, hint should say "HIGHER"
    result, message = check_guess(40, 50)
    assert result == "wrong"
    assert "HIGHER" in message


# Edge case tests
def test_negative_number_is_parsed_as_valid():
    # Edge case: negative numbers are outside the game range (1-100) but parse_guess accepts them
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert err is None

def test_decimal_input_is_truncated_not_rounded():
    # Edge case: "3.7" is truncated to 3, not rounded to 4
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert value == 3  # int(float("3.7")) truncates, not rounds

def test_extremely_large_number_is_parsed_as_valid():
    # Edge case: a huge number is accepted by parse_guess even though it's outside any game range
    ok, value, err = parse_guess("999999")
    assert ok is True
    assert value == 999999
    assert err is None


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "win"
