'''
Created on 26 mar 2015

@author: Jakob Axelsson

This program is a client that captures images from the Raspberyy Pi camera, and sends those images to a server who
does image processing and sends back the result to the client.

TODO:
- Add CAN output of the received data. See https://libbits.wordpress.com/2012/05/22/socketcan-support-in-python/ or http://elinux.org/Python_Can.
- Start capturing the next image as soon as possible, even if the result from the previous one has not yet been received.

This code is based on: http://picamera.readthedocs.org/en/release-1.9/recipes1.html#capturing-to-a-network-stream
It is intended to run on the Raspberry Pi.

Installation instructions:
- Update the firmware to the latest version
$ sudo apt-get update
$ sudo apt-get upgrade
- Reboot
- Install Python 3, if not already present:
$ sudo apt-get install python3
- Get the Python 3 package manager:
$ sudo apt-get install python3-pip
- Install camera software:
$ pip-3.2 install --user picamera
$ sudo apt-get install python3-picamera
- Install other libraries:
$ sudo pip-3.2 install requests
$ sudo apt-get install python-dev python-setuptools
$ sudo pip-3.2 install Pillow
- Enable the camera:
$ sudo raspi-config
Then select enable camera from the menu
- Run the program (specifying a map as argument, which is optional; add "&" if running from a script):
$ python3 OptiposRPiClient.py SSECorridorMap.json

To make optipos start when booting the RPi, do the following (see http://www.stuffaboutcode.com/2012/06/raspberry-pi-run-program-at-start-up.html):
- Create a file called /etc/init.d/optipos (note that this file has to be edited as sudo).
- The contents of the file should be:
#! /bin/sh
# /etc/init.d/optipos

### BEGIN INIT INFO
# Provides:          optipos
# Required-Start:    $all
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start optipos on boot
# Description:       Start optipos on boot
### END INIT INFO

# If you want a command to always run, put it here

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting optipos"
    # run application you want to start
    cd /home/pi/Optipos
    python3 OptiposRPiClient.py SSECorridorMap.txt > optipos-trace.txt 2>&1
    ;;
  stop)
    echo "Stopping optipos"
    # kill application you want to stop
    ;;
  *)
    echo "Usage: /etc/init.d/optipos {start|stop}"
    exit 1
    ;;
esac

exit 0

- Make the script executable:
$ sudo chmod 755 /etc/init.d/
- Register the script to be run at start-up:
$ sudo update-rc.d optipos defaults
- Reboot

If the script needs to be removed from the boot sequence:
$ sudo update-rc.d -f  optipos remove
'''

#import logging
import picamera
import requests
import sys
import time
from PIL import Image
# Libraries needed for CAN communication
import socket
import struct


# Libraries for image processing needed to convert image from RGB to greyscale
# from PIL import Image


#def getMAC(interface):
#    """
#    Return the MAC address of interface
#    """
#    try:
#        result = open("/sys/class/net/" + str(interface) + "/address").readline()
#    except:
#        result = "00:00:00:00:00:00"
#    return result[0:17]


#def setMap(url, mac, mapFile):
#    """
#    Set the map to be used for positioning, which is achieved by calling a service on the server.
#    """
#    print("Setting file name to " + mapFile)
#    try:
#        response = requests.post(url + "/selectmap", params={"mac": mac, "map": mapFile})
#    except Exception:
#        response = "...Failed!"
#    return response


#def postImage(session, url, mac):
#    """
#    Post an image to the server.
#    """
#    print("Posting image...")
#    try:
#        # Convert image to grayscale
#        #        im = Image.open("/dev/shm/optiposimage.jpg").convert("L").save("/dev/shm/optiposimage.jpg", quality = 25)
#        # Send image to server
#        response = session.post(url + "/processimage", params={"mac": mac},
#                                files={"file": ("", open("/dev/shm/optiposimage.jpg", "rb"), "image/jpeg")}).text
#    except Exception:
#        response = "Connection broken"
#    return response


#def initializeCAN(network):
#    """
#    Initializes the CAN network, and returns the resulting socket.
#    """
#    # create a raw socket and bind it to the given CAN interface
#    s = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
#    s.bind((network,))
#    return s


