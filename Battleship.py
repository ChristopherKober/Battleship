import random
from graphics import *
from time import sleep

#
# Helen Meng and Kent Kober
#
# Battleship.py
#


# this function is the main function in the module, it runs a game of battleship
#
# inputs: none
#
# Outputs: none
#
def main():
    #running the intro
    intro()

    #running the intermediate gif
    gif()

    #opening this user window
    UserWin = GraphWin('User Window', 499,699)

    #having the user place their ships
    userPlacement = userBoard(UserWin)

    #openning the computer screen
    ComputerWin = GraphWin('Computer Window', 499,699)

    #drawing the board on the computer window
    compBoard(ComputerWin)

    #having the computer place its ships
    compPlacement = placement()

    #initializing queue and guessboard variables
    queue = []
    guessBoard = ['O']
    for i in range(99):
        guessBoard = guessBoard + ['O']

    #while loop to cycle through turns
    while True:

        #getting the user to click a sqaure and changing the computer variable
        #accordingly
        compPlacement = userClick(ComputerWin,compPlacement)

        #getting the computer to click a square and changing the variables
        #accordingly
        guessBoard,queue = enhancedCompClick(UserWin,userPlacement,guessBoard,queue)

        #checking to see how many hits the computer has
        nofCHits = 0
        for i in guessBoard:
            if i == 'X': nofCHits = nofCHits + 1

        #checking to see how many hits the user has
        nofHHits = 0
        for i in compPlacement:
            if i == 'H': nofHHits = nofHHits + 1

        #if either the user or the computer has 17 hits, it breaks the loop
        if nofCHits == 17 or nofHHits == 17: break

    #checking to see who won and openning the correct gif
    if nofHHits == 17: winGif()
    else: loseGif()
        

#
# intro()
# writes instructions for game on graphwin
# inputs: none
# outputs: graphwin with instructions
        

def intro():
    # make graphwin 500x600
    win = GraphWin("Introduction", 500, 600)
    # make background black
    win.setBackground('black')
    # display greetings
    g1 = Text(Point(250, 100), "Greetings.")
    # make font courier 
    g1.setFace('courier')
    # set size of font to 18
    g1.setSize(18)
    # set text to green 
    g1.setFill('green')
    # draw text to graphwin
    g1.draw(win)
    # clone first greeting
    g2 = g1.clone()
    # set size of font to 13    
    g2.setSize(13)
    # move down from greetings 1
    g2.move(0, 50)
    # set text to the game is simple
    g2.setText("The game is simple: ")
    # draw to graphwin
    g2.draw(win)
    # make a list of strings of text that you want to print in
    # instrucitons paragraph
    text = ['You have two screens, one window','where you will place your ships,','and another where you will attack the enemy.',
            'You will attack the enemy by clicking', 'a section of the ocean to torpedo.','You will either hit or miss one',' of the enemy boats. Instructions will be',
            'displayed at every step.']
    # establish counter
    n = 0 
    # establish for loop to run through text
    for i in text:
        # make new greetings variable clone
        g3 = g2.clone()
        # set text to index of text list
        g3.setText(text[n])
        # move new text down by 30
        g3.move(0,(n+1)*30)
        # draw text to graphwin
        g3.draw(win)
        # increase n counter
        n = n + 1
    # make new greeting clone
    g4 = g3.clone()
    # tab back and down 
    g4.move(-70, 50)
    # set to message    
    g4.setText("Fear not brave soldier,")
    # draw in win
    g4.draw(win)
    # make g5 clone 
    g5 = g4.clone()
    # move right and down
    g5.move(40, 30)
    # set to message
    g5.setText("the battle has yet to come.")
    # draw in win
    g5.draw(win)    
    # make arrow object     
    arrow = Line(Point(360, 560), Point(460, 560))
    # set width to 3
    arrow.setWidth(3)
    # set arrow head to last pt
    arrow.setArrow('last')
    # make arrow green  
    arrow.setOutline('green')
    # draw to win
    arrow.draw(win)
    # wait until user clickse to close instructions
    win.getMouse()
    win.close()



