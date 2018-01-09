class Inventory(object):
    def ___init__(self,items):
        self.items = items

#class Map(object):
#    def __init__(self,):
#        self.

#class Hallway(Map):
#    def __init__(self,description):
#        self.description = description

class Item(object):
    def __init__(self, description):
        self.description = description
        self.name = None

#'Shiny Key' = Item('This key is shinier than the first. You recognise the colour from somewhere. Maybe retracing your steps will help you to find where it fits.')

#Toiletries = Item('You do not actually need these, but they smell nice.')

#Key = Item('A black key. Find something that it can unlock.')

#class Toiletries(object):


a=0

def take(inpsplit):
  """
  Should print out the second item followed by a description of it.
  """
  #t=input('Choose item ')
  print('Took the', inpsplit[1])
 # if inpsplit[1] == (''):

def look(inpsplit):
    """
    Prints the description of the item in inpsplit[1]
    """
    if inpsplit
    print()

def open(inpsplit):
    """
    Opening doors
    """
    if inpsplit[1] == ("front door"):
        if #player has key :
            print ("")
        else:
            print ("")
    elif inpsplit[1] == ("cellar door"):
        if #player has key :
            print ("")
        else:
            print ("")

def commandprompt(a):
  """
  This is how the player interacts with the game.
  """
  inp = input('What will you do?     ')
  inpsplit = inp.split(' ')
  #print(inpsplit[1])
  if inpsplit[0] == ('take'):
      take(inpsplit)
  elif inpsplit[0] == ('open'):
      open(inpsplit)
  elif inpsplit[0] == ('look'):
      look(inpsplit)
  #elif inpsplit[0] == ('drop'):
  else:
      print('')

print('You have found yourself in the hallway of a large building, possibly a mansion, by the general look of the place.')
print('As you try to remember how you ended up here, you hear a creaking behind you.')
print('You turn around to see the FRONT DOOR swing shut, making a loud "clunk".')
print("A  LOOK  around the hallway confirms that it has two ROOMs, one on the  LEFT  and the other on the  RIGHT,  and a set of  STAIRS  at the far end of it.")
commandprompt(a)