#def writePositionToCAN(canSocket, canFrameID, posX, posY, orientation, qualityFactor, delay):
#    """
#    Writes the position of the vehicle to CAN. The frame should include:
#    Variable                        Type            Unit    Bytes    Description
#    vehiclePositionX                signed short    cm        2      Global x coordinate of vehicle; set to 32767 if no marker was found
#    vehiclePositionY                signed short    cm        2      Global y coordinate of vehicle; set to 32767 if no marker was found
#    vehicleOrientation              unsigned char   0..255    1      Maps to degrees using 256 * vehicleOrientation / 360; set to 0 if no marker was found
#    vehiclePositionQualityFactor    unsigned char   0..100%   1      -
#    vehiclePositionAge              unsigned short  ms        2      Duration of image processing, i.e., delay from capturing image to sending the calculated position
#    """
#
#    # Build the CAN frame with length 8.
#    data = struct.pack("=hhBBH", int(posX * 100), int(posY * 100), round(256.0 * orientation / 360.0),
#                       min(100, int(qualityFactor * 100)), round(delay * 1000))
#    print("Orientation = " + str(round(360 * orientation / 256.0)))
#    print("QF = " + str(min(100, int(qualityFactor * 100))))
#    frame = struct.pack("=IB3x8s", canFrameID, 8, data)
#    try:
#        canSocket.send(frame)
#    except socket.error:
#        print("Error writing vehicle position to CAN")

def isColour(pixelColour, targetColour):
    redDiff = abs(pixelColour[0] - targetColour[0])
    greenDiff = abs(pixelColour[1] - targetColour[1])
    blueDiff = abs(pixelColour[2] - targetColour[2])
    if (redDiff < 70 and greenDiff < 70 and blueDiff < 70):
        return True
    else:
        return False


def isGreen(pixelColour):
    green = (0, 255, 0)
    return isColour(pixelColour, green)


def isRed(pixelColour):
    if pixelColour[0] > pixelColour[2] > pixelColour[1] and pixelColour[0] > 90:
        return True
    return False


def isBlue(pixelColour):
    blue = (0, 0, 255)
    return isColour(pixelColour, blue)


def isWhite(pixelColour):
    delta = 100
    if abs(pixelColour[0] - pixelColour[1]) <= delta and abs(pixelColour[0] - pixelColour[2]) <= delta and abs(
                    pixelColour[1] - pixelColour[2]) <= delta:
        if pixelColour[0] >= 120:
            return True
    return False

    # return isColour(pixelColour,white)


def isBlack(pixelColour):
    black = (0, 0, 0)
    return isColour(pixelColour, black)


def checkColourCode(colourWidth, centerColour, imageList):
    isBlueFound = isBlue(imageList[centerColour + colourWidth])
    isRedFound = isRed(imageList[centerColour - colourWidth])
    isColourCodeCorrect = isBlueFound and isRedFound
    return isColourCodeCorrect


def checkColourCode1(colourWidth, centerColour, imageList):
    isWhiteRightFound = isWhite(imageList[centerColour + colourWidth])
    isWhiteLeftFound = isWhite(imageList[centerColour - colourWidth])
    isColourCodeCorrect = isWhiteRightFound and isWhiteLeftFound
    return isColourCodeCorrect


def getGreenBorders(list, greenStartIndex):
    rightborder = greenStartIndex
    leftborder = greenStartIndex
    while isGreen(list[rightborder]):
        rightborder += 1

    while isGreen(list[leftborder]):
        leftborder -= 1
    leftborder += 1
    return (leftborder, rightborder)


def getWhiteBorders(list, greenStartIndex):
    rightborder = greenStartIndex
    leftborder = greenStartIndex
    while isWhite(list[rightborder]):
        rightborder += 1

    while isWhite(list[leftborder]):
        leftborder -= 1
    leftborder += 1
    return (leftborder, rightborder)


def getRedBorders(list, greenStartIndex):
    rightborder = greenStartIndex
    leftborder = greenStartIndex
    while isRed(list[rightborder]):
        rightborder += 1

    while isRed(list[leftborder]):
        leftborder -= 1
    leftborder += 1
    return (leftborder, rightborder)


dx = 9


