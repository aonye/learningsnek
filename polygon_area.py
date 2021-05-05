class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

  def set_width(self, width):
    self.width = width
  def set_height(self, height):
    self.height = height
  def get_area(self):
    return self.width * self.height
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."
    picture = ""
    for x in range(self.height):
      for y in range(self.width):
        picture+="*"
        if(y==self.width-1):
          picture+="\n"

    return picture

  def get_amount_inside(self, shape):
    # figure out which side is longer for the base shape
    wider = ""
    higher = ""
    num_loops = 1
    width_left = self.width
    height_left = self.height
    larger_side = max(self.width, self.height)

    if(larger_side==self.width):
        wider = True
    else:
        higher = True

    #check if the shorter side is 2x larger or more than shortest side of the object
    if(wider==True): # the short side is height
      num_loops = self.height // shape.height
    elif(higher==True): #the short side is width
      num_loops = self.width // shape.width

    count= 0
    while(num_loops>0 and shape.width >=0 and shape.height >=0): #cannot pass in negative or zero height/weight, will cause infinite loop
        if (wider):
            width_left-=shape.width
            if (width_left<0):
              if(num_loops==1):
                break
              else:
                num_loops-=1
                width_left=self.width # reset variable
                continue # restart loop
            count+=1
        if (higher):
            height_left-=shape.height
            if (height_left<0):
              if(num_loops==1):
                break
              else:
                num_loops-=1
                height_left=self.height
                continue
            count+=1

    return count


class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"
    
