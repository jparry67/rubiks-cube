from ascii_drawer import DrawCube
from turn_cube import RotateSide,availableCommands
import random
from time import sleep

solvedCube = ['W','W','W','W','W','W','W','W','W','G','G','G','G','G','G','G','G','G','R','R','R','R','R','R','R','R','R','B','B','B','B','B','B','B','B','B','O','O','O','O','O','O','O','O','O','Y','Y','Y','Y','Y','Y','Y','Y','Y']
currentCube = solvedCube.copy()

while True:
  DrawCube(currentCube)
  command = input()
  if command in availableCommands:
    RotateSide(currentCube, command)
  elif command == 'scramble':
    scrambleCommands = []
    for _ in range(30):
      rc = random.choice(list(availableCommands.keys()))
      scrambleCommands.append(rc)
      RotateSide(currentCube, rc)
      DrawCube(currentCube)
      sleep(0.3)
    print(scrambleCommands)
  elif command == 'reset':
    currentCube = solvedCube.copy()