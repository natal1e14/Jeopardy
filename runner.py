#!/usr/bin/env python
#Natalie Ashgriz
#ICS4U
#Mr. Cardinale
#This program simulates the quiz show Jeopardy!


import Tkinter
import random
import time
from tkFileDialog  import askopenfilename
from tkColorChooser import askcolor              

#Global variables
genre = "All"
doubleJeopardy = False 
score = 0
name = "startGame"
finalJeopardyStuff = None
finalJeopardy = False
dailyDouble = False
jeopardyCats = []
jeopardyScore = 0

#change this to decrease the # of questions that have to be answered/round
#min = 1, max = 30
answerNum = 30


#Getting game colours/theme
colourFile = open("colours.txt")
lenFile = colourFile.readlines()
colourFile.close()

colourFile = open("colours.txt")
for i in range(len(lenFile)):
    thisLine = colourFile.readline()
    thisLine = thisLine.split("    ")
    if thisLine[0] == "Name":
        t = int(thisLine[3])
        if thisLine[4] == "Y\n":
            allowRestart = True
        else:
            allowRestart =False
    if thisLine[2] == "Y1\n":
        color1 = thisLine[1]
    elif thisLine[2] == "Y2\n":
        color2 = thisLine[1]
colourFile.close()

#color1 = "#000392" #default1
#color2 = "#ffffff" #default2
#t = 10000






class HomeScreen(object):
        
    
    #def startGame - takes user from the home screen to the game board
    #@param: none
    #@return: none
    def startGame(self):
        global genre, doubleJeopardy, score
        global finalJeopardyStuff, finalJeopardy, dailyDouble
        global jeopardyCats, jeopardyScore
        
        #Resets variables
        genre = "All"
        doubleJeopardy = False 
        score = 0
        name = "startGame"
        finalJeopardyStuff = None
        finalJeopardy = False
        dailyDouble = False
        jeopardyCats = []
        jeopardyScore = 0
        self.window.withdraw()
        self.begin = Tkinter.Toplevel(self.window)
        startJeopardy = GameBoard(self.begin)
        
    #def toImport - takes user to the Import screen
    #@param: none
    #@return: none
    def toImport(self):
        self.window.withdraw()
        self.begin = Tkinter.Toplevel(self.window)
        self.window = Import(self.begin)
        
    #def toGenre - takes user to the Genre screen
    #@param: none
    #@return: none
    def toGenre(self):
        
        global genre, doubleJeopardy, score
        global finalJeopardyStuff, finalJeopardy, dailyDouble
        global jeopardyCats, jeopardyScore
        
        #Resets variables
        genre = "All"
        doubleJeopardy = False 
        score = 0
        name = "startGame"
        finalJeopardyStuff = None
        finalJeopardy = False
        dailyDouble = False
        jeopardyCats = []
        jeopardyScore = 0
        
        self.window.withdraw()
        self.begin = Tkinter.Toplevel(self.window)
        self.window = Genre(self.begin)
    

    #def toSettings: Takes user to the settings screen
    #@param: none
    #@return: none
    def toSettings(self):
        self.window.withdraw()
        self.begin = Tkinter.Toplevel(self.window)
        self.window = Settings(self.begin)
        
        
    #def viewScores - outputs high score rankings to the user
    #@param: none
    #@return: none
    def viewScores(self):
        
        newWindow = Tkinter.Tk()
        newWindow.title("Scores")
 
        #self.button = Tkinter.Button(newWindow, text="QUIT", command=newWindow.quit)
        #self.button.pack(side="bottom")
        #For specific file: !!Need double slash between each!
        #dir = '//Users//kcardinale//Google Drive//ICS4U//1-4U_Programs_16-17//Unit 4'
        
        self.text = Tkinter.Text(newWindow, font = "Monaco 16")
        self.text.pack(side="top")
        
        self.text.insert("end", open("highScore.txt").read())
    
    
    #def __init__ - constructor
    #@param: window (Tkinter Object)
    #@return: none
    def __init__(self,window2):
        global genre, color1, color2, t
        
        
        #Attributes
        self.window = window2
        self.window.title("Jeopardy!")
        self.window.geometry("1050x275+150+80")
        self.window.resizable(False, False)
        self.window.configure(bg = color1)
        
        #title
        title = Tkinter.Label(window2,text = "Jeopardy!",bg = color1, fg = color2, font = "Gyparody 72")
        title.pack()
        
        #start classic game button
        classic = Tkinter.Button(self.window,text = "Classic", command = self.startGame, highlightbackground = color1)
        classic.pack()
        
        #start game by genre button
        byGenre = Tkinter.Button(self.window,text = "Genre",command = self.toGenre,highlightbackground = color1)
        byGenre.pack()
        
        #go to import button
        importButton = Tkinter.Button(self.window, text = "Import New", command = self.toImport, highlightbackground = color1)
        importButton.pack()
        
        #go to settings button
        changeSettings = Tkinter.Button(self.window, text = "Settings", command = self.toSettings, highlightbackground = color1)
        changeSettings.pack()
        
        #view scores button
        seeScores = Tkinter.Button(self.window, text = "View Scores", command = self.viewScores, highlightbackground = color1)
        seeScores.pack()
        #
        
        #Generates menu bar
        self.menuBar = Tkinter.Menu(self.window)
        
        #help
        self.helpMenu = Tkinter.Menu(self.menuBar)
        self.helpMenu.add_command(label = "Manual", command = getInstructions)
        self.menuBar.add_cascade(label="Help",menu=self.helpMenu)
        self.window.configure(menu=self.menuBar)
        
        #program options
        gameMenu = Tkinter.Menu(self.menuBar)
        gameMenu.add_command(label = "Quit", command = quitProgram)
        self.menuBar.add_cascade(label = "Program Options", menu = gameMenu)
        #answer = Tkinter.Button(window2,text = "Answer", command = self.goAnswer, highlightbackground = color1)
        #answer.grid(column = 2, row = 3)
        

