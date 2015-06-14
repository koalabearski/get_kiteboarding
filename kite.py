wind = 0
gust = 0

def forecast(day):
  '''Looks up the wind forecast for today and tomorrow.'''
  if day % 2 = 0:
    wind, gust = (10,15)
  else:
    wind, gust = (5,8)

  print "Today's wind forecast is %d knots, gusting %d knots" % (wind, gust)

# create a shop where you can get inventory
def go_to_shop():
  '''Offers some choices of equipment to buy.'''
  # each piece of gear has stats that match a wind condition

def go_to_beach():
  '''Compares the actual wind condition to your equipment to see how many hours of surf you catch, if any.'''
    # need to clarify the gust decision model, for now use gust only

  if day == 1:
    


# the daily agenda
for day in range(5):
  # each day has wind data
  forecast(day)

  # prompts to go kiteboarding
  print "Should we go to the beach?"
  response = raw_input("y/n > ")

  if response == "y":
    go_to_beach()

  else:
    print "I'll take that as a no.  Maybe tomorrow!"



