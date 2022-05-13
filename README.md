# Udacity Adventure Game
This project was submitted to Udacity during the Intro to Programming Nanodegree course. It is a text-based Python adventure game created from scratch. In this game, a dog lover goes through a simple morning routine before work. Their decisions add to their `minutes` which will eventually dictate whether the player gets:
1. 🔥 Fired. 
2. 💰 A raise. 
3. 🏆 A promotion and new office! 🥳

### Try it out!
[![Run on Repl.it](https://repl.it/badge/github/JaqiGates/udacity-adventure-game)](https://replit.com/@JaqiGates/udacity-adventure-game#morning.py)

## Project Instructions
Udacity learners were given the freedom to choose what the "adventure" would be, but the game had to follow certain guidelines.

- Print descriptions of what is happening in the game.
- Add a time delay to each printed message so the player can have a better reading experience. I created a `pause_print` function for this purpose.
- Make the player's choices produce different outcomes in the game.
- Allow the player to choose their own path in the game buy inputing responses that will not crash the program. I created a `vaild_input` function so players can enter their response in uppercase or lowercase, with any punctuation or additional words, so `'yes'` is just as good as `'Yes, please!'` If the input is not vaild the program will display `'Sorry, I don't understand.'` and ask for input again.
- Add functions and refactor code in order to keep things as organized and logical as possible.
- Use the `random` module. I randomized the day of the week, the dog's name, and the number of people in the coffee shop. The dog's name was just for fun.
- Create a way to keep track of whether the player is winning or losing. In this game I created a `minutes` variable which increases a certain amount according to the player's choices.
- Ask if the player wants to play again.
