# HCI Project-PhotoGlue
### A Minesweeper game created through Pyqt5

##### Objective of the project

The project objective is the reproduction of the famous Minesweeper game, using Pyqt5.
Below the functions provided by the application are described.

##### Functions

- The game: the application provides the game grid. If mines button is clicked, the user looses the game. On the contrary, if all the non clicked buttons are mines the user wins. There is also the possibility to check a button if the user think that it is a mine.

- Refresh Button: if the user wants to start another match with the same grid characteristics, he can press the refresh button.

- Create new game: the user can create a new game with different grid characteristics: he can choose between three difficulty type (Beginner, Intermediate, Expert) or he can create a personal grid through the custom possibility.

- Save, load or delete the games: everytime the user can save a match in progress, load a saved game or delete some unnecessary saved games.

- Rankings: for the three difficulty type (Beginner, Intermediate, Expert) there are the rankings (one for each type). Only the first 20 best times are shown in each ranking. If the user does a new record on a ranking, the application leads the user to insert his name in the ranking.

- Autosave: a game in progress is saved every five seconds or after a grid button is clicked.

##### Packages Installation

The needed packages to play this Minesweeper game are:

- PYTHON (Recommended Version: 3.6.6)
- PYQT (Recommended Version : 5.9.2) 

##### Important notes

The Operating System used for the project development is Ubuntu. If you want to use the application on an other Operating System(like Windows), you need to modify the file paths in the project code: the policies are different depending on the Operating System used.
