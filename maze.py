#  Larry Xi & Jason Diao (Mar 30 2022)
import turtle

def game():
  # This is the game map, it actually contains a exit and a trap
  map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,0,0,1,1,0,1,1],
    [1,1,1,0,0,0,1,0,1,1,0,1,1],
    [1,1,1,0,1,1,1,0,1,1,0,0,0],
    [1,1,0,0,0,0,0,0,1,1,0,1,1],
    [1,1,0,1,1,1,1,0,0,0,0,1,1],
    [1,1,0,1,1,1,1,1,0,1,0,1,1],
    [1,1,1,1,1,1,1,1,0,1,0,1,1],
    [1,1,1,1,0,0,0,0,0,0,1,1,1],
    [1,1,1,0,0,1,1,1,0,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1]
  ]
 # Basic settings for the gameboard.
  window = turtle.Screen()
  # The window is 650 * 650 so that it can be the integer times of the size of the list, making us easier to display the board.
  window.setup(650,650)
  window.screensize(650, 650)
  # Interaction #1, to customize the title of the window
  name = turtle.textinput("Name", "Enter your name: ")
  window.title("{0}'s maze".format(name))
  
  def draw_map(maplst):
    # Draw the maze with Turtle
    drawer = turtle.Turtle()
    turtle.tracer(0)
    # hide animation
    drawer.pencolor("black")
    drawer.speed(0)
    # The fastest speed reduces the drawing time
    for r,v1 in enumerate(maplst):
      for c,v2 in enumerate(v1):
          # For each element, which represents the block in displacement, using a for loop to go through and each block is 50 * 50
          drawer.penup()
          drawer.goto(-325+c*50,295-r*50)
          drawer.pendown()
          drawer.begin_fill()
          drawer.forward(50)
          drawer.right(90)
          drawer.forward(50)
          drawer.right(90)
          drawer.forward(50)
          drawer.right(90)
          drawer.forward(50)
          drawer.right(90)
          drawer.forward(50)
          if v2 == 1:
            drawer.fillcolor('black')
            # 1 is treated as an impassable wall and filled with black
          else:
            drawer.fillcolor("white")
            # 0 is treated as a passable aisle, represented by a white square
          drawer.end_fill()

  # Determine if the game is won by the player   
  def win(m):
    # We have to do some calculation so that the pixel coordinate of the window can be transfered into the index of the list
    row = int((-player.pos()[1]+300)/50)
    col = int((player.pos()[0]+300)/50)
    # This is the position of the exit
    if row == 2 and col == 0:
      return True
    else:
      return False
  # This function is simply defined for us to call for ending the game
  def quit():
    window.bye()
  # This function works the same as win() function
  def loose(m):
    row = int((-player.pos()[1]+300)/50)
    col = int((player.pos()[0]+300)/50)
    if row == 10 and col == 3:
      return True
    else:
      return False
      
  def win_screen():
    # Displaying a graph for winning
    window.clear()
    winlist =[
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,0,1,0,1,0,1,1,1,0],
    [0,1,1,1,0,1,1,1,0,0,1,1,0],
    [0,1,1,1,0,1,0,1,0,1,1,1,0],
    [0,1,1,1,0,1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1,0,1,1,0,0],
    [0,0,1,0,0,1,0,1,0,1,1,1,0],
    [0,1,1,1,0,1,0,1,0,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1]
  ]
    draw_map(winlist)
    window.onkey(quit,"space")
    
  def loose_screen():
    # Displaying a graph for loosing
    window.clear()
    looselist=[
  [1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1],
  [0,0,0,1,1,1,0,1,0,0,0,0,0],
  [0,1,1,0,1,1,1,1,0,0,0,0,0],
  [0,1,1,1,0,1,0,1,0,1,1,1,1],
  [0,1,1,1,0,1,0,1,0,1,1,1,1],
  [0,1,1,1,0,1,0,1,0,0,0,0,0],
  [0,1,1,1,0,1,0,1,0,1,1,1,1],
  [0,1,1,1,0,1,0,1,0,1,1,1,1],
  [0,1,1,1,0,1,0,1,0,0,0,0,0],
  [0,0,0,0,1,1,0,1,0,0,0,0,0],
  [1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1]
]
    draw_map(looselist)
    
    window.onkey(quit,"space")
    # Interaction 4: After the game, press the space to exit, this is when we use the quit() function

  # a direction_check function is used with the coresponding move_direction function, it tells if the block ahead that direction is a wall of a path
  def up_check(m,r,c):
    print(r,c)
    if m[r-1][c] == 0:
      print("y")
      return True
    else:
      print("n")
      return False

  # Once the direction_check function declare that it can go in that direction, then the turtle will move with that direction.
  def move_up():
    row = int((-player.pos()[1]+300)/50)
    col = int((player.pos()[0]+300)/50)
    if up_check(map,row,col) == True:
      player.clearstamps()
      player.forward(50)
      player.stamp()
  
  # All of the remaining functions work the same as the first one
  def back_check(m,r,c):
    if m[r+1][c] == 0:
      print("t")
      print(c,r)
      print(m[r+1][c])
      return True
    else:
      print("f")
      print(c,r)
      print(m[r+1][c])
      return False

      
  def move_backward():
    row = int((-player.pos()[1]+300)/50)
    col = int((player.pos()[0]+300)/50)
    if back_check(map,row,col) == True:
      player.clearstamps()
      player.back(50)
      player.stamp()
      #backward
  
  def left_check(m,r,c):
    if m[r][c-1] == 0:
      print("t")
      print(c,r)
      print(m[r+1][c])
      return True
    else:
      print("f")
      print(c,r)
      print(m[r+1][c])
      return False

  # The move left function is a little different. It works the same as other direction function, except for it is a key function to keep checking if the game is won or lost by the player because the player need to move left to reach both the exit and the trap.    
  def move_left():
    row = int((-player.pos()[1]+300)/50)
    col = int((player.pos()[0]+300)/50)
    if left_check(map,row,col) == True:
      player.clearstamps()
      player.left(90)
      player.forward(50)
      player.right(90)
      player.stamp()
      if win(map) == True:
        window.title("You WIN!")
        win_screen()
        turtle.color("white")
        turtle.goto(0,-300)
        turtle.write("Champion, please press space to end the game!")
      elif loose(map) == True:
        window.title("It's a trap!")
        loose_screen()
        turtle.color("white")
        turtle.goto(0,-300)
        turtle.write("Press space to end the game you FOOL!")
  
  def right_check(m,r,c):
    if m[r][c+1] == 0:
      return True
    else:
      return False
      
  def move_right():
    row = int((-player.pos()[1]+300)/50)
    col = int((player.pos()[0]+300)/50)
    if right_check(map,row,col) == True:
      player.clearstamps()
      player.right(90)
      player.forward(50)
      player.left(90)
      player.stamp()
  
  draw_map(map)
  # the player is defined here, we use penup method so that it will not show its path.
  player = turtle.Turtle()
  player.penup()
  # Interaction 2, choosing the color for the turtle
  color = turtle.textinput("Color", "The color of your marker: ")
  player.color(color)
  # Interaction 3, choosing the shape for the turtle
  wshape = turtle.textinput('Shape', 'The shape of your marker: ("turtle", "circle", "square", "triangle", "classic"）')
  player.shape(wshape)
  # We do not consider this as a neccessary interaction because it does nothing, but it promps the user that there is one exit and one trap
  turtle.textinput('Disclaimer', 'There is one exit and one trap (enter "OK" to continue)')
  # We want to make sure that the turtle always face up so that the user can use direction key for motions control, we think it is easier to use left and right to move but not to turn. If it faces up all the time it will not increase complexitie.
  player.left(90)
  # This is where the player starts
  player.goto(300,75)
  player.stamp()

  # Interaction 5 - 8 for moving
  window.onkey(move_up, "Up")
  window.onkey(move_backward, "Down")
  window.onkey(move_left, "Left")
  window.onkey(move_right, "Right")
  window.listen()
  window.mainloop()

game()



