from PIL import Image
import picamera
import requests
import time
def isColour(pixelColour,targetColour):
    redDiff = abs(pixelColour[0] - targetColour[0])
    greenDiff = abs(pixelColour[1] - targetColour[1])
    blueDiff = abs(pixelColour[2] - targetColour[2])
    if(redDiff < 50 and greenDiff < 50 and blueDiff < 50):
        return True
    else: return False

def isGreen(pixelColour):
    green = (0,255,0)
    return isColour(pixelColour,green)

def isRed(pixelColour):
    red = (255,0,0)
    return isColour(pixelColour, red)

def isBlue(pixelColour):
    blue = (0,0,255)
    return isColour(pixelColour, blue)

def getGreenWidth(list, greenStartIndex):
    x = greenStartIndex
    while isGreen(list[x]):
        x += 1
    return x-greenStartIndex

def checkColourCode(colourWidth, centerColour, imageList):
    isBlueFound = isBlue(imageList[centerColour + colourWidth])
    isRedFound = isRed(imageList[centerColour - colourWidth])
    iscolourCodeCorrect = isBlueFound and isRedFound
    return iscolourCodeCorrect

def analyseImage():
    im = Image.open("/dev/shm/optiposimage.jpg")
    im.load()
    list = list(im.getdata())
    for x in range (0,im.width*im.height):
        if(isGreen(list[x])):
            gw = getGreenWidth(list,x)
            greenCenter = x + gw//2
            print(gw)
            if(checkColourCode(gw,greenCenter,list)):
                return (greenCenter%im.width)/im.width
                break

def main():
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
        for _ in camera.capture_continuous("/dev/shm/optiposimage.jpg", 'jpeg', use_video_port=True, quality=10):
                # Get the start time, to be able to calculate response time
                start = time.time()
                response = analyseImage()
                end = time.time()
                print('Received [' + response + '] after ' + str(end - start) + ' s')
