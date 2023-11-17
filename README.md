## Rules

* The objective is to have a sorted list by FIFA rankings in ascending order.
* You are given an empty list with ten slots.
* There are ten turns. For each turn, you will be randomly assigned a country to place on the list.
* You will not be given the same country more than once.
* You cannot delete countries from the list, nor may you overwrite them.

Example of a winning list as of November 15, 2023:

\[🇨🇴 (17), 🇵🇦 (44), 🇿🇦 (64), 🇭🇳 (78), 🇹🇬 (119), 🇨🇾 (124), 🇳🇪 (129), 🇰🇭 (178), 🇱🇦 (188), 🇸🇲 (207)]

## Features

* If you press "H" before starting this game, you will receive hints on where to rank the country.
  * These hints are based on the ratio of the country's rank to the total number of countries (207).
* I might add the option to combine men's rankings and women's rankings, since Austin Krance implemented this feature in his version of the game.

## Acknowledgements

This project was inspired by Austin Krance's "FIFA Blind 10" game series on TikTok. Sample gameplay can be found on his account: https://www.tiktok.com/@austinkranceminivids/video/7265843116551179562

## Built With

* [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/438px-Python-logo-notext.svg.png" alt="Python" width="50"/](https://www.python.org)
* <img src="https://miro.medium.com/v2/resize:fit:1400/1*tecoiavyUYc6GKveN7wQYg.png" alt="BeautifulSoup" width="150" url=[BeautifulSoup-url]/> 
* [![BeautifulSoup][BeautifulSoup-logo]][BeautifulSoup-url]

## Getting Started

This is a terminal-based game and may be played locally. An Internet connection is required since it accesses the latest FIFA World Rankings. This game was tested on Visual Studio Code, and fully supports this IDE.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python-logo]: https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/438px-Python-logo-notext.svg.png
[Python-url]: https://www.python.org
[BeautifulSoup-logo]: https://miro.medium.com/v2/resize:fit:1400/1*tecoiavyUYc6GKveN7wQYg.png
[BeautifulSoup-url]: https://www.crummy.com/software/BeautifulSoup/#Download
