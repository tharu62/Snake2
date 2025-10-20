# Snake2
This is the sequel to Snake, it implements all the features of the original game plus a competitor controlled by the CPU and a random obstacle generation to raise the difficulty. 
While the user plays the role of the usual green snake that eats red apples in the forest, the cpu is the evil yellow snake that searches for rotten purple apples in the shady rotten forest. 

The goal is to beat the score of the CPU. The CPU has the possibility of using two types of algorithms for path finding (A start or fixed directions).

To set the path finding algorithm it is required to un-comment some code on the Snake2.py file in the main loop of the game.

The game is already released with the A star algorithm with a launch ready executable but there are instruction for building the executable locally later on.

The snake can be controller with arrow keys and the game can be paused with the "p" key.

![Screenshot from 2025-05-16 13-17-58](https://github.com/user-attachments/assets/6f6c30ab-5e04-4e4c-bf3b-dca0141aaf0b)

## Install
Required : python3 with pygame and pyinstaller modules installed.
To build the python executable from source code: 
- clone this repo in a folder
- delete snake2.exe
- run this command using pyinstaller in the chosen folder:
```bash
pyinstaller -F .\src\snake2.py .\src\snake.py .\src\algorithm.py
```

```bash 
  _   _                        __ ___                     _      
 | | | |                      / /|__ \                   | |     
 | |_| |__   __ _ _ __ _   _ / /_   ) |      ___ ___   __| | ___ 
 | __| '_ \ / _` | '__| | | | '_ \ / /      / __/ _ \ / _` |/ _ \
 | |_| | | | (_| | |  | |_| | (_) / /_     | (_| (_) | (_| |  __/
  \__|_| |_|\__,_|_|   \__,_|\___/____|     \___\___/ \__,_|\___|
```     
