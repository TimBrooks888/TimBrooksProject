# simple_typing_game.py
import time
import random

def typing_game():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    word = random.choice(words)
    print(f"Type the word: {word}")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    if user_input == word:
        print(f"Correct! Time taken: {end_time - start_time:.2f} seconds")
    else:
        print("Incorrect!")

if __name__ == "__main__":
    typing_game()
