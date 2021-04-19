from cheatsheet import masterCheatSheet, printQualities, printElem, printNums, printCourt
from classes import Card, Deck

q = ""
print("Hello! Welcome to Toasty Tarot. What would you like to do?\n")
while True:
  deck = Deck()
  print("\t1. One card reading\n\t2. Three card reading\n\t3. Master cheat sheet\n\t4. What is tarot?\n\t5. [Exit]\n")
  action = input("Please type in a number: ")
  print("\n.==========.==========.==========.==========.")

  if action == "1":
    q = input("\nWhat would you like guidance on? (i.e. 'Where should I direct my energy today?'): ")
    deck.shuffle()
    print("\n================================================")
    print("|> " + q)
    print("================================================\n")
    c = deck.draw()
    c.show()

  elif action == "2":
    q = input("\nWhat would you like guidance on? (i.e. 'Where should I direct my energy today?'): ")
    deck.shuffle()
    print("\n================================================")
    print("|> " + q)
    print("================================================\n")
    c1 = deck.draw()
    c1.show()
    c2 = deck.draw()
    c2.show()
    c3 = deck.draw()
    c3.show()

  elif action == "3":
    while True:
      print("\nWhich cheat sheet category would you like to view?\n")
      print("\t1. Zodiac Qualities\n\t2. Elements + Suits\n\t3. Numbers\n\t4. Court Cards\n\t5. Major Arcana\n\t6. All of them!\n\t7. [Back]\n")
      cheatCat = input("Please type in a number: ")
      print("\n.==========.==========.==========.==========.")
      print()

      if cheatCat == "1":
        printQualities()
      elif cheatCat == "2":
        printElem()
      elif cheatCat == "3":
        printNums()
      elif cheatCat == "4":
        printCourt()
      elif cheatCat == "5":
        ######################################
        # TODO: add Major Arcana cheat sheet #
        ######################################
        print("'Major Arcana' is under construction!")
      elif cheatCat == "6":
        masterCheatSheet()
      elif cheatCat == "7":
        break
      else:
        print("\nInvalid input. Please type in a number (1-5).")

      print("\n.==========.==========.==========.==========.")

  elif action == "4":
    ############################
    # TODO: add What is tarot? #
    ############################
    print("\n'What is tarot?' is under construction!")

  elif action == "5":
    print("\nSee you next time!")
    break

  else:
    print("\nInvalid input. Please type in a number (1-5).")

  print("\n.==========.==========.==========.==========.")
  print("\nWhat would you like to do?\n")