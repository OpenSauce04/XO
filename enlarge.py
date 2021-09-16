from colors import colors

def up(n):
  print("\033["+str(n)+"A", end="")
def down(n):
  print("\033["+str(n)+"B", end="")
def right(n):
  print("\033["+str(n)+"C", end="")
def left(n):
  print("\033["+str(n)+"D", end="")

def printLarge(input):
  for x in input:
    match(x):
      case '╬':
        print(colors.WHITE, end="")
        print("╬", end="")
        left(1)
        down(1)
        print("║", end="")
        up(1)
      case '═':
        print(colors.WHITE, end="")
        print("══", end="")
        
      case '║':
        print(colors.WHITE, end="")
        print("║", end="")
        down(1)
        left(1)
        print("║", end="")
        up(1)
        
      case ' ':
        print("  ", end="")
        down(1)
        left(2)
        print("  ", end="")
        up(1)
        
      case 'X':
        print(colors.GREEN, end="")
        print("\\/", end="")
        down(1)
        left(2)
        print("/\\", end="")
        up(1)
        
      case 'O':
        print(colors.RED, end="")
        left(1)
        print("┌─┐", end="")
        down(1)
        left(3)
        print("└─┘", end="")
        up(1)
        
  print('\n\n', end="")
  print(colors.WHITE, end="")

    