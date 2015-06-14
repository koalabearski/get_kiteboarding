wind = 0
gust = 0
gear_range = range(10,16)
counter = 0

# create a shop where you can get inventory
def go_to_shop():
  '''Offers some choices of equipment to buy.'''
  # each piece of gear has stats that match a wind condition

def go_to_beach():
  '''Compares the actual wind condition to your equipment to see how many hours of surf you catch, if any.'''

  if gust in gear_range:
    print "You got a few hours out on the water today! \n"
  else:
    print "You arrive to a dead calm.  Where'd the wind go? \n"
  
for day in range(5):
  if day % 2 == 0:
    wind, gust = (10,15)
  else:
    wind, gust = (5,8)
  print "Today's wind forecast is %d knots, gusting %d knots" % (wind, gust)

  print "Should we go to the beach?"
  response = raw_input("y/n > ")

  if response == "y":
    go_to_beach()

  else:
    print "I'll take that as a no.  Maybe tomorrow!"

# how to keep a running total of hours surfed?