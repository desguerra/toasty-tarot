def pooploop(f):
  for i in f:
    if i[0] == "+":
      print("\t" + i)
    else:
      print(i)

  f.close()

def printQualities():
  print("================================================")
  print("|> ZODIAC QUALITIES")
  print("================================================\n")
  pq = open("qualities.txt", "r")
  pooploop(pq)

  print()


def printSuits():
  print("================================================")
  print("|> SUITS")
  print("================================================\n")
  ps = open("suits.txt", "r")
  pooploop(ps)
  
  print()

def printNums():
  print("================================================")
  print("|> NUMBERS")
  print("================================================\n")
  pn = open("numbers.txt", "r")
  pooploop(pn)
  
  print()

def printCourt():
  print("================================================")
  print("|> COURT CARDS")
  print("================================================\n")
  pc = open("court.txt", "r")
  pooploop(pc)

  print()
  pc2 = open("court2.txt", "r")
  pooploop(pc2)
  
  print()

def masterCheatSheet():
  print()

  printQualities()

  printSuits()

  printNums()

  printCourt()