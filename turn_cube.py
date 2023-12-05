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

availableCommands = {
  'R': '',
  '-R': '',
  'L': '',
  '-L': '',
  'F': '',
  '-F': '',
  'B': '',
  '-B': '',
  'U': '',
  '-U': '',
  'D': '',
  '-D': '',
  'M': '',
  '-M': '',
  'E': '',
  '-E': '',
  'S': '',
  '-S': '',
  'x': '',
  '-x': '',
  'y': '',
  '-y': '',
  'z': '',
  '-z': '',
}

def SwapSquares(cube, i1, i2, i3, i4):
  tmp = cube[i1]
  cube[i1] = cube[i2]
  cube[i2] = cube[i3]
  cube[i3] = cube[i4]
  cube[i4] = tmp


def RotateSide(cube, side):
  match side:
    case 'R':
      # corner front
      SwapSquares(cube, 2, 29, 51, 11)
      # corner top
      SwapSquares(cube, 17, 8, 35, 45)
      # corner side
      SwapSquares(cube, 18, 24, 26, 20)
      # edge front
      SwapSquares(cube, 5, 32, 48, 14)
      # edge side
      SwapSquares(cube, 21, 25, 23, 19)
    case '-R':
      # corner front
      SwapSquares(cube, 11, 51, 29, 2)
      # corner top
      SwapSquares(cube, 45, 35, 8, 17)
      # corner side
      SwapSquares(cube, 20, 26, 24, 18)
      # edge front
      SwapSquares(cube, 14, 48, 32, 5)
      # edge side
      SwapSquares(cube, 19, 23, 25, 21)
    case 'L':
      # corner front
      SwapSquares(cube, 9, 53, 27, 0)
      # corner top
      SwapSquares(cube, 47, 33, 6, 15)
      # corner side
      SwapSquares(cube, 36, 42, 44, 38)
      # edge front
      SwapSquares(cube, 12, 50, 30, 3)
      # edge side
      SwapSquares(cube, 37, 39, 43, 41)
    case '-L':
      # corner front
      SwapSquares(cube, 0, 27, 53, 9)
      # corner top
      SwapSquares(cube, 15, 6, 33, 47)
      # corner side
      SwapSquares(cube, 38, 44, 42, 36)
      # edge front
      SwapSquares(cube, 3, 30, 50, 12)
      # edge side
      SwapSquares(cube, 41, 43, 39, 37)
    case 'F':
      # corner front
      SwapSquares(cube, 6, 8, 2, 0)
      # corner top
      SwapSquares(cube, 38, 27, 24, 17)
      # corner side
      SwapSquares(cube, 15, 44, 29, 18)
      # edge front
      SwapSquares(cube, 3, 7, 5, 1)
      # edge side
      SwapSquares(cube, 41, 28, 21, 16)
    case '-F':
      # corner front
      SwapSquares(cube, 0, 2, 8, 6)
      # corner top
      SwapSquares(cube, 17, 24, 27, 38)
      # corner side
      SwapSquares(cube, 18, 29, 44, 15)
      # edge front
      SwapSquares(cube, 1, 5, 7, 3)
      # edge side
      SwapSquares(cube, 16, 21, 28, 41)
    case 'B':
      # corner front
      SwapSquares(cube, 45, 51, 53, 47)
      # corner top
      SwapSquares(cube, 20, 35, 42, 9)
      # corner side
      SwapSquares(cube, 11, 26, 33, 36)
      # edge front
      SwapSquares(cube, 48, 52, 50, 46)
      # edge side
      SwapSquares(cube, 23, 34, 39, 10)
    case '-B':
      # corner front
      SwapSquares(cube, 47, 53, 51, 45)
      # corner top
      SwapSquares(cube, 9, 42, 35, 20)
      # corner side
      SwapSquares(cube, 36, 33, 26, 11)
      # edge front
      SwapSquares(cube, 46, 50, 52, 48)
      # edge side
      SwapSquares(cube, 10, 39, 34, 23)
    case 'U':
      # corner front
      SwapSquares(cube, 11, 9, 15, 17)
      # corner top
      SwapSquares(cube, 45, 36, 0, 18)
      # corner side
      SwapSquares(cube, 20, 47, 38, 2)
      # edge front
      SwapSquares(cube, 10, 12, 16, 14)
      # edge side
      SwapSquares(cube, 46, 37, 1, 19)
    case '-U':
      # corner front
      SwapSquares(cube, 17, 15, 9, 11)
      # corner top
      SwapSquares(cube, 18, 0, 36, 45)
      # corner side
      SwapSquares(cube, 2, 38, 47, 20)
      # edge front
      SwapSquares(cube, 14, 16, 12, 10)
      # edge side
      SwapSquares(cube, 19, 1, 37, 46)
    case 'D':
      # corner front
      SwapSquares(cube, 29, 27, 33, 35)
      # corner top
      SwapSquares(cube, 8, 44, 53, 26)
      # corner side
      SwapSquares(cube, 24, 6, 42, 51)
      # edge front
      SwapSquares(cube, 28, 30, 34, 32)
      # edge side
      SwapSquares(cube, 7, 43, 52, 25)
    case '-D':
      # corner front
      SwapSquares(cube, 35, 33, 27, 29)
      # corner top
      SwapSquares(cube, 26, 53, 44, 8)
      # corner side
      SwapSquares(cube, 51, 42, 6, 24)
      # edge front
      SwapSquares(cube, 32, 34, 30, 28)
      # edge side
      SwapSquares(cube, 25, 52, 43, 7)
    case 'M':
      # edge front
      SwapSquares(cube, 1, 10, 52, 28)
      # edge top
      SwapSquares(cube, 16, 46, 34, 7)
      # center
      SwapSquares(cube, 4, 13, 49, 31)
    case '-M':
      # edge front
      SwapSquares(cube, 28, 52, 10, 1)
      # edge top
      SwapSquares(cube, 7, 34, 46, 16)
      # center
      SwapSquares(cube, 31, 49, 13, 4)
    case 'E':
      # edge front
      SwapSquares(cube, 5, 41, 50, 23)
      # edge side
      SwapSquares(cube, 21, 3, 39, 48)
      # center
      SwapSquares(cube, 4, 40, 49, 22)
    case '-E':
      # edge front
      SwapSquares(cube, 23, 50, 41, 5)
      # edge side
      SwapSquares(cube, 48, 39, 3, 21)
      # center
      SwapSquares(cube, 22, 49, 40, 4)
    case 'S':
      # edge front
      SwapSquares(cube, 14, 37, 30, 25)
      # edge side
      SwapSquares(cube, 19, 12, 43, 32)
      # center
      SwapSquares(cube, 13, 40, 31, 22)
    case '-S':
      # edge front
      SwapSquares(cube, 25, 30, 37, 14)
      # edge side
      SwapSquares(cube, 32, 43, 12, 19)
      # center
      SwapSquares(cube, 22, 31, 40, 13)
    case 'x':
      RotateSide(cube, 'R')
      RotateSide(cube, '-M')
      RotateSide(cube, '-L')
    case '-x':
      RotateSide(cube, '-R')
      RotateSide(cube, 'M')
      RotateSide(cube, 'L')
    case 'y':
      RotateSide(cube, 'U')
      RotateSide(cube, '-E')
      RotateSide(cube, '-D')
    case '-y':
      RotateSide(cube, '-U')
      RotateSide(cube, 'E')
      RotateSide(cube, 'D')
    case 'z':
      RotateSide(cube, 'F')
      RotateSide(cube, 'S')
      RotateSide(cube, '-B')
    case '-z':
      RotateSide(cube, '-F')
      RotateSide(cube, '-S')
      RotateSide(cube, 'B')