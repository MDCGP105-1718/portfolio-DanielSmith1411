looking='false'

class Hallway(object):
    def __init__(self,locations):
        self.locations=(Kitchen, DrawingRoom, Stairs)
        self.locations=locations
        self.looking=looking
    def get_description(self):
            print ('A LOOK around the hallway confirms that it has two ROOMS, one on the LEFT and the other on the RIGHT, and a set of STAIRS at the far end of it.')
            looking='false'
            inp='ready'

    if looking=='true':
        get_description
    def kitchen(self):
        return Kitchen()

    #class Stairs(Hallway):
    #    def __init__(sself):


#    class Player(Hallway):
#        def __init__(self,items):
#            self.items = items

class DrawingRoom(object):
    def __init__(self,description):
        self.description = description

class Book(DrawingRoom):
    def __init__(self,description):
        self.description = description

class Kitchen(object):
    def __init__(self,description):
        self.description = description

class Cellar(object):
    def __init__(self,description):
        self.description = description

class Key(Cellar):
    def __init__(self, description):
        self.description = description
        self.name = None

description = Key('This key is particularly shiny. You recognise the colour from somewhere. Maybe retracing your steps will help you to find where it fits.')


#Toiletries = Item('You do not actually need these, but they smell nice.')

#Key = Item('A black key. Find something that it can unlock.')

#class Toiletries(object):

def take(inpsplit):
  """
  Should print out the second item followed by a description of it.
  """
  #t=input('Choose item ')
  if len(inpsplit)==2 or (len(inpsplit)==3 and inpsplit[1]=='the'):
      print('Took the', inpsplit[-1])
      inp = 'ready'
 # elif len(inpsplit)==3 and inpsplit[1]=='the':
  else:
      print('Try again')
      inp = 'ready'
 # if inpsplit[1] == (''):

def look(inpsplit):
    """
    Prints the description of the thing in inpsplit[1]
    """
    if len(inpsplit)==1:
        looking='true'
    else:
        print ("error")
        inp='ready'

def go(inpsplit):
    """
    Should allow movement
    """
    if inpsplit[-1] in locations:
        print('success')
    else:
        inp='ready'
#def open(inpsplit):
#    """
#    Opening doors
#    """
#    if inpsplit[1] == ("front door"):
#        if #player has key :
#            print ("")
#        else:
#            print ("")
#    elif inpsplit[1] == ("cellar door"):
#        if #player has key :
#            print ("")
#        else:
#            print ("")

def commandprompt(inp):
  """
  This is how the player interacts with the game.
  """
  inp = 'ready'
  while inp == 'ready':
      inp = input('What will you do?     ')
      inpsplit = inp.split(' ')
      #print(inpsplit[1])
      if inpsplit[0] == ('take'):
          take(inpsplit)
          inp = 'ready'
      elif inpsplit[0] == ('go'):
          go(inpsplit)
          inp = 'ready'
      elif inpsplit[0] == ('look'):
          look(inpsplit)
          inp = 'ready'
      elif inpsplit[0] == ('end'):
          print('Ended.')
      else:
          print('Wrong input')
          inp = 'ready'


print('You have found yourself in the hallway of a large building, possibly a mansion, by the general look of the place.')
print('As you try to remember how you ended up here, you hear a creaking behind you.')
print('You turn around to see the FRONT DOOR swing shut, making a loud "clunk".')
print("A  LOOK  around the hallway confirms that it has two ROOMs, one on the  LEFT  and the other on the  RIGHT,  and a set of  STAIRS  at the far end of it.")
#looking='false'
inp='ready'
location=Hallway
commandprompt(inp)
