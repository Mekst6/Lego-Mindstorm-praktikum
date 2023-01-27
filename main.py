#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import os
import json
import time


ev3 = EV3Brick()
d = True
hostname = "google.de"
response = os.system("ping -c 1" + hostname)

if response == 0:
  print(hostname + ": is up")
else:
  print(hostname + ": is down")



def executeCommand(command):
  if command is "/hello":
    sendMessage("Hallo vom EV3")
    ev3.speaker.beep()
  if command is "/musik_1":
    ev3.speaker.play_notes(["G4/4", "G4/4", "G4/8", "A4/8", "G4/8", "F4/8"], tempo=120)
    ev3.speaker.play_notes(["E4/4", "E4/4", "E4/4"], tempo=120)
    ev3.speaker.play_notes(["F4/4", "F4/4", "F4/8", "G4/8", "F4/8", "E4/8"], tempo=120)
    ev3.speaker.play_notes(["D4/4", "D4/4", "D4/4"], tempo=120)
    ev3.speaker.play_notes(["C4/4", "D4/4", "E4/4", "F4/4"], tempo=120)
    ev3.speaker.play_notes(["G4/8", "A4/8", "G4/8", "A4/8", "F4/4"], tempo=120)
    ev3.speaker.play_notes(["B4/4", "G4/4", "G4/8", "A4/8", "G4/8", "F4/8"], tempo=120)
    ev3.speaker.play_notes(["B4/4", "G4/4", "G4/8", "A4/8", "G4/8", "F4/8"], tempo=120)
    ev3.speaker.play_notes(["B4/4", "G4/4", "G4/8", "A4/8", "G4/8", "F4/8"], tempo=120)
    ev3.speaker.play_notes(["E4/4", "D4/4", "G4/4"], tempo=120)
    ev3.speaker.play_notes(["B4/4", "G4/4", "G4/8", "A4/8", "G4/8", "F4/8"], tempo=120)
    ev3.speaker.play_notes(["E4/4", "D4/4", "C4/4"], tempo=120)
  if command is "/doom":
    ev3.speaker.play_file("doom.wav")
  if command is "/dest":
    ev3.speaker.play_file("dest2.wav")

""" def sendMessage(msg):
  print("Text: "+ sendUrl + msg)
  response = os.popen('curl ' + sendUrl + msg).read()
  #os.system('curl ' + sendUrl + msg)
  print("gesendet: " + response) """

def sendMessage(msg):
  os.system("""curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"chat_id": "-808126898", "text": " """ + msg + """ ", "disable_notification": true}' \
     https://api.telegram.org/bot5972370199:AAHCkiDxIEVCnS_gbFQPPc3UHCz9haIzBiw/sendMessage""")

# Write your program here.
#ev3.speaker.beep()
c = True
url = "https://api.telegram.org/bot5972370199:AAHCkiDxIEVCnS_gbFQPPc3UHCz9haIzBiw/getupdates" 
sendUrl = "https://api.telegram.org/bot5972370199:AAHCkiDxIEVCnS_gbFQPPc3UHCz9haIzBiw/sendMessage?chat_id=-808126898&text=" 
#response = os.system("curl " + url)
LastCommandId = None
while d == True:
  response = os.popen('curl ' + url).read()
  mydict = json.loads(response)
  NewCommandId = mydict["result"][-1]["message"]["message_id"]
  if NewCommandId is not LastCommandId:
    LastCommandId = NewCommandId
    command = mydict["result"][-1]["message"]["text"]
    executeCommand(command)
  time.sleep(5)

mydict = json.loads(response)
count = len(mydict["result"])
print(count)
while count >= 1 and c == True:
  count = count - 1
  print(count)
  command = mydict["result"][count]["message"]["text"]
  print(command)
  if command == "/hello" or "/musik_1" or "/doom":
    c = False
listenForCommand()




# Create your objects here.