# This function randomly places the ships on a board then outputs the list that
# represents the placed board
#
# Inputs: none
#
# Outputs: board - The list that represents the computer's placement
#
def placement():
    #initializing the board list
    board = ['O']
    for i in range(99):
        board = board + ['O']

    #initializing a reference table
    ships = [5,4,3,3,2]

    #for loop to cycle through placing each ship
    for i in ships:

        #while looop to wait until placement is correct
        while True:

            #picking a random x and y starting position
            xstart = random.randint(0,9)
            ystart = random.randint(0,9)

            #randomly choosing if the ship is horiontal or vertical
            if random.randint(0,1) == 0:

                #setting the ship to be horizontal
                yend = ystart
                #randomly choosing if the ship moves to the left or the right
                if random.randint(0,1)==0:
                    xend = xstart + i
                else:
                    xend = xstart - i
                    
            else:
                #setting the ship to be vertical
                xend = xstart

                #randomly choosing if the ship moves up or down
                if random.randint(0,1) == 0:
                    yend = ystart + i
                else:
                    yend = ystart - i

            #checking to see if the x and y values are valid
            if -1<xend<10 and -1<yend<10:
                #initializing checking variable
                x = True
                #making sure the ship is horizontal
                if ystart == yend:
                    #for loop to check to see if the spaces are taken
                    for j in range(i):
    
                        n = ystart * 10 + min(xstart,xend) + j
                        #changing the checking variable if a spot is taken
                        if board[n] == 'X': x = False
                #making sure the ship is vertical
                else:
                    #for loop to check to see if the spaces are taken
                    for j in range(i):
                        n = 10 * (min(ystart,yend) + (j)) + xstart
                        #changing the checking variable if a spot is taken
                        if board[n] =='X': x = False
                #checking to see if the checking variable changed
                if x == True:
                    #Checking if the ship is horizontal
                    if ystart == yend:
                        #for loop to change each list member to occupied ship
                        # status
                        for j in range(i):
                            n = ystart * 10 + min(xstart,xend) + j
                            board[n] = 'X'
                    #checking if the ship is vertical
                    else:
                        #for loop to change each list member to occupied ship
                        # status
                        for j in range(i):
                            n = 10 * ( min(ystart,yend) + j) + xstart
                            board[n] ='X'
                    #breaking the while loop because the placement was valid
                    break
    #returning the changed board list
    return board
        


            
    