# def analyseImage():
#    im = Image.open("/dev/shm/optiposimage.jpg")
#    #im = im.convert("RGBA")
#    im.load()
#    imList = list(im.getdata())
#    middle = im.width * im.height // 2
#    print(imList[middle])
#    for x in range(middle, 0, -dx):
#        if (isGreen(imList[x])):
#            greenBorders = getGreenBorders(imList, x)
#            gw = greenBorders[1] - greenBorders[0]
#            x += gw
#            print(gw)
#            greenCenter = greenBorders[0] + gw // 2
#            if (checkColourCode(gw, greenCenter, imList)):
#                return (greenCenter % im.width) / im.width
#    for x in range(middle, im.width * im.height - 1, dx):
#        if (isGreen(imList[x])):
#            greenBorders = getGreenBorders(imList, x)
#            gw = greenBorders[1] - greenBorders[0]
#            x += gw
#            print(gw)
#            greenCenter = greenBorders[0] + gw // 2
#            if (checkColourCode(gw, greenCenter, imList)):
#                return (greenCenter % im.width) / im.width

def analyseImage1():
    im = Image.open("/dev/shm/optiposimage.jpg")
    # im = im.convert("RGBA")
    im.load()
    imList = list(im.getdata())
    t = im.size
    width = t[0]
    height = t[1]
    middle = width * height // 2
    print(imList[middle])
    start = time.time()
    for x in range(middle, 0, -dx):
        if (isRed(imList[x])):
            redBorders = getRedBorders(imList, x)
            rw = redBorders[1] - redBorders[0]
            if(rw > 20):
                #print(rw)
                redCenter = redBorders[0] + rw // 2
                if (checkColourCode1(rw, redCenter, imList)):
                    return (redCenter % width) / width
            if time.time() - start > 3: break
    for x in range(middle, width * height - 1, dx):
        if (isRed(imList[x])):
            redBorders = getRedBorders(imList, x)
            rw = redBorders[1] - redBorders[0]
            if(rw > 20):
                #print(rw)
                redCenter = redBorders[0] + rw // 2
                if (checkColourCode1(rw, redCenter, imList)):
                    return (redCenter % width) / width
            if time.time() - start > 6: break


image_value = 0.0

def main(thread_event,ivContainer):
    markerf = open("/tmp/marker0", "w")
    ## Set up logging
    #logging.basicConfig(filename="optipos.log", filemode="w", level=logging.DEBUG, format="%(asctime)s %(message)s")
    #logger = logging.getLogger(__name__)

    ## Get the mac address of the client. It is used by the server to identify different clients.
    #macAddress = getMAC("eth0")
    #print("MAC address is " + macAddress)

    ## server = 'http://jaxlaptop.sics.se:8080'
    #server = 'http://appz-ext.sics.se:8080'
    #canNetwork = "can0"
    #canFrameID = 1025
    # Initialize the CAN network, if it exists
    #try:
    #    canSocket = initializeCAN(canNetwork)
    #except:
    #    pass

    # If a map file name was provided on the command line, send it to the server
    #if (len(sys.argv) > 1):
    #    setMap(server, macAddress, sys.argv[1])

    with picamera.PiCamera() as camera:
        # It is recommended to use 972 x 972 or 1944 x 1944 pixels to get full camera field of view
        #        resolution = 486
        resolution = 972
        camera.resolution = (resolution, resolution)

        # Use sports mode to reduce blur
        #        camera.exposure_mode = "sports"

        # Use backlit mode to handle lamps, and use the ISO setting to get short exposure time
        camera.iso = 800
        #        camera.exposure_compensation = -2 # ev
        #        camera.shutter_speed = 6000
        camera.meter_mode = "backlit"

        # Let the camera warm up for 2 seconds
        time.sleep(2)

        response = None
        # Construct a stream to hold image data temporarily (we could write it directly to connection but in this
        # case we want to find out the size of each capture first to keep the protocol simple)
        #counter = 0
        for _ in camera.capture_continuous("/dev/shm/optiposimage.jpg", 'jpeg', use_video_port=True, quality=10):
            #import shutil
            #shutil.copy("/dev/shm/optiposimage.jpg", "/home/pi/java/image_" + str(counter) + ".jpg")
            #counter += 1
            if thread_event != None:
                thread_event.wait()
            try:
                # Get the start time, to be able to calculate response time
                start = time.time()
                response = analyseImage1()
                end = time.time()
                print('Received [' + str(response) + '] after ' + str(end - start) + ' s')
                print("actual image_value:", str(image_value))
                if response != None:
                    ivContainer[0] = response * 100

                # If the response is a valid position, write it to CAN, else do nothing

            except Exception as e:
                # Catch all exceptions, and print them to the log. Then continue taking more pictures
                print(str(e))
                #return None



if __name__ == '__main__':
    main(None, None)
