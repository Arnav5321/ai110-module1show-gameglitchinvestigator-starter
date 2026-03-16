# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [The app is a simple number-guessing game where the player tries to guess a secret number within a limited number of attempts. It provides feedback after each guess to help the player narrow down the correct number.] 
Describe the game's purpose.
- [The hint messages were reversed: when the guess was too high, it said to go higher instead of lower and vice versa.] 
Detail which bugs you found.
- [Refactored core game logic into `logic_utils.py`, Fixed the hint logic so "Too High" now shows "Go LOWER!" and "Too Low" shows "Go HIGHER!", Corrected difficulty ranges so Normal is 1–50 and Hard is 1–100.] 
Explain what fixes you applied.

## 📸 Demo

- [Winning Screenshot] [C:\CodePath\ai110-module1show-gameglitchinvestigator-starter\Win Screenshot.png]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
