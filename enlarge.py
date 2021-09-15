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
        print("╬", end="")
        left(1)
        down(1)
        print("║", end="")
        up(1)
      case '═':
        print("══", end="")
        
      case '║':
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
        print("\\/", end="")
        down(1)
        left(2)
        print("/\\", end="")
        up(1)
        
      case 'O':
        left(1)
        print("┌─┐", end="")
        down(1)
        left(3)
        print("└─┘", end="")
        up(1)
        
  print('\n\n', end="")

    