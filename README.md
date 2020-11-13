# Hugo Kat Pygame Chess
Chess using Pygame

References
Alvaro, D., 2017. Devinalvaro/Yachess. [online] GitHub. Available at: <https://github.com/devinalvaro/yachess/tree/master/src> [Accessed 2 October 2020].

Code Review Stack Exchange. 2015. Enumerating Moves For A Chess Piece. [online] Available at: <https://codereview.stackexchange.com/questions/94465/enumerating-moves-for-a-chess-piece> [Accessed 11 October 2020].

GitHub. 2017. Chattarajoy/Shatranj. [online] Available at: <https://github.com/chattarajoy/Shatranj/blob/master/helperfunctions.py> [Accessed 27 September 2020].

Sanchez, A., 2016. Anthonyasanchez/Pythonchessai. [online] GitHub. Available at: <https://github.com/AnthonyASanchez/PythonChessAi> [Accessed 2 October 2020].

Instruction Manual:
You can play against the chess AI or see a live demonstrate in which the AI takes images as inputs by running main.py. To pick which mode you wish to play click on the labelled button that corresponds to your preference on the main menu screen. A drag and drop system is used to move the pieces (when playing against the AI). 
 
If you are interested in seeing how the vision code works by itself, please follow the instructions in the vision.py file. This will calibrate the colour bounds from a starting board then generate a Python board matrix from another image. 
 
To try communicating between an Arduino and a Python script, you will need to follow the instructions in the serial_communication.py. You will also need to upload the receive.ino or send.ino script to an Arduino Uno (i.e. do you want the Arduino to receive or send). When you are trying to communicate between the two scripts do not attempt to open the serial monitor - this will throw an error as it is already being used. 
NOTE: The Arduino script shows it received certain data by blinking the in-built Arduino Uno LED.

We used the picture.py file to take pictures and analyse them.The code is not implemented into the submission as there is no point taking pictures of a board that does not change. Some of the test images are saved in the images folder. To use it yourself make sure the directory in line 27 is set to a directory of your choice.

Creating a Virtual Environment (NOTE: These steps assume that you are currently in the project directory):
Step 1: In Powershell, run the following (what this does is makes a folder in the directory called "venv" and makes it a virtual environment):
py -m venv venv

Step 2:
In Powershell, run the following script: "venv/Scripts/activate"

Step 3:
pip install -r requirements.txt

TO SAVE YOUR requirements INCASE U ADD MORE:
pip freeze > requirements.txt
