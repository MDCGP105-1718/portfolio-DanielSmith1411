def take(inpsplit):
  """
  Should print out 't'
  """
  t=input("Choose item ")
  print("Took the", t)

inp = input("Choose command ")
inpsplit = inp.split(' ')
#print(inpsplit[1])
if inpsplit[0] == ("take"):
    take(inpsplit)