class Settings(object):
    
    #def getColour - opens built-in colour picker, allows user to pick a colour
    #@param: whichColor - str: the current hexadecimal colour value
    #@return: whichColor -str: the new hexadecimal colour value 
    def getColour(self,whichColor):
        
        #opens built-in colour picker
        color = list(askcolor())
        whichColor = color[1]
        #self.highlights.insert(len(self.highlights)-1,whichColor)
        #
        return whichColor

        #Button(text='Select Color', command=getColor).pack()

    
    #def - changeMain: changes main colour (color1)
    #@param: none
    #@return: str: color1 - the hexadecimal value of color1
    def changeMain(self):
        global color1
        
        #gets color selection from listbox
        selection = self.mainColour.curselection()

        try:
            #converts selection to index position
            selection = [int(x) for x in selection]
            selection = int(selection[0])
            
            #if the index is the last option in the listbox, takes user to the colorpicker
            if selection == len(self.lines)-1:
                color1 = self.getColour(color1)
                name = raw_input("Enter a name to save this colour, leave blank for a temporary colour: ")
                
                #if the user enters a name for the colour, it saves the colour to the default colors
                #otherwise, the colour is temporary and will disappear once the user quits the program
                if name != "":
                    line = "{}    {}    {}\n".format(name,color1,"N")
                    newColour = open("colours.txt","a")
                    newColour.write(line)
                    newColour.close()
        
            #if the index is any other value, color1 becomes the colour at the corresponding index
            else:
                color1 = self.hexas[selection]
                
            #if self.changeMain() was called in self.changeDefault(), return color1
            if self.changing == True:
                return color1
        
            #Otherwise, redraw the Settings window to update colours
            else:
                self.window.withdraw()
                self.set = Tkinter.Toplevel(self.window)
                self.window = Settings(self.set)
            
            
        #if no colour is selected, do nothing
        except:
            None
            #self.window.withdraw()
            #self.set = Tkinter.Toplevel(self.window)
            #self.window = Settings(self.set)
            #self.getMainSelection()
          #  self.getMainSelection()
           # self.mainColour.curselection()
        
        
        
        


    
    #def - changeAccents: changes the secondary colour (color2)
    #@param: none
    #@return: str: color2 - the hexadecimal value of color2
    def changeAccents(self):
        global color2
        
        #gets colour selection from listbox
        selection = self.highlights.curselection()
        
        try:
            #converts selection to index position
            selection = [int(x) for x in selection]
            selection = int(selection[0])
            if selection == len(self.lines)-1:
                color2 = self.getColour(color2)
                
                #if the index is the last option in the listbox, takes user to the colorpicker
                name = raw_input("Enter a name to save this colour, leave blank for a temporary colour: ")
                
                #if the user enters a name for the colour, it saves the colour to the default colors
                #otherwise, the colour is temporary and will disappear once the user quits the program
                if name != "":
                    line = "{}    {}    {}\n".format(name,color2,"N")
                    newColour = open("colours.txt","a")
                    newColour.write(line)
                    newColour.close()
                    
            
            #if the index is any other value, color1 becomes the colour at the corresponding index
            else:
                color2 = self.hexas[selection]
                
            #if self.changeMain() was called in self.changeDefault(), return color2
            if self.changing == True:
                return color2
        
            #Otherwise, redraw the Settings window to update colours
            else:
                self.window.withdraw()
                self.set = Tkinter.Toplevel(self.window)
                self.window = Settings(self.set)
            
            
        #if no colour is selected, do nothing
        except:
            None
    
    #def home - takes user to the home screen when the button is pressed (not in use)
    #@param: none
    #@return: none
    def home(self):
        self.window.withdraw()
        self.begin = Tkinter.Toplevel(self.window)
        startJeopardy = HomeScreen(self.begin)
    
    #def getAccentSelection - redraws + fills listbox (not in use)
    #@param: none
    #@return: none
    def getAccentSelection(self):
        #generates listbox
        self.highlights = Tkinter.Listbox(window,selectmode = Tkinter.SINGLE)
        self.highlights.grid(column = 1, row = 2)
        
        #opens colours file, separates the name + hexadecimal value
        f = open("colours.txt")
        for i in range(0,len(self.lines)):
            line = f.readline()
            line = line.split("    ")
            if line[0] != "Name":
                col = line[1]
                self.highlights.insert(i, line[0])
                self.hexas.append(col[:-1])
        
        f.close()
        self.highlights.insert(len(self.lines),"custom")
        
        #generates submit button
        self.go = Tkinter.Button(window, text = "-->", command = self.changeAccents)
        self.go.grid(column = 1, row = 3)
    
    
    #def getMainSelection - redraws + fills listbox (not in use)
    #@param: none
    #@return: none
    def getMainSelection(self):
        
        #generates listbox
        self.mainColour = Tkinter.Listbox(window,selectmode = Tkinter.SINGLE)
        self.mainColour.grid(column = 1, row = 2)
        
        #opens colours file, separates the name + hexadecimal value
        f = open("colours.txt")
        for i in range(0,len(self.lines)):
            line = f.readline()
            line = line.split("    ")
            if line[0] != "Name":
                col = line[1]
                self.mainColour.insert(i, line[0])
                self.hexas.append(col[:-1])
        
        f.close()
        self.mainColour.insert(len(self.lines),"custom")
        
        #generates submit button
        self.go = Tkinter.Button(window, text = "-->", command = self.changeMain)
        self.go.grid(column = 1, row = 3)
    

    #def changeTime - changes the amount of time allowed for answering questions
    #@param: none
    #@return: int:t - the number of milliseconds allowed to answer the question
    def changeTime(self):
        global t
        
        #gets selection from listbox
        select = self.timer.curselection()
        
        try:
            #converts select to index value
            selection = [int(x) for x in select]
            selection = int(selection[0])

            
            #gets new time value from time-options list
            t = self.toptions[selection] *1000
            
            #outputs message to let user know time has been changed
            if t == 0:
                print "Unlimited amount of time granted for questions."
            else:
                print "new alloted time:", str(t//1000), "s"
            return t
            

        #if nothing was selected, do nothing
        except:
            None
        #  #  self.getMainSelection()
        #   # self.mainColour.curselection()
        
       # self.window.withdraw()
       # self.set = Tkinter.Toplevel(self.window)
       # self.new = Settings(self.set)
        
    
    #def getTimeSelection - redraws + fills listbox (not in use)
    #@param: none
    #@return: none
    def getTimeSelection(self):
        self.timer = Tkinter.Listbox(window,selectmode = Tkinter.SINGLE)
        self.timer.grid(column = 1, row = 8)
        
        for i in range(0,60,5):
            self.timer.insert(i%5,i)


        self.timer.insert(len(self.lines),"custom")
        
        self.go = Tkinter.Button(window, text = "-->", command = self.changeTime)
        self.go.grid(column = 1, row = 9)
    
    #def yes - restricts/allows the option to allow restarting a game
    #@param: none
    #@return: allowRestart (boolean)
    def yes(self):
        global allowRestart

        #if the check box is unchecked, allow restarting
        if self.var.get() == 1:
            
            allowRestart = True
        #If the check box is unchecked, do not allow restarting
        else:
            allowRestart = False
        return allowRestart
    
    
    #def changeDefault - changes the default settins in the defaults file
    #@param: none
    #@return: none
    def changeDefault(self):
        global t, color1, color2
        
        #changing defaults is True
        self.changing = True

        #gets value for allowRestart
        allowRestart = self.yes()
        
        #if a new time has been selected, gets the value
        if len(self.timer.curselection()) > 0:
            t = self.changeTime()
        
        #if a new color1 has been selected, gets the value
        if len(self.mainColour.curselection()) > 0:
            color1 = self.changeMain()
        
        #if a new color2 has been selected, gets the value
        if len(self.highlights.curselection()) > 0:
            color2 = self.changeAccents()
        
        
       # y2 = self.highlights.curselection()
       
       #opnes the colours file, where all default settings are stored
        colourFile = open("colours.txt")
        lenFile = colourFile.readlines()
        colourFile.close()
        
        color = []
        hexa = []
        yn = []

        #gets data from colours.txt
        colourFile = open("colours.txt")
        for i in range(len(lenFile)):
            thisLine = colourFile.readline()
            thisLine = thisLine.split("    ")
            if thisLine[0] != "Name":
                
                #color name
                color.append(thisLine[0])
                #hexadecimal value
                hexa.append(thisLine[1])
                #if it is a default colour
                yn.append(thisLine[2])

        colourFile.close()
        

        #if the two colours selected are the same, changes colours but does not allow them to be default
        #tells user to choose different colours
        if color1 == color2:
            print "Please choose a different color from each box"
            self.window.withdraw()
            self.set = Tkinter.Toplevel(self.window)
            self.window = Settings(self.set)
        
        #else
        else:
            
            for i in range(len(color)):
                
                #if color1 is equal to the hexadecimal value at i in the hexa list
                if hexa[i] == color1:
                    
                    #if there is a default color1 in the list yn, gets its index position + changes it to not be default
                    if ("Y1\n" in yn) == True:  
                        index = yn.index("Y1\n")
                        yn[index] = "N\n"
                        
                    #makes the default value at color1's index (i) set to default color1
                    yn[i] = "Y1\n"
                    
                #if color2 is equal to the hexadecimal value at i
                elif hexa[i] == color2:
                    
                    #if there is a default color2 in the yn, gets its index pos + chages it to not be default
                    if ("Y2\n" in yn) == True:  
                        index = yn.index("Y2\n")
                        yn[index] = "N\n"
                        
                    #mkaes the default value at color2's index (i), set to default color2
                    yn[i] = "Y2\n"
                    
                #otherwise, the default setting at yn[i] is set to not default
                else:
                    yn[i] = "N\n"
            
            #if allowRestart is true, the default is changed to indicate it is allowed
            if allowRestart == True:
                yes = "Y\n"
                
            #if allowRestart is False, the default is changed to indicate it is not allowed
            else:
                yes= "N\n"
            
            #writes default settings to the colours.txt file
            colourFile = open("colours.txt","w")
            colourFile.write("Name    Hexa    Default    "+str(t)+"    "+yes)
            for i in range(len(color)):
                line = "{}    {}    {}".format(color[i],hexa[i],yn[i])
                colourFile.write(line)
            colourFile.close()
            
            self.changing = False
            
            #redraws Settings screen to apply new default colours
            self.window.withdraw()
            self.set = Tkinter.Toplevel(self.window)
            self.window = Settings(self.set)
        
    #def getHome - menuBar item takes user to the Home Screen
    #@param: none
    #@return: none
    def getHome(self):
        self.window.withdraw()
        self.home = Tkinter.Toplevel(self.window)
        goHome = HomeScreen(self.home)
    
    #def classic - menuBar item starts a classic game
    #@param:none
    #@return: none
    def classic(self):
        self.window.withdraw()
        self.game =Tkinter.Toplevel(self.window)
        goStart = GameBoard(self.game)
        
    #def goGenre - menuBar item takes user to the choose Genre screen
    #@param: none
    #return: none
    def goGenre(self):
        self.window.withdraw()
        self.game = Tkinter.Toplevel(self.window)
        goTo = Genre(self.game)
    

    #def quitSettings - quits the program
    #@param: none
    #@return: none
    def quitSettings(self):
        self.window.destroy()
        quitProgram()
    
    
    #def __init__  - constructor
    #@param: window, Tkinter Object
    #@return: none
    def __init__(self,window):
        
        global color1, color2, t
        
        #listbox of different settings options -- Click button,
        #dropdown listbox w default colour options/time options OR
        #Extra option
        
        #configures window
        self.window = window
        self.window.configure(bg = color1)
        self.window.geometry("500x750+350+70")
        self.window.resizable(False, False)
        
        
        self.changing = False
        
        #home button
        #self.button = Tkinter.Button(window, text = "Home", command = self.home, highlightbackground = color1)
        #self.button.grid(column = 1, row = 0)
        
        #main colour (label, listbox, apply button)
        self.lbl1 = Tkinter.Label(window, text = "Main Colour", bg = color1, fg = color2)
        self.lbl1.grid(column = 1, row = 1)
        self.mainColour = Tkinter.Listbox(window,selectmode = Tkinter.SINGLE, exportselection = False)
        self.mainColour.grid(column = 1, row = 2)
        self.go = Tkinter.Button(window, text = "-->", command = self.changeMain, highlightbackground = color1)
        self.go.grid(column = 1, row = 3)
        
        #secondary colour (label, listbox, apply button)
        self.lbl2 = Tkinter.Label(window, text = "Accents", bg = color1, fg = color2)
        self.lbl2.grid(column = 1, row = 4)
        self.highlights = Tkinter.Listbox(window,selectmode = Tkinter.SINGLE, exportselection = False)
        self.highlights.grid(column = 1, row = 5)
        self.go = Tkinter.Button(window, text = "-->", command = self.changeAccents, highlightbackground = color1)
        self.go.grid(column = 1, row = 6)
        
        #time (label, listbox, apply button)
        self.lbl3 = Tkinter.Label(window, text = "Time to Answer -- set to 0 for unlimited time", bg = color1, fg = color2)
        self.lbl3.grid(column = 1, row = 7)
        self.timer = Tkinter.Listbox(window,selectmode = Tkinter.SINGLE, exportselection = False)
        self.timer.grid(column = 1, row = 8)
        self.go = Tkinter.Button(window, text = "-->", command = self.changeTime, highlightbackground = color1)
        self.go.grid(column = 1, row = 9)
        
        #checkBox to allow restarting
        self.var = Tkinter.IntVar()
        self.restartYN = Tkinter.Checkbutton(self.window,text = "Allow Restarting",variable = self.var, command = self.yes, bg = "#ffffff", fg = color1)
        self.restartYN.grid(column = 1, row = 10)
        
        #checkbox to make default
        self.var2 = Tkinter.IntVar()
        self.makeDefault = Tkinter.Checkbutton(self.window, text = "Make settings default", variable = self.var2, command = self.changeDefault)
        self.makeDefault.grid(column = 3, row = 5)
        
        

        #button = Tkinter.Button(window,text="Submit",command = on_select)
        #button.pack()
        
        
        self.hexas = []
        self.toptions = []
        
        #populate time listbox
        for i in range(60,-5,-5):
            self.timer.insert(i%5,i)
            self.toptions.insert(i%5,i)
        

        #populate color listboxes from default colours file
        f = open("colours.txt")
        self.lines= f.readlines()
        f.close()
        
        f = open("colours.txt")
        for i in range(0,len(self.lines)):
            line = f.readline()
            line = line.split("    ")
            if line[0] != "Name":
                col = line[1]
                self.mainColour.insert(i, line[0])
                self.highlights.insert(i,line[0])
                self.hexas.append(col)
        
        f.close()
        
        #adds "custom" option to each listbox
        self.mainColour.insert(len(self.lines),"custom")
        self.highlights.insert(len(self.lines),"custom")
        
        
        #generates menubar
        self.menuBar = Tkinter.Menu(self.window)
        
        #help menu
        self.helpMenu = Tkinter.Menu(self.menuBar)
        self.helpMenu.add_command(label = "Manual", command = getInstructions)
        self.menuBar.add_cascade(label="Help",menu=self.helpMenu)
        
        #navigation menu
        self.navigationMenu= Tkinter.Menu(self.menuBar)
        self.navigationMenu.add_command(label = "Home", command = self.getHome)
        self.navigationMenu.add_command(label = "Start Classic Game", command = self.classic)
        self.navigationMenu.add_command(label = "Start Game by Genre", command = self.goGenre)
        self.navigationMenu.add_command(label = "Quit", command = self.quitSettings)
        self.menuBar.add_cascade(label ="Navigate",menu = self.navigationMenu)
    
        self.window.configure(menu=self.menuBar)
        
        self.window.mainloop()
        
        
        

    #    
    #    def on_select():
    #global names
    #val = []
    #
    ##what has been selected in the listbox
    #selections = listbox.curselection()
    #
    ##gets index values of listbox selections
    #selections = [int(x) for x in selections]
    #
    ##converts index values to actual values
    #value = [val.append(names[x]) for x in selections]
    #print val


#default listbox allows you to select 1 option at a time, Tkinter.MULTIPLE allows multiple to be selected


        
        
        
        
        


class Wager(object):
    
    
    #def checkWager - checks the wager to make sure it's an appropriate value, takes action accordingly
    #@param: none
    #@return: none
    def checkWager(self):
        global score
        global dailyDouble
        
        #gets playerWager
        playerWager = self.playerWager.get()
        self.makeWager.grid_forget()
        
    
        
        try:
            
            #if user entered value + $
            if playerWager[0] == "$":
                playerWager = playerWager[1:]
                
            #try concatenate playerWager to integer
            playerWager = int(playerWager)
            
            dailyDouble = True
            
            #if player score is greater than 0
            if score > 0:
                
                #if player wager is greater than or equal to 0 and less than or equal to their score, go to AnswerScreen
                if playerWager <= score and playerWager >= 0:
                    self.new_window = AnswerScreen(self.window3,self.question,self.answer,playerWager,self.playerScore,self.disabled)
                
                #if player wager is less than 0, output message, go to getWager()
                elif playerWager < 0:
                    lbl = Tkinter.Label(self.window3, text = "Wager cannot be negative")
                    lbl.grid(column = 2, row = 0)
                    self.getWager()
                
                #if wager is greater than score, output message + go to self.getWager()
                else:
                    lbl = Tkinter.Label(self.window3, text = "Wager cannot exceed score")
                    lbl.grid(column = 2, row = 0)
                    self.getWager()
            
            #If player score is less than or equal to 0
            else:
                #if playerWager is less than or equal to 2000 and greater than or equal to 0, go to AnswerScreen
                if playerWager <= 2000 and playerWager >= 0:
                    self.new_window = AnswerScreen(self.window3,self.question,self.answer,playerWager,self.playerScore,self.disabled)
                
                #if playerWager is less than 0, output message, go to self.getWager
                elif playerWager < 0:
                    lbl = Tkinter.Label(self.window3, text = "Wager cannot be negative")
                    lbl.grid(column = 2, row = 0)
                    self.getWager()
                
                #if playerWager is greater than $2000, output message, go to self.getWager
                else:
                    lbl = Tkinter.Label(self.window3, text = "Wager cannot exceed $2000")
                    lbl.grid(column = 2, row = 0)
                    self.getWager()
        
        #if input is not an integer, or $___ value, go to self.getWager()
        except:
            print "Invalid input"
            self.getWager()
            
            
        
    
    #def getWager - generates entry box + button for entering wager
    #@param: none
    #@return: none
    def getWager(self):
        
        #entry box
        self.playerWager = Tkinter.Entry(self.window3, highlightbackground = color1)
        self.playerWager.grid(column = 2, row = 2)
        
        #submit wager button, goes to self.checkWager
        self.makeWager = Tkinter.Button(self.window3, text = "Wager $",highlightbackground = color1, command = self.checkWager) #, command = self.checkWager,highlightbackground = color1)
        self.makeWager.grid(column = 2, row = 3)
    
    
    #def new - starts a new game
    #@param: none
    #@return: none
    def new(self):
        global genre, doubleJeopardy, score
        global finalJeopardy, finalJeopardyStuff, dailyDouble,jeopardyCats
        self.window3.withdraw()
        #reset all global variables to original values
        genre = "All"
        doubleJeopardy = False 
        score = 0
        finalJeopardyStuff = None
        finalJeopardy = False
        dailyDouble = False
        jeopardyCats = []
        
        #generate new GameBoard
        self.home = Tkinter.Toplevel(self.window3)
        newGame = GameBoard(self.home)
        
            
        
    #def getHome - goes to home screen
    #@param: none
    #@return: none
    def getHome(self):
        self.window3.withdraw()
        self.begin = Tkinter.Toplevel(self.window3)
        window = HomeScreen(self.begin)
    
    
    #def seeScores - view scores
    #@param: none
    #@return: none
    def seeScores(self):

        #generate Scores window
        newWindow = Tkinter.Tk()
        newWindow.title("Scores")
 
        #self.button = Tkinter.Button(newWindow, text="QUIT", command=newWindow.quit)
        #self.button.pack(side="bottom")
        #For specific file: !!Need double slash between each!
        #dir = '//Users//kcardinale//Google Drive//ICS4U//1-4U_Programs_16-17//Unit 4'
        
        #configure text
        self.text = Tkinter.Text(newWindow, font = "Monaco 16")
        self.text.pack(side="top")
        
        #open file
        self.text.insert("end", open("highScore.txt").read())
    
    #def __init__ - constructor
    #@param: new_window: Tkinter Object, btn: Tkinter Object, question: str, answer: str, value: int, cat: str, playerScore: Tkinter Object, disabled:int
    #@return: none
    def __init__(self,new_window,btn,question,answer,value,cat,playerScore,disabled):
        global score, finalJeopardyStuff, finalJeopardy
        
        #defines attributes
        self.window3 = new_window
        self.window3.geometry("1080x600+150+80")
        self.window3.resizable(False, False)
        self.question = question
        self.answer = answer
        self.value = value
        self.playerScore = playerScore
        self.disabled = disabled
        
        #if finalJeopardy is True, screen title is: 
        if finalJeopardy == True:
            self.window3.title("Final Jeopardy!")
            self.category = cat
        
        #otherwise, screen title is: 
        else:
            self.window3.title("Daily Double!")
            self.category = cat[0]
        
        self.window3.configure(bg = color1)
        
        

        #Outputs category onto screen
        title = Tkinter.Label(self.window3,text =self.category, bg = color1, fg = color2)
        title.grid(column = 2, row = 0)
        
        #outputs player score
        yourScore = Tkinter.Label(self.window3, text = "Your Score: $" + str(score), bg = color1, fg = color2)
        yourScore.grid(column = 2, row = 1)
        
        #gets wager
        self.getWager()
        
        #Generate Menubar
        self.menuBar = Tkinter.Menu(self.window3)
        
        #game menu
        self.gameMenu = Tkinter.Menu(self.menuBar)
        
        
        self.gameMenu.add_command(label = "New Game", command = self.new)
        self.gameMenu.add_command(label = "View Scores", command = self.seeScores)
        
        #help menu
        self.helpMenu = Tkinter.Menu(self.menuBar)
        self.helpMenu.add_command(label = "Manual", command = getInstructions)
        
        #navigation menu
        self.navigationMenu= Tkinter.Menu(self.menuBar)
        self.navigationMenu.add_command(label = "Home", command = self.getHome)
        self.navigationMenu.add_command(label = "Quit", command = quitProgram)
        
        self.menuBar.add_cascade(label="Help",menu=self.helpMenu)
        self.menuBar.add_cascade(label="Game Options",menu=self.gameMenu)
        self.menuBar.add_cascade(label ="Navigate",menu = self.navigationMenu)
        
        self.window3.configure(menu=self.menuBar)
        
        
        

class Import(object):
    
    
    #def importData - imports data from a file to the general file + corresponding genre file
    #@param: name (str)
    #@return: none
    def importData(self,name):
        
       #lists to be populated
        existingLines = []
        newLines = []
        newCats = []
        newQs = []
        newGenres = []
        oldQs = []
        oldCats = []
        oldGenres = []
        
        f = open(name)
        lines = f.readlines()
        f.close()
        
        #get data from file
        f = open(name)
        for i in range(len(lines)):
            line= f.readline()
            lineSplit = line.split("         ")
            if lineSplit[0] == "Genre" or lineSplit[0] == "" or lineSplit[0] == "\n":
                continue
            else:
                #q = lineSplit[2]
                #a = lineSplit[3]
                #g = lineSplit[0]
                #c = lineSplit[1]
                #if a[len(a)-1] == " ":
                #    while a[len(a)-1] == " ":
                #        a = a[:-1]
                #if q[len(q)-1] == " ":
                #    while q[len(q)-1] == " ":
                #        q = q[:-1]
                #if c[len(c)-1] == " ":
                #    while c[len(c)-1] == " ":
                #        c = c[:-1]
                #if g[len(g)-1] == " ":
                #    while g[len(g)-1] == " ":
                #        g = g[:-1]
                
                #separate data into correct lists
                if line[-1:] != "\n":
                    line = line + "\n"
                newAs = lineSplit[3]
                newCats.append(lineSplit[1])
                newQs.append(lineSplit[2])
                newGenres.append(lineSplit[0])
               # line = "{}         {}         {}         {}".format(g,c,q,a)
                newLines.append(line)
        f.close()
        
        
        #open general file
        f = open("general.txt")
        lines = f.readlines()
        f.close()
        
        #add data from general file to correct lists
        f = open("general.txt")
        for i in range(len(lines)):
            line = f.readline()
            existingLines.append(line)
            line = line.split("         ")
            oldCats.append(line[1])
            oldQs.append(line[2])
            oldGenres.append(line[0])
        f.close()
        

        nonExistantGenres = []
        genreLines = []
        for i in range(len(newCats)):
           # print newCats[i]
           # print newQs[i]
           
            #if the question does not exist
            if (newQs[i] in oldQs) == False:
                
                #if the category already exists, insert the category into the correct position 
                if (newCats[i] in oldCats) == True:
                    num = oldCats.index(newCats[i])
                    existingLines.insert(num,newLines[i])
                    oldGenres.insert(num,newGenres[i])

                    
                #If the genre exists but category doesn't
                elif (newGenres[i] in oldGenres) == True:
                    #if there are at least 5 questions for the new category,
                    #insert category to the correct index (with questions of the same genre)
                    if newCats.count(newCats[i]) >= 5:
                        num = oldGenres.index(newGenres[i])
                        existingLines.insert(num,newLines[i])
                        oldGenres.insert(num,newGenres[i])
                    #otherwise, output message telling user what to do
                    else:
                        print newCats[i], "is a new category and must have at least 5 questions before being added to the file."
                        print "Please check the formatting of this category. The rest of your data will continue to be inputted\n"

                
                #if the genre doesn't exist, add the line to the end of the file
                else:
                    if newCats.count(newCats[i]) >= 5:
                        existingLines.append(newLines[i])
                        oldGenres.append(newGenres[i])
                    else:
                        print newCats[i], "is a new category and must have at least 5 questions before being added to the file."
                        print "Please check the formatting of this category. The rest of your data will continue to be inputted\n"
                    #nonExistantGenres.append(newLines[i])
                    #else:

                #print newGenres[i], "is a new genre and must have at least 13 categories with 5 questions each, before being added to the file."
            #
            #if i>0 and (newGenres[i] == newGenres[i-1]):
            #    genreLines.append(newLines[i])
            #    genres.append(newGenres[i])
            #else:
            #    try:
            #        f = open(newGenres[i] + ".txt")
            #        lines = f.readlines()
            #        f.close()
            #        for i in range(len())
            #        
                    
                
                
                
            
        
        f = open("general.txt","w")
        for i in range(len(existingLines)):
            f.write(existingLines[i])
        f.close()
        
        
        allGenres = []
        addedGenres = []
        

        for i in range(len(newGenres)):
            #if the newGenre is not already in allGenres, add it
            if (newGenres[i] in allGenres) == False:
                allGenres.append(newGenres[i])
                
        
        for i in range(0,len(allGenres)):
            fileName = allGenres[i].lower() + ".txt"
            if allGenres[i] != "Genre":
            
                #if specific genre file existss
                try:
                    #open specific genre file 
                    genreFile = open(fileName)
                    lines = genreFile.readlines()
                    genreFile.close()
                    
                    existingGenre = []
                    existingCat = []
                    genreExisting = []
                    existingQ = []
                    
                    #get data from genreFile, add it to correct lists
                    genreFile = open(fileName)
                    for k in range(len(lines)):
                        line = genreFile.readline()
                        existingGenre.append(line)
                        line = line.split("         ")
                        existingCat.append(line[1])
                        genreExisting.append(line[0])
                        existingQ.append(line[2])
                    genreFile.close()
                
                    for j in range(len(newCats)):
                        
                        #if newGenres[j] is equal to the current value of allGenres and the question does not already exist in the file
                        if (newGenres[j] == allGenres[i]) and (newQs[j] in existingQ) == False:
                            
                            #if the Category already exists, add line to correct position
                            if (newCats[j] in existingCat) == True:
                                num = existingCat.index(newCats[j])
                                existingGenre.insert(num,newLines[j])
                               # oldGenres.insert(num,newGenres[j])
                            
                            #if category is new
                            else:
                                #if there are at least 5 questions for that category, add it to the file
                                if newCats.count(newCats[j]) >= 5:
                                    existingLines.append(newLines[j])
                                    oldGenres.insert(num,newGenres[j])
                        
                    
                    
                    #write data to specific genre file
                    f = open(fileName,"w")
                    for k in range(len(existingGenre)):
                        f.write(existingGenre[k])
                    f.close()
                        
                        
                #if genre file does not exist (new genre)
                except:
                    
                    for j in range(len(newGenres)):
                        if (newGenres[j] == allGenres[i]) and newCats.count(newCats[j]) >= 5:
                        
                        #added = False
                            #create a new file for that genre, add data to it
                            f = open(fileName,"w+")
                            f.write("Genre         Category         Question         Answer\n")
                            for j in range(len(newCats)):
                            
                                #added = True
                                    f.write(newLines[j])
                            f.close()
                        
                        #add new genre to the genres file (contains list of all genres)
                        #if added == True:
                            f = open("genres.txt","a")
                            f.write(allGenres[i]+"\n")
                            f.close()
                        
                
        print "Data has been successfully recorded.\n"
                    
                   # addedGenres.append(allGenres[i]+"\n")
        

        
   
    #def checkEntry - checks if the file entered is valid
    #@param: none
    #@return: none
    def checkEntry(self):
        
     #   print self.fileName.get()
     
        #try to open the given file
        #go to impotData if it works
        try:
            name = self.fileName.get()
            f = open(name)
            f.close()

            self.importData(name)
            
        #if the file does not exist, output messages + go to getFile()
        except:
            print "Uh-oh! There was an error uploading your data"
            print "Please ensure that you have entered a valid file path and that your data is in the correct format."
            print "See the user guide for more details.\n"
            self.getFile()
            
        
        
    #def getFile - alters original screen for inputting file name
    #@param: none
    #@return: none
    def getFile(self):
        
        self.specific = True
        self.menuBrr()
        #instructions
        instructions1 = Tkinter.Label(self.window, text = "See Terminal for Instructions.\n Enter File Path:")
        instructions1.grid(column = 2, row = 2)
            
        print "!FILE MUST BE IN .TXT FORMAT \n Ensure the file is divided into 4 columns: Genre, Category, Question, Answer \n and that there are 9 spaces between each column."
        print "Please have at least 5 questions per category, if that category does not already exist. \n Enter the file path."
        
        #entry box for file name
        self.fileName = Tkinter.Entry(self.window, highlightbackground = color1)
        self.fileName.grid(column = 2, row = 3)
        
        #sumbit button, goes to self.checkEntry()
        submit = Tkinter.Button(self.window, highlightbackground = color1, text = "Submit", command = self.checkEntry)
        submit.grid(column = 2, row = 4)
        

    #def addQuestion - adds individual question to file
    #@param: none
    #@return: none
    def addQuestion(self):
        
        #gets question + answer data
        question = self.enterQuestion.get()
        answer = self.enterAnswer.get()
        
        #clears entry boxes
        self.enterQuestion.delete(0, "end")
        self.enterAnswer.delete(0,"end")
        
        
        #if the data is not blank
        if question != "" and answer != "":
            try:
                #gets rid of excess spaces
                if answer[len(answer)-1] == " ":
                    while answer[len(answer)-1] == " ":
                        answer = answer[:-1]
                if question[len(question)-1] == " ":
                    while question[len(question)-1] == " ":
                        question = question[:-1]
                
                #gets category from listbox
                category = self.catBox.curselection()
                cat = [int(x) for x in category]
                cat = cat[0]
                cat = self.entered[cat]
                
                #formats data
                newLine = "{}         {}         {}         {}\n".format(self.genre,cat,question,answer)
                
               
                f = open(self.genre + ".txt")
                lines = f.readlines()
                f.close()
                
                existingCat = []
                existingQ = []
                data = []
                dataGeneral = []
                generalCat = []
                generalQ = []
                
                #gets data from genre file
                genreFile = open(self.genre+".txt")
                for k in range(len(lines)):
                    line = genreFile.readline()
                    data.append(line)
                    line = line.split("         ")
                    existingCat.append(line[1])
                    existingQ.append(line[2])
                genreFile.close()
                
                generalFile = open("general.txt")
                generalLines = generalFile.readlines()
                generalFile.close()
                
                #gets data from generalFile
                generalFile = open("general.txt")
                for i in range(len(generalLines)):
                    line = generalFile.readline()
                    dataGeneral.append(line)
                    line = line.split("         ")
                    generalCat.append(line[1])
                    generalQ.append(line[2])
                generalFile.close()
            
                
                for j in range(len(lines)):
                    #inserts category into the correct place in genreFile
                    if (cat == existingCat[j]) and (question in existingQ) == False:
                        num = existingCat.index(cat)
                        data.insert(num,newLine)
                        break
                    
                for j in range(len(generalLines)):
                    #inserts category into the correct place in generalFile
                    if (cat == generalCat[j]) and (question in existingQ) == False:
                        num = generalCat.index(cat)
                        dataGeneral.insert(num,newLine)
                        break
                           # oldGenres.insert(num,newGenres[j])
                
                #writes data to genreFile
                f = open(self.genre+".txt","w")
                for k in range(len(data)):
                    f.write(data[k])
                f.close()
                
                #writes data to generalFile
                f = open("general.txt","w")
                for k in range(len(dataGeneral)):
                    f.write(dataGeneral[k])
                f.close()
    
                print "Data has been successfully recorded."
            
            #if a category has not been selected
            except:
                print "Please select a category."
                category = self.catBox.curselection()
        
        
        
    
    #def getCats: gets existing categories for selected genre + populates listbox
    #@param: none
    #@return: none
    def getCats(self):
        
        #gets genre selection from self.genreBox (listbox)
        self.genre = self.genreBox.curselection()
        try:
            self.genre = [int(x) for x in self.genre]
            self.genre = int(self.genre[0])
            self.genre = self.genres[self.genre]
            
            #opens genre file + gets categories that exist under that genre
            cats = []
            f = open(self.genre + ".txt")
            lines = f.readlines()
            f.close()
            
            f = open(self.genre + ".txt")
            for i in range(len(lines)):
                line = f.readline()
                line = line.split("         ")
                #if it is not the header + the category has not already been added to cats
                if line[1] != "Category" and (line[1] in cats) == False:
                    cats.append(line[1])
            f.close()
            
            #generates categories listbox
            self.entered = []
            self.catBox = Tkinter.Listbox(self.window, highlightbackground = color1, exportselection = False)
            self.catBox.grid(column = 5, row = 2)
            
            #populates categories listbox
            for i in range(len(cats)):
                if (cats[i] in self.entered) == False:
                    self.catBox.insert(i,cats[i])
                    self.entered.append(cats[i])
            
            #label + entry box for question 
            lbl3 = Tkinter.Label(self.window, bg = color1, fg = color2, text = "Question: ")
            lbl3.grid(column = 2, row = 4)
            self.enterQuestion = Tkinter.Entry(self.window, highlightbackground = color1)
            self.enterQuestion.grid(column = 2, row = 5)
            
            #label + entry box for answer
            lbl4 = Tkinter.Label(self.window, bg = color1, fg = color2, text = "Answer: ")
            lbl4.grid(column = 5, row = 4)
            self.enterAnswer = Tkinter.Entry(self.window, highlightbackground = color1)
            self.enterAnswer.grid(column = 5, row = 5)
            
            #submit button, goes to self.addQuestion()
            submit = Tkinter.Button(self.window, text = "Submit", highlightbackground = color1, command = self.addQuestion)
            submit.grid(column = 5, row = 6)
        except:
            print "Please choose a genre"
        
        
        
        
        
    #def getGenres - alters screen once "Import Questions" is selected to have a listbox with possible genres
    #@param: none
    #@return: none
    def getGenres(self):
    
        #remove byQuestion option
        self.byQuestion.grid_forget()
        self.specific = True
        self.menuBrr()
        
        #generate listbox for selecting a genres
        lbl1 = Tkinter.Label(self.window, text = "Select Genre:", bg = color1, fg = color2)
        lbl1.grid(column = 2, row = 1)
        self.genreBox = Tkinter.Listbox(self.window, highlightbackground = color1, exportselection = False)
        self.genreBox.grid(column = 2, row = 2)
        
        #submit takes selected genre to self.getCats
        self.selectGenre = Tkinter.Button(self.window, text = "-->", highlightbackground = color1, command = self.getCats)
        self.selectGenre.grid(column = 2, row = 3)
        
        #genreates listbox (remains empty until self.selectGenre is clicked)
        lbl2 = Tkinter.Label(self.window, text = "Select Category:", bg = color1, fg = color2)
        lbl2.grid(column = 5, row = 1)
        self.catBox = Tkinter.Listbox(self.window, highlightbackground = color1, exportselection = False)
        self.catBox.grid(column = 5, row = 2)
        
       #populates genreBox with data from genres.txt
        f = open("genres.txt")
        lines = f.readlines()
        f.close()
        
        self.genres = []
        for i in range(len(lines)):
            line = lines[i]
            self.genreBox.insert(i,line[:-1])
            self.genres.insert(i, line[:-1])
       # print self.genres
        
    
    #def getHome - goes to home screen
    #@param: none
    #@return: none
    def getHome(self):
        self.window.withdraw()
        self.home = Tkinter.Toplevel(self.window)
        goHome = HomeScreen(self.home)
        
    
    #def classics - starts a classic game
    #@param: none
    #@return: none
    def classic(self):
        self.window.withdraw()
        self.game =Tkinter.Toplevel(self.window)
        goStart = GameBoard(self.game)
        
    #def goGenre - goes to genre select screen
    #@param: none
    #@return: none
    def goGenre(self):
        self.window.withdraw()
        self.game = Tkinter.Toplevel(self.window)
        goTo = Genre(self.game)
        
    #def goBack - goes to Import screen
    #@param: none
    #@return: none
    def goBack(self):
        self.window.withdraw()
        self.screen = Tkinter.Toplevel(self.window)
        back = Import(self.screen)
      
    #def menuBrr - generates the Menu Bar for the Import Screen
    #@param: none
    #@return: none
    def menuBrr(self):
        #generate menubar
        self.menuBar = Tkinter.Menu(self.window)
        
        #helpmenu
        self.helpMenu = Tkinter.Menu(self.menuBar)
        self.helpMenu.add_command(label = "Manual", command = getInstructions)
        self.menuBar.add_cascade(label="Help",menu=self.helpMenu)
        
        #navigation menu
        self.navigationMenu= Tkinter.Menu(self.menuBar)
        self.navigationMenu.add_command(label = "Home", command = self.getHome)
        
        #if in a specific import screen
        if self.specific == True:
            self.navigationMenu.add_command(label = "Back", command = self.goBack)
        
        self.navigationMenu.add_command(label = "Start Classic Game", command = self.classic)
        self.navigationMenu.add_command(label = "Start Game by Genre", command = self.goGenre)
        self.navigationMenu.add_command(label = "Quit", command = quitProgram)
        self.menuBar.add_cascade(label ="Navigate",menu = self.navigationMenu)
        
        self.window.configure(menu=self.menuBar)
    
        
    #def __init__ - constructor
    #@param: window (Tkinter Object)
    #@return: none
    def __init__(self,window):
        
        #configure window
        self.window = window
        self.window.geometry("1050x500+150+90")
        self.window.resizable(False, False)
        self.window.configure(bg = color1)
        self.window.title("Importing")

        
        self.entered = []
        self.specific = False
   
        #Import File Button
        self.fromFile = Tkinter.Button(self.window, text = "Import File", highlightbackground = color1, command = self.getFile)
        self.fromFile.grid(column = 2, row = 2)
        
        #Import Questions button
        self.byQuestion = Tkinter.Button(self.window, text = "Import Questions", highlightbackground = color1, command = self.getGenres)
        self.byQuestion.grid(column = 2, row = 3)
        
        self.menuBrr()


class Genre(object):
    
    #def startGame - goes to GameBoard to start game
    #@param: newGenre (str)
    #@return: none
    def startGame(self, newGenre):
        global genre
        #print newGenre
        #the game genre = the selected genre
        genre = newGenre
        
        #Withdraws window + goes to GameBoard
        self.window.withdraw()
        self.begin = Tkinter.Toplevel(self.window)
        startJeopardy = GameBoard(self.begin)
        
    #def getHome - goes to home screen
    #@param: none
    #@return: none
    def getHome(self):
        self.window.withdraw()
        self.home = Tkinter.Toplevel(self.window)
        goHome = HomeScreen(self.home)
    
    #def classic - starts a classic game
    #@param: none
    #@return: none
    def classic(self):
        self.window.withdraw()
        self.game =Tkinter.Toplevel(self.window)
        goStart = GameBoard(self.game)
        
    #def __init__ - contructor
    #@param: window (Tkinter Object)
    #@return: none
    def __init__(self,window):
        
        #configure window
        self.window = window
        self.window.title("Genre")
        self.window.configure(bg = color1)
        self.window.geometry("1050x500+150+90")
        self.window.resizable(False, False)

        
        numCats = []
        genres = []
        new = []
        
        #opens genre file
        f = open("genres.txt")
        lines = f.readlines()
        f.close()
        
        #gets data from genre File
        f = open("genres.txt")
        for i in range(len(lines)):
            options = f.readline()
            options = options[:-1]
            genres.append(options)
            #ommand = lambda index = [valuePos,j,len(self.buttons)]:self.newWindow(index) 
        f.close()
        
        #opens general File + gets genre data
        f = open("general.txt")
        lines2 = f.readlines()
        f.close()
        
        possibleGens = []
        numCats = []
        
        
        for j in range(len(genres)):
            current = genres[j]
            f = open("general.txt")
            for i in range(len(lines2)):
                line = f.readline()
                line = line.split("         ")
                #print line
                if i > 0 and line[0] != "":
                    #if the category is not already in numCats and the genre  = current 
                    if (line[1] in numCats) == False and (line[0] == current):
                        numCats.append(line[1])
            f.close()
            #if there are at least 13 categories for the current genre, add genre to possibilities list
            if len(numCats) >= 13 and (current in new) == False:
                new.append(current)
          #  print numCats
            numCats = []
    
        
        #for all the possible genres, create a button
        for i in range(len(new)):
            #if there are more than 65 
           # total = numCats.count(genres[i])
           # if total >= 65:
            button = Tkinter.Button(self.window,text = new[i], highlightbackground = color1, command = lambda newGenre = new[i]: self.startGame(newGenre))
            button.pack() #(row = i, column = 2)
        
        #generate All button
        btn = Tkinter.Button(self.window, text = "All", highlightbackground = color1, command = lambda:self.startGame("All"))
        btn.pack() #(row = len(new), column = 2)
        
        #generate menubar
        self.menuBar = Tkinter.Menu(self.window)
        
        #help menu
        self.helpMenu = Tkinter.Menu(self.menuBar)
        self.helpMenu.add_command(label = "Manual", command = getInstructions)
        self.menuBar.add_cascade(label="Help",menu=self.helpMenu)
        
        #navigation menu
        self.navigationMenu= Tkinter.Menu(self.menuBar)
        self.navigationMenu.add_command(label = "Home", command = self.getHome)
        
        #self.navigationMenu.add_command(label = "Back", command = self.goBack)
        self.navigationMenu.add_command(label = "Start Classic Game", command = self.classic)
        self.navigationMenu.add_command(label = "Quit", command = quitProgram)
        self.menuBar.add_cascade(label ="Navigate",menu = self.navigationMenu)
        
        self.window.configure(menu=self.menuBar)


class GameBoard(object):
    
    #def newWindow: goes to correct screen based on question
    #@param: index (lst of integers)
    #@return: none
    def newWindow(self,index):
        global dailyDouble, jeopardyScore, score
        
        
        val = index[0]
        start = index[1]
        btnIndex = index[2]
        
        #setting variables 
        question = self.selectedQs[start]
        answer = self.selectedAs[start]
        value =  self.values[val]
        cat = self.selectedCats[btnIndex/5]
        btn = self.buttons[btnIndex]
        
        self.new_window = Tkinter.Toplevel(window)
        
        #disables the button that was clicked
        btn.configure(state = "disabled")
        
        
        self.disabled = self.disabled + 1
        
        #if 3 questions have been clicked, withdraw the current Jeopardy screen
        if self.disabled == answerNum:
            self.window.withdraw()
        
        
        #if doubleJeopardy is True (multiple daily Double values)
        if doubleJeopardy == True:
           # self.dailyDouble.append(-1)
           
           #if selected question is a daily double, go to Wager screen
            if (start in self.dailyDouble) == True:
                dailyDouble = True
                self.new_window = Wager(self.new_window,btn,question,answer,value,cat,self.playerScore,self.disabled)
            
            #if selected question is normal, go to Answer Screen
            else:
                self.window2 = AnswerScreen(self.new_window,question,answer,value,self.playerScore,self.disabled)
        
        #if it's normal jeopardy (1 daily double)
        else:
            #if the selected question is daily double, go to Wager Screen
            if start == self.dailyDouble: #or (start in self.dailyDouble) == True:
                dailyDouble = True
                self.new_window = Wager(self.new_window,btn,question,answer,value,cat,self.playerScore,self.disabled)
        
            #if the selected question is normal, go to Answer Screen
            else:
                self.window2 = AnswerScreen(self.new_window,question,answer,value,self.playerScore,self.disabled)
        #self.playerScore.configure(text = score)

    #def getInstructions - opens manual
    #@param: none
    #@return: none
    def getInstructions():
        #generate Scores window
        newWindow = Tkinter.Tk()
        newWindow.title("User Guide")
    
    
        #configure text
        self.text = Tkinter.Text(newWindow, font = "Monaco 16")
        self.text.pack(side="top")
        
        #open file
        self.text.insert("end", open("manual.txt").read())
        
    #def new - starts a new game
    #@param: none
    #@return: none
    def new(self):
        global genre, doubleJeopardy, score
        global finalJeopardy, finalJeopardyStuff, dailyDouble,jeopardyCats
        self.window.withdraw()
        #reset all global variables to original values
        genre = "All"
        doubleJeopardy = False 
        score = 0
        finalJeopardyStuff = None
        finalJeopardy = False
        dailyDouble = False
        jeopardyCats = []
        
        #generate new GameBoard
        self.home = Tkinter.Toplevel(self.window)
        newGame = GameBoard(self.home)
        
    #def restart - restarts current game from current round (jeopardy/double jeopardy)
    #@param: none
    #@return: none
    def restart(self):
        global doubleJeopardy, jeopardyScore
        
        #if doubleJeopardy is true, set score to score at end of Jeopardy
        if doubleJeopardy == True:
            self.playerScore.configure(text = "$" + str(jeopardyScore))
            
        #otherwise, set score to 0
        else:
            self.playerScore.configure(text = "$0")
        
        #change the state of all buttons to "normal" + reset disabled
        self.disabled = 0
        for i in range(len(self.buttons)):
            self.buttons[i].configure(state = "normal")
        
                
            
        
    #def getHome - goes to home screen
    #@param: none
    #@return: none
    def getHome(self):
        self.window.withdraw()
        self.begin = Tkinter.Toplevel(self.window)
        window = HomeScreen(self.begin)
    
    
    #def seeScores - view scores
    #@param: none
    #@return: none
    def seeScores(self):

        #generate Scores window
        newWindow = Tkinter.Tk()
        newWindow.title("Scores")
 
        #self.button = Tkinter.Button(newWindow, text="QUIT", command=newWindow.quit)
        #self.button.pack(side="bottom")
        #For specific file: !!Need double slash between each!
        #dir = '//Users//kcardinale//Google Drive//ICS4U//1-4U_Programs_16-17//Unit 4'
        
        #configure text
        self.text = Tkinter.Text(newWindow, font = "Monaco 16")
        self.text.pack(side="top")
        
        #open file
        self.text.insert("end", open("highScore.txt").read())
    

    #def __init__ - constructor
    #@param: window (Tkinter Object)
    #@return: none
    def __init__(self,window):

        global genre
        global score
        global jeopardyCats
        global doubleJeopardy
        global finalJeopardyStuff, finalJeopardy, allowRestart
        
        #configure window
        self.window = window
        self.window.geometry("1050x275+150+80")
        self.window.resizable(False, False)
        self.window.configure(bg = color1)
       # self.window.protocol('WM_DELETE_WINDOW', dontquit)
        
        
        #set window title based on game mode
        if doubleJeopardy == True:    
            self.window.title("Double Jeopardy!")
        else:
            self.window.title("Jeopardy!")

        
        self.categories = []
        category = []
        self.questions = []
        self.answers = []
        cats = []
        qs = []
        ans = []

        #For classic jeopardy (all genres)
        if genre == "general.txt" or genre == None or genre == "All":
            genre = "general.txt"

        #If a specific genre was selected
        else:
            if doubleJeopardy == False:
                genre = genre.lower() + ".txt"
        
        f = open(genre)
        
        lines = f.readlines()
        f.close()
        
        #open genre file
        f = open(genre)
        for i in range(len(lines)):
            line = f.readline()
            col = line.split("         ")
            col[3] = col[3].split("\n")
            col[3] = col[3][0]
            
            #if the column is not a header
            if col[0] != "Genre":
                #add the current category, question, and answer to the corresponding lists 
                cats.append(col[1])
                self.questions.append(col[2])
                self.answers.append(col[3])

        f.close()
        
        #compressing the # of categories by removing repeats + populating self.cateogires and category
        for i in range(len(cats)):
            
            #if the category does not already exist in the lists
            if (cats[i] in category) == False and (cats[i] in jeopardyCats) == False:
                #self.categories.append(cats[i])
                num = cats.count(cats[i])
                
                #stores the name of the category
                category.append(cats[i])
                
                #stores the name of the category + how many questions are in that category
                self.categories.append([cats[i],num])
                
                #add all the questions in the category + the corresponding answer to the correct lists
                for j in range(i,(i+num)):
                    qs.append(self.questions[j])
                    ans.append(self.answers[j])
            else:
                continue

        
        #for i in range(len(self.categories)):
            
            
        
        self.selectedCats = []
        possibleQs = []
        possibleAs = []
        self.selectedQs = []
        self.selectedAs = []
        
        
        #populate self.selectedCats (categories that will be used in the current game) with 6 categories
        while len(self.selectedCats) <= 5:
            
            #randomely select a category from self.categories
            num = random.randint(0,len(self.categories)-1)
            selected = self.categories[num]
            
            #if the category was not already selected
            if (selected in self.selectedCats) == False:
                start = 0
                
                #figure out the starting index + ending index positions of the questions corresponding
                #with the current category in the lists qs and as
                for j in range(num):
                    start = start + (self.categories[j][1])
                
                #add category to self.selectedCats
                self.selectedCats.append(selected)
                
                #add the corresponding questions + answers to possibleQs and possibleAs
                for i in range(start,start+selected[1]):
                    possibleQs.append(qs[i])
                    possibleAs.append(ans[i])
        
        #for i in range(len(possibleQs)):
         #   print i, possibleQs[i]
        
        #Select 5 questions from each of the selected category for the current game
        for i in range(len(self.selectedCats)):
            cat = self.selectedCats[i]

            #find the starting index for the questions&answers corresponding to the current category in possibleQs & possibleAs
            start = 0
            for k in range(i):
                start = (start + self.selectedCats[k][1])
            added = 0


            nums = []
            #print self.selectedQs
            
            #Until 5 questions have been selected for this category 
            while added < 5:

                #absolute = abs((start+cat[1])-start)
                #print absolute
                
                
                #if the last index position for the questions in the category is greater than the last possible index pos in possibleQs,
                
                if start+cat[1] > len(possibleQs)-1: #or abs((cat[1]+start) - start) == 1:
                    #randomize a number from start index to the last possible index in the list
                    num = random.randint(start,len(possibleQs)-1)
                
                #Otherwise, 
                else:
                    #randomize from start index to the (start index + the # of possible questions for the category)
                    num = random.randint(start,start+(cat[1]-1))

                nums.append(num)
        
                #if the same number has been randomely generated more than 3 times
                if nums.count(num) > 3:
                    
                    #if (start index + # of possible questions) is less than or equal to the last possible index pos
                    if start+cat[1] <= len(possibleQs)-1:

                        #the range is from start to the (# of possible qs + 1)
                        rangee =  start+(cat[1]+1)
                        
                    #otherwise, 
                    else:
                        #the range is from start to the lenght of possibleQs
                        rangee = start + len(possibleQs)
                        
                    #go through all the possible questions for the category
                    for k in range(start,rangee):
                        
                        #if the question has not been selected yet
                        if (possibleQs[k] in self.selectedQs) == False:
                            #append the question + correct answer to the corresponding lists
                            self.selectedQs.append(possibleQs[k])
                            self.selectedAs.append(possibleAs[k])
                            added = added + 1
                            nums = []
                            break    
                    
                    
                #if the randomely selected question has already been selected
                elif (possibleQs[num] in self.selectedQs) == True:
                    continue

                #if it has not been selected, add the question + answer to the corresponding lists
                else:
                    self.selectedQs.append(possibleQs[num])
                    self.selectedAs.append(possibleAs[num])
                    added = added + 1

        
        #if the board is being generated for Double Jeopardy
        if doubleJeopardy == True:
            
            #double Jeopardy Values
            self.values = ["$400","$800","$1200","$1600","$2000"]
            
            self.dailyDouble = []
            
            #randomely generate 2 daily doubles
            while len(self.dailyDouble) < 2:
                num = random.randint(0,len(self.selectedQs)-1)
                
                #if this daily double location has not already been selected
                if (num in self.dailyDouble) == False:
                    self.dailyDouble.append(num)
                    
            #Set up for Final Jeopardy
            
            finalCats = []
            finalQs = []
            finalAs = []
            possibleFinal = []
            
            #Append all imported categories to possibleFinal jeopardy categories
            for i in range(len(cats)):
                possibleFinal.append(cats[i])
            
            #Append all the selected double Jeopardy categories (w/o # of questions) to jeopardy Cats
            for j in range(len(self.selectedCats)):
                jeopardyCats.append(self.selectedCats[j][0])
                

            for i in range(len(possibleFinal)):
                #if the possibleFinal category has not already been used in jeopardy and doublejeopardy
                if (possibleFinal[i] in jeopardyCats) == False:
                    
                    #add it to finalCats
                    finalCats.append(possibleFinal[i])
            
            #randomely select the final jeopardy category out of the possibilities in finalCats
            num = random.randint(0,len(finalCats)-1)
            finalCat = finalCats[num]
            
            #open + read the genre file
            f = open(genre)
            for i in range(len(lines)):
                line = f.readline()
                line = line.split("         ")
                
                #if the current category is the final jeopardy category
                if line[1] == finalCat:
                    #add the question + answer from this line to the corresponding lists
                    finalQs.append(line[2])
                    finalAs.append(line[3])
                    
     
            #randomely select a final jeopardy question from the possible questions
            num = random.randint(0,len(finalQs)-1)
            finalQ = finalQs[num]
            finalA = finalAs[num]
            
            finalJeopardyStuff = [finalCat,finalQ,finalA]
        

            
        
        #for regular Jeopardy
        else:
            #regular values
            self.values = ["$200","$400","$600","$800","$1000"]
            
            #randomely generate 1 daily double 
            self.dailyDouble = random.randint(0,len(self.selectedQs)-1)
            
            #Add the selected categories for this round to jeopardyCats
            for i in range(len(self.selectedCats)):
                jeopardyCats.append(self.selectedCats[i][0])
                
            
       # print self.selectedCats
       # print self.selectedQs
       
        #Populate Window
        
        #title
        self.title = Tkinter.Label(window,text = "Jeopardy!",bg = color1,fg = color2)
        self.title.grid(row = 0, column = 0)
        
        #Score label
        showScore = "$" + str(score)
        self.playerScore = Tkinter.Label(window,text = showScore,bg = color1,fg = color2)
        self.playerScore.grid(row = 0, column = 5)
    
        #generate the gameboard
        self.buttons = []
        self.disabled = 0
        for i in range(0,6):
            
            #create a label for the category
            self.cat = self.selectedCats[i]
            self.lbl = Tkinter.Label(window,text = self.cat[0],bg = color1,fg = color2)
            self.lbl.grid(column = i, row = 1)
            valuePos = 0
            start = i*5
            
            #Generate buttons for each question under the category
            for j in range(start,((start)+5)):
                val = self.values[valuePos]
                btn = Tkinter.Button(window,text = val, state = "normal", width = 16, highlightbackground = color1, command = lambda index = [valuePos,j,len(self.buttons)]:self.newWindow(index))
                btn.grid(column = i, row = valuePos+2)
                self.buttons.append(btn)
                valuePos = valuePos + 1
                
        #Generate Menubar
        self.menuBar = Tkinter.Menu(self.window)
        
        #game menu
        self.gameMenu = Tkinter.Menu(self.menuBar)
        
        #if restarting a game is allowed, show this menu option

        if allowRestart == True:
            self.gameMenu.add_command(label = "Restart Round", command = self.restart)
            
        self.gameMenu.add_command(label = "New Game", command = self.new)
        self.gameMenu.add_command(label = "View Scores", command = self.seeScores)
        
        #help menu
        self.helpMenu = Tkinter.Menu(self.menuBar)
        self.helpMenu.add_command(label = "Manual", command = getInstructions)
        
        #navigation menu
        self.navigationMenu= Tkinter.Menu(self.menuBar)
        self.navigationMenu.add_command(label = "Home", command = self.getHome)
        self.navigationMenu.add_command(label = "Quit", command = quitProgram)
        
        self.menuBar.add_cascade(label="Help",menu=self.helpMenu)
        self.menuBar.add_cascade(label="Game Options",menu=self.gameMenu)
        self.menuBar.add_cascade(label ="Navigate",menu = self.navigationMenu)
        
        self.window.configure(menu=self.menuBar)
            

class EndScreen(object):
    
    #def seeScores - open window to see saved scores
    #@param: none
    #@return: none
    def seeScores(self):
 
        #generate window
        newWindow = Tkinter.Tk()
        newWindow.title("Scores")
 
        #self.button = Tkinter.Button(newWindow, text="QUIT", command=newWindow.quit)
        #self.button.pack(side="bottom")
        #For specific file: !!Need double slash between each!
        #dir = '//Users//kcardinale//Google Drive//ICS4U//1-4U_Programs_16-17//Unit 4'
        
        #configure text + open scores file
        self.text = Tkinter.Text(newWindow, font = "Monaco 16")
        self.text.pack(side="top")
        self.text.insert("end", open("highScore.txt").read())
    
    #def finale - quit game
    #@param: none
    #@return: none
    def finale(self):
        print "Thanks for playing!"
        quitProgram()
        

    #def getHome - goes to home screen (not in use)
    #@param: none
    #@return: none
    def getHome(self):
        
        
        self.begin = Tkinter.Toplevel(self.window)
        window = HomeScreen(self.begin)
    
    #def new - starts a new game
    #@param: none
    #@return: none
    def new(self):
        global genre, doubleJeopardy, score
        global finalJeopardy, finalJeopardyStuff, dailyDouble,jeopardyCats
        
        #if the score has not been recorded
        if self.added == False:
            self.addScore()
            
        self.window.withdraw()
        #reset all global variables to original values
        genre = "All"
        doubleJeopardy = False 
        score = 0
        finalJeopardyStuff = None
        finalJeopardy = False
        dailyDouble = False
        jeopardyCats = []
        
        #generate new GameBoard
        self.home = Tkinter.Toplevel(self.window)
        newGame = GameBoard(self.home)
    
    
    #def seeScores - view scores
    #@param: none
    #@return: none
    def seeScores(self):

        #generate Scores window
        newWindow = Tkinter.Tk()
        newWindow.title("Scores")
 
        #self.button = Tkinter.Button(newWindow, text="QUIT", command=newWindow.quit)
        #self.button.pack(side="bottom")
        #For specific file: !!Need double slash between each!
        #dir = '//Users//kcardinale//Google Drive//ICS4U//1-4U_Programs_16-17//Unit 4'
        
        #configure text
        self.text = Tkinter.Text(newWindow, font = "Monaco 16")
        self.text.pack(side="top")
        
        #open file
        self.text.insert("end", open("highScore.txt").read())
        
        
    #def addScore - add score to high scores file
    #@param: none
    #@return: none
    def addScore(self):
        global score
        
        #get name from entry box
        yourName = self.lbl2.get()
        
        #clear entry box
        self.lbl2.delete(0, "end")
        self.added =True
        
        #if nothing was entered, name = N/A
        if yourName == "":
            yourName = "N/A"
        
        #line = yourName + "         " + "$" + str(score) + "\n"
        
        #open high scores fie
        f = open("highScore.txt")
        lines = f.readlines()
        f.close()
        
        #you = [score,yourName]
        #data = [you]
        names = []
        scores = []
        
        #get data from highScores file
        f = open("highScore.txt")
        for i in range(len(lines)):
            line = f.readline()
            line = line.split("         ")
            
            #if line is not a header
            if line[0] != "Rank":
                #data.append([line[2],line[1]])
                
                #append name (line[1]) to names list
                names.append(line[1])
                dollarSign = line[2].split("$")
                newLine = dollarSign[1].split("\n")
                
                #append the person's score as an integer to scores
                scores.append(int(newLine[0]))
        f.close()
        
        #add the current player's name + score to the lists
        scores.append(score)
        names.append(yourName)
        
        #sort scores list based on score (descending order),
        #sort names list simultaneously to ensure scores remain with correct user
        for index in range(1,len(scores)):
        
            currentvalue = scores[index]
            currentName = names[index]
            position = index
        
            while position>0 and scores[position-1]<currentvalue:
                scores[position]=scores[position-1]
                names[position] = names[position-1]
                position = position-1
        
            scores[position]=currentvalue
            names[position] = currentName
        
        #print scores
        #print names

        #USE a sorting algorithm + work with 3 lists at once??
        
        #f.write(line)
        
        #data.sort()
        
        
        
        
        #Update high score file
        f = open("highScore.txt","w")
        f.write("Rank         Name         Score\n")
        
        #if the # of scores in scores is greater than or equal to 100,
        #length = 100 (100 rankings will be put in file)
        if len(scores) >= 100:
            length = 100
            
            #if the player's score was less than the 100th rank, they are not placed
            if score < scores[length-1]:
                print "You did not rank."
                
        #if the # of scores in scores is less than 100,
        #length = the # of scores there are
        else:
            length = len(scores)
    
        #write updated rankings to file
        for i in range(length):
            line = str(i+1) + "         " + names[i] + "         " + "$" + str(scores[i]) + "\n"
            f.write(line)
        f.close()
        
        
        #remove entry box + submit button from window
        self.lbl1.pack_forget()
        self.lbl2.pack_forget()
        self.submit.pack_forget()
        
        #homeScreen button
        self.homeScreen = Tkinter.Button(self.window, text = "Home Screen", highlightbackground = color1, command = self.toHome)#HomeScreen(self.home)
        self.homeScreen.pack()
        
        #generate View Scores button
        self.lbl2 = Tkinter.Button(self.window, text = "View Scores", command = self.seeScores, highlightbackground = color1)
        self.lbl2.pack()
        
        #quit button
        self.quit= Tkinter.Button(self.window, text = "Quit", command = self.finale, highlightbackground = color1)
        self.quit.pack()
        
        
        
    #def toHome - to homeScreen 
    #@param: none
    #@return: none
    def toHome(self):
        global genre, doubleJeopardy, score
        global finalJeopardy, finalJeopardyStuff, dailyDouble,jeopardyCats
        
        #if the score has not been recorded
        if self.added == False:
            self.addScore()
        self.window.withdraw()
        
        #reset all jeopardy values
        genre = "All"
        doubleJeopardy = False 
        score = 0
        finalJeopardyStuff = None
        finalJeopardy = False
        dailyDouble = False
        jeopardyCats = []
        
        #go to home screen
        self.home = Tkinter.Toplevel(self.window)
        home = HomeScreen(self.home)
    
    #def goAway - when user clicks quit on menu bar, makes sure score has been ranked then quits
    #@param: none
    #@return: none
    def goAway(self):
        
        #if the score has not been recorded
        if self.added == False:
            self.addScore()
        self.window.withdraw()
        quitProgram()
    
    
    #def __init__ - constructor
    #@param: window (Tkinter Object), score (int)
    #@return: none
    def __init__(self,window,score):
        
        #configure window
        self.window = window
        self.window.configure(bg = color1)
        self.window.geometry("1080x600+150+80")
        self.window.resizable(False, False)
        
        #Attributes
        
        self.score = score
        self.added = False
        
        #Final Score label
        self.lbl = Tkinter.Label(self.window,text = "Your Final Score:$" + str(self.score), bg = color1, fg = color2)
        self.lbl.pack()
        
        #text = "If you would like to add save your score, enter your name. Otherwise, press Continue",
        
        #instructions for saving rankings
        self.lbl1 = Tkinter.Label(self.window, text = "Enter your name to save your ranking")
        self.lbl1.pack()
        
        #enter + save name+ranking
        self.lbl2 = Tkinter.Entry(self.window, highlightbackground = color1)
        self.lbl2.pack()
        self.submit = Tkinter.Button(self.window, text = "Continue", command = lambda:self.addScore(), highlightbackground = color1)
        self.submit.pack()
        
        #Generate Menubar
        self.menuBar = Tkinter.Menu(self.window)
        
        #game menu
        self.gameMenu = Tkinter.Menu(self.menuBar)
        
            
        self.gameMenu.add_command(label = "New Game", command = self.new)
        self.gameMenu.add_command(label = "View Scores", command = self.seeScores)
        
        #help menu
        self.helpMenu = Tkinter.Menu(self.menuBar)
        self.helpMenu.add_command(label = "Manual", command = getInstructions)
        
        #navigation menu
        self.navigationMenu= Tkinter.Menu(self.menuBar)
        self.navigationMenu.add_command(label = "Home", command = self.toHome)
        self.navigationMenu.add_command(label = "Quit", command = self.goAway)
        
        self.menuBar.add_cascade(label="Help",menu=self.helpMenu)
        self.menuBar.add_cascade(label="Game Options",menu= self.gameMenu)
        self.menuBar.add_cascade(label ="Navigate",menu = self.navigationMenu)
        
        
        self.window.configure(menu=self.menuBar)
        
        #self.window.withdraw()
        #self.home = Tkinter.Toplevel(self.window)
        
        #homeScreen button
        #self.homeScreen = Tkinter.Button(self.window, text = "Home Screen", highlightbackground = color1, command = self.toHome)#HomeScreen(self.home)
        #self.homeScreen.pack()
    
#Question class not in use
#Generates a window that outputs question + gives user option to Pass or Answer
#If Answer - go to Answer, if Pass - returns to window 
#class QuestionScreen(object):
#
#    def back(self):
#        global name
#        self.window2.withdraw()
#        #self.goHome = Tkinter.Toplevel(self.window)
#        #self.window = name
#    
#    def goAnswer(self):
#        #newWindow other
#        self.window2.withdraw()
#        self.toAnswer = Tkinter.Toplevel(self.window2)
#        self.window2 = AnswerScreen(self.toAnswer,self.question,self.correct,self.val,self.playerScore)
#    
#    def __init__(self,window2,btn,question,correct,val,playerScore):
#        self.question = question
#        self.correct = correct
#        self.btn = btn
#        self.val = val
#        self.window2 = window2
#        self.window2.title("Question!")
#        self.window2.configure(bg = color1)
#        self.playerScore= playerScore
#        self.window.geometry("1080x600+150+80")
#        self.window.resizable(False, False)
#        
#        question = Tkinter.Label(window2,text = self.question,bg = color1, fg = color2)
#        question.grid(column = 2, row = 0)
#        value = Tkinter.Label(window2,text =self.val, bg = color1, fg = color2)
#        value.grid(column = 2, row = 1)
#        
#        passs = Tkinter.Button(window2,text = "Pass", command = self.back, highlightbackground = color1)
#        passs.grid(column = 2, row = 2)
#        #
#        answer = Tkinter.Button(window2,text = "Answer", command = self.goAnswer, highlightbackground = color1)
#        answer.grid(column = 2, row = 3)
    
class AnswerScreen(object):
    
    #def checkAnswer - check's player answer + takes appropriate action
    #@param: none
    #@return: none
    def checkAnswer(self):
        global score
        global dailyDouble
        global doubleJeopardy, jeopardyScore
        global finalJeopardyStuff, finalJeopardy
        
        #gets player answer
        answer = self.playerAnswer.get()
        answer= answer.lower()
        
        #correct answer
        self.correct = self.correct.lower()
        
        self.answerChecked = True
        
        #if the player has wagered
        if dailyDouble == True or finalJeopardy == True:
            #add = their wager
            add = self.val
        
        #for normal questions  
        else:
            #add = the question value
            add = int(self.val[1:])

        #if there are multiple correct answers
        if self.correct[0] == "[":
            self.correct = self.correct[1:]
            
            #split self.correct into a list
            lst = self.correct.split(", ")
            lst2= lst[len(lst)-1].split("]")
            lst[len(lst)-1] = lst2[0]

            #if the player's answer is one of the correct answers
            if (answer in lst) == True:
                
                    
                #add to player score
                score = score + add
                print "Correct\n"
            
            #if the answer is incorrect
            else:
                print "Incorrect"
                
                print "Acceptable Answers are:"
                
                #output the acceptalbe answers
                for i in range(len(lst)):
                    print "    ", lst[i]
                print ""
                #subtract from score
                score= score - add
        
        #if there is only one correct answer
        else:

            self.correct = self.correct.split("\n")
            self.correct = self.correct[0]
            
            #if the player's answer is correct
            if answer == self.correct:
                
                #add to their score
                score= score + add
                print "Correct\n"
            
            #if the player's answer is wrong
            else:
                print "Incorrect"
                print "The correct Answer is: ", self.correct
                print ""
                #take away from their score
                score= score - add
        
        #configure self.playerScore to show the updated score
        self.playerScore.configure(text = ("$" + str(score)))
        dailyDouble = False
        
        #if it is final Jeopardy, go to the end screen
        if finalJeopardy == True:
            self.window.withdraw()
            self.final = Tkinter.Toplevel(self.window)
            end = EndScreen(self.final,score)

        #if 3 questions have been selected 
        if self.disabled == answerNum:
            
            #if it is regular jeopardy
            if doubleJeopardy == False:
                jeopardyScore = score
                #begin double jeopardy
                doubleJeopardy = True
                self.window.withdraw()
                self.double = Tkinter.Toplevel(self.window)
                startDouble = GameBoard(self.double)
            
            #if it is double jeopardy
            elif finalJeopardy == False and doubleJeopardy == True:
                
                #begin final jeopardy
                finalJeopardy = True
                self.window.withdraw()
                self.final = Tkinter.Toplevel(self.window)
                startFinal = Wager(self.final,None,finalJeopardyStuff[1],finalJeopardyStuff[2],score,finalJeopardyStuff[0],self.playerScore,self.disabled)
                
        self.window.withdraw()
       # window.playerScore.configure(text = showScore)

    #def dontQuit - if the built-in quit button is clicked, go to killScreen
    #@param: none
    #@return: none
    def dontQuit(self):
        
        self.killScreen()
        self.killed = True
    
    #def killScreen - kill the current screen, take away from the score + go to the appropriate screen
    #@param: none
    #@return: none
    def killScreen(self):
        global score
        global dailyDouble
        global doubleJeopardy
        global finalJeopardyStuff, finalJeopardy
        
        #if time runs out before the answer has been submitted OR tries to quit the answer screen
        if self.answerChecked == False and self.killed == False:
            
            #if the player has wagered
            if dailyDouble == True or finalJeopardy == True:
                    add = self.val
            #otherwise
            else:
                add = int(self.val[1:])
                
            #subtract score
            score= score - add
            
            #configure score object on screen
            self.playerScore.configure(text = ("$" + str(score)))
            dailyDouble = False
            
            #if it is final jeopardy, go to end screen
            if finalJeopardy == True:
                self.window.withdraw()
                self.final = Tkinter.Toplevel(self.window)
                end = EndScreen(self.final,score)
    
            #if 3 questions have been selected
            if self.disabled == answerNum:
                
                #if it is regular jeopardy, start Double Jeopardy
                if doubleJeopardy == False:
                    doubleJeopardy = True
                    jeopardyScore = score
                    self.window.withdraw()
                    self.double = Tkinter.Toplevel(self.window)
                    startDouble = GameBoard(self.double)
                
                #if it is double jeopardy, go start Final jeopardy (go to Wager)
                else:
                    finalJeopardy = True
                    self.window.withdraw()
                    self.final = Tkinter.Toplevel(self.window)
                    startFinal = Wager(self.final,None,finalJeopardyStuff[1],finalJeopardyStuff[2],score,finalJeopardyStuff[0],self.playerScore,self.disabled)
        
                
                    
            self.window.withdraw()
            

            print "Too bad! Answer faster and don't try and quit next time!"
            print "The correct Answer is: ", self.correct
            print ""


    #def new - starts a new game
    #@param: none
    #@return: none
    def new(self):
        
        global genre, doubleJeopardy, score
        global finalJeopardy, finalJeopardyStuff, dailyDouble,jeopardyCats
        self.killed = True
        self.window.withdraw()
        #reset all global variables to original values
        genre = "All"
        doubleJeopardy = False 
        score = 0
        finalJeopardyStuff = None
        finalJeopardy = False
        dailyDouble = False
        jeopardyCats = []
        
        #generate new GameBoard
        self.home = Tkinter.Toplevel(self.window)
        newGame = GameBoard(self.home)
        
        
    #def getHome - goes to home screen
    #@param: none
    #@return: none
    def getHome(self):
        self.killed = True
        self.window.withdraw()
        self.begin = Tkinter.Toplevel(self.window)
        window = HomeScreen(self.begin)
    
    
    #def seeScores - view scores
    #@param: none
    #@return: none
    def seeScores(self):

        #generate Scores window
        newWindow = Tkinter.Tk()
        newWindow.title("Scores")
 
        
        #configure text
        self.text = Tkinter.Text(newWindow, font = "Monaco 16")
        self.text.pack(side="top")
        
        #open file
        self.text.insert("end", open("highScore.txt").read())
        
    #def __init__ - constructor
    #@param: window (Tkinter Object), question (str), correct = (str), val (int), playerScore (Tkinter Object), disabled (int)
    #@reutrn: none
    def __init__(self,window,question,correct,val,playerScore,disabled):
        global score, t
        
        #configure window
        self.window = window
        self.window.title("Answer!")
        self.window.geometry("1050x200+150+90")
        self.window.resizable(False, False)
        self.window.configure(bg = color1)
        
        #Attributes
        
        self.answerChecked = False
        self.killed = False
        
        self.question = question
        self.correct = correct
        self.val = val
        self.playerScore = playerScore
        self.disabled = disabled
        
        #Question Label
        question = Tkinter.Label(window,text = self.question, bg = color1, fg = color2, pady = 15, font = "Helvetica 14")
        question.grid(column = 2, row = 0)
        
        #Entry box for player answer
        self.playerAnswer = Tkinter.Entry(window, highlightbackground = color1)
        self.playerAnswer.grid(column = 2, row = 2)
        submit = Tkinter.Button(window, text = "Submit", command = self.checkAnswer,highlightbackground = color1)
        submit.grid(column = 2, row = 3)
        
        print "You have", t//1000, "seconds to answer"

        #after t milliseconds (time is up), go to self.killScreen
        if t > 0:
            self.window.after(t, self.killScreen)
        
        #If the built-in window quit button is clicked, go to self.dontQuit
        self.window.protocol('WM_DELETE_WINDOW', self.dontQuit)
        
        
        #Generate Menubar
        self.menuBar = Tkinter.Menu(self.window)
        
        #game menu
        self.gameMenu = Tkinter.Menu(self.menuBar)
        
        
        self.gameMenu.add_command(label = "New Game", command = self.new)
        self.gameMenu.add_command(label = "View Scores", command = self.seeScores)
        
        #help menu
        self.helpMenu = Tkinter.Menu(self.menuBar)
        self.helpMenu.add_command(label = "Manual", command = getInstructions)
        
        #navigation menu
        self.navigationMenu= Tkinter.Menu(self.menuBar)
        self.navigationMenu.add_command(label = "Home", command = self.getHome)
        self.navigationMenu.add_command(label = "Quit", command = quitProgram)
        
        self.menuBar.add_cascade(label="Help",menu=self.helpMenu)
        self.menuBar.add_cascade(label="Game Options",menu=self.gameMenu)
        self.menuBar.add_cascade(label ="Navigate",menu = self.navigationMenu)
        
        self.window.configure(menu=self.menuBar)
        
        
        
        #if t == 0:
        #    add = int(self.val[1:])
        #    score = score - add
        #    print "SCORE"
        #    self.playerScore.configure(text = ("$" + str(score)))
        #


#def getInstructions - opens manual
#@param: none
#@return: none
def getInstructions():
    #generate Scores window
    newWindow = Tkinter.Tk()
    newWindow.title("User Guide")


    #configure text
    text = Tkinter.Text(newWindow, font = "Monaco 16")
    text.pack(side="top")
    
    #open file
    text.insert("end", open("manual.txt").read())
        
#def getHome - goes to home screen
#@param: none
#@return: none
#def getHome():
#    toHome = HomeScreen(window)


#def quitProgram - quits program
#@param: none
#@return: none
def quitProgram():
    window.destroy()



#Generate Window
window = Tkinter.Tk()


#Menu bar
#menuBar = Tkinter.Menu(window)
#helpMenu = Tkinter.Menu(menuBar)
#helpMenu.add_command(label = "Manual", command = getInstructions)
#
#gameMenu = Tkinter.Menu(menuBar)
#gameMenu.add_command(label = "Quit", command = quitProgram)
#menuBar.add_cascade(label = "Game Options", menu = gameMenu)
#
#menuBar.add_cascade(label="Help",menu=helpMenu)
#window.configure(menu=menuBar)

#start game by going to home screen
startGame = HomeScreen(window)

window.mainloop()


