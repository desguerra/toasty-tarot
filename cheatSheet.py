def printQualities():
  print("================================================")
  print("|> ZODIAC QUALITIES")
  print("================================================\n")
  print("Cardinal: \n\t+ initiator and leader signs\n\t+ represent start of their respective seasons\n\t+ Aries, Cancer, Libra, Capricorn")
  print("Fixed: \n\t+ reliable and stable signs\n\t+ dedicated with strong follow through\n\t+ Leo, Scorpio, Aquarius, Taurus")
  print("Mutable: \n\t+ adaptable and versitile signs\n\t+ represent end of their respective seasons\n\t+ Sagittarius, Pisces, Gemini, Virgo")
  
  print()


def printSuits():
  print("================================================")
  print("|> SUITS")
  print("================================================\n")
  print("Wands: \n\t+ fire\n\t+ action & willpower (focusing time & energy, personal growth\n\t+ active energy like air/swords\n\t+ Aries, Leo, Sagittarius")
  print("Cups: \n\t+ water\n\t+ emotions (internal & external, relationships)\n\t+ passive energy like earth/pentacles\n\t+ Cancer, Scorpio, Pisces")
  print("Swords: \n\t+ air\n\t+ mental (higher thinking, life purpose, spirituality)\n\t+ active energy, like fire/wands\n\t+ Libra, Aquarius, Gemini")
  print("Pentacles: \n\t+ earth\n\t+ physical & earthly matters (money, family, health, stability)\n\t+ passive energy, like water/cups\n\t+ Capricorn, Taurus, Virgo")
  
  print()

def printNums():
  print("================================================")
  print("|> NUMBERS")
  print("================================================\n")
  print("Zero: \n\t+ unlimited potential")
  print("Ace: \n\t+ spark of action, new ideas\n\t+ can also signify impulsiveness")
  print("Two: \n\t+ a choice, cooperation\n\t+ first stable number, can also mean a standstill")
  print("Three: \n\t+ abundance, fun, completion, self-expressive, optimistic")
  print("Four: \n\t+ strong sense of order and logic, discipline and organization")
  print("Five: \n\t+ quick-thinking, curious, exploring, visionary ideas\n\t+ can also mean restlessness")
  print("Six: \n\t+ restoration of peace and harmony, generous")
  print("Seven: \n\t+ impatient seeker of knowledge, scientific & inventive\n\t+ can be aloof with motives, perfectionism")
  print("Eight: \n\t+ strength, power\n\t+ can be a workaholic that suffers from stress")
  print("Nine: \n\t+ friendly, self-knowing, comfort, spiritual strength")
  print("Ten: \n\t+ made from 1 and 0, brings new changes and luck")
  
  print()

def printCourt():
  s = ["wands", "cups", "swords", "pentacles"]
  e = ["earth", "fire", "water", "air"]
  c = ["Page", "Knight", "Queen", "King"]
  print("================================================")
  print("|> COURT CARDS")
  print("================================================\n")
  for i in range(4):
    if c[i] == "Page":
      d1 = ": rebuilding\n\t\t+ "
      d2 = ": new life\n\t\t+ "
      d3 = ": finance\n\t\t+ "
      d4 = ": grounded"
    elif c[i] == "Knight":
      d1 = ": quest for passion\n\t\t+ "
      d2 = ": quest for love\n\t\t+ "
      d3 = ": quest for philosophy\n\t\t+ "
      d4 = ": quest for physical"
    elif c[i] == "Queen":
      d1 = ": nurturing passion\n\t\t+ "
      d2 = ": nurturing love\n\t\t+ "
      d3 = ": nurturing intellect\n\t\t+ "
      d4 = ": nurturing environment"
    else:
      d1 = ": harbinger\n\t\t+ "
      d2 = ": poet\n\t\t+ "
      d3 = ": philosopher\n\t\t+ "
      d4 = ": planner"
    
    print(c[i] + ": \n\t+ " + e[i] + "\n\t\t+ " + s[0] + d1 + s[1] + d2 + s[2] + d3 + s[3] + d4)

  print()

  print("\nCourt cards can represent:")
  print("\n\t+ the sitter\n\t+ the person who the reading is about\n\t+ outside person\n\t+ positive aspect in situation\n\t+ negative aspect in situation\n\t+ specific situation\n\t+ course of action\n\t+ estimated time something will happen\n\t+ maturity\n\t+ person who hold the key to outcome")
  
  print()

def masterCheatSheet():
  print()

  printQualities()

  printSuits()

  printNums()

  printCourt()