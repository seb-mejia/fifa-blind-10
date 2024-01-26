## Rules

* The objective is to have a sorted board by FIFA rankings in ascending order.
* You are given an empty board with ten slots.
* There are ten turns. For each turn, you will be randomly assigned a country to place on the board.
* You will not be given the same country more than once.
* You cannot delete countries from the board, nor may you overwrite them.

Example of a winning board as of November 15, 2023:

\[🇨🇴 (17), 🇵🇦 (44), 🇿🇦 (64), 🇭🇳 (78), 🇹🇬 (119), 🇨🇾 (124), 🇳🇪 (129), 🇰🇭 (178), 🇱🇦 (188), 🇸🇲 (207)]

## Features

* If you press "H" before starting this game, you will receive hints on where to rank the country.
  * These hints are based on the ratio of the country's rank to the total number of countries (207 for men's, 192 for women's).
* You can play with men's rankings (M) or women's rankings (W).
* Various quality of life improvements that the TikTok filter doesn't have: You cannot get repeat countries, rankings are displayed after you put a country on the board, and winning/losing boards are determined for you.
* I thought about creating a combined rankings gamemode, where each country's ranking can be male or female to create a winning board.
  * But then I'd have to consider all 10! = 3628800 possible board orderings. And you couldn't see how your board is being evaluated at the moment.
  * Maybe I attempt to tackle this in the future.

## Acknowledgements

This project was inspired by Austin Krance's "FIFA Blind 10" game series on TikTok. Sample gameplay can be found on his account: https://www.tiktok.com/@austinkranceminivids/video/7265843116551179562

## Built With

* [<img src=https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/438px-Python-logo-notext.svg.png alt="Python" width="50"/>](https://www.python.org)
* [<img src="https://miro.medium.com/v2/resize:fit:1400/1*tecoiavyUYc6GKveN7wQYg.png" alt="BeautifulSoup" width="150" url=[BeautifulSoup-url]/>](https://www.crummy.com/software/BeautifulSoup/)

## Getting Started

This is a terminal-based game and may be played locally. The game was designed and tested on Visual Studio Code, meaning that the game can be reliably run on VS Code. Be sure you have installed Beautiful Soup in addition to Python. An Internet connection is required since this game accesses the latest FIFA World Rankings. 

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python-logo]: https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/438px-Python-logo-notext.svg.png
[Python-url]: https://www.python.org
[BeautifulSoup-logo]: https://miro.medium.com/v2/resize:fit:1400/1*tecoiavyUYc6GKveN7wQYg.png
[BeautifulSoup-url]: https://www.crummy.com/software/BeautifulSoup/
