from cheatSheet import masterCheatSheet, printQualities, printSuits, printNums, printCourt

import random

################################
# TODO: add Major Arcana cards #
################################

# Card class
class Card:

  def __init__(self, value, suit, quality, element, zodiac):
    self.value = value
    self.suit = suit
    self.quality = quality
    self.element = element
    self.zodiac = zodiac

  def __str__(self):
    # change 1 into 'ace', 11 into 'page', 12 into 'knight', etc.
    if (self.value == 1):
      self.value = "Ace"
    elif (self.value == 11):
      self.value = "Page"
    elif (self.value == 12):
      self.value = "Knight"
    elif (self.value == 13):
      self.value = "Queen"
    elif (self.value == 14):
      self.value = "King"
    else:
      pass

    ##################################################
    # TODO: add keywords accoring to element/value?? #
    ##################################################

    # print out card
    ret = "\t" + str(self.value) + " of " + self.suit + "\n\t\t" + self.quality + self.element + "\n\t\tZodiac(s): " + self.zodiac + "\n"
    return ret

# Deck class
class Deck:

  def __init__(self):
    self.deck = []
    suits = ["Wands", "Cups", "Swords", "Pentacles"]
    qual = ""
    elem = ""
    zodList = []
    zod = ""
    for i in range(4):
      if (suits[i] == "Wands"):
        elem = "Fire"
      elif (suits[i] == "Cups"):
        elem = "Water"
      elif (suits[i] == "Swords"):
        elem = "Air"
      else:
        elem = "Earth"

      for j in range(1,15):
        if (j == 1):
          qual = "Entire element of "
          zodList = ["Aries, Leo, & Sagittarius", "Cancer, Scorpio, & Pisces", "Libra, Aquarius, & Gemini", "Capricorn, Taurus, & Virgo"]
        elif (j < 5):
          qual = "Cardinal "
          zodList = ["Aries", "Cancer", "Libra", "Capricorn"]
        elif (j < 8):
          qual = "Fixed "
          zodList = ["Leo", "Scorpio", "Aquarius", "Taurus"]
        elif (j < 11):
          qual = "Mutable "
          zodList = ["Sagittarius", "Pisces", "Gemini", "Virgo"]
        else:
          qual = ""
          zodList = ["Aries, Leo, & Sagittarius", "Cancer, Scorpio, & Pisces", "Libra, Aquarius, & Gemini", "Capricorn, Taurus, & Virgo"]

        if (suits[i] == "Wands"):
          zod = zodList[i]
        elif (suits[i] == "Cups"):
          zod = zodList[i]
        elif (suits[i] == "Swords"):
          zod = zodList[i]
        else:
          zod = zodList[i]

        card = Card(j, suits[i], qual, elem, zod)
        self.deck.append(card)

  # shuffles order of deck
  def shuffle(self):
    for i in range(len(self.deck)):
      r = random.randint(0, len(self.deck)-1)
      temp = self.deck[i]
      self.deck[i] = self.deck[r]
      self.deck[r] = temp

  # draws card from top of deck
  def draw(self):
    if (len(self.deck) > 0):
      return self.deck.pop(0) # returns element at top and removes it from deck
    else:
      print("No cards left in the deck.")

  def __str__(self):
    ret = "testing deck functionality..."
    return ret

### test Card class ###
# card1 = Card(3, "Wands", "Mutable", "Fire")
# print(card1)

### test Deck class ###
# deck = Deck()
# deck.shuffle()
# print(deck.draw())

q = ""
print("Hello! Welcome to Toasty Tarot. What would you like to do?\n")
while True:
  deck = Deck()
  print("\t1. One card reading\n\t2. Three card reading\n\t3. Master cheat sheet\n\t4. [Exit]\n")
  action = input("Please type in a number: ")
  print("\n.==========.==========.==========.==========.")

  if action == "1":
    q = input("\nWhat would you like guidance on? (i.e. 'Where should I direct my energy today?'): ")
    deck.shuffle()
    print("\n================================================")
    print("|> " + q)
    print("================================================\n")
    print(deck.draw())

  elif action == "2":
    q = input("\nWhat would you like guidance on? (i.e. 'Where should I direct my energy today?'): ")
    deck.shuffle()
    print("\n================================================")
    print("|> " + q)
    print("================================================\n")
    print(deck.draw())
    print(deck.draw())
    print(deck.draw())

  elif action == "3":
    while True:
      print("\nWhich cheat sheet category would you like to view?\n")
      print("\t1. Zodiac Qualities\n\t2. Suits\n\t3. Numbers\n\t4. Court Cards\n\t5. All of them!\n\t6. [Back]\n")
      cheatCat = input("Please type in a number: ")
      print("\n.==========.==========.==========.==========.")
      print()

      if cheatCat == "1":
        printQualities()
      elif cheatCat == "2":
        printSuits()
      elif cheatCat == "3":
        printNums()
      elif cheatCat == "4":
        printCourt()
      elif cheatCat == "5":
        masterCheatSheet()
      elif cheatCat == "6":
        break
      else:
        print("\nInvalid input. Please type in a number (1-5).")

      print("\n.==========.==========.==========.==========.")

  elif action == "4":
    print("\nSee you next time!")
    break

  else:
    print("\nInvalid input. Please type in a number (1-5).")

  print("\n.==========.==========.==========.==========.")
  print("\nWhat would you like to do?\n")