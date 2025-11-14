import turtle

bob = turtle.Turtle()
#draw lines
def lines (distance , angle):
      
   for times in range(500):
       bob.width(2)
       bob.forward( distance + times * 2)
       bob.left(angle)
      
      
    


