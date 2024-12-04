#############################
# project.py
#
# Your name: Ahmad Aljabri
# Your andrew id: aaljabri
#################################################

from cmu_graphics import *
import math
import random

#brazil qatar lebanon syria

def onAppStart(app):
    app.enemies = []
    app.background = rgb(224, 255, 255)
    app.poem = '/Users/ahmedaljabri/Desktop/English Project/sprites/Poems.png'  
    app.china = '/Users/ahmedaljabri/Desktop/English Project/sprites/china.webp'
    app.qatar = '/Users/ahmedaljabri/Desktop/English Project/sprites/qatar.png'
    app.ethiopia = '/Users/ahmedaljabri/Desktop/English Project/sprites/ethiopia.png'
    app.pakistan = '/Users/ahmedaljabri/Desktop/English Project/sprites/pakistan.png'
    app.back = '/Users/ahmedaljabri/Desktop/English Project/sprites/back.webp'
    app.home = '/Users/ahmedaljabri/Desktop/Project/Sprites/menu/houseIcon.png'
    app.current = 0
    app.state = 'start'
    app.currentCountry = ''
    app.backButton = '/Users/ahmedaljabri/Desktop/English Project/sprites/backButton.png'
    app.menu = False
    app.rightArrow = '/Users/ahmedaljabri/Desktop/English Project/sprites/ArrowRight.png'
    app.s = False

    app.harry = '/Users/ahmedaljabri/Desktop/English Project/sprites/Harry.jpeg'
    app.harryVoice = Sound(r'./harryVoice.mp3')

    app.jassim = '/Users/ahmedaljabri/Desktop/English Project/sprites/Jassim.jpeg'
    app.jassimVoice = Sound(r'./jassimVoice.mp3')


    app.mikiyas = '/Users/ahmedaljabri/Desktop/English Project/sprites/Mikiyas.jpeg'
    app.mikiyasVoice = Sound(r'./mikiyasVoice.mp3')

    app.aun = '/Users/ahmedaljabri/Desktop/English Project/sprites/Aun.jpeg'
    app.aunVoice = Sound(r'./aunVoice.mp3')


def drawBackground(app):  
    #drawImage(app.back, 0,0,)
    #drawImage(app.back, 600,0)
    #drawImage(app.back, 600,200)
    #drawImage(app.back, 600,400)
    #drawImage(app.back, 0,0)
    #drawImage(app.back, 0,200)
    #drawImage(app.back, 0,400)
    drawImage(app.backButton, 10,10,)
    #drawImage(app.menu, 0,0,)
    

######################################################
# The Main Menu
######################################################

def main_onScreenActivate(app):
    app.current = 0

