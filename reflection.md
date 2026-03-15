# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looks pretty simple. A guessing game with numbers, using a text box. Also, there's a developer info box for testing, and the ability to show hints and change difficulty.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The hints were indeed backwards. (LOWER when it should be HIGHER)
The difficulties are not accurate either, the "hard" difficulty isn't harder it's easier.
After clicking the New Game button, the attempts are reset, but guesses are not able to be submitted.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot and ChatGPT. Mostly Copilot, but used ChatGPT for setup.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
When I was fixing the hints being reversed, the AI suggested the correct output, and I verified the result through logical reasoning. When the guess > secret, the hint should be GO LOWER, and vice versa when the guess < secret.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI's suggestion was misleading when changing the values for the "hard" difficulty. It wanted to set the "hard" difficulty to 200 instead of changing the "normal" to 50, and the "hard" to 100.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
