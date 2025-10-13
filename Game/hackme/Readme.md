# 🕵️ Codebreaker: Simple Python Game

Welcome to **Codebreaker**, a fun little Python guessing game you can play right in your terminal!  
Try to **crack the secret 3-digit code** before you run out of attempts. 🔢

---

## 🎮 How to Play

1. Run the game with:
   ```bash
   python3 codebreaker_simple.py
   ```
2. The computer will generate a random **3-digit secret code** (digits may repeat).
3. You have **6 attempts** to guess the code.
4. After each guess, you’ll get emoji feedback:

   | Emoji | Meaning |
   |--------|----------|
   | ✅ | Correct digit in the **right position** |
   | ⚠️ | Digit is in the code but in the **wrong position** |
   | ❌ | Digit is **not in the code** |

### 🧩 Example

If the secret code is `123` and you guessed `321`, the feedback would be:
```
⚠️3 ⚠️2 ⚠️1
```
That means all digits are in the code but in the wrong places.

---

## 💻 Requirements

- Python 3.6 or later  
(Already installed on most systems)

---

## 🚀 Run the Game

### 🐧 On Linux / macOS
Clone or download this repository, then run:

```bash
python3 codebreaker_simple.py
```

If you’re on Linux and want to make it executable:
```bash
chmod +x codebreaker_simple.py
./codebreaker_simple.py
```

### 🪟 On Windows
1. **Install Python** (if not installed):
   - Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Download and install **Python 3.x**
   - ✅ Make sure to check “Add Python to PATH” during installation.

2. **Open Command Prompt or PowerShell**  
   Navigate to the folder where you saved the file:
   ```bash
   cd path\to\your\file
   ```

3. **Run the game:**
   ```bash
   python codebreaker_simple.py
   ```
   If that doesn’t work, try:
   ```bash
   python3 codebreaker_simple.py
   ```

---

## 🧠 Example Gameplay

```
=== CODEBREAKER ===
Can you guess the 3-digit code?
✅ = correct spot, ⚠️ = wrong spot, ❌ = not in code

[6 attempts left] Enter 3 digits: 123
⚠️1 ❌2 ✅3
[5 attempts left] Enter 3 digits: 173
ACCESS GRANTED! ✅ You cracked the code!
```

---

## 🧑‍💻 Author
Built with ❤️ by a Python enthusiast.

Enjoy cracking the code! 💣