# this function draws a miss animation on a given graphics window
#
# Inputs: win - the graphics window you want the animation to be drawn to
#         listNumber - the square you want the animation to be drawn to
#
# Outputs: none
#
def miss(win,listNumber):
    #calculating the center x y pair for the given square
    center = Point(listNumber%10 * 40 + 70, 320 + listNumber//10 * 40)

    #drawing a center circle
    circle = Circle(center, 4)

    #making the circle look right
    circle.setOutline('blue1')
    circle.setWidth(5)
    circle.draw(win)

    #for loop to increase the size of the circle
    for i in range(10):
        #undrawing the circle
        circle.undraw()

        #changing the circle size
        circle = Circle(center, 4 + 4 * i)

        #changing the circle's appearance
        circle.setOutline('blue1') 
        circle.setWidth(5)

        #redrawing the circle and waiting .02 seconds
        circle.draw(win)
        time.sleep(.02)

    #for loop to decrease the size of the circle
    for i in range(5):
        #undrawing the circle
        circle.undraw()

        #changing the circle size
        circle = Circle(center, 40 - 4 * i)

        #changing the circle's appearance
        circle.setOutline('blue1')
        circle.setWidth(5)

        #redrawing the circle and waiting .02 seconds
        circle.draw(win)
        time.sleep(.02)

    #for loop to increase the size of the circle
    for i in range(5):
        #undrawing the circle
        circle.undraw()

        #changing the circle size
        circle = Circle(center, 20 + 4 * i)

        #changing the circle's appearance
        circle.setOutline('blue1') 
        circle.setWidth(5)

        #redrawing the circle and waiting .02 seconds
        circle.draw(win)
        time.sleep(.02)

    #for loop to decrease the size of the circle
    for i in range(10):
        #undrawing the circle
        circle.undraw()

        #changing the circle size
        circle = Circle(center, 46 - 4 * i)
        
        #changing the circle's appearance
        circle.setOutline('blue1') 
        circle.setWidth(5)

        #redrawing the circle and waiting .02 seconds
        circle.draw(win)
        time.sleep(.02)




# This function draws a hit animation on a given graphics window
#
# Inputs: win - the graphics window that the animation will be drawn to
#         listNumber - the square where the animation will occur
#
# Outputs: none
#
def hit(win,listNumber):
    #getting the center of the given square
    center = Point(listNumber%10 * 40 + 70, 320 + listNumber//10 * 40)

    #creating the correct circle object
    circle = Circle(center,4)
    circle.setOutline('red')
    circle.setWidth(5)


    #drawing the circle to the graphics window
    circle.draw(win)

    #initializing the reference table
    colors = ['red','orange2','orange']

    #for loop to cycle through the three colors
    for j in range(3):

        #for loop to increase the circle's size
        for i in range(6):
            #undrawing the circle
            circle.undraw()

            #changing the circle's appearance
            circle = Circle(center,4 + 4 * i)
            circle.setWidth(5)
            circle.setOutline(colors[j])

            #drawing the circle and waiting
            circle.draw(win)
            time.sleep(.04)
        #clearing the circle once the animation is complete
        circle.undraw()

    #creating the X image
    line1 = Line(Point(center.getX() - 10, center.getY() - 10),
                 Point(center.getX() + 10, center.getY() + 10))
    line2 = Line(Point(center.getX() + 10, center.getY() - 10),
                 Point(center.getX() - 10, center.getY() + 10))

    #making the X look better
    line1.setWidth(5)
    line2.setWidth(5)
    line1.setFill('red')
    line2.setFill('red')

    #drawing the X image to the graphics window
    line1.draw(win)
    line2.draw(win)


# this fucntion makes the user click inside of the playing area and outputs the
# resutls
#
# inputs: win - the graphics window
#         shipBoard - the computer's ship placement
# 
# outputs: shipBoard - the changed ship placement list
#
def userClick(win,shipBoard):

        #while loop to wait until a valid click
        while True:
            #getting the user to click
            n = win.getMouse()

            #checking to see if its inside the playable area and breaking
            if 50<n.getX()<450 and 300<n.getY()<700:
                break

        #calculating the x and y coordinates of the click
        x = (n.getX() - 50)//40
        y = (n.getY() - 300)//40

        #calculating the list member that corresponds to the click
        place = y*10 + x

        #checking to see if the click was a miss
        if shipBoard[place] == 'O':
            #running the miss program
            miss(win,place)
            #returning the new ship list
            return shipBoard
        else:
            #running the hit program
            hit(win,place)

            #changing the list member
            shipBoard[place] = 'H'

            #returning the new ship list
            return shipBoard
        

    

#this function opens up a graphics window and shows a gif on it
#
# inputs: none
#
# outputs: none
#
def gif():
    #defining the image variable
    image = Image(Point(0,0),'BattleshipGif0.gif')

    #opening the graphics window
    win = GraphWin('Battleship', image.getWidth(), image.getHeight())
    win.setCoords(-image.getWidth(),-image.getHeight(),image.getWidth(),
                  image.getHeight())

    #for loop to cycle through each gif picture
    for i in range(14):
        #saving the image file name to a string variable
        name = 'BattleshipGif' + str(i) + '.gif'

        #saving the image variable to the correct image file
        image = Image(Point(0,0),name)

        #drawing the image
        image.draw(win)

        #waiting
        time.sleep(.15)

    #prompting the user to continue
    text = Text(Point(0,-170),'Click to Continue')
    text.setSize(18)
    text.setFace('courier')
    text.setFill(color_rgb(0,255,0))
    text.draw(win)

    #closing the window when clicked
    win.getMouse()
    win.close()




#
# compBoard()
# draws computer board in graphwin 
# inputs: win
# outputs: compboard in graphwin
# 

def compBoard(win):
    # set background to blafk
    win.setBackground('black')
    # draw battleship logo image to graphwin
    filename = 'battleship.gif'
    logo = Image(Point(355,20), filename)
    logo.draw(win)

    # filling in blank areas/cover up some of battleship image
    rec = Rectangle(Point(-10,150), Point(510,200))
    rec.setFill('black')
    rec.draw(win)
    rec2 = Rectangle(Point(0,0), Point(5, 149))
    rec2.setFill('black')
    rec2.draw(win)
    rec3 = Rectangle(Point(0,201), Point(5, 215))
    rec3.setFill('black')
    rec3.draw(win)

    # draw picture of ocean to graphwin
    ocean = Image(Point(255,534), 'ocean.gif')
    ocean.draw(win)
    h1 = Line(Point(-10,200), Point(510,200))
    h1.setFill('white')
    h1.draw(win)
    h2 = Line(Point(-10,150), Point(510,150))
    h2.setFill('white')
    h2.draw(win)
    
    # filling in right side of grid 
    rec4 = Rectangle(Point(470,280), Point(510, 710))
    rec4.setFill('black')
    rec4.draw(win)
    # draw white horizontal dividing line 1
    v = Line(Point(469, 283), Point(469,710))
    v.setFill('white')
    v.draw(win)
    
    # filling in left side of grid
    rec5 = Rectangle(Point(0,280), Point(30,710))
    rec5.setFill('black')
    rec5.draw(win)
    # draw white horizontal dividing line 2
    v2 = Line(Point(31, 283), Point(31,710))
    v2.setFill('white')
    v2.draw(win)
    
    # third horizontal line
    h4 = Line(Point(-10, 283), Point(510,283))
    h4.setFill('white')
    h4.draw(win)
    win.setBackground('black')

    
    # draw the grid: 10x10, each square 40 pixels each
    # write for loop in range of beginning x coord of grid to end x coord
    # count by 40 
    for i in range(50, 451, 40):
        # draw vertical line at x coord in for loop
        # keep y coord constant
        L = Line(Point(i,300), Point(i,700))
        # make thick black line and draw to win
        L.setFill('black')
        L.setWidth(2)
        L.draw(win)

    # make for loop to run through beginning and x y coords
    # coutning by 40
    for i in range(300, 700, 40):
        # draw a line at changing x coord and constant y --> horizontal line
        L = Line(Point(50,i), Point(450,i))
        L.setFill('black')
        L.setWidth(2)
        L.draw(win)

    # create a list of number and letter strings to draw onto grid label
    numbers = ['1','2','3','4','5','6','7','8', '9', '10']
    letters = ['a','b','c','d','e','f','g','h','i','j']
    # create counter variable a
    a = 70

    # create for loop that runs through list of number labels
    for i in numbers:
        # create t# text object centered at point a that starts at x=70
        # and increases by 40 each time
        # i(text) is each string in list
        ta = Text(Point(a, 293), i)
        ta.setSize(15)
        ta.setFill('white')
        ta.setFace('courier')
        # draw ta to win
        ta.draw(win)
        # increase counter a by 40
        a = a + 40
        
    # create counter b to start at y = 320
    b = 320
    # for loop to run through letters list
    for i in letters:
        # create text object centered at changing points
        # that shift down by 40 every time
        # and contain text of string in a
        ta = Text(Point(41.5, b), i)
        ta.setSize(15)
        ta.setFill('white')
        ta.setFace('courier')
        ta.draw(win)
        b = b + 40

    # create greet text object welcome message
    greet = Text(Point(250,165), "Welcome to BATTLESHIP")
    # set font, size, and color
    greet.setFace('courier')
    greet.setSize(18)
    greet.setFill(color_rgb(0,255,0))
    # draw to graphwin
    greet.draw(win)

    # create greet text 2 object to prompt user to click
    greet2 = Text(Point(250, 185), "Click a square to FIRE")
    greet2.setSize(18)
    greet2.setFace('courier')
    greet2.setFill(color_rgb(0,255,0))
    greet2.draw(win)

    # wait for user click
    win.getMouse()


# this function works in conjunction with the enhancedCompClick to output a 
# shot on the user's board
#
# inputs: queue - a list containing the board places to guess
#         board - the user's ship placement
#
# outputs: x - the x coordinate of the guess
#          y - the y coordinate of the guess
#          queue - a lsit containing the board places to guess
#          last - the last guess
#
#
def enhancedGuess(queue,board):
    #initializing the variables
    last = False
    x = True

    #while loop to pick a correct x and y if there are items in the queue
    while len(queue) > 0:
        #setting the first member of the list to the pick
        pick = queue[0]

        #taking away that member
        queue = queue[1:]

        #correcting the pick variable if its in the first row
        if pick[1] == 'r' or pick[1] == 'l' or pick[1] == 'd' or pick[1] == 'u':
            pick = '0' + pick

        #setting the last variable to the pick variable
        last = pick
        
        #calculating the x and y coordinates depending on the pick string
        if pick[2] == 'u':
            x = int(pick[1])
            y = int(pick[0]) - 1
        elif pick[2] == 'l':
            x = int(pick[1]) - 1
            y = int(pick[0])
        elif pick[2] == 'r':
            x = int(pick[1]) + 1
            y = int(pick[0]) 
        else:
            x = int(pick[1])
            y = int(pick[0]) + 1

        #checking to see if the x and y is a guess or known
        if len(pick) == 4 and ((x%2 == 0 and y%2 == 0) or (x%2 != 0 and y%2 != 0)):
            #setting the x variable accordingly
            x = True
            
        #try statement to catch errors
        try:
            #checking to see if the guess has already been guessed, and breaking
            #if not
            if board[y*10 + x] == 'O' and -1<x<10 and -1<y<10: break
            #changing the x variable accordingly
            else: x = True
        except:
            #changing the x variable accordingly
            x = True

    #checking to see if the queue is empty
    if len(queue) == 0 and x == True:
        #changing the last variable
        last = False

        #setting the counter variable to zero
        counter = 0

        #while loop to choose a random point
        while True:

            #picking a random number between 0 and 1
            n = random.randint(0,1)

            #checking to see if it has cycled through too many times and manually
            #changing the random variable
            if counter > 10 and counter % 2 == 0: n = 0
            elif counter > 10 and counter % 2 == 1: n = 1

            #picking a random x and y coordinate
            if n == 0:
                x = random.randint(0,4) * 2
                y = random.randint(0,4) * 2
                #checking to see if the pick has been guessed and if not breaking
                if board[y * 10 + x ] == 'O': break
            else:
                x = random.randint(0,4) * 2 + 1
                y = random.randint(0,4) * 2 + 1
                #checking to see if the pick has been guessed and if not breaking
                if board[y * 10 + x ] == 'O': break
            #adding one to the counter variable
            counter = counter + 1
            
    #returning values
    return x,y,queue, last

#this function works in conjunction with enhancedGuess to output the guess to 
#the user
#
# inputs: win - the graphics window
#         shipboard - the usesr's ship placement
#         guessBoard - the computer's previous guesses
#         queue - the current queue for the computer's guesses
#
# outputs: guessBoard - the computer's previous guesses
#          queue - the current queue for the computer's guesses
#
def enhancedCompClick(win,shipboard,guessBoard,queue):
    #while loop to make sure that the guess is correct
    while True:
        #saving the output to variables
        x,y,queue,last = enhancedGuess(queue,guessBoard)
        if guessBoard[y*10+x] == 'O': break
    #checking to see if the guess is a miss
    if shipboard[y*10+x] == 'O':
        #saving the miss to the guess list
        guessBoard[y*10+x] = 'M'
        #running the miss program to output guess to the user
        miss(win,y*10+x)

    else:
        #running the hit program to output guess to the user
        hit(win,y*10+x)

        #changing the guess list
        guessBoard[y*10+x] = 'X'
        
        #checking to see if the hit was from the queue or not
        if len(queue) == 0:
            #adding possible hits to the queue variable
            for j in range(2):
                temp = [str(y*10+x) + 'l'] + [str(y*10+x) + 'u'] + [str(y*10+x) + 'r'] + [str(y*10+x) + 'd']
                for i in range(4):
                    c = random.randint(0,len(temp) - 1)
                    queue = [temp[c]] + queue
                    temp = temp[0:c] + temp[c+1:]
        else:
            #adding possible hits to the queue becauase the hit was from the
            #queue
            for j in range(2):
                #checking to see if the hit was vertical
                if last[2] == 'u' or last [2] == 'd':
                    #adding members to the list accordingly
                    temp1 = [str(y*10+x) + 'u'] + [str(y*10+x) + 'd']
                    temp2 = [str(y*10+x) + 'lg'] + [str(y*10+x) + 'rg']
                    for i in range(2):
                        rand1 = random.randint(0,len(temp1) - 1)
                        rand2 = random.randint(0,len(temp2) - 1)

                        queue = [temp1[rand1]] + queue + [temp2[rand2]]

                        temp1 = temp1[0:rand1] + temp1[rand1+1:]
                        temp2 = temp2[0:rand2] + temp2[rand2 + 1:]
                #checking to see if the hit was horizontal
                elif last [2] == 'l' or last [2] == 'r':
                    #adding the list members accordingly
                    temp2 = [str(y*10+x) + 'ug'] + [str(y*10+x) + 'dg']
                    temp1 = [str(y*10+x) + 'l'] + [str(y*10+x) + 'r']
                    for i in range(2):
                        rand2 = random.randint(0,len(temp1) - 1)
                        rand1 = random.randint(0,len(temp2) - 1)

                        queue = [temp1[rand1]] + queue + [temp2[rand2]]

                        temp1 = temp1[0:rand1] + temp1[rand1+1:]
                        temp2 = temp2[0:rand2] + temp2[rand2 + 1:]
                    
    #returning the variables
    return guessBoard, queue









#
# userBoard()
# draws user board 
# inputs: win
# outputs: userboard ship placement
# 

def userBoard(win):

    # all this code copied directly from compBoard()
    # Note: see compBoard for full comments (ONLY on copied section)
    
    win.setBackground('black')
    # draw battleship logo image
    filename = 'battleship.gif'
    logo = Image(Point(355,20), filename)
    logo.draw(win)

    # filling in blank areas/cover up some of battleship image
    rec = Rectangle(Point(-10,150), Point(510,200))
    rec.setFill('black')
    rec.draw(win)
    rec2 = Rectangle(Point(0,0), Point(5, 149))
    rec2.setFill('black')
    rec2.draw(win)
    rec3 = Rectangle(Point(0,201), Point(5, 215))
    rec3.setFill('black')
    rec3.draw(win)

    # ocean pic
    ocean = Image(Point(255,534), 'ocean.gif')
    ocean.draw(win)
    h1 = Line(Point(-10,200), Point(510,200))
    h1.setFill('white')
    h1.draw(win)
    h2 = Line(Point(-10,150), Point(510,150))
    h2.setFill('white')
    h2.draw(win)

    # filling on right side of grid 
    rec4 = Rectangle(Point(470,280), Point(510, 710))
    rec4.setFill('black')
    rec4.draw(win)
    v = Line(Point(469, 283), Point(469,710))
    v.setFill('white')
    v.draw(win)

    # filling on left side of grid
    rec5 = Rectangle(Point(0,280), Point(30,710))
    rec5.setFill('black')
    rec5.draw(win)
    v2 = Line(Point(31, 283), Point(31,710))
    v2.setFill('white')
    v2.draw(win)

    # third horizontal line
    h4 = Line(Point(-10, 283), Point(510,283))
    h4.setFill('white')
    h4.draw(win)

    win.setBackground('black')

    # draw grid
    for i in range(50, 451, 40):
        L = Line(Point(i,300), Point(i,700))
        L.setFill('black')
        L.setWidth(2)
        L.draw(win)

    for i in range(300, 700, 40):
        L = Line(Point(50,i), Point(450,i))
        L.setFill('black')
        L.setWidth(2)
        L.draw(win)

    numbers = ['1','2','3','4','5','6','7','8', '9', '10']

    letters = ['a','b','c','d','e','f','g','h','i','j']

    a = 70

    for i in numbers:
        ta = Text(Point(a, 293), i)
        ta.setSize(15)
        ta.setFill('white')
        ta.setFace('courier')
        ta.draw(win)
        a = a + 40

    b = 320

    for i in letters:
        ta = Text(Point(41.5, b), i)
        ta.setSize(15)
        ta.setFill('white')
        ta.setFace('courier')
        ta.draw(win)
        b = b + 40

    greet = Text(Point(250,165), "Welcome to BATTLESHIP")
    greet.setFace('courier')
    greet.setSize(18)
    greet.setFill(color_rgb(0,255,0))
    greet.draw(win)

    greet2 = Text(Point(250, 185), "Click to Begin")
    greet2.setSize(18)
    greet2.setFace('courier')
    greet2.setFill(color_rgb(0,255,0))
    greet2.draw(win)

    win.getMouse()

    # return the output of userPlaceShips
    return userPlaceShips(win,greet,greet2)








#
# userPlaceShips()
# inputs: user clicks, win, greet, greet2
# outputs: ships, original and placed
# draws the subs to win and allows user to click to place them 

def userPlaceShips(win,greet,greet2):

    # undraw greets
    greet.undraw()
    greet2.undraw()

    # create list of x and y coords for pts where subs should be placed
    subx1 = [20,220,380,150,310]
    suby1 = [210,210,210,245,245]
    subx2 = [200,360,480,250,370]
    suby2 = [240,240,240,275,275]

    # create for loop of 5 to run through all sub points
    for i in range(5):
        # create s# sub object that draws the sub at the indexed
        # correct x and y coord
        si = Oval(Point(subx1[i], suby1[i]), Point(subx2[i], suby2[i]))
        # set outline of subs to grey
        si.setOutline('grey')
        # set color to black
        si.setFill('black')
        # draw to graphwin
        si.draw(win)

    # create a list of x and y coords of where the circles for each
    # sub should be drawn
    ptx = [80,267,420,190,340]
    pty = [225, 225, 225, 260, 260]

    # create counter variable beginning at h = 5
    h = 5

    # create for loop of range 5 to cycle through all subs
    for i in range(5):
        # subtract 1 from h through every run of the for loop
        h = h-1
        # nestle another for loop in range h
        # because each sub draws one less circle
        for a in range(h): 
            # create c# object circle centered at point indexed
            # from lists, and changing x by 20 pixels each time
            ca = Circle(Point(ptx[i] + 20*a, pty[i]), 5)
            # set circles to grey
            ca.setFill('grey')
            # draw to graphwin
            ca.draw(win)
            
    # draw remaining two circles that could not be included in for loop
    # because of repeating 3 requirements
    c2 = Circle(Point(210,260), 5)
    c2.setFill('grey')
    c2.draw(win)
    c1 = Circle(Point(340, 260),5)
    c1.setFill('grey')
    c1.draw(win)

    # create board list containing one 'O'
    board = ['O']
    # write for loop to run 99 times and add another 'O' to list every time
    # to create list of 100 'O's
    for i in range(99):
            board = board + ['O']

    # create ships list of number of squares encapsulated by each sub
    # AKA sub size
    ships = [5,4,3,3,2]
    # create list of accompanying labels for each sub that
    # prompt will run through 
    texthelp = ['first','second','third','fourth','fifth']

    # create for loop to run through all ships
    for i in range(5):
        # create placet line 1 prompt
        # index user ship size description to prompt user # of squares to click
        placet = Text(Point(250,165), "Click the 1st and " + str(ships[i]) + "th square of a sequence of")
        # create place2t line 2 prompt
        # index user ship length to say how many square-distances to click
        place2t = Text(Point(250, 185), str(ships[i]) + " squares to place your " + texthelp[i] +" ship.")
        # set size, font, and color of prompts
        # and draw to graphwin
        placet.setSize(15)
        placet.setFace('courier')
        placet.setFill(color_rgb(0,255,0))
        placet.draw(win)
        place2t.setSize(15)
        place2t.setFace('courier')
        place2t.setFill(color_rgb(0,255,0))
        place2t.draw(win)

        # create while loop 
        while True:
            # create test variable 
            test = 0
            # getMouse and save pt as first
            first = win.getMouse()
            # undraw direction
            placet.undraw()
            place2t.undraw()
            # getMouse and save pt as second
            second = win.getMouse()
            placet.draw(win)
            place2t.draw(win)

            # subtract 50 from x-coord to account for black bar
            # int divide by 40 to get x square place on board for both
            # first and second
            X1 = (first.getX() - 50) // 40
            # subtract 300 from user click y-coord to account for all the
            # stuff above the grid and int divide by 40 to get y place
            # on board of user click for first and second
            Y1 = (first.getY() - 300) // 40
            X2 = (second.getX() - 50) // 40
            Y2 = (second.getY() - 300) // 40

            # if the x positions of the two clicsk are the same
            # and difference in y = correct length of ship 
            if X1 == X2 and abs(Y1-Y2) == ships[i] - 1:
                # set test to True 
                test = True
                # create for loop to run through ship length
                for j in range(ships[i]):
                    # if place in board list already = 'X' change test to F
                    if board[(min(Y1,Y2) + j) * 10 + X1] == 'X': test = False
            # if the user places a ship horizontally and the correct length: 
            elif Y1 == Y2 and abs(X1 - X2) == ships[i] - 1:
                # test is True
                test = True
                # create for loop to run through ship length
                for j in range(ships[i]):
                    # if any point on board is already in list as X test = F
                    if board[Y1*10 + min(X1,X2) + j] == 'X': test = False
            # create a try except
            try:
                # if the test = False, display error message
                if test == False:
                    placet.setText('Your ship placement was not valid.')
                    place2t.setText('Please re-place your ship in a different location.')
                # if the test is true, break from loop
                if test == True: break
            except:
                # if test is neither True nor False (AKA = 0)
                # tell user they did not click correct ship length
                placet.setText('Please click the correct number of spaces apart.')
                place2t.setText('')

        # if ship placed vertically and correctly: 
        if X1 == X2 and abs(Y1-Y2) == ships[i] - 1:
            # create for loop to run through ship length
            for j in range(ships[i]):
#                print((min(Y1,Y2) + j) * 10 + X1)
                # change value in list board to X 
                board[(min(Y1,Y2) + j) * 10 + X1] = 'X'
        # if ship is placed horizontally and correctly: 
        elif Y1 == Y2 and abs(X1 - X2) == ships[i] - 1:
            # create for loop to run through ship length
            for j in range(ships[i]):
#                print(Y1*10 + min(X1,X2) + j)
                # change string in board list to X 
                board[Y1*10 + min(X1,X2) + j] = 'X'

        # if ship was placed vertically and with the correct # of spaces
        if X1 == X2 and abs(Y1-Y2) == ships[i] - 1:
            # if click 2 is further down than click 1
            if Y2 > Y1:
                # draw sub at X1+1 * 40 pixels(across the grid) and +15
                # to account for cushioning on left hand side of the grid
                # and set Y coords equal except for first point is 10 units to
                # the left of the second to create
                # width of sub
                sub = Oval(Point((X1+1)*40+15, (Y1)*40+315), Point((X1+1)*40+45, (Y2)*40+325))
                sub.setFill('black')
                sub.setOutline('grey')
                sub.draw(win)

                # create for loop to run through number of circles
                # that need to be drawn 
                for p in range(ships[i] - 1):
                    # create b4 variable that tells where on the ship
                    # the circles should begin being drawn
                    # relative to length of ship and number of pts
                    b4 = abs(Y1-Y2) // (ships[i] - 1)
                    # write different if elifs for each possibility of
                    # submarine, with the only difference being the
                    # addition of the number in the y coord that decreases
                    # every time in order to properly center and place
                    # the circles
                    # circles are placed 20 pixels apart each time
                    if ships[i] == 5: 
                        cp = Circle(Point((X1*40)+70,(Y1*40)+b4+365+(20*p)), 5)
                    elif ships[i] == 4:
                        cp = Circle(Point((X1*40)+70,(Y1*40)+b4+357+(20*p)), 5)                       
                    elif ships[i] == 3: 
                        cp = Circle(Point((X1*40)+70,(Y1*40)+b4+350+(20*p)), 5)
                    elif ships[i] == 2:
                        cp = Circle(Point((X1*40)+70,(Y1*40)+b4+337+(20*p)), 5)
                    # set circle outline to black and inside to grey and draw
                    cp.setOutline('black')
                    cp.setFill('grey')
                    cp.draw(win)

            else:
                # if Y1 > Y2
                # create oval object of subarmine and draw to graphwin
                # but this time y-coord addition is changed
                # (flipped from if Y2>Y1)
                sub = Oval(Point((X1+1)*40+15, (Y1)*40+325), Point((X1+1)*40+45, (Y2)*40+315))
                sub.setFill('black')
                sub.setOutline('grey')
                sub.draw(win)

                # create for loop to run through number of circles to be drawn
                for k in range(ships[i] - 1):
                    # create b4 length from end point on sub variable
                    b4 = abs(Y1-Y2) // (ships[i] - 1)
                    # if elifs to run through each length of sub
                    # and change beginning place of circle series
                    # beginning from the endpoint Y2 rather than Y1
                    if ships[i] == 5: 
                        ck = Circle(Point((X1*40)+70,(Y2*40)+b4+365+(20*k)), 5)
                    elif ships[i] == 4:
                        ck = Circle(Point((X1*40)+70,(Y2*40)+b4+357+(20*k)), 5)                       
                    elif ships[i] == 3: 
                        ck = Circle(Point((X1*40)+70,(Y2*40)+b4+350+(20*k)), 5)
                    elif ships[i] == 2:
                        ck = Circle(Point((X1*40)+70,(Y2*40)+b4+337+(20*k)), 5)
                    ck.setOutline('black')
                    ck.setFill('grey')
                    # draw to graphwin
                    ck.draw(win)

        # else if ship is placed horizontally and with the correct length
        elif Y1 == Y2 and abs(X1 - X2) == ships[i] - 1:
            # create o variable that is the ship length - 1
            o = ships[i] - 1

            # if user click 1 x coord is less than user click 2 x coord
            if X2 > X1:
                # draw submarine with constant y and changing x
                # with the beginning pt + 65 and end pt + 75
                # draw to graphwin
                sub = Oval(Point((X1)*40+65, (Y1)*40+305), Point((X2)*40+75, (Y2)*40+335))
                sub.setFill('black')
                sub.setOutline('grey')
                sub.draw(win)

                # create list l of distances from the sub the circles
                # should begin at
                l = [90,90,100,110,120] 

                # create for loop that runs through the same number
                # of times as there are circle
                for j in range(ships[i] - 1):
                    # drawing each circle at a different x coord
                    # and same y coord
                    # spacing each circle drawn by 20 pixels
                    ci = Circle(Point(X1*40 + (l[o]) + 20*j, 40*Y1 + 320),5)
                    ci.setOutline('black')
                    ci.setFill('grey')
                    ci.draw(win)
            # if X1 > X2
            else:
                # run same as if condition body but replace
                # min point of X1 with X2
                sub = Oval(Point((X1)*40+75, (Y1)*40+305), Point((X2)*40+65, (Y2)*40+335))
                sub.setFill('black')
                sub.setOutline('grey')
                sub.draw(win)
                l = [90,90,100,110,120]
                for j in range(ships[i] - 1):
                    # use x min point of X2
                    cj = Circle(Point(X2*40 + (l[o]) + 20*j, 40*Y1 + 320),5)
                    cj.setOutline('black')
                    cj.setFill('grey')
                    cj.draw(win)
                    
        # undraw prompts 
        placet.undraw()
        place2t.undraw()

    # return the board
        
    
    #redrawing the prompts
    
    placet.setText("Your ships are now armed.")

    place2t.setText("Time for WAR!")

    placet.draw(win)

    place2t.draw(win)

    #return the board

    return board


# this function displays a winning gif to the user
#
# inputs: none
#
# outputs: none
#
def winGif():
    #defining the initial image
    image = Image(Point(0,0), 'WinGif0.gif')

    
    #opening up the correct graphics window and defining its coordinates
    win = GraphWin('You Won',image.getWidth(),image.getHeight())
    win.setCoords(-1 * image.getWidth(),-1 *image.getHeight(),image.getWidth(),image.getHeight())

    
    #for loop to run the gif 5 times
    for j in range(5):
        #for loop to run through each of the images
        for i in range(6):
            #setting the correct image name
            imageName = 'WinGif' + str(i) + '.gif'

            #saving the image variable
            image = Image(Point(0,0),imageName)

            #drawing the image to the window
            image.draw(win)

            #sleeping to make the gif look good
            time.sleep(.05)

    #telling the user their result
    text = Text(Point(0,0),'You Won!')
    text.setSize(30)
    text.setFace('courier')
    text.setFill(color_rgb(0,255,0))
    text.draw(win)       

#this function shows a losing gif to the user
#
# inputs: none
#
# Outputs: none
#
def loseGif():
    #defining the initial image variable
    image = Image(Point(0,0),'LoseGif0.gif')

    #opening up the correct graphics window and defining its coordinates
    win = GraphWin('You Lost',image.getWidth(),image.getHeight())
    win.setCoords(-1 * image.getWidth(),-1 *image.getHeight(),image.getWidth(),image.getHeight())

    #for loop to run the gif 3 times
    for j in range(3):
        #for loop to run though each of the images
        for i in range(19):

            #setting the correct image name
            imageName = 'LoseGif' + str(i) + '.gif'

            #saving the image variable
            image = Image(Point(0,0),imageName)

            #drawing the image to the window
            image.draw(win)

            #sleeping to make the gif look good
            time.sleep(.05)

    #telling the user their result
    text = Text(Point(0,0),'You Lost!')
    text.setSize(30)
    text.setFace('courier')
    text.setFill(color_rgb(0,255,0))
    text.draw(win)        
        



main()
