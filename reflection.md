# 🔍 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

- Describe at least three bugs you found during Phase 1.
- For each, explain what you expected to happen versus what actually happened.

1. **Reversed hint messages**: When I guessed a number higher than the secret, the game displayed "Go HIGHER!" instead of "Go LOWER!". Similarly, guessing below the secret showed "Go LOWER!" when it should have said, "Go HIGHER!". This made it impossible to narrow down the correct answer since the hints led you further away.

2. **Swapped difficulty ranges**: Normal mode was using a range of 1–100, and Hard mode was using 1–50. I expected Normal to have a smaller range than Hard, but they were flipped. This meant "Normal" was actually harder than "Hard" in terms of number range.

3. **Attempt counter mismatch**: The debugger section showed the attempt count starting at 1 on initial page load, but when a new game started, it reset to 0. I expected the counter to be consistent — either always starting at 0 or always at 1.

4. **No input validation for out-of-range values**: The game accepted numbers like 500 or -10 as valid guesses even when the range was 1–100. I expected the game to reject or warn about values outside the valid range.

---

## 2. How did you use AI as a teammate?

- Describe two types of AI suggestions you received: one correct and one incorrect/misleading.

**Correct suggestion**: I asked the AI to explain why the hints were pointing in the wrong direction. It correctly identified that in the `check_guess` function, the conditions were mapped to the wrong messages — `guess > secret` returned "Go HIGHER!" when it should have returned "Go LOWER!" The fix was simply swapping the two hint strings. I verified this by running the game with the debug panel open, guessing above the secret number, and confirming the hint now said: "Go LOWER!"

**Incorrect/misleading suggestion**: When I asked the AI to help fix the difficulty range issue, it initially suggested changing the maximum attempts per difficulty instead of fixing the actual number ranges in `get_range_for_difficulty`. This would have left the core bug in place. I rejected this suggestion and gave it a more specific context about the range function, which led to the correct fix: swapping the return values so Normal returns `(1, 50)` and Hard returns `(1, 100)`.

---

## 3. Debugging and testing your fixes

- Describe how you verified your repairs.

I used a combination of automated tests and manual testing. First, I wrote pytest cases in `tests/test_game_logic.py` targeting the specific bugs: tests to verify that Normal returns a range of 1–50 and Hard returns a range of 1–100, and tests to confirm that a guess higher than the secret returns a "LOWER" hint and vice versa. I ran `pytest` in the terminal and confirmed all tests passed. Then I played through the game manually at each difficulty level with the Developer Debug Info panel open, verifying that hints matched expectations and the ranges were correct for each difficulty setting.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Every time you interact with a Streamlit app — clicking a button, typing in a text box — the entire Python script reruns from top to bottom. This means any regular variable gets reset to its initial value on every interaction. Session state (`st.session_state`) is like a dictionary that survives these reruns. In this game, the secret number, attempt count, and score all need to persist across button clicks, so they're stored in session state. Without it, the secret number would regenerate every time you submit a guess, making the game unwinnable.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- This could be a testing habit, a prompting strategy, or a way you used Git.

Writing targeted tests before and after fixing bugs. Having a failing test that specifically checks for the broken behavior, then seeing it pass after the fix, gave me much more confidence than just manual testing alone. I also found that giving the AI a specific file context (like referencing `logic_utils.py` directly) produced much better suggestions than vague prompts.

- What is one thing you would do differently next time you work with AI on a coding task?

I'd spend more time understanding the code myself before asking the AI for fixes. A couple of times, I jumped straight to asking for a solution, and the AI's suggestion didn't match what I actually needed because I hadn't described the problem precisely enough. Reading the code first and forming my own hypothesis would help me write better prompts.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI-generated code can look correct at first glance but contain subtle logic errors that only show up during testing. This project reinforced that I need to always verify AI suggestions against actual behavior rather than trusting them at face value.
