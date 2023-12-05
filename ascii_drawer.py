'''
cube array indices
         09 10 11
         12 13 14
         15 16 17
        ----------
36 37 38|00 01 02|18 19 20|45 46 47
39 40 41|03 04 05|21 22 23|48 49 50
42 43 44|06 07 08|24 25 26|51 52 53
        ----------
         27 28 29
         30 31 32
         33 34 35
'''

from colorama import init as colorama_init
from colorama import Back, Fore, Style

colorama_init()

edgeColor = Fore.BLACK
colors = {
  'W': Fore.WHITE,
  'G': Fore.GREEN,
  'R': Fore.RED,
  'B': Fore.BLUE,
  'O': Fore.MAGENTA,
  'Y': Fore.YELLOW,
}

def DrawCube(cube):
  # cube is an array with 6*9 chars representing the colors in each square
  print(f"{Back.BLACK}{Style.BRIGHT}      {edgeColor}+++++++++++++")
  print(f"     {edgeColor}+{colors[cube[9]]}XXX{edgeColor}+{colors[cube[10]]}XXX{edgeColor}+{colors[cube[11]]}XXX{edgeColor}++")
  print(f"    {edgeColor}+++++++++++++{colors[cube[20]]}X{edgeColor}+")
  print(f"   {edgeColor}+{colors[cube[12]]}XXX{edgeColor}+{colors[cube[13]]}XXX{edgeColor}+{colors[cube[14]]}XXX{edgeColor}++{colors[cube[20]]}X{edgeColor}+")
  print(f"  {edgeColor}+++++++++++++{colors[cube[19]]}X{edgeColor}+{colors[cube[20]]}X{edgeColor}+")
  print(f" {edgeColor}+{colors[cube[15]]}XXX{edgeColor}+{colors[cube[16]]}XXX{edgeColor}+{colors[cube[17]]}XXX{edgeColor}++{colors[cube[19]]}X{edgeColor}+++")
  print(f"{edgeColor}+++++++++++++{colors[cube[18]]}X{edgeColor}+{colors[cube[19]]}X{edgeColor}+{colors[cube[23]]}X{edgeColor}+")
  print(f"{edgeColor}+{colors[cube[0]]}XXX{edgeColor}+{colors[cube[1]]}XXX{edgeColor}+{colors[cube[2]]}XXX{edgeColor}+{colors[cube[18]]}X{edgeColor}+++{colors[cube[23]]}X{edgeColor}+")
  print(f"{edgeColor}+{colors[cube[0]]}XXX{edgeColor}+{colors[cube[1]]}XXX{edgeColor}+{colors[cube[2]]}XXX{edgeColor}+{colors[cube[18]]}X{edgeColor}+{colors[cube[22]]}X{edgeColor}+{colors[cube[23]]}X{edgeColor}+")
  print(f"{edgeColor}+{colors[cube[0]]}XXX{edgeColor}+{colors[cube[1]]}XXX{edgeColor}+{colors[cube[2]]}XXX{edgeColor}+++{colors[cube[22]]}X{edgeColor}+++")
  print(f"{edgeColor}+++++++++++++{colors[cube[21]]}X{edgeColor}+{colors[cube[22]]}X{edgeColor}+{colors[cube[26]]}X{edgeColor}+")
  print(f"{edgeColor}+{colors[cube[3]]}XXX{edgeColor}+{colors[cube[4]]}XXX{edgeColor}+{colors[cube[5]]}XXX{edgeColor}+{colors[cube[21]]}X{edgeColor}+++{colors[cube[26]]}X{edgeColor}+")
  print(f"{edgeColor}+{colors[cube[3]]}XXX{edgeColor}+{colors[cube[4]]}XXX{edgeColor}+{colors[cube[5]]}XXX{edgeColor}+{colors[cube[21]]}X{edgeColor}+{colors[cube[25]]}X{edgeColor}+{colors[cube[26]]}X{edgeColor}+")
  print(f"{edgeColor}+{colors[cube[3]]}XXX{edgeColor}+{colors[cube[4]]}XXX{edgeColor}+{colors[cube[5]]}XXX{edgeColor}+++{colors[cube[25]]}X{edgeColor}++")
  print(f"{edgeColor}+++++++++++++{colors[cube[24]]}X{edgeColor}+{colors[cube[25]]}X{edgeColor}+")
  print(f"{edgeColor}+{colors[cube[6]]}XXX{edgeColor}+{colors[cube[7]]}XXX{edgeColor}+{colors[cube[8]]}XXX{edgeColor}+{colors[cube[24]]}X{edgeColor}++")
  print(f"{edgeColor}+{colors[cube[6]]}XXX{edgeColor}+{colors[cube[7]]}XXX{edgeColor}+{colors[cube[8]]}XXX{edgeColor}+{colors[cube[24]]}X{edgeColor}+")
  print(f"{edgeColor}+{colors[cube[6]]}XXX{edgeColor}+{colors[cube[7]]}XXX{edgeColor}+{colors[cube[8]]}XXX{edgeColor}++")
  print(f"{edgeColor}+++++++++++++{Style.RESET_ALL}")