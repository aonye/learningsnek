import copy
import random
# Consider using the modules imported above.

class Hat(object):
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)
    self.contents = []
    for key, value in kwargs.items():
      for x in range(value):
        self.contents.append(key)
    self.contents_copy = copy.copy(self.contents)
    #print(self.contents)
    #print(len(self.contents))

  def draw(self, numofdraws):
    balldrawn = []
    if (numofdraws>len(self.contents)):
      return self.contents
    while(numofdraws>0):
      balltodraw = random.randint(0,len(self.contents)-1)
      balldrawn.append(self.contents.pop(balltodraw))
      numofdraws-=1
    return balldrawn

  def replenishstock(self):
    self.contents = copy.copy(self.contents_copy)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  #def __init__(self, hat, expected_balls, num_balls_drawn, num_experiments):
  hat_copy = copy.copy(hat)
  #print(expected_balls)
  #print(expected_balls.items()
  M = 0
  N = num_experiments
  probability = 0
  contents = []

  for key in expected_balls: # dict of key, val into list of balls
    for x in range(expected_balls[key]):
      contents.append(key)

  while(num_experiments>0):
    balls_drawn = hat_copy.draw(num_balls_drawn)
    hat_copy.replenishstock()

    #balls_drawn = ['blue','blue','blue','red'] #test line to check loop
    len_balls_drawn = len(balls_drawn)

    for x in contents:
      if (x in balls_drawn):
        balls_drawn.remove(x)

    if (len_balls_drawn - len(contents) == len(balls_drawn)):
      #indicates that the number of balls removed is equal to expected_balls by comparing lengths before and after removing
      M+=1

    num_experiments-=1

  probability = M/N
  return probability
