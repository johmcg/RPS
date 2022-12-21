import random
import turtle

tr = turtle.Turtle()
rock = turtle.Turtle()
paper = turtle.Turtle()
scissors = turtle.Turtle()
wn = turtle.Screen()


##begin style
wn.screensize(canvwidth=1200, canvheight=800,
                  bg="pink")
style = ('Courier', 30, 'bold')
wn.setup(width=1.0, height=1.0, startx=None, starty=None)
##end style

wn.title("Paper Rock Scissors!")

winner=" "

def play(player):
        wn.reset()
        Rock = 0
        Paper = 1
        Scissors = 2
        cpuSelection = random.randint(0, 2)
        cpu=' '
        if cpuSelection == 0:
                cpu='rock'
        elif cpuSelection == 1:
                cpu='paper'
        else:
                cpu='scissors'
        if player == 'rock' and cpu == 'rock':
                tr.write("CPU chose " + cpu + "."+"\nTie!", font=style, align='center')
        elif player == 'rock' and cpu == 'paper':
                tr.write("CPU chose " + cpu + "."+"\nCPU Wins!", font=style, align='center')
        elif player == 'rock' and cpu == 'scissors':
                tr.write("CPU chose " + cpu + "."+"\nPlayer Wins!", font=style, align='center')
        elif player == 'paper' and cpu == 'rock':
                tr.write("CPU chose " + cpu + "."+"\nPlayer Wins!", font=style, align='center')
        elif player == 'paper' and cpu == 'paper':
                tr.write("CPU chose " + cpu + "."+"\nTie!", font=style, align='center')
        elif player == 'paper' and cpu == 'scissors':
                tr.write("CPU chose " + cpu + "."+"\nCPU Wins!", font=style, align='center')
        elif player == 'scissors' and cpu == 'rock':
                tr.write("CPU chose " + cpu + "."+"\nCPU Wins!", font=style, align='center')
        elif player == 'scissors' and cpu == 'paper':
                tr.write("CPU chose " + cpu + "."+"\nCPU Wins!", font=style, align='center')
        elif player == 'scissors' and cpu == 'scissors':
                tr.write("CPU chose " + cpu + "."+"\nTie!", font=style, align='center')

tr.penup()
tr.hideturtle()
tr.goto(0,250)
tr.write("Make Your Move!", font=style, align='center')
  
rock.penup()
wn.addshape('rock.gif')
rock.goto(-250,100)
rock.shape('rock.gif')

 
paper.penup()
wn.addshape('paper.gif')
paper.goto(0,100)
paper.shape('paper.gif')
 
scissors.penup()
wn.addshape('scissors.gif')
scissors.goto(250,100)
scissors.shape('scissors.gif')


def move(x, y):
        wn.clear()
        ##begin style
        wn.screensize(canvwidth=1200, canvheight=800,
                  bg="yellow")
        style = ('Courier', 30, 'bold')
        ##end style
        wn.title("Paper Rock Scissors!")
        coordinate = float(str(x))
        if coordinate < -130:
                play('rock')
        if coordinate < 119 and coordinate > -120:
                play('paper')
        if coordinate > 130:
                play('scissors')
        

  

wn.onclick(move)
wn.mainloop()