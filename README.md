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
In the beginning of the project the group made a  [`Social Contract`](/Social_Contract.pdf), in which we state what unwritten rules the group should apply.

## App
Our app ItLabsApp is built on the previous app WirelessIno. However, we did add a button for turning ACC on and off, as well as some moderations to the GUI. We also added a connection between the newly established python server and the application, which can be found in [`/OurPythonScripts/car_driver.py`](/OurPythonScripts/car_driver.py) and in  [`/itlabsapp/MopedStream.java`](/app/WirelessIno/app/src/main/java/itlabsapp/MopedStream.java). Because of the many similarities with the previous code we did not test this code with FindBugs.*

## Python scripts
The MOPED is run on python scripts. Our own code can be found in pi as well as in OurPythonScripts. The folder pi was imported when the project started, because of that there are a lot of unused files (e.g ^.wav). We did not test this code with FindBugs because it does not run on python. The python equivalent recommended by the teachers 'PyLint' does not search for static errors but for grammatical errors and unreadable code. For example unnecessary parenthesis and space.*

## Camera
We borrowed code for image recognition from blabla. The camera is used for making the MOPED follow an object of our choice. The object of our own choice is hard coded and cannot be changed without changing the code itself. We chose a red rectangle as our object. The camera code can be found in [`/OurPythonScripts/camReader.py`](/OurPythonScripts/camReader.py).

*Further reading about our test methods can be found in our [`Reflection Report`](/ITLabs(1).pdf).