def main_redrawAll(app):
    # Draw the flags
    drawImage(app.china, 50, 50, width=200, height=150)
    drawImage(app.qatar, 550, 50, width=200, height=150)
    drawImage(app.ethiopia, 50, 400, width=200, height=150)
    drawImage(app.pakistan, 550, 400, width=200, height=150)

    # Add borders for flag images
    drawRect(50, 50, 200, 150, fill=None, border='black', borderWidth=0.5)
    drawRect(550, 50, 200, 150, fill=None, border='black', borderWidth=0.5)
    drawRect(50, 400, 200, 150, fill=None, border='black', borderWidth=0.5)
    drawRect(550, 400, 200, 150, fill=None, border='black', borderWidth=0.5)

    # Add author label
    drawLabel("by Ahmad Aljabri", app.width // 2, 570, size=18, bold=True, align='center', fill='black')

    # Add Poem button
    buttonColor = 'lightgreen'
    drawRect(app.width // 2 - 75, 470, 150, 50, fill=buttonColor, border='black', borderWidth=2)
    drawLabel("Poems", app.width // 2, 495, size=20, bold=True, align='center')

    # Add Context button
    buttonColor = 'lightyellow'
    drawRect(app.width // 2 - 75, 410, 150, 50, fill=buttonColor, border='black', borderWidth=2)
    drawLabel("Context", app.width // 2, 435, size=20, bold=True, align='center')


def main_onMousePress(app, x, y):
    # Check if Poem button is clicked
    if 325 <= x <= 475 and 470 <= y <= 520:
        setActiveScreen('poem')

    # Check if Brazil flag is clicked
    elif 50 <= x <= 250 and 50 <= y <= 200:
        app.currentCountry = 'brazil'
        setActiveScreen('brazil')

    # Check if Qatar flag is clicked
    elif 550 <= x <= 750 and 50 <= y <= 200:
        app.currentCountry = 'qatar'
        setActiveScreen('qatar')

    # Check if Lebanon flag is clicked
    elif 50 <= x <= 250 and 400 <= y <= 550:
        app.currentCountry = 'lebanon'
        setActiveScreen('lebanon')

    # Check if Syria flag is clicked
    elif 550 <= x <= 750 and 400 <= y <= 550:
        app.currentCountry = 'syria'
        setActiveScreen('syria')

    # Check if Context button is clicked
    elif 325 <= x <= 475 and 410 <= y <= 460:
        setActiveScreen('context')



######################################################
# The context Menu
######################################################

def context_onScreenActivate(app):
    app.current = 0

def context_redrawAll(app):
    # Translanguaging context
    # Title
    drawLabel("Context", 400, 20, size=30, fill='black', align='center', bold=True)

    # Context paragraph
    drawLabel("Translanguaging is a powerful tool in academic contexts,", 400, 60, size=20, fill='black', align='center')
    drawLabel("allowing students to draw from all their linguistic resources to", 400, 85, size=20, fill='black', align='center')
    drawLabel("communicate and deepen their understanding of complex material", 400, 110, size=20, fill='black', align='center')
    drawLabel("they are studying. By blending languages, translanguaging helps", 400, 135, size=20, fill='black', align='center')
    drawLabel("bridge gaps in comprehension. This approach not only enhances", 400, 160, size=20, fill='black', align='center')
    drawLabel("communication but also validates the diverse linguistic", 400, 185, size=20, fill='black', align='center')
    drawLabel("backgrounds of students, promoting equity and creativity in education.", 400, 210, size=20, fill='black', align='center')

    # Translanguaging Definition
    drawLabel("Translanguaging:", 400, 260, size=25, fill='black', align='center', bold=True)
    drawLabel("The process of using multiple languages fluidly to communicate,", 400, 300, size=20, fill='black', align='center')
    drawLabel("learn, and create meaning, breaking traditional boundaries", 400, 325, size=20, fill='black', align='center')
    drawLabel("between languages.", 400, 350, size=20, fill='black', align='center')

    # Academic Translanguaging Definition
    drawLabel("Academic Translanguaging:", 400, 400, size=25, fill='black', align='center', bold=True)
    drawLabel("The use of multiple languages in academic work to enhance understanding,", 400, 450, size=20, fill='black', align='center')
    drawLabel("foster creativity, and support learning by integrating diverse", 400, 475, size=20, fill='black', align='center')
    drawLabel("linguistic resources.", 400, 500, size=20, fill='black', align='center')




    # Draw the title
    drawImage(app.backButton, 10,10,)


def context_onMousePress(app, x, y):
    if 10 <= x <= 90 and 10 <= y <= 85:
        setActiveScreen('main')
######################################################
# The Poem Menu
######################################################


def poem_onScreenActivate(app):
    app.current = 0

def poem_redrawAll(app):
    #drawBackground
    drawImage(app.poem,0,0)#, width = 500 , height = 400
    # Draw the title
    drawImage(app.backButton, 10,10,)


def poem_onMousePress(app, x, y):
    if 10 <= x <= 90 and 10 <= y <= 85:
        setActiveScreen('main')

######################################################
# The Qatar Menu
######################################################

def qatar_redrawAll(app):
    drawBackground(app)

    drawImage(app.jassim, 50, 75, width = 300, height = 200, rotateAngle=90)

    drawRect(50,350,700,100,fill=rgb(245, 245, 210),border='black')

    if app.current == 0:
        drawLabel('....', 100, 400, size = 16, align = 'left')

        drawRect(50,455,700,35,fill=rgb(245, 245, 210),border='black')
        drawRect(50,495,700,35,fill=rgb(245, 245, 210),border='black')

        drawLabel('What do you think about translanguing', 90, 475, size = 16, align = 'left')
        drawLabel("Can you say 'I will work on the project today' using translanguing", 90, 515, size = 16, align = 'left')

    if app.current == 1:
        drawLabel('I think translanguaging is important in academic settings because it helps me express ', 100, 400, size = 16, align = 'left')
        drawLabel('my ideas effectively.', 100, 420, size = 16, align = 'left')

        drawRect(50,455,700,35,fill=rgb(245, 245, 210),border='black')
        drawLabel('back', 150, 475, size = 16, align = 'left')

    if app.current == 2:
        drawLabel('....', 150, 400, size = 16, align = 'left')
        app.jassimVoice.play(restart = True)

        drawRect(50,455,700,35,fill=rgb(245, 245, 210),border='black')
        drawLabel('back', 150, 475, size = 16, align = 'left')
    

def qatar_onMousePress(app, x, y):
    if 10 <= x <= 90 and 10 <= y <= 85:
        setActiveScreen('main')

    if 50 <= x <= 750 and 455 <= y <= 490:
        if app.current == 1:
            app.current = 0
        elif app.current == 2:
            app.current = 0
        else:
            app.current = 1

    if 50 <= x <= 750 and 495 <= y <= 530:
        if app.current == 1:
            app.current = 0
        if app.current == 2:
            app.current = 0
        else:
            app.current = 2


######################################################
# The China Menu
######################################################

def brazil_redrawAll(app):
    drawBackground(app)
    drawImage(app.harry, 50, 75, width = 300, height = 200, rotateAngle=90)

    drawRect(50,350,700,100,fill=rgb(245, 245, 210),border='black')



    if app.current == 0:
        drawLabel('....', 100, 400, size = 16, align = 'left')

        drawRect(50,455,700,35,fill=rgb(245, 245, 210),border='black')
        drawRect(50,495,700,35,fill=rgb(245, 245, 210),border='black')
        drawLabel('What do you think about translanguing', 90, 475, size = 16, align = 'left')
        drawLabel("Can you say 'I will work on the project today' using translanguing", 90, 515, size = 16, align = 'left')

    if app.current == 1:
        drawLabel('translanguaging helps me express myself and makes communication more comfortable.', 100, 400, size = 16, align = 'left')
        

        drawRect(50,455,700,35,fill=rgb(245, 245, 210),border='black')
        drawLabel('back', 150, 475, size = 16, align = 'left')

    if app.current == 2:
        drawLabel('....', 150, 400, size = 16, align = 'left')
        app.harryVoice.play(restart = True)
        drawRect(50,455,700,35,fill=rgb(245, 245, 210),border='black')
        drawLabel('back', 150, 475, size = 16, align = 'left')
    

def brazil_onMousePress(app, x, y):
    if 10 <= x <= 90 and 10 <= y <= 85:
        setActiveScreen('main')

    if 50 <= x <= 750 and 455 <= y <= 490:
        if app.current == 1:
            app.current = 0
        elif app.current == 2:
            app.current = 0
        else:
            app.current = 1

    if 50 <= x <= 750 and 495 <= y <= 530:
        if app.current == 1:
            app.current = 0
        if app.current == 2:
            app.current = 0
        else:
            app.current = 2



######################################################
# The Pakistan Menu
######################################################

def syria_redrawAll(app):
    drawBackground(app)
    drawImage(app.aun, 50, 75, width = 300, height = 200, rotateAngle=90)
    drawRect(50,350,700,100,fill=rgb(245, 245, 210),border='black')


    if app.current == 0:
        drawLabel('....', 100, 400, size = 16, align = 'left')

        drawRect(50,455,700,35,fill=rgb(245, 245, 210),border='black')
        drawRect(50,495,700,35,fill=rgb(245, 245, 210),border='black')
        drawLabel('What do you think about translanguing', 90, 475, size = 16, align = 'left')
        drawLabel("Can you say 'I will work on the project today' using translanguing", 90, 515, size = 16, align = 'left')

    if app.current == 1:
        drawLabel('I often find myself using translanguaging in class to explain ideas ', 100, 400, size = 16, align = 'left')
        

        drawRect(50,455,700,35,fill=rgb(245, 245, 210),border='black')
        drawLabel('back', 150, 475, size = 16, align = 'left')

    if app.current == 2:
        drawLabel('....', 150, 400, size = 16, align = 'left')
        app.aunVoice.play(restart = True)
        drawRect(50,455,700,35,fill=rgb(245, 245, 210),border='black')
        drawLabel('back', 150, 475, size = 16, align = 'left')
    

def syria_onMousePress(app, x, y):
    if 10 <= x <= 90 and 10 <= y <= 85:
        setActiveScreen('main')

    if 50 <= x <= 750 and 455 <= y <= 490:
        if app.current == 1:
            app.current = 0
        elif app.current == 2:
            app.current = 0
        else:
            app.current = 1

    if 50 <= x <= 750 and 495 <= y <= 530:
        if app.current == 1:
            app.current = 0
        if app.current == 2:
            app.current = 0
        else:
            app.current = 2



######################################################
# The ethiopia Menu
######################################################

def lebanon_redrawAll(app):
    drawBackground(app)
    drawImage(app.mikiyas, 50, 75, width = 300, height = 200, rotateAngle=90)
    drawRect(50,350,700,100,fill=rgb(245, 245, 210),border='black')


    if app.current == 0:
        drawLabel('....', 100, 400, size = 16, align = 'left')

        drawRect(50,455,700,35,fill=rgb(245, 245, 210),border='black')
        drawRect(50,495,700,35,fill=rgb(245, 245, 210),border='black')

        drawLabel('What do you think about translanguing', 90, 475, size = 16, align = 'left')
        drawLabel("Can you say 'I will work on the project today' using translanguing", 90, 515, size = 16, align = 'left')

    if app.current == 1:
        drawLabel('Translanguaging helps me combine my languages in a way that feels natural.', 100, 400, size = 16, align = 'left')
        

        drawRect(50,455,700,35,fill=rgb(245, 245, 210),border='black')
        drawLabel('back', 150, 475, size = 16, align = 'left')

    if app.current == 2:
        drawLabel('....', 150, 400, size = 16, align = 'left')
        app.mikiyasVoice.play(restart = True)
        drawRect(50,455,700,35,fill=rgb(245, 245, 210),border='black')
        drawLabel('back', 150, 475, size = 16, align = 'left')
    

def lebanon_onMousePress(app, x, y):
    if 10 <= x <= 90 and 10 <= y <= 85:
        setActiveScreen('main')

    if 50 <= x <= 750 and 455 <= y <= 490:
        if app.current == 1:
            app.current = 0
        elif app.current == 2:
            app.current = 0
        else:
            app.current = 1

    if 50 <= x <= 750 and 495 <= y <= 530:
        if app.current == 1:
            app.current = 0
        if app.current == 2:
            app.current = 0
        else:
            app.current = 2

runAppWithScreens(initialScreen='main',width=800,height=600)
