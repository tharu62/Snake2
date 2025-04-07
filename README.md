# Snake2
This is the sequel to Snake, it implements all the feature of the original game plus a competitor (on the write part of the screen) controlled by the CPU and a random obstacle generation to raise the difficulty. 

The goal is to beat the score of the CPU. The CPU has the possibility of using two types of algorithms for path finding : Dijkstra or A star.

To set the path finding algorithm it is require to un-comment some code on the Snake2.py file in the main loop of the game.

The game is already released with the A star algorithm with a launch ready executable.

The snake can be controller with arrow keys and the game can be paused with the "p" key.

## Install
To build the python executable from source code: 
- clone this repo in a folder
- delete snake2.exe
- run this command using pyinstaller in the chosen folder:
```bash
pyinstaller -F .\src\snake2.py .\src\snake.py .\src\algorithms.py
```
