# logic_utils.py
# FIX: Refactored core game logic from app.py into this module using Copilot Agent mode.
# This keeps the UI (app.py) separate from the game logic for testability.


def get_range_for_difficulty(difficulty):
    """
    Returns (low, high) range for the given difficulty level.
    Easy: 1-10, Normal: 1-50, Hard: 1-100
    """
    # FIXME: Original code had Normal and Hard ranges swapped
    # FIX: Corrected so Normal returns (1, 50) and Hard returns (1, 100)
    if difficulty == "Easy":
        return 1, 10
    elif difficulty == "Normal":
        return 1, 50
    elif difficulty == "Hard":
        return 1, 100
    else:
        return 1, 50  # default fallback


def check_guess(guess, secret):
    """
    Compares the guess to the secret number.
    Returns a tuple: (result, message)
      - ("win", message) if correct
      - ("wrong", hint_message) if incorrect
    """
    # FIXME: Original code had hints reversed — "Go HIGHER!" when guess was too high
    # FIX: Swapped hint messages so they point in the correct direction
    if guess == secret:
        return "win", "🎉 You guessed it!"
    elif guess > secret:
        # FIX: guess is too high, so player needs to go LOWER
        return "wrong", "📉 Go LOWER!"
    else:
        # FIX: guess is too low, so player needs to go HIGHER
        return "wrong", "📈 Go HIGHER!"


def parse_guess(guess_str):
    """
    Parses a string input into an integer guess.
    Returns a tuple: (ok, value, error_message)
      - (True, int_value, None) on success
      - (False, None, error_string) on failure
    """
    try:
        value = int(float(guess_str))
        return True, value, None
    except (ValueError, TypeError):
        return False, None, "Please enter a valid number."
