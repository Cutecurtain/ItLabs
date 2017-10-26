# Iteration Laboratories |DAT255 2017|

## Group members

| Name               |  Github nickname   |
|--------------------|--------------------|
| Robert Agrell      |  Car0b1nius        |
| Jack Ahlkvist      |  jacktheman        |
| Niklas Baerveldt   |  NiklasBaerveld    |
| Linnéa Bark        |  linneabark        |
| Alice Gunnarsson   |  blackfisken       |
| Max Johansson      |  blizzlord         |
| Eli Knoph          |  ZeroGravity97     |
| Jonatan Magnusson  |  asdBeowulf        |
| Aron Sandstedt     |  Cutecurtain       |
| Matilda Sjöblom    |  rackarmattan      |
| Rasmus Tomasson    |  FrodoIT           |

# Projects
The project is divided in three different parts. The python scripts, the app and the camera.

## Process Resources
In the beginning of the project the group made a  [`Social Contract`](/Social_Contract.pdf), in which we state what unwritten rules the group should apply.

### Trello
SCRUM was visualized and managed in Trello. The links are below:
1. [Trello Sprint 1](https://trello.com/b/Fd1E4pl3/sprint-1)
2. [Trello Sprint 2](https://trello.com/b/8V52WH8t/sprint-2)
3. [Trello Sprint 3](https://trello.com/b/jozrVdBN/sprint-3)
4. [Trello Sprint 4](https://trello.com/b/bICjmW0V/sprint-4)
5. [Trello Sprint 5](https://trello.com/b/0KTiahAt/sprint-5)

### Google Drive
Seperate sprint retrospectives, application APK's, motivation levels for group members can be found in our shared [Google Drive folder](https://drive.google.com/drive/folders/0B7JWVG3xDoQTYks4YUJvTFU2TE0?usp=sharing).

### Sprint Retrospective
The Sprint Retrospective Conclusion can be found in our repo at [Dokumentation från alla sprint retrospectives.pdf](https://github.com/Cutecurtain/ItLabs/blob/master/Dokumentation%20fr%C3%A5n%20alla%20sprint%20retrospectives.pdf)

### Product Vision
The product vision can be found at [`/Vision`](/Vision.pdf)

## App
Our app ItLabsApp is built on the previous app WirelessIno. However, we did add a button for turning ACC on and off, as well as some moderations to the GUI. We also added a connection between the newly established python server and the application, which can be found in [`/OurPythonScripts/car_driver.py`](/OurPythonScripts/car_driver.py) and in  [`/itlabsapp/MopedStream.java`](/app/WirelessIno/app/src/main/java/itlabsapp/MopedStream.java). Because of the many similarities with the previous code we did not test this code with FindBugs.*

## Python scripts
The MOPED is run on python scripts. Our own code can be found in pi as well as in OurPythonScripts. The folder pi was imported when the project started, because of that there are a lot of unused files (e.g ^.wav). The pi folder is an exact copy of the home folder on the MOPED. The reason for this is that we had to change the CAN clock rate, and comment out all the uses of the file 'nav_imu.py' since some of the MOPEDs had problems with their IMU. We did not test this code with FindBugs because it does not run on python. The python equivalent recommended by the teachers 'PyLint' does not search for static errors but for grammatical errors and unreadable code. For example unnecessary parenthesis and space.*

## Camera
We borrowed code for image recognition from  Jakob Axelsson, who had written the existing code from Optipos for Camreader. The camera is used for making the MOPED follow an object of our choice. The object of our choice is hard coded and cannot be changed without changing the code itself. We chose a red rectangle as our object. The camera code can be found in [`/OurPythonScripts/camReader.py`](/OurPythonScripts/camReader.py).

*Further reading about our test methods can be found in our [`Reflection Report`](/ITLabs(1).pdf).
