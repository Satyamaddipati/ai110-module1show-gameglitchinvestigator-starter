import streamlit as st
import random
# FIX: Importing refactored game logic from logic_utils.py
from logic_utils import check_guess, parse_guess, get_range_for_difficulty

st.set_page_config(page_title="🎮 Number Guessing Game", layout="centered")
st.title("🎮 Number Guessing Game")

# --- Difficulty Selection ---
difficulty = st.selectbox("Choose difficulty:", ["Easy", "Normal", "Hard"])
low, high = get_range_for_difficulty(difficulty)

# --- Session State Initialization ---
# FIX: Using session_state to persist values across Streamlit reruns
if "secret" not in st.session_state or st.session_state.get("difficulty") != difficulty:
    st.session_state.secret = random.randint(low, high)
    st.session_state.attempts = 0
    st.session_state.max_attempts = {
        "Easy": 10,
        "Normal": 7,
        "Hard": 5
    }.get(difficulty, 7)
    st.session_state.score = 100
    st.session_state.game_over = False
    st.session_state.message = ""
    st.session_state.difficulty = difficulty

# --- Game Input ---
st.write(f"Guess a number between **{low}** and **{high}**")
st.write(f"Attempts: {st.session_state.attempts} / {st.session_state.max_attempts}")

guess_input = st.text_input("Your guess:", key="guess_input")

if st.button("Submit Guess") and not st.session_state.game_over:
    ok, guess_value, err = parse_guess(guess_input)

    if not ok:
        st.warning(err)
    elif guess_value < low or guess_value > high:
        st.warning(f"Please enter a number between {low} and {high}.")
    else:
        st.session_state.attempts += 1
        result, message = check_guess(guess_value, st.session_state.secret)
        st.session_state.message = message

        if result == "win":
            st.session_state.game_over = True
            st.success(f"{message} You got it in {st.session_state.attempts} attempts!")
            st.balloons()
        else:
            # Deduct points for wrong guesses
            st.session_state.score = max(0, st.session_state.score - 10)
            st.info(message)

            if st.session_state.attempts >= st.session_state.max_attempts:
                st.session_state.game_over = True
                st.error(f"Game over! The secret number was {st.session_state.secret}.")

# --- Display current message if game still going ---
if st.session_state.message and not st.session_state.game_over:
    pass  # message already shown above

# --- Score Display ---
st.sidebar.header("📊 Score")
st.sidebar.write(f"Current Score: {st.session_state.score}")

# --- New Game Button ---
if st.session_state.game_over:
    if st.button("🔄 New Game"):
        st.session_state.secret = random.randint(low, high)
        st.session_state.attempts = 0
        st.session_state.score = 100
        st.session_state.game_over = False
        st.session_state.message = ""
        st.rerun()

# --- Developer Debug Info ---
with st.expander("🔧 Developer Debug Info"):
    st.write(f"Secret Number: {st.session_state.secret}")
    st.write(f"Attempts: {st.session_state.attempts}")
    st.write(f"Max Attempts: {st.session_state.max_attempts}")
    st.write(f"Score: {st.session_state.score}")
    st.write(f"Game Over: {st.session_state.game_over}")
    st.write(f"Difficulty: {difficulty}")
    st.write(f"Range: {low} - {high}")
