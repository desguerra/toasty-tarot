import random

# Card class
class Card:

  def __init__(self, value, suit, quality, element, zodiac):
    self.value = value
    self.suit = suit
    self.quality = quality
    self.element = element
    self.zodiac = zodiac

  def show(self):
    if self.value == str(self.value):
      showCard = "\t" + self.value + " of " + self.suit + "\n\t\t" + self.quality + self.element + "\n\t\tAstrology: " + self.zodiac + "\n"
    else:
      showCard = "\t" + str(self.value) + ": " + self.suit + "\n\t\t" + self.element + "\n\t\tAstrology: " + self.zodiac + "\n"
    print(showCard)

  def __str__(self):
    ret = "testing card funtionality..."
    return ret

# Deck class
class Deck:

  def __init__(self):
    self.deck = []
    self.buildMinor()
    self.buildMajor()

  # builds Minor Arcana
  def buildMinor(self):
    suits = ["Wands", "Cups", "Swords", "Pentacles"]
    qual = ""
    elem = ""
    zodList = []
    zod = ""
    val = ""
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

        if (j == 1):
          val = "Ace"
        elif (j == 2):
          val = "Two"
        elif (j == 3):
          val = "Three"
        elif (j == 4):
          val = "Four"
        elif (j == 5):
          val = "Five"
        elif (j == 6):
          val = "Six"
        elif (j == 7):
          val = "Seven"
        elif (j == 8):
          val = "Eight"
        elif (j == 9):
          val = "Nine"
        elif (j == 10):
          val = "Ten"
        elif (j == 11):
          val = "Page"
        elif (j == 12):
          val = "Knight"
        elif (j == 13):
          val = "Queen"
        else:
          val = "King"

        card = Card(val, suits[i], qual, elem, zod)
        self.deck.append(card)

  # builds Major Arcana
  def buildMajor(self):
    name = [("Fool", "Uranus"), ("Magician", "Mercury"), ("High Priestess", "Moon"), ("Empress", "Venus"), ("Emperor", "Aries"), ("Hierophant", "Taurus"), ("Lovers", "Gemini"), ("Chariot", "Cancer"), ("Strength", "Leo"), ("Hermit", "Virgo"), ("Wheel of Fortune", "Jupiter"), ("Justice", "Libra"), ("Hanged Man", "Neptune"), ("Death", "Scorpio"), ("Temperance", "Sagittarius"), ("Devil", "Capricorn"), ("Tower", "Mars"), ("Star", "Aquarius"), ("Moon", "Pisces"), ("Sun", "Sun"), ("Judgement", "Pluto"), ("World", "Saturn")]
    qual = ""
    elem = ""
    ast = ""
    for i in range(4):
      for j in range(0,22):

        if (j == (4 or 8 or 10 or 14 or 16 or 19 or 20)):
          elem = "Fire"
        elif (j == (2 or 7 or 12 or 13 or 18)):
          elem = "Water"
        elif (j == (0 or 1 or 6 or 11 or 17)):
          elem = "Air"
        else:
          elem = "Earth"

        ast = name[j][1]

        card = Card(j, name[j][0], qual, elem, ast)
        self.deck.append(card)

  # shuffles order of deck (Fisher Yates shuffle algorithm)
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