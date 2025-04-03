print('IMPORTING TKINTER...')
from tkinter import*
from tkinter import messagebox, ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory
###--THIS IS TO SAVE THE CONSOLE DATA
import sys
class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush() # If you want the output to be visible immediately
    def flush(self) :
        for f in self.files:
            f.flush()
f = open('_AppData_\\data\\_ConsoleData_.txt', 'w')
original = sys.stdout # ORIGINAL IS THE NAME OF THIS FUNC.
sys.stdout = Tee(sys.stdout, f)

print("======================CRACK-IT(STARTED SUCESSFULLY)========================")
print(" ")

# MAIN WINDOW IS CREATED HERE        
mainWin = Tk()
mainWin.title('CRACKIT')
mainWin.geometry('1250x620')
mainWin.overrideredirect(True)
###-IT COMES IN CENTER
window_height = 620
window_width = 1250
screen_width = mainWin.winfo_screenwidth()
screen_height = mainWin.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
mainWin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
icon = PhotoImage(file="_AppData_\\Icons\\Crack.png")
mainWin.tk.call('wm', 'iconphoto', mainWin._w, icon)
mainWin.attributes("-alpha", 0.0)

# LOADING/SPLASH WINDOW POPUPS
SplashWin = Toplevel(mainWin)
SplashWin.title("SPLASH")
SplashWin.configure(cursor="wait")
SplashWin.overrideredirect(True)
###-IT COMES IN CENTER
window_height = 350
window_width = 600
screen_width = SplashWin.winfo_screenwidth()
screen_height = SplashWin.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
SplashWin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
SplashWin.tk.call('wm', 'iconphoto', SplashWin._w, icon)

COL = '#0F1523' #191f26'
SplashWin.configure(background='black')
MainFrame = Frame(SplashWin, background=COL)
MainFrame.pack(fill=BOTH, expand=1)
PhotoHolder = Frame(MainFrame, background=COL) 
PhotoHolder.pack(side=TOP, fill=X)
SIROLogo = Frame(PhotoHolder, background=COL)
SIROLogo.pack(side=LEFT, fill=BOTH)
IconFrame = Frame(PhotoHolder, width=200, background=COL)
IconFrame.pack(side=LEFT, fill=X, expand=1)
LoadingFrame = Frame(SplashWin, height=5, background="black")
LoadingFrame.pack(side=BOTTOM, expand=1, fill=X, padx=2, pady=2)
CrackIT = PhotoImage(file='_AppData_\\Icons\\Crack.png')
WLogo = PhotoImage(file='_AppData_\\Icons\\WLogo.png')
ShowWaterMark = Label(SIROLogo, bg=COL, anchor='s', image=WLogo) 
PhotoLabel = Label(IconFrame, bg=COL, anchor='nw', image=CrackIT)
ShowWaterMark.pack(side=TOP, fill=Y, padx=10)
PhotoLabel.pack(side=LEFT, fill=X, padx=100, pady=50)
def AnimLoadBar():
    SplashWin.focus_force()
    Label1 = Label(LoadingFrame, width=9, bg='cyan')
    Label1.pack(side=LEFT)
    Label1.update()

## required to make window show before the program gets to the mainloop
SplashWin.focus_force()
SplashWin.update()

###--------IMPORTS
print('================================')
print('IMPORTING DATETIME...')
import datetime
from datetime import date, time
from datetime import datetime
import pygame
print('================================')
print('IMPORTING OS...')
import os
print('================================')
print('IMPORTING PANDAS...')
import pandas
import pandas as pd
print('================================')
print('IMPORTING MATPLOTLIB...')
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.pyplot as plt
print('================================')
print('IMPORTING PIL...')
from PIL import Image, ImageTk
print('================================')
print('IMPORTING RANDOM...')
import random
print('================================')
print('IMPORTING SHUTIL & SYS...')
import shutil
print('================================')
print('IMPORTING CSV WRITER...')
import csv
from csv import writer

AnimLoadBar() # AFTER IMPORTS COMPLETE LOADBAR UPDATE
ImpDirectory = ['_AppData_//', '_AppData_//chapters//', '_AppData_//data//', '_AppData_//gifs//', '_AppData_//Icons//', '_AppData_//questions//',
                '_AppData_//sounds//', '_AppData_//questions//physics//', '_AppData_//questions//chemistry//', '_AppData_//questions//maths//',
                '_AppData_//questions//custom']

ImageDirectory = ["_AppData_\\Icons\\Close_Dis.png", "_AppData_\\Icons\\Close_Hover.png", "_AppData_\\Icons\\Crack.png", "_AppData_\\Icons\\icon.png",
                  "_AppData_\\Icons\\phy.png", "_AppData_\\Icons\\chem.png", "_AppData_\\Icons\\math.png", "_AppData_\\Icons\\custom.png",
                  "_AppData_\\Icons\\phySel.png", "_AppData_\\Icons\\chemSel.png", "_AppData_\\Icons\\mathSel.png", "_AppData_\\Icons\\customSel.png",
                  "_AppData_\\Icons\\mute.png", "_AppData_\\Icons\\unmute.png", "_AppData_\\Icons\\AddQ.png", "_AppData_\\Icons\\AddQ2.png",
                  "_AppData_\\Icons\\AddChp.png", "_AppData_\\Icons\\AddChp2.png", "_AppData_\\Icons\\Analysis_Btn.png", "_AppData_\\Icons\\Analysis_BtnH.png",
                  "_AppData_\\Icons\\Open_Btn.png", "_AppData_\\Icons\\Open_BtnH.png", "_AppData_\\Icons\\Reset_Btn.png", "_AppData_\\Icons\\Reset_BtnH.png",
                  "_AppData_\\Icons\\Welcome_IMG.png", "_AppData_\\Icons\\Empty.png", "_AppData_\\Icons\\omrBtn.png", "_AppData_\\Icons\\omrBtn2.png",
                  "_AppData_\\Icons\\omrBtn_unanswered.png", "_AppData_\\Icons\\omrBtn_selected.png", "_AppData_\\Icons\\omrBtn_hover.png", "_AppData_\\Icons\\omrBtn_answered.png",
                  "_AppData_\\Icons\\omrBtn_answered_hover.png", "_AppData_\\Icons\\visited_unanwered.png", "_AppData_\\Icons\\visited_unanwered_hover.png",
                  "_AppData_\\Icons\\omrBtn_answered.png", "_AppData_\\Icons\\nextBTN.png", "_AppData_\\Icons\\nextBTNH.png",
                  "_AppData_\\Icons\\previousBTN.png", "_AppData_\\Icons\\previousBTNH.png", "_AppData_\\gifs\\optionbutton_one.gif",
                  "_AppData_\\gifs\\optionbutton_two.gif", "_AppData_\\gifs\\optionbutton_third.gif", "_AppData_\\gifs\\optionbutton_four.gif",
                  "_AppData_\\gifs\\end_test.gif", "_AppData_\\gifs\\resultLoad.gif"]

for check in range(len(ImpDirectory)):
    if not os.path.exists(ImpDirectory[check]):
        print('================================')
        print("!!! DIRECORY CREATED --> ", ImpDirectory[check])
        os.mkdir(ImpDirectory[check])
print('====================================================')
print("DIRECTORY CHECK COMPLETED")
ErrorIMG = [0]
for check2 in range(len(ImageDirectory)):
    if not os.path.exists(ImageDirectory[check2]):
        ErrorIMG[0] = 1
        print('================================')
        print("!!! FILE/IMAGE NOT FOUND --> ", ImageDirectory[check2])
print('====================================================')
print("IMAGE/FILE CHECK COMPLETED")
if ErrorIMG[0] == 1:
    resp = messagebox.askquestion('FATAL ERROR', 'Some files are missing are you sure to proceed?', icon='error')
    if resp == 'yes':
        SplashWin.focus_force()
        mainWin.focus_force()
        pass
    elif resp == 'no':
        mainWin.destroy()
del ImpDirectory
del ImageDirectory
del ErrorIMG
###--LISTS ARE HERE
print('==============================================')
print('CREATING LISTS...')
Tab_chk = [1]  ##---CHECKS FOR LEVEL
SubjSel = []
_getChpName_ = [] ###---SELECTED CHAPTER GOES HERE
zoom_chk = [0] ###---CHECK FULLSCREEN
phy = pandas.read_csv('_AppData_\\chapters\\physics_chapter.csv')
chem = pandas.read_csv('_AppData_\\chapters\\chemistry_chapter.csv')
math = pandas.read_csv('_AppData_\\chapters\\maths_chapter.csv')
custom = pandas.read_csv('_AppData_\\chapters\\custom_chapter.csv')
phy_chp = phy['CHAPTERS'].values.tolist()
chem_chp = chem['CHAPTERS'].values.tolist()
maths_chp = math['CHAPTERS'].values.tolist()
custom_chp = custom['CHAPTERS'].values.tolist()
phy_chp.sort()
chem_chp.sort()
maths_chp.sort()
custom_chp.sort()
checkROOT = [0]
totalQuestions = []
lblnames = []                          ##-------CHAPTER NAME LABEL ARE COLLECTED
selectnames = []                       ##-------BLUE LABELS ARE COLLECTED
glitchSol =[1, 0] ##---THIS IS TO SOLVE THE GLITCH OF HOVERING CHAPTER LABELS 
Vol = []
if os.path.exists('_AppData_\\data\\setting.csv'):
    sett = pandas.read_csv('_AppData_\\data\\setting.csv')
    Vol1 = sett['SETTING'].values.tolist()
    Vol.append(int(Vol1[0]))
else:
    Vol.append[1]

AnimLoadBar() # AFTER CREATING LISTS COMPLETE LOADBAR UPDATE
    
### - FUNCTION TO ADDING ELEMENTS IN LIST
def sumOfLists(list, size):
    if(size == 0): 
        return 0
    else: 
        return list[size - 1] + sumOfLists(list, size - 1)
    
###-TIME ON TITLE
checker = 0
def TimeTitle():
    d = str(setTime.get())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    setTime.set('CRACKIT - '+str(current_time))
    del Tab_chk[0:-2]
    if (checker == 0):
        mainWin.after(1000, TimeTitle)
###COLORS---HERE###
GuiControlColor = '#172134'
QuizControlColor = '#32375d'
###------------------------------> CSV FILE SAVING FUNCTION BELOW
def append_list_as_row(file_name, list_of_elem):
    # ---> Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # ----> Create a writer object from csv module
        csv_writer = writer(write_obj)
        # ----> Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
 
###SOUNDS---HERE###
        
pygame.mixer.init()
def play_click():
    if Vol[-1] == 1:
        pygame.mixer.music.load("_AppData_\\sounds\\btn_click05.mp3")
        pygame.mixer.music.play()

def play_whoosh():
    if Vol[-1] == 1:
        pygame.mixer.music.load("_AppData_\\sounds\\whoosh.mp3")
        pygame.mixer.music.play()
# WINDOW--EFFECTS HERE#
fd = [1.0]
def Fade_Out():
    no = fd[-1]-0.02
    fd.append(no)
    mainWin.attributes("-alpha", no)
    if fd[-1] >= 0.65:
        mainWin.after(4, Fade_Out)
    else:
        fd.clear()
        fd.append(1.0)
        
fd2 = [0.65]
def Fade_In():
    no = fd2[-1]+0.03
    fd2.append(no)
    mainWin.attributes("-alpha", no)
    if fd2[-1] <= 1.0:
        mainWin.after(1, Fade_In)
    else:
        fd2.clear()
        fd2.append(0.65)

AnimLoadBar() # AFTER CREATING WINDOW FUNCTIONS COMPLETE LOADBAR UPDATE

###IMAGES---HERE###
print('================================')
print('CHECKING IMAGES...')
Close_Dis = PhotoImage(file=("_AppData_\\Icons\\Close_Dis.png"))
Close_Hover = PhotoImage(file=("_AppData_\\Icons\\Close_Hover.png"))
Icon = PhotoImage(file=("_AppData_\\Icons\\icon.png"))
PhyImg = PhotoImage(file=("_AppData_\\Icons\\phy.png"))
ChemImg = PhotoImage(file=("_AppData_\\Icons\\chem.png"))
MathImg = PhotoImage(file=("_AppData_\\Icons\\math.png"))
CustomImg = PhotoImage(file=("_AppData_\\Icons\\custom.png"))
PhySel = PhotoImage(file=("_AppData_\\Icons\\phySel.png"))
ChemSel = PhotoImage(file=("_AppData_\\Icons\\chemSel.png"))
MathSel = PhotoImage(file=("_AppData_\\Icons\\mathSel.png"))
CustomSel = PhotoImage(file=("_AppData_\\Icons\\customSel.png"))
mute = PhotoImage(file=("_AppData_\\Icons\\mute.png"))
unmute = PhotoImage(file=("_AppData_\\Icons\\unmute.png"))
addQ =  PhotoImage(file=("_AppData_\\Icons\\AddQ.png"))
addQ2 =  PhotoImage(file=("_AppData_\\Icons\\AddQ2.png"))
addChp =  PhotoImage(file=("_AppData_\\Icons\\AddChp.png"))
addChp2 =  PhotoImage(file=("_AppData_\\Icons\\AddChp2.png"))
openAnalysis = PhotoImage(file=("_AppData_\\Icons\\Analysis_Btn.png"))
openAnalysis2 = PhotoImage(file=("_AppData_\\Icons\\Analysis_BtnH.png"))
Open_Btn = PhotoImage(file=("_AppData_\\Icons\\Open_Btn.png"))
H_Open = PhotoImage(file=("_AppData_\\Icons\\Open_BtnH.png"))
Reset_Btn = PhotoImage(file=("_AppData_\\Icons\\Reset_Btn.png"))
H_Reset = PhotoImage(file=("_AppData_\\Icons\\Reset_BtnH.png"))
Wel_Img = PhotoImage(file=("_AppData_\\Icons\\Welcome_IMG.png"))
empty_img = PhotoImage(file=("_AppData_\\Icons\\Empty.png"))
fullscreen = PhotoImage(file=("_AppData_\\Icons\\fullscreen.png"))
windowed = PhotoImage(file=("_AppData_\\Icons\\windowed.png"))

AnimLoadBar() # AFTER GETTING IMAGES COMPLETE LOADBAR UPDATE

####MAIN----FRAMESS####
GuiControl = Frame(mainWin, background=GuiControlColor, height=32)
GuiControl.pack(side=TOP, fill=X)
QuizControl = Frame(mainWin, background=QuizControlColor, height=590)
QuizControl.pack(fill=BOTH)
mainWin.configure(background=QuizControlColor)

print('================================')
print('CREATING ROOT...')  
# creating root 
root = Toplevel(mainWin) 
root.title('ADD QUESTIONS')
root.overrideredirect(True)
icon = PhotoImage(file="_AppData_\\Icons\\Crack.png")
root.tk.call('wm', 'iconphoto', root._w, icon)
###-IT COMES IN CENTER
window_height = 600
window_width = 900
screen_width = mainWin.winfo_screenwidth()
screen_height = mainWin.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
root.tk.call('wm', 'iconphoto', root._w, icon)
root.withdraw()
####INSIDE---FRAMES###
setTime = StringVar()
IconLabel = Label(GuiControl, bg=GuiControlColor, image=Icon)
IconLabel.grid(row=0, sticky=NW, pady=1, padx=1)
TitleLabel = Label(GuiControl, width=20, textvariable=setTime, bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
TitleLabel.grid(row=0, sticky=N, padx=474)
TimeTitle() 
def Close_In(event):
    CloseLabel.configure(image=Close_Hover, cursor='hand2')
def Close_Out(event):
    CloseLabel.configure(image=Close_Dis)
def Quit(event):
    print(" ")
    print("======================CRACK-IT(CLOSED SUCESSFULLY)========================")
    sys.stdout = original
    f.close()
    if Vol[-1] == 1:
        play_click()
    mainWin.destroy()
CloseLabel = Label(GuiControl, bg=GuiControlColor, image=Close_Dis)
CloseLabel.bind("<Enter>", Close_In)
CloseLabel.bind("<Leave>", Close_Out)
CloseLabel.bind("<Button-1>", Quit)
CloseLabel.grid(row=0, column=1, sticky=E, pady=1, padx=1)

AnimLoadBar() # AFTER CREATING TOPLEVEL AND FRAMES COMPLETE LOADBAR UPDATE

HoverCol1 = '#383e69'
def Level1_In(event):
    if Tab_chk[-1] != 1:
        Level1.configure(bg=HoverCol1, cursor='hand2')
def Level2_In(event):
    if Tab_chk[-1] != 2:
        Level2.configure(bg=HoverCol1, cursor='hand2')
def Level3_In(event):
    if Tab_chk[-1] != 3:
        Level3.configure(bg=HoverCol1, cursor='hand2')
def Level1_Out(event):
    if Tab_chk[-1] != 1:
        Level1.configure(bg='#1e213c')
def Level2_Out(event):
    if Tab_chk[-1] != 2:
        Level2.configure(bg='#1e213c')
def Level3_Out(event):
    if Tab_chk[-1] != 3:
        Level3.configure(bg='#1e213c')
def Lvl1Click(event):
    if Tab_chk[-1] != 1:
        if Vol[-1] == 1:
            play_click()
        Tab_chk.append(1)
        Level1.configure(bg=QuizControlColor)
        Level2.configure(bg='#1e213c')
        Level3.configure(bg='#1e213c')
def Lvl2Click(event):
    if Tab_chk[-1] != 2:
        if Vol[-1] == 1:
            play_click()
        Tab_chk.append(2)
        Level2.configure(bg=QuizControlColor)
        Level1.configure(bg='#1e213c')
        Level3.configure(bg='#1e213c')
def Lvl3Click(event):
    if Tab_chk[-1] != 3:
        if Vol[-1] == 1:
            play_click()
        Tab_chk.append(3)
        Level3.configure(bg=QuizControlColor)
        Level2.configure(bg='#1e213c')
        Level1.configure(bg='#1e213c')
def TurnOnOffSound(event):
    del Vol[0:-2]
    if Vol[-1] == 1:
        with open('_AppData_\\data\\setting.csv', 'w', newline='') as fl:
            row_con = ['SETTING']
            append_list_as_row('_AppData_\\data\\setting.csv', row_con)
            row_con2 = ['0']
            append_list_as_row('_AppData_\\data\\setting.csv', row_con2)
            fl.close()
        Vol.append(0)
        soundControl.configure(image=mute)
    elif Vol[-1] == 0:
        with open('_AppData_\\data\\setting.csv', 'w', newline='') as fl:
            row_con = ['SETTING']
            append_list_as_row('_AppData_\\data\\setting.csv', row_con)
            row_con2 = ['1']
            append_list_as_row('_AppData_\\data\\setting.csv', row_con2)
            fl.close()
        Vol.append(1)
        soundControl.configure(image=unmute)
def addQ_In(event):
    addQuestions.configure(cursor='hand2', image=addQ2)
def addQ_Out(event):
    addQuestions.configure(image=addQ)
def addChp_In(event):
    addChapters.configure(cursor='hand2', image=addChp2)
def addChp_Out(event):
    addChapters.configure(image=addChp)
def openGraph_In(event):
    checkAnalysis.configure(image=openAnalysis2)
def openGraph_Out(event):
    checkAnalysis.configure(image=openAnalysis)

OutlineFrames = []
def Back_Home():
    ChapterScroll.pack_forget()
    ChapterHolder.pack_forget()
    TabHolder.pack(fill=X)
    SubHolder.pack(fill=X)
    ChapterScroll.pack(fill=BOTH, expand=1)
    ChapterHolder.pack(fill=BOTH, expand=1)
    for i in range(len(OutlineFrames)):
        OutlineFrames[i].destroy()  
    SubjSel.clear()
    lblnames.clear()
    selectnames.clear()
    _getChpName_.clear()
    totalQuestions.clear()
    glitchSol.clear()
    OutlineFrames.clear()
    glitchSol.append(1)
    glitchSol.append(0)
    mainWin.attributes("-alpha", 0.0)
    mainWin.deiconify()
    play_whoosh()
    mainWin.after(200, Fade_In)
    
def Back_Home2(event):
    if len(SubjSel) != 0:
        Back_Home()
mainWin.bind("<Escape>", Back_Home2)
class Scrollable(Frame):
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            
        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL, width=12)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, height=620, bd=0, bg=QuizControlColor, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=TOP, fill=BOTH, expand=1)
        vscrollbar.config(command=canvas.yview)
        # reset the vie
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas, bg=QuizControlColor)
        interior_id = canvas.create_window(0, 0, window=interior,
                                        anchor=NW)
        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)
        def _bound_to_mousewheel(event):
            canvas.bind_all("<MouseWheel>", _on_mousewheel)   
        def _unbound_to_mousewheel(event):
            canvas.unbind_all("<MouseWheel>") 
        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        mainWin.bind('<Enter>', _bound_to_mousewheel)
        mainWin.bind('<Leave>', _unbound_to_mousewheel)

def OpenTracker(event):
    shadowWin = Toplevel(mainWin)
    shadowWin.configure(background="black")
    shadowWin.overrideredirect(True)
    ###-IT COMES IN CENTER
    window_height = 620
    window_width = 1250
    screen_width = shadowWin.winfo_screenwidth()
    screen_height = shadowWin.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    shadowWin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    shadowWin.attributes("-alpha", 0.8)
    shadowWin.focus_force()
    play_whoosh()
    allSelect = []
    for ak in range(len(phy_chp)):
        if os.path.exists('_AppData_\\questions\\physics\\'+str(phy_chp[ak])+'\\'):
            allSelect.append(str(phy_chp[ak]))

    for lk in range(len(chem_chp)):
        if os.path.exists('_AppData_\\questions\\chemistry\\'+str(chem_chp[lk])+'\\'):
            allSelect.append(str(chem_chp[lk]))

    for k in range(len(maths_chp)):
        if os.path.exists('_AppData_\\questions\\maths\\'+str(maths_chp[k])+'\\'):
            allSelect.append(str(maths_chp[k]))

    for bk in range(len(custom_chp)):
        if os.path.exists('_AppData_\\questions\\custom\\'+str(custom_chp[bk])+'\\'):
            allSelect.append(str(custom_chp[bk]))

    graphWin = Toplevel(mainWin)
    graphWin.title('TRACKER')
    graphWin.overrideredirect(True)
    graphWin.attributes("-alpha", 0.0)   
    window_height = 620
    window_width = 1000
    graphWin.geometry('%dx%d+%d+%d' % (1000, 620, 310, 74))
    graphWin.tk.call('wm', 'iconphoto', graphWin._w, icon)
    shadowWin.attributes("-alpha", 0.0)
    graphWin.attributes("-alpha", 0.0)
    graphWin.focus_force()
    
    def focuss():
        graphWin.focus_force()
        graphWin.after(10, focuss)
    #focuss()
    ####MAIN----FRAMESS####
    GuiControl = Frame(graphWin, background=GuiControlColor, height=32)
    GuiControl.pack(side=TOP, fill=X)
    QuizControl = Frame(graphWin, background=QuizControlColor, height=590)
    QuizControl.pack(side=TOP, fill=BOTH)
    NothingLabel = Label(graphWin, image=Wel_Img, background=QuizControlColor)
    NothingLabel.pack(side=TOP, fill=X, pady=120)
    graphWin.configure(background=QuizControlColor)

    fd1 = [1.0]
    def Fade_Out3():
        no = fd1[-1]-0.01
        fd1.append(no)
        shadowWin.attributes("-alpha", no)
        graphWin.attributes("-alpha", no)
        if fd1[-1] >= 0.65:
                graphWin.after(1, Fade_Out3)
        else:
            fd1.clear()
            fd1.append(1.0)
                
    fd22 = [0.0]
    def Fade_In3():
        graphWin.focus_force()
        no = fd22[-1]+0.1
        fd22.append(no)
        if fd22[-1] <= 0.7:
            shadowWin.attributes("-alpha", no)
        graphWin.attributes("-alpha", no)
        if fd22[-1] <= 1.0:
            graphWin.after(1, Fade_In3)
        else:
            fd22.clear()
            fd22.append(0.65)

    def Close_In(event):
        CloseLabel.configure(image=Close_Hover, cursor='hand2')
    def Close_Out(event):
        CloseLabel.configure(image=Close_Dis)
    def FALTU(event):
        a = 0
    def QuitGraphWin():
        Fade_Out3()
        graphWin.attributes("-alpha", 0.0)
        shadowWin.attributes("-alpha", 0.0)
        shadowWin.destroy()
        mainWin.bind("<Enter>", FALTU)
        graphWin.destroy()
    def CheckFocus(event):
        QuitGraphWin()
    mainWin.bind("<Enter>", CheckFocus)
    def Quit2(event):
        play_whoosh()
        QuitGraphWin()
    shadowWin.bind('<1>', Quit2)

    CloseLabel = Label(GuiControl, bg=GuiControlColor, image=Close_Dis)
    CloseLabel.bind("<Enter>", Close_In)
    CloseLabel.bind("<Leave>", Close_Out)
    CloseLabel.bind("<Button-1>", Quit2)
    CloseLabel.pack(side=LEFT, pady=1, padx=1)

    ###-----------FRAMES------------###
    upperFrame = Frame(QuizControl, background=QuizControlColor)
    upperFrame.pack(side=TOP, fill=X, pady=10)



    chpCombo = ttk.Combobox(upperFrame, state='readonly', font= ("Bahnschrift", 25), width=31, values=allSelect)
    chpCombo.pack(side=LEFT, fill=Y, padx=5)

    chpCombo2 = ttk.Combobox(upperFrame, state='readonly', font= ("Bahnschrift", 25), width=12, values=['SPEED(SECS/Q)','PERCENTAGE'])
    chpCombo2.pack(side=LEFT, fill=Y, padx=5)

    FRAME_N = []
    FRAME_N2 = []
    def Make_Graph(event):
        if str(chpCombo.get()) != '' and str(chpCombo2.get()) != '':
            graphWin.attributes("-alpha", 0.0)
            del FRAME_N[0:-2]
            del FRAME_N2[0:-2]
            graphFrame = Frame(QuizControl, background=QuizControlColor)
            toolFrame = Frame(QuizControl, background=QuizControlColor)
            toolFrame.pack(side=BOTTOM, fill=X)
            graphFrame.pack(side=TOP, fill=X)
            FRAME_N.append(graphFrame)
            FRAME_N2.append(toolFrame)
            btn.pack_forget()
            btn2.pack(side=LEFT, fill=Y)
            at = str(chpCombo.get())

            js = ''
            if str(at[0]) == 'P':
                js = 'physics'
            elif str(at[0]) == 'C':
                js = 'chemistry'
            elif str(at[0]) == 'M':
                js = 'maths'
            else:
                js = 'custom'

            main_path = "_AppData_\\questions\\"+str(js)+"\\"+str(chpCombo.get())+"\\"
            dir1 = main_path+"LEVEL1\\Test_Details.csv"
            dir2 = main_path+"LEVEL2\\Test_Details.csv"
            dir3 = main_path+"LEVEL3\\Test_Details.csv"

            if os.path.exists(dir1) or os.path.exists(dir2) or os.path.exists(dir3):
                print("========================================")
                print("CREATING GRAPH OF "+str(js).upper())
                ##STYLES
                plt.style.use('fivethirtyeight')
                fig = plt.figure(figsize=(12,8), dpi=120)

                # ---------------> LEVEL 1
                if os.path.exists(dir1):
                    read1 = pd.read_csv(dir1)
                    percent_lvl1 = read1['SPEED(SECS/Q)'].values.tolist() 
                    speed_lvl1 = read1['PERCENTAGE'].values.tolist() 
                else:
                    percent_lvl1 = [0, 0]
                    speed_lvl1 = [0, 0]
                # ---------------> LEVEL 2    
                if os.path.exists(dir2):
                    read2 = pd.read_csv(dir2)
                    percent_lvl2 = read2['SPEED(SECS/Q)'].values.tolist() 
                    speed_lvl2 = read2['PERCENTAGE'].values.tolist() 
                else:
                    percent_lvl2 = [0, 0]
                    speed_lvl2 = [0, 0]
                # ----------------> LEVEL 3
                if os.path.exists(dir3):
                    read3 = pd.read_csv(dir3)
                    percent_lvl3 = read3['SPEED(SECS/Q)'].values.tolist() 
                    speed_lvl3 = read3['PERCENTAGE'].values.tolist() 
                else:
                    percent_lvl3 = [0, 0]
                    speed_lvl3 = [0, 0]

                if str(chpCombo2.get()) == 'PERCENTAGE':
                    plt.plot(percent_lvl1,color='#00e1ff', label="LEVEL 1", linewidth=2)
                    plt.plot(percent_lvl2, color='#007bff', label="LEVEL 2", linewidth=2)
                    plt.plot(percent_lvl3, color='#0015ff', label="LEVEL 3", linewidth=2)

                elif str(chpCombo2.get()) == 'SPEED(SECS/Q)':
                    plt.plot(speed_lvl1,color='#00e1ff', label="LEVEL 1", linewidth=2)
                    plt.plot(speed_lvl2, color='#007bff', label="LEVEL 2", linewidth=2)
                    plt.plot(speed_lvl3, color='#0015ff', label="LEVEL 3", linewidth=2)

                plt.xticks([])
                plt.title('PROGRESS OF '+chpCombo.get())
                plt.legend()
                plt.grid(True)
                ##CANVAS
                canvas = FigureCanvasTkAgg(fig, master=graphFrame)
                canvas.draw()
                canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=0)
                ##TOOLBARS
                toolbar = NavigationToolbar2Tk(canvas, toolFrame)
                toolbar.update()
                canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=1)
                #btn.configure(state=DISABLED)
                chpCombo.config(state=DISABLED)
                graphWin.attributes("-alpha", 1.0)
            else:
                messagebox.showerror('FILE ERROR', 'PLEASE GIVE TEST ON THIS CHAPTER TO VIEW DETAILS!!')
                QuitGraphWin()
        else:
            messagebox.showerror('INPUT ERROR', 'PLEASE SELECT CHAPTER FOR RESULT')
            QuitGraphWin()
            
    def reset(event):
        FRAME_N[-1].destroy()
        FRAME_N2[-1].destroy()
        btn.pack(side=LEFT, fill=Y)
        btn2.pack_forget()
        #btn.config(state=NORMAL)
        chpCombo.config(state='readonly')

    def btn_in(event):
        btn.configure(image=H_Open)
    def btn_out(event):
        btn.configure(image=Open_Btn)
    def btn2_in(event):
        btn2.configure(image=H_Reset)
    def btn2_out(event):
        btn2.configure(image=Reset_Btn)
    btn = Label(upperFrame, bg=QuizControlColor, cursor='hand2', image=Open_Btn, font= ("Bahnschrift Light SemiCondensed", 18))
    btn.bind("<1>", Make_Graph)
    btn.bind("<Enter>", btn_in)
    btn.bind("<Leave>", btn_out)
    btn.pack(side=LEFT, fill=Y)
    btn2 = Label(upperFrame, bg=QuizControlColor, cursor='hand2', image=Reset_Btn, font= ("Bahnschrift Light SemiCondensed", 18))
    btn2.bind("<1>", reset)
    btn2.bind("<Enter>", btn2_in)
    btn2.bind("<Leave>", btn2_out)
    graphWin.focus_force()
    Fade_In3()

def AddChapters(event):
    chapterWin = Toplevel(mainWin)
    chapterWin.title('ADD QUESTIONS')
    chapterWin.geometry('1250x620')
    chapterWin.overrideredirect(True)
    chapterWin.tk.call('wm', 'iconphoto', chapterWin._w, icon)
    chapterWin.attributes("-alpha", 0.0)
    play_whoosh()
    Fade_Out()
    ###-IT COMES IN CENTER
    window_height = 140
    window_width = 650
    screen_width = chapterWin.winfo_screenwidth()
    screen_height = chapterWin.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    chapterWin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    ####-----------MAIN----FRAMES--------####
    GuiControl = Frame(chapterWin, background=GuiControlColor, height=32)
    GuiControl.pack(side=TOP, fill=X)
    QuizControl = Frame(chapterWin, background=QuizControlColor, height=590)
    QuizControl.pack(fill=BOTH)
    chapterWin.configure(background=QuizControlColor)
    ####INSIDE---FRAMES###
    chapterLIST = ['']
    labelList = []
    selectedCOL = 'black'
    def FocusMe():
        chapterWin.focus_force()
        chapterWin.lift()
        mainWin.after(10, FocusMe)
    def Change(event):
        ab = event.widget
        ab.configure(cursor='hand2', bg="#23314d")
    def Change2(event):
        ab = event.widget
        ab.configure(bg=GuiControlColor)
    def Fake(event):
        a = 1
    def Selected(event):
        play_click()
        del chapterLIST[0:-2]
        ab = event.widget
        if ab == labelList[0]:
            if chapterLIST[-1] != 'physics' and chapterLIST[-1]=='':
                chapterLIST.append('physics')
                ab.configure(bg=selectedCOL)
                ab.bind("<Enter>", Fake)
                ab.bind("<Leave>", Fake)
            elif chapterLIST[-1] == 'physics':
                chapterLIST.remove('physics')
                ab.configure(bg=GuiControlColor)
                ab.bind("<Enter>", Change)
                ab.bind("<Leave>", Change2)

        elif ab == labelList[1]:
            if chapterLIST[-1] != 'chemistry' and chapterLIST[-1]=='':
                chapterLIST.append('chemistry')
                ab.configure(bg=selectedCOL)
                ab.bind("<Enter>", Fake)
                ab.bind("<Leave>", Fake)
            elif chapterLIST[-1] == 'chemistry':
                chapterLIST.remove('chemistry')
                ab.configure(bg=GuiControlColor)
                ab.bind("<Enter>", Change)
                ab.bind("<Leave>", Change2)

        elif ab == labelList[2]:
            if chapterLIST[-1] != 'maths' and chapterLIST[-1]=='':
                chapterLIST.append('maths')
                ab.configure(bg=selectedCOL)
                ab.bind("<Enter>", Fake)
                ab.bind("<Leave>", Fake)
            elif chapterLIST[-1] == 'maths':
                chapterLIST.remove('maths')
                ab.configure(bg=GuiControlColor)
                ab.bind("<Enter>", Change)
                ab.bind("<Leave>", Change2)

        elif ab == labelList[3]:
            if chapterLIST[-1] != 'custom' and chapterLIST[-1]=='':
                chapterLIST.append('custom')
                ab.configure(bg=selectedCOL)
                ab.bind("<Enter>", Fake)
                ab.bind("<Leave>", Fake)
            elif chapterLIST[-1] == 'custom':
                chapterLIST.remove('custom')
                ab.configure(bg=GuiControlColor)
                ab.bind("<Enter>", Change)
                ab.bind("<Leave>", Change2)
    def SaveChapter(event):
        if chpEN.get() != '' and chapterLIST[-1] != '':
            sub = chapterLIST[-1]
            if sub == 'physics':
                chpName = 'P-'+str(chpEN.get()).upper()
                phy_chp.append(str(chpName))
                phy_chp.sort()
            elif sub == 'chemistry':
                chpName = 'C-'+str(chpEN.get()).upper()
                chem_chp.append(str(chpName))
                chem_chp.sort()
            elif sub == 'maths':
                chpName = 'M-'+str(chpEN.get()).upper()
                maths_chp.append(str(chpName))
                maths_chp.sort()
            elif sub == 'custom':
                chpName = str(chpEN.get()).upper()
                custom_chp.append(str(chpName))
                custom_chp.sort()
            if os.path.exists(str("_AppData_\\chapters\\"+str(sub)+"_chapter.csv")):
                row_contents = [str(chpName)]
                append_list_as_row(str("_AppData_\\chapters\\"+str(sub)+"_chapter.csv"), row_contents)
            else:
                row_contents = [str('CHAPTERS')]
                append_list_as_row(str("_AppData_\\chapters\\"+str(sub)+"_chapter.csv"), row_contents)
                row_contents2 = [str(chpName)]
                append_list_as_row(str("_AppData_\\chapters\\"+str(sub)+"_chapter.csv"), row_contents2)
            
        else:
            messagebox.showerror("DATA ERROR", "PLEASE PROVIDE US ENOUGH INFO!")
            chapterWin.focus_force()

        chapterLIST.clear()
        chapterLIST.append('')
        phyLabel.configure(bg=GuiControlColor)
        chemLabel.configure(bg=GuiControlColor)
        mathsLabel.configure(bg=GuiControlColor)
        customLabel.configure(bg=GuiControlColor)
        chpEN.set('')

    chapterWin.bind("<Return>", SaveChapter)
    QuizControlIn = Frame(QuizControl, background=QuizControlColor, height=590)
    QuizControlIn.pack(fill=BOTH)
    phyLabel = Label(QuizControlIn, text='PHYSICS', width=12, font=("Bahnschrift Light", 18), background=GuiControlColor, fg="#6fa5fd")
    chemLabel = Label(QuizControlIn, text='CHEMISTRY', width=12, font=("Bahnschrift Light", 18), background=GuiControlColor, fg="#6fa5fd")
    mathsLabel = Label(QuizControlIn, text='MATHS', width=12, font=("Bahnschrift Light", 18), background=GuiControlColor, fg="#6fa5fd")
    customLabel = Label(QuizControlIn, text='CUSTOM', width=12, font=("Bahnschrift Light", 18), background=GuiControlColor, fg="#6fa5fd")
    phyLabel.bind("<1>", Selected)
    chemLabel.bind("<1>", Selected)
    mathsLabel.bind("<1>", Selected)
    customLabel.bind("<1>", Selected)
    phyLabel.bind("<Enter>", Change)
    chemLabel.bind("<Enter>", Change)
    mathsLabel.bind("<Enter>", Change)
    customLabel.bind("<Enter>", Change)
    phyLabel.bind("<Leave>", Change2)
    chemLabel.bind("<Leave>", Change2)
    mathsLabel.bind("<Leave>", Change2)
    customLabel.bind("<Leave>", Change2)
    phyLabel.pack(side=LEFT, fill=X, padx=2, pady=5)
    chemLabel.pack(side=LEFT, fill=X, padx=2, pady=5)
    mathsLabel.pack(side=LEFT, fill=X, padx=2, pady=5)
    customLabel.pack(side=LEFT, fill=X, padx=2, pady=5)
    labelList.append(phyLabel)
    labelList.append(chemLabel)
    labelList.append(mathsLabel)
    labelList.append(customLabel)
    chpEN = StringVar()
    chapterEntry = Entry(QuizControl,insertbackground=GuiControlColor, textvariable=chpEN, fg=GuiControlColor, font=("Bahnschrift Light", 20),
                         bg='#88cbfe', highlightthickness=2, highlightbackground='#b8c6d0')
    chapterEntry.pack(fill=X, padx=2, pady=10)
    IconLabel = Label(GuiControl, bg=GuiControlColor, image=Icon)
    IconLabel.grid(row=0, column=0, sticky=NW, pady=1, padx=1)
    TitleLabel = Label(GuiControl, width=30, text='ADD CHAPTER', bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    TitleLabel.grid(row=0, column=1, sticky=N, padx=91)
    def Close_In(event):
        CloseLabel.configure(image=Close_Hover, cursor='hand2')
    def Close_Out(event):
        CloseLabel.configure(image=Close_Dis)
    def Quit(event):
        play_whoosh()
        Fade_In()
        chapterWin.destroy()
    CloseLabel = Label(GuiControl, bg=GuiControlColor, image=Close_Dis)
    CloseLabel.bind("<Enter>", Close_In)
    CloseLabel.bind("<Leave>", Close_Out)
    CloseLabel.bind("<Button-1>", Quit)
    CloseLabel.grid(row=0, column=2, sticky=E, pady=1, padx=1)
    chapterWin.attributes("-alpha", 1.0)
    

def AddQuestions():
    print('====================================================')
    print('ADD QUESTIONS (STARTED)!')    
    checkROOT.append(1)
    ####MAIN----FRAMESS###
    class Scrollable20(Frame):
        def __init__(self, parent, *args, **kw):
            Frame.__init__(self, parent, *args, **kw)            
            # create a canvas object and a vertical scrollbar for scrolling it
            vscrollbar = Scrollbar(self, orient=VERTICAL, width=12)
            vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
            canvas = Canvas(self, height=620, bd=0, bg=QuizControlColor, highlightthickness=0,
                            yscrollcommand=vscrollbar.set)
            canvas.pack(side=TOP, fill=BOTH, expand=1)
            vscrollbar.config(command=canvas.yview)
            # reset the vie
            canvas.xview_moveto(0)
            canvas.yview_moveto(0)
            # create a frame inside the canvas which will be scrolled with it
            self.interior = interior = Frame(canvas, bg=QuizControlColor)
            interior_id = canvas.create_window(0, 0, window=interior,
                                            anchor=NW)
            # track changes to the canvas and frame width and sync them,
            # also updating the scrollbar
            def _on_mousewheel(event):
                canvas.yview_scroll(int(-1*(event.delta/150)), "units")
            def _configure_interior(event):
                # update the scrollbars to match the size of the inner frame
                size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
                canvas.config(scrollregion="0 0 %s %s" % size)
                if interior.winfo_reqwidth() != canvas.winfo_width():
                    # update the canvas's width to fit the inner frame
                    canvas.config(width=interior.winfo_reqwidth())
            interior.bind('<Configure>', _configure_interior)
            def _bound_to_mousewheel(event):
                canvas.bind_all("<MouseWheel>", _on_mousewheel)   
            def _unbound_to_mousewheel(event):
                canvas.unbind_all("<MouseWheel>") 
            def _configure_canvas(event):
                if interior.winfo_reqwidth() != canvas.winfo_width():
                    # update the inner frame's width to fill the canvas
                    canvas.itemconfigure(interior_id, width=canvas.winfo_width())
            canvas.bind('<Configure>', _configure_canvas)
            canvas.bind_all("<MouseWheel>", _on_mousewheel)
            root.bind('<Enter>', _bound_to_mousewheel)
            root.bind('<Leave>', _unbound_to_mousewheel)

    GuiControl = Frame(root , background=GuiControlColor, height=32)
    GuiControl.pack(side=TOP, fill=X)
    
    mainFrame1 = Frame(root, background=QuizControlColor)
    mainFrame2 = Scrollable20(root, background=QuizControlColor, width=430)
    mainFrame1.pack(side=LEFT, fill=BOTH)
    mainFrame2.pack(side=RIGHT, fill=BOTH)
    
    QuizControl = Frame(mainFrame1, background=QuizControlColor)
    QuizControl.pack(fill=BOTH)
    btnFrame = Frame(mainFrame1, background=QuizControlColor)
    btnFrame.pack(fill=BOTH)
    root.configure(background=QuizControlColor)

    emptyLabel = Label(mainFrame2.interior, image=empty_img, bg=QuizControlColor)
    emptyLabel.pack(padx=120, pady=150)

    ###LISTS---HERE###
    subjectLIST = ['']
    levelLIST = ['']
    optionLIST = [0, 0, 0, 0]
    _getSubjLabel_=[]
    _getLvlLabel_=[]
    _getCorrectLabel_=[]
    
    ####INSIDE---FRAMES###
    def MouseChg(event):
        QEntry.configure(cursor='hand2', bg="#23314d")
    def MouseChg2(event):
        QEntry.configure(bg=GuiControlColor)
    def Change(event):
        ab = event.widget
        ab.configure(cursor='hand2', bg="#23314d")
    def Change2(event):
        ab = event.widget
        ab.configure(bg=GuiControlColor)
    
    selectedCOL = 'cyan'
    selectedCOLFg = 'black'
    normalCOL = GuiControlColor
    normalCOLFg = '#6fa5fd' 
    labelCOL = '#111927'
    def FALTU(event):
        faltu = str('MAT PADH YE FALTU HAI!!')
    def MakeNormal():
        PHYLabel.configure(bg=normalCOL, fg=normalCOLFg)
        CHEMLabel.configure(bg=normalCOL, fg=normalCOLFg)
        MATHSLabel.configure(bg=normalCOL, fg=normalCOLFg)
        CUSLabel.configure(bg=normalCOL, fg=normalCOLFg)
    def MakeNormal2():
         Lvl1Label.configure(bg=normalCOL, fg=normalCOLFg)
         Lvl2Label.configure(bg=normalCOL, fg=normalCOLFg)
         Lvl3Label.configure(bg=normalCOL, fg=normalCOLFg)

    def SELECTED(event):
        ab = event.widget
        del subjectLIST[0:-1]
        del levelLIST[0:-1]
    
        ###---------------SUBJECT-LIST-----------------###
        if ab == _getSubjLabel_[0]:
            if subjectLIST[-1] != 'physics':
                MakeNormal()
                ab.configure(bg=selectedCOL, fg=selectedCOLFg)
                subjectLIST.append('physics')
                ab.bind('<Enter>', FALTU)
                ab.bind('<Leave>', FALTU)
                chapter_entry.configure(state='readonly', values=phy_chp)
            elif subjectLIST[-1] == 'physics':
                ab.configure(bg=normalCOL, fg=normalCOLFg)
                subjectLIST.remove('physics')
                subjectLIST.append('')
                ab.bind('<Enter>', Change)
                ab.bind('<Leave>', Change2)
                chapter_entry.configure(state=DISABLED, values=[''])
                
        elif ab == _getSubjLabel_[1]:
            if subjectLIST[-1] != 'chemistry' :
                MakeNormal()
                ab.configure(bg=selectedCOL, fg=selectedCOLFg)
                subjectLIST.append('chemistry')
                ab.bind('<Enter>', FALTU)
                ab.bind('<Leave>', FALTU)
                chapter_entry.configure(state='readonly', values=chem_chp)
            elif subjectLIST[-1] == 'chemistry':
                ab.configure(bg=normalCOL, fg=normalCOLFg)
                subjectLIST.remove('chemistry')
                subjectLIST.append('')
                ab.bind('<Enter>', Change)
                ab.bind('<Leave>', Change2)
                chapter_entry.configure(state=DISABLED, values=[''])
                
        elif ab == _getSubjLabel_[2]:
            if subjectLIST[-1] != 'maths':
                MakeNormal()
                ab.configure(bg=selectedCOL, fg=selectedCOLFg)
                subjectLIST.append('maths')
                ab.bind('<Enter>', FALTU)
                ab.bind('<Leave>', FALTU)
                chapter_entry.configure(state='readonly', values=maths_chp)
            elif subjectLIST[-1] == 'maths':
                ab.configure(bg=normalCOL, fg=normalCOLFg)
                subjectLIST.remove('maths')
                subjectLIST.append('')
                ab.bind('<Enter>', Change)
                ab.bind('<Leave>', Change2)
                chapter_entry.configure(state=DISABLED, values=[''])
                
        elif ab == _getSubjLabel_[3]:
            if subjectLIST[-1] != 'custom' :
                MakeNormal()
                ab.configure(bg=selectedCOL, fg=selectedCOLFg)
                subjectLIST.append('custom')
                ab.bind('<Enter>', FALTU)
                ab.bind('<Leave>', FALTU)
                chapter_entry.configure(state='readonly', values=custom_chp)
            elif subjectLIST[-1] == 'custom':
                ab.configure(bg=normalCOL, fg=normalCOLFg)
                subjectLIST.remove('custom')
                subjectLIST.append('')
                ab.bind('<Enter>', Change)
                ab.bind('<Leave>', Change2)
                chapter_entry.configure(state=DISABLED, values=[''])
                
    
        ###---------------LEVEL-LIST-----------------###
                
        if ab == _getLvlLabel_[0]:
            if levelLIST[-1] != 'LEVEL1':
                MakeNormal2()
                ab.configure(bg=selectedCOL, fg=selectedCOLFg)
                levelLIST.append('LEVEL1')
                ab.bind('<Enter>', FALTU)
                ab.bind('<Leave>', FALTU)
            elif levelLIST[-1] == 'LEVEL1':
                ab.configure(bg=normalCOL, fg=normalCOLFg)
                levelLIST.remove('LEVEL1')
                levelLIST.append('')
                ab.bind('<Enter>', Change)
                ab.bind('<Leave>', Change2)            
    
        elif ab == _getLvlLabel_[1]:
            if levelLIST[-1] != 'LEVEL2':
                MakeNormal2()
                ab.configure(bg=selectedCOL, fg=selectedCOLFg)
                levelLIST.append('LEVEL2')
                ab.bind('<Enter>', FALTU)
                ab.bind('<Leave>', FALTU)
            elif levelLIST[-1] == 'LEVEL2':
                ab.configure(bg=normalCOL, fg=normalCOLFg)
                levelLIST.remove('LEVEL2')
                levelLIST.append('')
                ab.bind('<Enter>', Change)
                ab.bind('<Leave>', Change2)
                
        elif ab == _getLvlLabel_[2]:
            if levelLIST[-1] != 'LEVEL3':
                MakeNormal2()
                ab.configure(bg=selectedCOL, fg=selectedCOLFg)
                levelLIST.append('LEVEL3')
                ab.bind('<Enter>', FALTU)
                ab.bind('<Leave>', FALTU)
            elif levelLIST[-1] == 'LEVEL3':
                ab.configure(bg=normalCOL, fg=normalCOLFg)
                levelLIST.remove('LEVEL3')
                levelLIST.append('')
                ab.bind('<Enter>', Change)
                ab.bind('<Leave>', Change2)      
    
        ###------------OPTION-LIST-------------------###
    
        if ab == _getCorrectLabel_[0]:
            if optionLIST[0] != 1:
                ab.configure(bg=selectedCOL, fg=selectedCOLFg)
                optionLIST[0] = 1
                ab.bind('<Enter>', FALTU)
                ab.bind('<Leave>', FALTU)
            elif optionLIST[0] == 1:
                ab.configure(bg=normalCOL, fg=normalCOLFg)
                optionLIST[0] = 0
                ab.bind('<Enter>', Change)
                ab.bind('<Leave>', Change2)
                
        elif ab == _getCorrectLabel_[1]:
            if optionLIST[1] != 1:
                ab.configure(bg=selectedCOL, fg=selectedCOLFg)
                optionLIST[1] = 1
                ab.bind('<Enter>', FALTU)
                ab.bind('<Leave>', FALTU)
            elif optionLIST[1] == 1:
                ab.configure(bg=normalCOL, fg=normalCOLFg)
                optionLIST[1] = 0
                ab.bind('<Enter>', Change)
                ab.bind('<Leave>', Change2)
                
        elif ab == _getCorrectLabel_[2]:
            if optionLIST[2] != 1:
                ab.configure(bg=selectedCOL, fg=selectedCOLFg)
                optionLIST[2] = 1
                ab.bind('<Enter>', FALTU)
                ab.bind('<Leave>', FALTU)
            elif optionLIST[2] == 1:
                ab.configure(bg=normalCOL, fg=normalCOLFg)
                optionLIST[2] = 0
                ab.bind('<Enter>', Change)
                ab.bind('<Leave>', Change2)
                         
        elif ab == _getCorrectLabel_[3]:
            if optionLIST[3] != 1:
                ab.configure(bg=selectedCOL, fg=selectedCOLFg)
                optionLIST[3] = 1
                ab.bind('<Enter>', FALTU)
                ab.bind('<Leave>', FALTU)
            elif optionLIST[3] == 1:
                ab.configure(bg=normalCOL, fg=normalCOLFg)
                optionLIST[3] = 0
                ab.bind('<Enter>', Change)
                ab.bind('<Leave>', Change2)

    def set_path_users_field(event):
        path = askopenfilename(filetypes=[("Image File",("*.png","*.jpg"))]) 
        input_text.set(path)
        root.focus_force()
    def ChangeSave(event):
        SaveControl.configure(cursor='hand2', bg='#28dbdb')
    def DefaultSave(event):
        SaveControl.configure(bg='cyan')

    def Clear():
        input_text.set('')
        optionLIST.clear()
        for j in range(4):
            optionLIST.append(0)
        Opt1Label.configure(bg=normalCOL, fg='#6fa5fd')
        Opt2Label.configure(bg=normalCOL, fg='#6fa5fd')
        Opt3Label.configure(bg=normalCOL, fg='#6fa5fd')
        Opt4Label.configure(bg=normalCOL, fg='#6fa5fd')

    def Save(event):
        root.attributes("-alpha", 0.5)
        qEn = str(QEntry.cget("text"))
        chpEn = str(chapter_entry.get())
        no = 0
        get_i = []
        for i in range(4):
            if optionLIST[i] == 0:
                no += 1
            if optionLIST[i] == 1:
                if i == 0:
                    get_i.append('A')
                elif i == 1:
                    get_i.append('B')
                elif i == 2:
                    get_i.append('C')
                elif i == 3:
                    get_i.append('D')
            
        if qEn != '' and chpEn != '' and subjectLIST[-1] != '' and levelLIST[-1] != '' and no != 4:
            destination = '_AppData_\\questions\\'+str(subjectLIST[-1])+'\\'+str(chpEn)+'\\'+str(levelLIST[-1])+'\\'
            csvSetting = destination+'setting.csv'
            csvSolution = destination+'solution.csv'
            emptyLabel.destroy()
            if not os.path.exists(destination):
                if not os.path.exists('_AppData_\\questions\\'+str(subjectLIST[-1])+'\\'+str(chpEn)):
                    os.mkdir('_AppData_\\questions\\'+str(subjectLIST[-1])+'\\'+str(chpEn))
                os.mkdir('_AppData_\\questions\\'+str(subjectLIST[-1])+'\\'+str(chpEn)+'\\'+str(levelLIST[-1])+'\\')

                # SAVING THE OPTION
                options1 = ['OPTION1', 'OPTION2', 'OPTION3', 'OPTION4']
                append_list_as_row(csvSolution, options1)
                options2 = [optionLIST[0], optionLIST[1], optionLIST[2], optionLIST[3]]
                append_list_as_row(csvSolution, options2)

                # SAVING THE BASEWIDTH & #SAVING TOTAL SEEN AND HOW CORRECT  --> FOR CALCULATING ACCURACY
                row_con = ['BASEWIDTH','TS','HC']
                append_list_as_row(csvSetting, row_con)
                row_con2 = [950,0,0]
                append_list_as_row(csvSetting, row_con2)
                
                QImage = Image.open(qEn)
                QImage.save(destination+str(0)+".png", 'PNG')
                os.remove(qEn)
                print('====================================================')
                print('SELECTED IMG! ', qEn)
                print('SAVED IMG! ', destination+str(0)+".png")
                print('SUBJECT -->', subjectLIST[-1], 'LEVEL -->', levelLIST[-1], 'OPTIONS -->', optionLIST)
                Clear()
                root.focus_force()
            else:
                ##READING CSV FILE
                csvSol = pandas.read_csv(csvSolution)
                _option1_ = csvSol['OPTION1'].values.tolist()
                _option1_.append(optionLIST[0])
                MaxQ = int(len(_option1_))
                QImage = Image.open(qEn)
                QImage.save(destination+str(MaxQ-1)+".png", 'PNG')

                options = [optionLIST[0], optionLIST[1], optionLIST[2], optionLIST[3]]
                append_list_as_row(csvSolution, options)        

                row_con2 = [950,0,0]
                append_list_as_row(csvSetting, row_con2)
                print('====================================================')
                print('SELECTED IMG! ', qEn)
                print('SAVED IMG! ', destination+str(0)+".png")
                print('SUBJECT -->', subjectLIST[-1], 'LEVEL -->', levelLIST[-1], 'OPTIONS -->', optionLIST)
                Clear()
                os.remove(qEn)
                root.focus_force()

            listToStr = ' & '.join([str(elem) for elem in get_i]) 
            FrameT = Frame(mainFrame2.interior, bg='cyan')
            FrameT.pack(side=BOTTOM, pady=3, padx=3)
            nam = str(str(qEn).upper()).split('/')
            prevPath = Label(FrameT, width=26, anchor='e', text=str(nam[-1]).upper(), bg='cyan', fg=QuizControlColor, font=("Bahnschrift", 21))
            details1 = Label(FrameT, anchor='w', text=str('SUBJECT : '+str(subjectLIST[-1]).upper()+' / LEVEL 1 : '+str(levelLIST[-1])), bg='turquoise', fg=QuizControlColor, font=("Bahnschrift Light", 15))
            details2 = Label(FrameT, anchor='w', text=str(' OPTIONS : '+listToStr), bg='turquoise', fg=QuizControlColor, font=("Bahnschrift Light", 15))
            prevPath.pack(fill=BOTH, expand=1)
            details1.pack(fill=BOTH, expand=1)
            details2.pack(fill=BOTH, expand=1)
            
        else:
            messagebox.showerror("ERROR",'SOMETHING SEEMS MISSING!!')
            root.focus_force()
        root.attributes("-alpha", 1.0)
            
    root.bind("<Return>", Save)
    root.bind("<o>", set_path_users_field)
    root.bind("<O>", set_path_users_field)
    SaveControl = Label(btnFrame, bg='cyan', height=40, text='SAVE QUESTION', font=("Bahnschrift Light", 18), fg=QuizControlColor)
    SaveControl.bind("<Enter>", ChangeSave)
    SaveControl.bind("<Leave>", DefaultSave)
    SaveControl.bind("<1>", Save)
    SaveControl.pack(fill=BOTH, padx=10, pady=10)
    
    input_text = StringVar()   
    QLabel = Label(QuizControl, width=16, text='QUESTION PATH:', bg=labelCOL, font=("Bahnschrift Light", 20), fg="#6fa5fd")
    QEntry = Label(QuizControl, width=15, anchor='e', textvariable=input_text, bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    SubjLabel = Label(QuizControl, width=16, text='SUBJECT:', bg=labelCOL, font=("Bahnschrift Light", 20), fg="#6fa5fd")
    PHYLabel = Label(QuizControl, width=15, text='PHYSICS', bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    CHEMLabel = Label(QuizControl, width=15, text='CHEMISTRY', bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    MATHSLabel = Label(QuizControl, width=15, text='MATHS', bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    CUSLabel = Label(QuizControl, width=15, text='CUSTOM', bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    IDLabel = Label(QuizControl, width=16, text='CHAPTER:', bg=labelCOL, font=("Bahnschrift Light", 20), fg="#6fa5fd")
    chapter_entry = ttk.Combobox(QuizControl, state=DISABLED, values=(""), font=("Bahnschrift Light SemiCondensed", 20), width=12)
    LvlLabel = Label(QuizControl, width=16, text='LEVEL:', bg=labelCOL, font=("Bahnschrift Light", 20), fg="#6fa5fd")
    Lvl1Label = Label(QuizControl, width=15, text='LEVEL1', bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    Lvl2Label = Label(QuizControl, width=15, text='LEVEL2', bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    Lvl3Label = Label(QuizControl, width=15, text='LEVEL3', bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    CorrectLabel = Label(QuizControl, width=16, text='CORRECT:', bg=labelCOL, font=("Bahnschrift Light", 20), fg="#6fa5fd")
    Opt1Label = Label(QuizControl, width=15, text='OPTION (A)', bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    Opt2Label = Label(QuizControl, width=15, text='OPTION (B)', bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    Opt3Label = Label(QuizControl, width=15, text='OPTION (C)', bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    Opt4Label = Label(QuizControl, width=15, text='OPTION (D)', bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
    
    def Close_In(event):
        CloseLabel.configure(image=Close_Hover, cursor='hand2')
    def Close_Out(event):
        CloseLabel.configure(image=Close_Dis)
    def Quit(event):
        mainWin.deiconify()
        play_whoosh()
        Fade_In()
        mainWin.focus_force()
        root.withdraw()

        
    QEntry.bind("<1>", set_path_users_field)
    
    CloseLabel = Label(GuiControl, bg=GuiControlColor, image=Close_Dis)
    CloseLabel.bind("<Enter>", Close_In)
    CloseLabel.bind("<Leave>", Close_Out)
    CloseLabel.bind("<Button-1>", Quit)
    CloseLabel.grid(row=0, column=1, sticky=E, pady=1, padx=1)
    
    PHYLabel.bind("<1>", SELECTED)
    CHEMLabel.bind("<1>", SELECTED)
    MATHSLabel.bind("<1>", SELECTED)
    CUSLabel.bind("<1>", SELECTED)
    
    Lvl1Label.bind("<1>", SELECTED)
    Lvl2Label.bind("<1>", SELECTED)
    Lvl3Label.bind("<1>", SELECTED)
    
    Opt1Label.bind("<1>", SELECTED)
    Opt2Label.bind("<1>", SELECTED)
    Opt3Label.bind("<1>", SELECTED)
    Opt4Label.bind("<1>", SELECTED)
    
    QEntry.bind("<Enter>", MouseChg)
    QEntry.bind("<Leave>", MouseChg2)
    
    PHYLabel.bind("<Enter>", Change)
    CHEMLabel.bind("<Enter>", Change)
    MATHSLabel.bind("<Enter>", Change)
    CUSLabel.bind("<Enter>", Change)
    PHYLabel.bind("<Leave>", Change2)
    CHEMLabel.bind("<Leave>", Change2)
    MATHSLabel.bind("<Leave>", Change2)
    CUSLabel.bind("<Leave>", Change2)
    
    Lvl1Label.bind("<Enter>", Change)
    Lvl2Label.bind("<Enter>", Change)
    Lvl3Label.bind("<Enter>", Change)
    Lvl1Label.bind("<Leave>", Change2)
    Lvl2Label.bind("<Leave>", Change2)
    Lvl3Label.bind("<Leave>", Change2)
    
    Opt1Label.bind("<Enter>", Change)
    Opt2Label.bind("<Enter>", Change)
    Opt3Label.bind("<Enter>", Change)
    Opt4Label.bind("<Enter>", Change)
    Opt1Label.bind("<Leave>", Change2)
    Opt2Label.bind("<Leave>", Change2)
    Opt3Label.bind("<Leave>", Change2)
    Opt4Label.bind("<Leave>", Change2)
    
    QLabel.grid(row=0, column=0, pady=1, padx=1, ipady=1, ipadx=1)
    QEntry.grid(row=0, column=1, padx=1, ipady=1, ipadx=1)
    SubjLabel.grid(row=1, column=0, pady=1, padx=1, ipady=1, ipadx=1)
    PHYLabel.grid(row=1, column=1, pady=1, padx=1)
    CHEMLabel.grid(row=2, column=1, pady=1, padx=1)
    MATHSLabel.grid(row=3, column=1, pady=1, padx=1)
    CUSLabel.grid(row=4, column=1, pady=1, padx=1)
    IDLabel.grid(row=5, column=0, pady=1, padx=1)
    chapter_entry.grid(row=5, column=1, pady=1, padx=1)
    LvlLabel.grid(row=6, column=0, pady=1, padx=1)
    Lvl1Label.grid(row=6, column=1, pady=1, padx=1)
    Lvl2Label.grid(row=7, column=1, pady=1, padx=1)
    Lvl3Label.grid(row=8, column=1, pady=1, padx=1)
    CorrectLabel.grid(row=9, column=0, pady=1, padx=1)
    Opt1Label.grid(row=9, column=1, pady=1, padx=1)
    Opt2Label.grid(row=10, column=1, pady=1, padx=1)
    Opt3Label.grid(row=11, column=1, pady=1, padx=1)
    Opt4Label.grid(row=12, column=1, pady=1, padx=1)
    
    ### APPENDING THE LISTS WITH THE LABELS INFO
    _getSubjLabel_.append(PHYLabel)
    _getSubjLabel_.append(CHEMLabel)
    _getSubjLabel_.append(MATHSLabel)
    _getSubjLabel_.append(CUSLabel)
    
    _getLvlLabel_.append(Lvl1Label)
    _getLvlLabel_.append(Lvl2Label)
    _getLvlLabel_.append(Lvl3Label)
    
    _getCorrectLabel_.append(Opt1Label)
    _getCorrectLabel_.append(Opt2Label)
    _getCorrectLabel_.append(Opt3Label)
    _getCorrectLabel_.append(Opt4Label)
    root.focus_force()
    
ptk = [0.0]
def FadeROOTWin():
    del ptk[0:-2]
    no = float(ptk[-1])+0.1
    ptk.append(no)
    root.attributes("-alpha", no)
    if ptk[-1] < 1:
        if no == 0.1:
            root.deiconify()
        root.after(1, FadeROOTWin)
    elif ptk[-1] > 1:
        del ptk[0:-1]
        ptk.append(0.0)
def AddQuestion(event):
    mainWin.withdraw()
    if checkROOT[-1] == 0:
        AddQuestions()
        play_whoosh()
        FadeROOTWin()
    else:
        play_whoosh()
        FadeROOTWin()
    root.focus_force()

AnimLoadBar() # AFTER CHECKING FUNCTIONS COMPLETE LOADBAR UPDATE

print('================================')
print('SETTING MAINWIN...')        
TabHolder = Frame(QuizControl, background='#3c426e')
SubHolder = Frame(QuizControl, background=QuizControlColor, height=800)
ChapterScroll = Scrollable(QuizControl, background=QuizControlColor, height=1000)
ChapterHolder = Frame(ChapterScroll.interior, background=QuizControlColor, height=1000)
Level1 = Label(TabHolder, text='LEVEL1', font=("Bahnschrift", 15), height=1, fg="white", width=10, bg=QuizControlColor)
Level2 = Label(TabHolder, text='LEVEL2', font=("Bahnschrift", 15), height=1, fg="white", width=11, bg='#1e213c')
Level3 = Label(TabHolder, text='LEVEL3', font=("Bahnschrift", 15), height=1, fg="white", width=12, bg='#1e213c')
waste = Label(TabHolder, bg='#3c426e')
addQuestions = Label(TabHolder, cursor='hand2', image=addQ, bg='#3c426e')
addChapters = Label(TabHolder, cursor='hand2', image=addChp, bg='#3c426e')
checkAnalysis = Label(TabHolder, cursor='hand2', image=openAnalysis , bg='#3c426e')
soundControl = Label(TabHolder, cursor='hand2', image=unmute, bg='#3c426e')
if Vol[-1] == 1:
    soundControl.configure(image=unmute, cursor='hand2')
    soundControl.image = unmute
elif Vol[-1] == 0:
    soundControl.configure(image=mute, cursor='hand2')
    soundControl.image = mute
    
Level1.bind("<Enter>", Level1_In)
Level1.bind("<Leave>", Level1_Out)
Level2.bind("<Enter>", Level2_In)
Level2.bind("<Leave>", Level2_Out)
Level3.bind("<Enter>", Level3_In)
Level3.bind("<Leave>", Level3_Out)
Level1.bind("<1>", Lvl1Click)
Level2.bind("<1>", Lvl2Click)
Level3.bind("<1>", Lvl3Click)
addChapters.bind("<1>", AddChapters)
addChapters.bind("<Enter>", addChp_In)
addChapters.bind("<Leave>", addChp_Out)
addQuestions.bind("<1>", AddQuestion)
addQuestions.bind("<Enter>", addQ_In)
addQuestions.bind("<Leave>", addQ_Out)
checkAnalysis.bind("<1>", OpenTracker)
checkAnalysis.bind("<Enter>", openGraph_In)
checkAnalysis.bind("<Leave>",openGraph_Out)
soundControl.bind("<1>", TurnOnOffSound)
TabHolder.pack(fill=X)
SubHolder.pack(fill=BOTH)
ChapterScroll.pack(fill=BOTH, expand=1)
ChapterHolder.pack(fill=BOTH, expand=1)
Level1.grid(row=0, column=0, ipadx=5, ipady=1)
Level2.grid(row=0, column=1, ipadx=5, ipady=1)
Level3.grid(row=0, column=2, ipadx=5, ipady=1)
waste.grid(row=0, column=3, padx=205, ipady=1)
checkAnalysis.grid(row=0, column=4, ipady=1)
addChapters.grid(row=0, column=5, ipady=1)
addQuestions.grid(row=0, column=6, ipady=1)
soundControl.grid(row=0, column=7, ipadx=1, ipady=1)

AnimLoadBar() # AFTER SETTING MAINWIN COMPLETE LOADBAR UPDATE

def Faltu(event):
    jhetalal = 'Haagray!!'
def FadeWin():
    jk = float(0.0)
    for i in range(100):
        jk += 0.05
        mainWin.attributes("-alpha", jk)       
        
def StartQuizFinal():
    if str(SubjSel[-1]) == 'P':
        xjs = 'physics'
    elif str(SubjSel[-1]) == 'C':
        xjs = 'chemistry'
    elif str(SubjSel[-1]) == 'M':
        xjs = 'maths'
    elif str(SubjSel[-1]) == 'CUS':
        xjs = 'custom'
       
    pathDIR = "_AppData_\\questions\\"+str(xjs)+"\\"+str(_getChpName_[-1])+"\\LEVEL"+str(Tab_chk[-1])+"\\"
    if os.path.exists(pathDIR):
        print('====================================================')
        print('STARTING TEST ON ', _getChpName_[-1])
        ###--STARTING THE QUIZWIN
        quizWin = Toplevel(mainWin)
        quizWin.title(str(_getChpName_[-1]))
        quizWin.overrideredirect(True)      
        ###-IT COMES IN CENTER
        if int(zoom_chk[-1]) == 0:
            window_height = 650
            window_width = 1300
            screen_width = quizWin.winfo_screenwidth()
            screen_height = quizWin.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int((screen_height/2) - (window_height/2))
            quizWin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        else:
            screen_width = quizWin.winfo_screenwidth()
            screen_height = quizWin.winfo_screenheight()
            quizWin.geometry("{}x{}".format(screen_width, screen_height))

        quizWin.tk.call('wm', 'iconphoto', quizWin._w, icon)
        quizWin.attributes("-alpha", 0.0)  
        
        shadowWin = Toplevel(mainWin)
        shadowWin.configure(background="black")
        shadowWin.overrideredirect(True)
        ###-IT COMES IN CENTER
        if int(zoom_chk[-1]) == 0:
            window_height = 650
            window_width = 1300
            screen_width = shadowWin.winfo_screenwidth()
            screen_height = shadowWin.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int((screen_height/2) - (window_height/2))
            shadowWin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        else:
            shadowWin.geometry("{}x{}".format(screen_width, screen_height))
            
        shadowWin.attributes("-alpha", 0.0)
    
        ###LISTS N VARIABLES
        getQNO = int(totalQuestions[-1])
        getSub = str(SubjSel[-1])
        getLvl = str(Tab_chk[-1]) 
        getChpName = str(_getChpName_[-1])
        basewidth = 950
        final_QNo = [] # -------------> SHUFFLED QUESTION NUMBER GOES HERE
        question_images = []  ##------>QUESTION IMAGES GO HERE
        omrBtnList = [] ##----->OMR BUTTON GOES HERE
        # --------> THEY ALL ARE USED TO SAVE SHUFFLED_SOLUTION CSV FILE
        OPTION1 = []
        OPTION2 = []
        OPTION3 = []
        OPTION4 = []
        ####WHEN YOU SELECT OPTION IT INTERPRETS 1/0
        #1 means OPTION selected.
        #0 means OPTION not selected.
        mahaOPT1 = [] 
        mahaOPT2 = []
        mahaOPT3 = []
        mahaOPT4 = []
        # TO CALCULATE THE TIME REQURIED
        EntertimeQ = []  # WHEN U ENTER A QUESTION THIS GETS APPENDED.
        timeQ = []
        ##TO CHECK WHETHER USER HAS VISITED THE QUESTION OR NOT
        visitCHK = []
        ##CHECKING THE LOCKED OMR BUTTON
        lockedBTN = [0]
        ##THIS IS TO GET THE CURRENT BUTTON NUMBER
        ##BY DEFAULT IT REMAINS '0'.
        btnNUM = [0]
        endTEST = [0]
        count = [0]
        hour = [0]
        minute = [0]
        second = [0]
        resize_list = [] # ZOOM_IN & ZOOM_OUT FEATURE

        ## ======== ===== ======= ----> THESE LISTS BELOW ARE TO CHECK WHETHER U PREVIOUSLY CLICKED THE OPTION BTN OR NOT
        
        OPT1GIF_CHK = [0]
        OPT1GIF_CHK2 = [10]

        OPT2GIF_CHK = [0]
        OPT2GIF_CHK2 = [10]

        OPT3GIF_CHK = [0]
        OPT3GIF_CHK2 = [10]

        OPT4GIF_CHK = [0]
        OPT4GIF_CHK2 = [10]

        # ---------------------> TIMER
        def timer():     
            if(count[-1]==0):
                d = str(t.get())

                if second[-1] == 59:
                    second.clear()
                    second.append(0)
                else:
                    second.append(int(second[-1])+1)

                if minute[-1] == 59 and second[-1] == 0:
                    minute.clear()
                    minute.append(0)
                    hour.append(int(hour[-1])+1)
                elif second[-1] == 0:
                    minute.append(int(minute[-1])+1)

                if (hour[-1] < 10):
                    h="0"+str(hour[-1])
                else:
                    h=str(hour[-1])

                if (minute[-1] < 10):
                    m="0"+str(minute[-1])
                else:
                    m=str(minute[-1])

                if (second[-1] < 10):
                    s="0"+str(second[-1])
                else:
                    s=str(second[-1])  

                del hour[0:-2]
                del minute[0:-2]
                del second[0:-2]

                d=str(h)+":"+str(m)+":"+str(s)
                #t.set(d)
                if(count[-1]==0):
                    t.set(d)
                    quizWin.after(1000, timer)
        ###IMAGES---HERE###
        omrBTNImg = PhotoImage(file=("_AppData_\\Icons\\omrBtn.png"))
        omrBTNImg2 = PhotoImage(file=("_AppData_\\Icons\\omrBtn2.png"))
        omrBtn_unanswer = PhotoImage(file=("_AppData_\\Icons\\omrBtn_unanswered.png"))
        omrBtn_selected = PhotoImage(file=("_AppData_\\Icons\\omrBtn_selected.png"))
        omrBtn_Hover = PhotoImage(file=("_AppData_\\Icons\\omrBtn_hover.png"))
        omrBtn_answered = PhotoImage(file=("_AppData_\\Icons\\omrBtn_answered.png"))
        omrBtn_answered_hover = PhotoImage(file=("_AppData_\\Icons\\omrBtn_answered_hover.png"))
        visited_unanwered = PhotoImage(file=("_AppData_\\Icons\\visited_unanwered.png"))
        visited_unanwered_hover = PhotoImage(file=("_AppData_\\Icons\\visited_unanwered_hover.png"))
        omrBtn_answered = PhotoImage(file=("_AppData_\\Icons\\omrBtn_answered.png"))
        omrBtn_answered = PhotoImage(file=("_AppData_\\Icons\\omrBtn_answered.png"))
        nextBTN = PhotoImage(file=("_AppData_\\Icons\\nextBTN.png"))
        nextBTNH = PhotoImage(file=("_AppData_\\Icons\\nextBTNH.png"))
        previousBTN = PhotoImage(file=("_AppData_\\Icons\\previousBTN.png"))
        previousBTNH = PhotoImage(file=("_AppData_\\Icons\\previousBTNH.png"))
        print("==================================================================")
        print("LOADING CHECKBUTTON.GIF")
        print("------------------------------------------------------------------")
        Option1GIF = '_AppData_\\gifs\\optionbutton_one.gif'
        Opt1frames = [PhotoImage(file=Option1GIF,format = 'gif -index %i' %(i)) for i in range(13)]
        Option2GIF = '_AppData_\\gifs\\optionbutton_two.gif'
        Opt2frames = [PhotoImage(file=Option2GIF,format = 'gif -index %i' %(i)) for i in range(13)]
        Option3GIF = '_AppData_\\gifs\\optionbutton_third.gif'
        Opt3frames = [PhotoImage(file=Option3GIF,format = 'gif -index %i' %(i)) for i in range(13)]
        Option4GIF = '_AppData_\\gifs\\optionbutton_four.gif'
        Opt4frames = [PhotoImage(file=Option4GIF,format = 'gif -index %i' %(i)) for i in range(13)]
        EndTestGIF = '_AppData_\\gifs\\end_test.gif'
        Endtestframes = [PhotoImage(file=EndTestGIF,format = 'gif -index %i' %(i)) for i in range(7)]
        LoadResult = '_AppData_\\gifs\\resultLoad.gif'
        LoadResultF = [PhotoImage(file=LoadResult,format = 'gif -index %i' %(i)) for i in range(10)]
        print("LOADED CHECKBUTTON.GIF")
        print("==================================================================")
        ###----------------COLORS-----####
        optionFrameCol = '#1c2131'
        toolBarColor = '#414879'
        GuiControlColor = '#172134'
        QuizControlColor = '#232853'
        omrRowCol = QuizControlColor
        statusFrameCol = '#100a28'
        sFrameLabCol = '#dee9fb'
        ####MAIN----FRAMESS####
        GuiControl = Frame(quizWin, background=GuiControlColor, height=32)
        GuiControl.pack(side=TOP, fill=X)
        QuizControl = Frame(quizWin, background=QuizControlColor, height=590)
        QuizControl.pack(fill=BOTH)
        quizWin.configure(background=QuizControlColor)

        #WINDOW-EFFECTS
        fd1 = [1.0]
        def Fade_Out2():
            no = fd1[-1]-0.01
            fd1.append(no)
            quizWin.attributes("-alpha", no)
            if fd1[-1] >= 0.65:
                quizWin.after(6, Fade_Out2)
            else:
                fd1.clear()
                fd1.append(1.0)
                
        fd22 = [0.65]
        def Fade_In2():
            no = fd22[-1]+0.01
            fd22.append(no)
            quizWin.attributes("-alpha", no)
            if fd22[-1] <= 1.0:
                quizWin.after(2, Fade_In2)
            else:
                fd22.clear()
                fd22.append(0.65)

        ###CLOSE--BTN--FUNCTION###
        def Close_In(event):
            CloseLabel.configure(image=Close_Hover, cursor='hand2')
        def Close_Out(event):
            CloseLabel.configure(image=Close_Dis)
        def Close_In2(event):
            CloseLabel2.configure(image=Close_Hover, cursor='hand2')
        def Close_Out2(event):
            CloseLabel2.configure(image=Close_Dis)
        def Quit(event):
            play_click()
            response2=messagebox.askquestion('WARNING', 'DO YOU REALLY WANT TO CLOSE THE TEST WINDOW?')
            if response2 == 'yes':
                if endTEST[-1] == 1:
                    print('====================================================')
                    print('AFTER CHECKING RESULT QUIZWIN CLOSED!')
                else:
                    print('====================================================')
                    print('TEST CANCELLED WITHOUT ATTEMPTING QUESTIONS (CANCEL)')
                shadowWin.destroy()
                omrWin.destroy()
                question_images.clear()
                omrBtnList.clear() 
                OPTION1.clear()
                OPTION2.clear()
                OPTION3.clear()
                OPTION4.clear()
                mahaOPT1.clear()
                mahaOPT2.clear()
                mahaOPT3.clear()
                mahaOPT4.clear()
                lockedBTN.clear()
                btnNUM.clear()
                endTEST.clear()
                resize_list.clear()  
                quizWin.destroy()
                Back_Home()
            else:
                pass
        def QuitWin():
            play_whoosh()
            shadowWin.attributes("-alpha", 0.0)
            omrWin.attributes("-alpha", 0.0)
            quizWin.focus_force()
            omrWin.withdraw()
            quizWin.focus_force()
        def Quit2(event):
            QuitWin()
        shadowWin.bind("<1>", Quit2)
        ###OMR-TOPLEVEL-WINDOW###
        omrWin = Toplevel(mainWin)
        omrWin.title('OMR WINDOW')
        omrWin.overrideredirect(True)
        omrWin.attributes("-alpha", 0.0)
        if int(zoom_chk[-1]) == 0:
            omrWin.geometry('%dx%d+%d+%d' % (325, 651, 1007, 59))
        else:
            omrWin.geometry('%dx%d+%d+%d' % (325, screen_height, 1040, 0))
            
        omrWin.tk.call('wm', 'iconphoto', omrWin._w, icon)
        omrWin.configure(background=QuizControlColor)
        
        closeFrame = Frame(omrWin, background=GuiControlColor, height=32)
        closeFrame.pack(side=TOP, fill=X)
        CloseLabel2 = Label(closeFrame, bg=GuiControlColor, image=Close_Dis)
        CloseLabel2.bind("<Enter>", Close_In2)
        CloseLabel2.bind("<Leave>", Close_Out2)
        CloseLabel2.bind("<Button-1>", Quit2)
        CloseLabel2.grid(row=0, column=0, sticky=E, pady=1, padx=1)
        resultLab = Label(omrWin, text='YOUR RESULT', fg='#f7f8ff', bg='#3d447a', font=("Bahnschrift Light", 30))
        resultLab.pack(side=TOP, fill=X, padx=5, pady=5)
        omrWin.withdraw()
        class Scrollable(Frame):
                def __init__(self, parent, *args, **kw):
                    Frame.__init__(self, parent, *args, **kw)            
                    # create a canvas object and a vertical scrollbar for scrolling it
                    vscrollbar = Scrollbar(self, orient=VERTICAL, width=12)
                    vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
                    canvas = Canvas(self, height=620, bd=0, bg=optionFrameCol, highlightthickness=0,
                                    yscrollcommand=vscrollbar.set)
                    canvas.pack(side=TOP, fill=X, expand=0)
                    vscrollbar.config(command=canvas.yview)
                    # reset the vie
                    canvas.xview_moveto(0)
                    canvas.yview_moveto(0)
                    # create a frame inside the canvas which will be scrolled with it
                    self.interior = interior = Frame(canvas, bg=optionFrameCol)
                    interior_id = canvas.create_window(0, 0, window=interior,
                                                    anchor=NW)
                    # track changes to the canvas and frame width and sync them,
                    # also updating the scrollbar
                    def _on_mousewheel(event):
                        canvas.yview_scroll(int(round(-1*(event.delta/120))), "units")
                    def _configure_interior(event):
                        # update the scrollbars to match the size of the inner frame
                        size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
                        canvas.config(scrollregion="0 0 %s %s" % size)
                        if interior.winfo_reqwidth() != canvas.winfo_width():
                            # update the canvas's width to fit the inner frame
                            canvas.config(width=interior.winfo_reqwidth())
                    interior.bind('<Configure>', _configure_interior)
                    def _bound_to_mousewheel(event):
                        canvas.bind_all("<MouseWheel>", _on_mousewheel)   
                    def _unbound_to_mousewheel(event):
                        canvas.unbind_all("<MouseWheel>") 
                    def _configure_canvas(event):
                        if interior.winfo_reqwidth() != canvas.winfo_width():
                            # update the inner frame's width to fill the canvas
                            canvas.itemconfigure(interior_id, width=canvas.winfo_width())
                    canvas.bind('<Configure>', _configure_canvas)
                    quizWin.bind_all("<MouseWheel>", _on_mousewheel)
                    quizWin.bind('<Enter>', _bound_to_mousewheel)
                    quizWin.bind('<Leave>', _unbound_to_mousewheel)
        ###--TRIFRAMES---###
        toolBar =  Frame(QuizControl, background=toolBarColor, height=20)
        questionFrameScroll = Scrollable(QuizControl, background=optionFrameCol)
        statusFrame =  Frame(QuizControl, background=statusFrameCol, height=20)
        toolBar.pack(side=TOP, fill=X)
        statusFrame.pack(side=BOTTOM, fill=X)
        questionFrameScroll.pack(side=TOP, fill=X)
        ####INSIDE---FRAMES###

        # --------------------------------------------------> THIS FUNCTION IS VERY IMPORTANT AS IT SETTLES THE FILES
        width_img = []
        height_img = []
        
        def GetFiles():
            ##---CSV-FILE-FOR-SOLUTION
            if getSub == 'P':
                subj = 'physics'
            if getSub == 'C':
                subj = 'chemistry'
            if getSub == 'M':
                subj = 'maths'
            if getSub == 'CUS':
                subj = 'custom'
            ##FILE LOCATION
            csvFile = str('_AppData_\\questions\\'+str(subj)+'\\'+str(getChpName)+'\\LEVEL'+str(getLvl)+'\\'+'solution.csv')
            settingFile = str('_AppData_\\questions\\'+str(subj)+'\\'+str(getChpName)+'\\LEVEL'+str(getLvl)+'\\'+'setting.csv')
            qImg = str('_AppData_\\questions\\'+str(subj)+'\\'+str(getChpName)+'\\LEVEL'+str(getLvl)+'\\')

            ##READING CSV FILE
            csvSol = pandas.read_csv(csvFile)
            csvSet = pandas.read_csv(settingFile)
            _option1_ = csvSol['OPTION1'].values.tolist()
            _option2_ = csvSol['OPTION2'].values.tolist()
            _option3_ = csvSol['OPTION3'].values.tolist()
            _option4_ = csvSol['OPTION4'].values.tolist()
            _basewidth_ = csvSet['BASEWIDTH'].values.tolist()
            max_questions = int(len(_option1_))
            ###-MAKING LIST OF TOTAL NO OF QUESTION
            _QuestionNo_ = (list(range(0, int(max_questions))))
            ###-SHUFFLING THE _QuestionNo_
            if int(max_questions) > 50:
                for wait in range(5):
                    random.shuffle(_QuestionNo_)
            else:
                for wait in range(10):
                    random.shuffle(_QuestionNo_)
            print('_QuestionNo_ --> ',_QuestionNo_)
            ###--GETTING THE QUESTIONS AS PER USER SELECTED NUMBER
            final_QNo.extend(_QuestionNo_[0:int(getQNO)])
            print('final_Qno --> ',final_QNo)

            ###---MOVING QUESTION IMAGES AND CSV DATA TO SHUFFLED QUESTION FOLDER
            for qNo in range(int(len(final_QNo))):
                picName = str(final_QNo[qNo])+'.png'
                catchPIC = qImg+picName
                # ------------------------------------------------------------>   RESIZING THE IMAGES
                img = Image.open(catchPIC)
                wpercent = (basewidth/float(img.size[0]))
                hsize = int((float(img.size[1])*float(wpercent)))
                img = img.resize((basewidth,hsize), Image.ANTIALIAS)
                # -------------------------------------------------------------
                #---------------------------------------------------------------> APPENDING QUESTION_IMAGES LIST WITH RESIZED IMAGES
                question_images.append(img)
                # ---------------------------------------------------------------> PRINTING THE STATUS
                #print('===============================================================================')
                #print('Selecting QImg...  --> '+str(catchPIC))
                #print('Resizing QImg...  --> '+str(catchPIC))
                #print('Embeding... --->', question_images[-1])
                #print('===============================================================================')
                # ------------------------------------------------------------> APPENDING RIGHT ANSWERS LIST
                qN = int(final_QNo[qNo])
                # ---------> qN & qNo are different 
                OPTION1.append(_option1_[qN])
                OPTION2.append(_option2_[qN])
                OPTION3.append(_option3_[qN])
                OPTION4.append(_option4_[qN])
                # THIS IS TO CHECK THE SIZE WHILE ZOOMING
                baseNO = int(_basewidth_[int(final_QNo[qNo])])
                print(baseNO)
                if int(zoom_chk[-1]) == 1 and int(baseNO) == 950:
                    resize_list.append(1200)
                elif int(zoom_chk[-1]) == 0 and int(baseNO) == 1200:
                    resize_list.append(950)
                else:
                    resize_list.append(baseNO)
                print('--->', resize_list[qNo])
                ## THE TOTAL NO OF QUEST ---> PREPARING LIST FOR OMR
                timeQ.append(0)
                EntertimeQ.append(0)
                mahaOPT1.append(0)
                mahaOPT2.append(0)
                mahaOPT3.append(0)
                mahaOPT4.append(0)
                visitCHK.append(0)
        GetFiles()
        print('====================================================')
        print('QUESTION SETTING AND QUESTIONS ARE READY')
        visitCHK[0] = 1
        def removeBIND(event):
            play_click()
        ptk = [0.0]
        def FadeWin():
            del ptk[0:-2]
            no = float(ptk[-1])+0.1
            ptk.append(no)
            omrWin.attributes("-alpha", no)
            if ptk[-1] < 1:
                if no == 0.1:
                    omrWin.deiconify()
                omrWin.after(5, FadeWin)
            elif ptk[-1] > 1:
                del ptk[0:-1]
                ptk.append(0.0)

        chk_forTSHC = [0]
        totalSeen = []
        totalCorrect = []
        def PutCorrectOpt():
            if chk_forTSHC[-1] == 0:
                if getSub == 'P':
                    subj = 'physics'
                if getSub == 'C':
                    subj = 'chemistry'
                if getSub == 'M':
                    subj = 'maths'
                if getSub == 'CUS':
                    subj = 'custom'
                settingFile = str('_AppData_\\questions\\'+str(subj)+'\\'+str(getChpName)+'\\LEVEL'+str(getLvl)+'\\'+'setting.csv')
                csvSet = pandas.read_csv(settingFile)
                _totalSeen_ = csvSet['TS'].values.tolist()
                _totalCorrect_ = csvSet['HC'].values.tolist()
                totalSeen.extend(_totalSeen_)
                totalCorrect.extend(_totalCorrect_)
                chk_forTSHC.append(1)
                
            no = int(btnNUM[-1])
            get_o = []
            tC = int(totalCorrect[no])
            tS = int(totalSeen[no])

            if tS == 0:
                acc = 0
            else:
                acc = (tC*100)/tS
            
            if OPTION1[no] == 1:
                get_o.append('(A)')
            if OPTION2[no] == 1:
                get_o.append('(B)')
            if OPTION3[no] == 1:
                get_o.append('(C)')
            if OPTION4[no] == 1:
                get_o.append('(D)')
                
            abcd = ' & '.join([str(elem) for elem in get_o]) 
            correctOpt.set(abcd)
            accQ.set(str(round(acc, 1))+'%')
            if round(acc, 1) < 50:
                accAnLabelShow.configure(bg='#FF0000')
            else:
                accAnLabelShow.configure(bg='#00ff30')
            if int(EntertimeQ[no]) == 0:
                correctAnLabelShow.configure(bg='red')
            elif int(EntertimeQ[no]) == 1:
                correctAnLabelShow.configure(bg='#00ff30')
            if int(timeQ[no]) == 0 or int(timeQ[no]) == 1:
                timetook.set(str(timeQ[no])+' SEC')
            else:
                timetook.set(str(timeQ[no])+' SECS')

        cal = []
        _RESULTGIF_1 = [-1]
        _RESULTGIF_2 = [-1]
        _RESULTGIF_3 = [-1]
        _RESULTGIF_4 = [-1]
        _RESULTGIF_5 = [-1]

        def update_RESULT1():
            i = int(_RESULTGIF_1[-1])+1
            if i == int(cal[0]):
                _RESULTGIF_1.clear()
                _RESULTGIF_1.append(-1)
            else:    
                frame = LoadResultF[i]
                frame1GIF.configure(image=frame)
                _RESULTGIF_1.append(i)
                quizWin.after(40, update_RESULT1)   

        def update_RESULT2():
            i = int(_RESULTGIF_2[-1])+1
            if i == int(cal[1]):
                _RESULTGIF_2.clear()
                _RESULTGIF_2.append(-1)
            else:    
                frame = LoadResultF[i]
                frame2GIF.configure(image=frame)
                _RESULTGIF_2.append(i)
                quizWin.after(40, update_RESULT2)

        def update_RESULT3():
            i = int(_RESULTGIF_3[-1])+1
            if i == int(cal[2]):
                _RESULTGIF_3.clear()
                _RESULTGIF_3.append(-1)
            else:    
                frame = LoadResultF[i]
                frame3GIF.configure(image=frame)
                _RESULTGIF_3.append(i)
                quizWin.after(40, update_RESULT3)


        def update_RESULT4():
            i = int(_RESULTGIF_4[-1])+1
            if i == int(cal[3]):
                _RESULTGIF_4.clear()
                _RESULTGIF_4.append(-1)
            else:    
                frame = LoadResultF[i]
                frame4GIF.configure(image=frame)
                _RESULTGIF_4.append(i)
                quizWin.after(40, update_RESULT4) 

        def CheckFocus(event):
            if quizWin.focus_get() == shadowWin:
                QuitWin()
        
        def EndTest(event):
            if endTEST[-1] == 0:
                response=messagebox.askquestion('END TEST', 'DO YOU WANT TO END TEST?')
                if response == 'yes':
                    print('====================================================')
                    print('TEST ENDED SUCESSFULLY (RESULT BELOW)')
                    option1.bind("<1>", removeBIND)
                    option2.bind("<1>", removeBIND)
                    option3.bind("<1>", removeBIND)
                    option4.bind("<1>", removeBIND)
                    count.append(1)
                    endTEST.append(1)
                    marks = 0
                    correct = 0
                    incorrect = 0
                    EntertimeQ.clear() #Reusing LIST
                    for op in range(int(getQNO)):
                        if int(OPTION1[op]) == int(mahaOPT1[op]) and int(OPTION2[op]) == int(mahaOPT2[op]) and int(OPTION3[op]) == int(mahaOPT3[op]) and int(OPTION4[op]) == int(mahaOPT4[op]):
                            EntertimeQ.append(1)
                            marks += 4
                            correct += 1
                        elif(int(mahaOPT1[op]) == 0 and int(mahaOPT2[op]) == 0 and
                            int(mahaOPT3[op]) == 0 and int(mahaOPT4[op]) == 0):
                            EntertimeQ.append(11)
                            pass
                        else:
                            EntertimeQ.append(0)
                            marks -=1
                            incorrect += 1

                    outOf =str(marks)+'/'+str(int(getQNO)*4)
                    #Totaltime = (int(hour[-1])*60*60)+(int(minute[-1])*60)+(int(second[-1]))
                    Totaltime = (int(sumOfLists(timeQ, len(timeQ))))/len(timeQ)
                    #_AppData_\questions
                    mt = int(int(marks)*100)
                    ed = int(getQNO)*4
                    percentage = mt/ed
                    if int(answeredLabelShow.cget("text")) > 0:
                        speed = int(Totaltime)/int(answeredLabelShow.cget("text"))
                    else:
                        speed = int(0)
                    if getSub == 'P':
                        subj = 'physics'
                    elif getSub == 'C':
                        subj = 'chemistry'
                    elif getSub == 'M':
                        subj = 'maths'
                    elif  getSub == 'CUS':
                        subj = 'custom'
                    path_testD = '_AppData_\\questions\\'+str(subj)+'\\'+str(getChpName)+'\\'+'\\LEVEL'+str(getLvl)+'\\'+'Test_Details.csv'
                    if os.path.exists(path_testD):
                        row_contents = [str(getChpName), int(getLvl), int(Totaltime), int(speed), int(answeredLabelShow.cget("text")), int(unansweredLabelShow.cget("text")), int(correct), int(incorrect), float(percentage)]
                        append_list_as_row(path_testD, row_contents)
                    else:
                        row_contents = ['CHAPTER', 'LEVEL', 'TIME(SECS)', 'SPEED(SECS/Q)','ANSWERED', 'UNANSWERED', 'CORRECT', 'INCORRECT', 'PERCENTAGE']
                        append_list_as_row(path_testD, row_contents)            
                        row_contents2 = [str(getChpName), int(getLvl), int(Totaltime), int(speed), int(answeredLabelShow.cget("text")), int(unansweredLabelShow.cget("text")), int(correct), int(incorrect), float(percentage)]
                        append_list_as_row(path_testD, row_contents2)

                    timetookFrame.pack(side=LEFT, padx=4, pady=5)
                    accFrame.pack(side=LEFT, padx=4, pady=5)
                    correctFrame.pack(side=LEFT, padx=4, pady=5)
                    strAns.set('ANSWERED:   '+str(answeredLabelShow.cget("text")))
                    strUnans.set('UNANSWERED:   '+str(unansweredLabelShow.cget("text")))
                    strcorrect.set('CORRECT:   '+str(correct))
                    strincorrect.set('INCORRECT:   '+str(incorrect))
                    strspeed.set('SPEED(SECS/Q): '+str(round(speed)))
                    strmarks.set('MARKS: '+str(outOf))

                    print('----------------------------------------------------')
                    print('TOTAL TIME: ', Totaltime)
                    print('ANSWERED:   '+str(answeredLabelShow.cget("text")))
                    print('UNANSWERED:   '+str(unansweredLabelShow.cget("text")))
                    print('CORRECT:   '+str(correct))
                    print('INCORRECT:   '+str(incorrect))
                    print('SPEED(SECS/Q):   '+str(speed))
                    print('MARKS:   '+str(outOf))
                    print('----------------------------------------------------')
                    print('====================================================')

                    cal.append(int(round(((int(answeredLabelShow.cget("text"))*100)/int(getQNO))/10)))
                    cal.append(int(round(((int(unansweredLabelShow.cget("text"))*100)/int(getQNO))/10)))
                    if int(answeredLabelShow.cget("text")) > 0:
                        cal.append(int(round(((int(correct)*100)/int(answeredLabelShow.cget("text")))/10)))
                        cal.append(int(round(((int(incorrect)*100)/int(answeredLabelShow.cget("text")))/10)))
                    else:
                        cal.append(0)
                        cal.append(0)                            

                    # SAVING THE BASEWIDTH
                    csvSetting = str('_AppData_\\questions\\'+str(subj)+'\\'+str(getChpName)+'\\LEVEL'+str(getLvl)+'\\'+'setting.csv')
                    r = csv.reader(open(csvSetting)) # Here your csv file
                    lines = list(r)
                    
                    for bw in range(int(getQNO)):
                        lines[int(final_QNo[bw])+1][0] = resize_list[bw] # ADDING 1 B'COZ 'BASEWIDTH' WILL BE COUNTED AS 0.
                        if visitCHK[bw] == 1:
                            lines[int(final_QNo[bw])+1][1] = int(lines[int(final_QNo[bw])+1][1])+1
                        if (int(OPTION1[bw]) == int(mahaOPT1[bw]) and int(OPTION2[bw]) == int(mahaOPT2[bw]) and
                            int(OPTION3[bw]) == int(mahaOPT3[bw]) and int(OPTION4[bw]) == int(mahaOPT4[bw])):
                            lines[int(final_QNo[bw])+1][2] = int(lines[int(final_QNo[bw])+1][2])+1

                    with open(csvSetting, mode='w', newline='') as setting_file:
                        setting_writer = csv.writer(setting_file)
                        setting_writer.writerows(lines)
                    
                    final_QNo.clear()
                    PutCorrectOpt()
                    # STARTING THE WINDOW
                    FadeWin()
                    play_whoosh()
                    CheckCOL()
                    update_RESULT1()
                    update_RESULT2()
                    update_RESULT3()
                    update_RESULT4()
                    #Fade_Out2()
                    shadowWin.attributes("-alpha", 0.8)
                    shadowWin.focus_force()
                    omrWin.focus_force()
                    quizWin.bind('<Expose>', CheckFocus)
                    
                else:
                    pass
                    quizWin.focus_force()
            else:
                FadeWin()
                play_whoosh()
                update_RESULT1()
                update_RESULT2()
                update_RESULT3()
                update_RESULT4()
                #Fade_Out2()
                shadowWin.attributes("-alpha", 0.8)
                shadowWin.focus_force()
                omrWin.focus_force()

        # ----------------->  INSIDE--OMR--WIN

        strAns = StringVar()
        strUnans = StringVar()
        strcorrect = StringVar()
        strincorrect = StringVar()
        strmarks = StringVar()
        strspeed = StringVar()

        outD = Frame(omrWin, background='gray85',width=200)
        frame1 = Frame(omrWin, background=QuizControlColor)
        frame2 = Frame(omrWin, background=QuizControlColor)
        frame3 = Frame(omrWin, background=QuizControlColor)
        frame4 = Frame(omrWin, background=QuizControlColor)
        outD.pack(side=TOP, padx=2, pady=1)
        frame1.pack(side=TOP, fill=X, padx=5, pady=5)
        frame2.pack(side=TOP, fill=X, padx=5, pady=5)
        frame3.pack(side=TOP, fill=X, padx=5, pady=5)
        frame4.pack(side=TOP, fill=X, padx=5, pady=5)

        resultBgCol = '#373d6e'
        ansLab = Label(frame1, anchor='w', textvariable=strAns, text='ANSWERED:', fg='white', bg=resultBgCol, font=("Bahnschrift", 24))
        ansLab.pack(side=TOP, fill=X)
        frame1GIF = Label(frame1, bg=QuizControlColor, image=LoadResultF[0])
        frame1GIF.pack(side=TOP, fill=X)

        unansLab = Label(frame2, anchor='w', textvariable=strUnans, text='UNANSWERED:', fg='white', bg=resultBgCol, font=("Bahnschrift", 24))
        unansLab.pack(side=TOP, fill=X)
        frame2GIF = Label(frame2, bg=QuizControlColor, image=LoadResultF[0])
        frame2GIF.pack(side=TOP, fill=X)

        correctLab = Label(frame3, anchor='w', textvariable=strcorrect, text='CORRECT:', fg='white', bg=resultBgCol, font=("Bahnschrift", 24))
        correctLab.pack(side=TOP, fill=X)
        frame3GIF = Label(frame3, bg=QuizControlColor, image=LoadResultF[0])
        frame3GIF.pack(side=TOP, fill=X)

        incorrectLab = Label(frame4, anchor='w', textvariable=strincorrect, text='INCORRECT:', fg='white', bg=resultBgCol, font=("Bahnschrift", 24))
        incorrectLab.pack(side=TOP, fill=X)
        frame4GIF = Label(frame4, bg=QuizControlColor, image=LoadResultF[0])
        frame4GIF.pack(side=TOP, fill=X)
        
        marksLab = Label(omrWin, anchor='w', textvariable=strmarks, text='MARKS:', fg='white', bg='#3d447a', font=("Bahnschrift", 24))
        marksLab.pack(side=BOTTOM, fill=X, padx=5, pady=5)

        outD2 = Frame(omrWin, background='gray85',width=300)
        outD2.pack(side=BOTTOM, padx=2, pady=2)

        speedLab = Label(omrWin, anchor='w', textvariable=strspeed, text='SPEED:', fg='white', bg='#3d447a', font=("Bahnschrift", 24))
        speedLab.pack(side=BOTTOM, fill=X, padx=5, pady=5)

        def Check_CheckBTN():
            Opt4frames
            if endTEST[-1] == 0:
                ### ------------------------------------------->> OPTION 1 
                if mahaOPT1[int(btnNUM[-1])] == 0:
                    option1.configure(image=Opt1frames[0])
                elif mahaOPT1[int(btnNUM[-1])] == 1:
                    option1.configure(image=Opt1frames[10])

                ### ------------------------------------------->> OPTION 2 
                if mahaOPT2[int(btnNUM[-1])] == 0:
                    option2.configure(image=Opt2frames[0])
                elif mahaOPT2[int(btnNUM[-1])] == 1:
                    option2.configure(image=Opt2frames[10])

                ### ------------------------------------------->> OPTION 3
                if mahaOPT3[int(btnNUM[-1])] == 0:
                    option3.configure(image=Opt3frames[0])
                elif mahaOPT3[int(btnNUM[-1])] == 1:
                    option3.configure(image=Opt3frames[10])

                ### ------------------------------------------->> OPTION 4
                if mahaOPT4[int(btnNUM[-1])] == 0:
                    option4.configure(image=Opt4frames[0])
                elif mahaOPT4[int(btnNUM[-1])] == 1:
                    option4.configure(image=Opt4frames[10])

            if endTEST[-1] == 1:
                ### ------------------------------------------->> OPTION 1 
                if mahaOPT1[int(btnNUM[-1])] == 0:
                    option1.configure(image=Opt1frames[0])
                elif mahaOPT1[int(btnNUM[-1])] == 1 and int(OPTION1[int(btnNUM[-1])]) == int(mahaOPT1[int(btnNUM[-1])]):
                    option1.configure(image=Opt1frames[11])
                else:
                    option1.configure(image=Opt1frames[12])

                ### ------------------------------------------->> OPTION 2 
                if mahaOPT2[int(btnNUM[-1])] == 0:
                    option2.configure(image=Opt2frames[0])
                elif mahaOPT2[int(btnNUM[-1])] == 1 and int(OPTION2[int(btnNUM[-1])]) == int(mahaOPT2[int(btnNUM[-1])]):
                    option2.configure(image=Opt2frames[11])
                else:
                    option2.configure(image=Opt2frames[12])

                ### ------------------------------------------->> OPTION 3
                if mahaOPT3[int(btnNUM[-1])] == 0:
                    option3.configure(image=Opt3frames[0])
                elif mahaOPT3[int(btnNUM[-1])] == 1 and int(OPTION3[int(btnNUM[-1])]) == int(mahaOPT3[int(btnNUM[-1])]):
                    option3.configure(image=Opt3frames[11])
                else:
                    option3.configure(image=Opt3frames[12])

                ### ------------------------------------------->> OPTION 4
                if mahaOPT4[int(btnNUM[-1])] == 0:
                    option4.configure(image=Opt4frames[0])
                elif mahaOPT4[int(btnNUM[-1])] == 1 and int(OPTION4[int(btnNUM[-1])]) == int(mahaOPT4[int(btnNUM[-1])]):
                    option4.configure(image=Opt4frames[11])
                else:
                    option4.configure(image=Opt4frames[12])

        # ======================= -------> UPDATING ANSWERED/UNANSWERED
        def Update_ANS():
            length = int(len(mahaOPT1))
            ans = 0
            unans = 0
            for op in range(length):
                if mahaOPT1[op] == 1 or mahaOPT2[op] == 1 or mahaOPT3[op] == 1 or mahaOPT4[op] == 1:
                    ans += 1
                else:
                    unans += 1
                ansVar.set(str(ans))
                unansVar.set(str(unans))

        # ======================= -------> This runs for GIVING the OMR button right COLORS
        AutoDetails = []
        def CalScrollbar():
            canvas_width = float(canvas.winfo_width())
            scroll_width = float(buttonFrame.winfo_width())
            percent = round((canvas_width*100)/scroll_width, 8)
            AutoDetails.append(canvas_width)
            AutoDetails.append(scroll_width)
            AutoDetails.append(percent)
            AutoDetails.append(0)            
        def AutoForward():
            if int(zoom_chk[-1]) == 0:
                att = (int(btnNUM[-1]+1) // 18)
            else:
                att = (int(btnNUM[-1]+1) // 19)
            if len(AutoDetails) == 0:
                CalScrollbar()
            canvas_width = AutoDetails[0]
            scroll_width = AutoDetails[1]
            percent = AutoDetails[2]
            AutoDetails[3] = float(percent/100)*(att-1)
            canvas.xview_moveto(float(percent/100)*att)
        def AutoBackward():
            if int(zoom_chk[-1]) == 0:
                if int(btnNUM[-2]+1) % 18 == 0:
                    canvas.xview_moveto(float(AutoDetails[3]))
            else:
                if int(btnNUM[-2]+1) % 19 == 0:
                    canvas.xview_moveto(float(AutoDetails[3]))

        # THIS IS TO CHANGE THE COLOR OF OMR BUTTON
        def CheckCOL():
            length = int(len(mahaOPT1))
            for i in range(length):
                if i != int(lockedBTN[-1]):
                    if int(mahaOPT1[i]) == 1 or int(mahaOPT2[i]) == 1 or int(mahaOPT3[i]) == 1 or int(mahaOPT4[i]) == 1:
                        omrBtnList[i].configure(image=omrBtn_answered, fg="white")
                    elif visitCHK[i] == 1:
                        omrBtnList[i].configure(image=visited_unanwered, fg="white")
                    else:
                        omrBtnList[i].configure(image=omrBtn_unanswer, fg="white")
                else:
                    omrBtnList[i].configure(image=omrBtn_selected, fg="#6fa5fd")
            # ---> TO TELL THE RIGHT OPTION
            if endTEST[-1] == 1:
                PutCorrectOpt()

        def OpenOMR(event):
            FadeWin()
            CheckCOL()

        ENDGIF_CHK = [0]
        ENDGIF_CHK2 = [7]

        def omrBtnIn2():
            i = int(ENDGIF_CHK[-1])+1
            if i == 7:
                ENDGIF_CHK.clear()
                ENDGIF_CHK.append(0)
            else:
                frame = Endtestframes[i]
                omrBtn.configure(image=frame)
                quizWin.after(15, omrBtnIn2)
                ENDGIF_CHK.append(i)
        def omrBtnIn(event):
            #omrBtn.configure(image=omrBTNImg2, cursor='hand2')
            omrBtnIn2()

        def omrBtnOut2():
            i = int(ENDGIF_CHK2[-1])-1
            if i == -1:
                ENDGIF_CHK2.clear()
                ENDGIF_CHK2.append(7)
            else:
                frame = Endtestframes[i]
                omrBtn.configure(image=frame)
                quizWin.after(15, omrBtnOut2)
                ENDGIF_CHK2.append(i)
        def omrBtnOut(event):
            #omrBtn.configure(image=omrBTNImg)
            omrBtnOut2()

        # ======================= -------> This runs when you the click the OMR button
        def SetImage(event):
            play_click()
            del btnNUM[0:-2]
            del lockedBTN[0:-2]
            ab = event.widget
            no = int(ab.cget("text"))
            if visitCHK[int(no)-1] == 0:
                visitCHK[int(no)-1] = 1
            if endTEST[-1] == 0:
                Totaltime = (int(hour[-1])*60*60)+(int(minute[-1])*60)+(int(second[-1]))
                EntertimeQ[no-1] = Totaltime
            qLabelT.set(str(no)+')')
            new_width = int(round(resize_list[no-1]))
            wpercent = (new_width/float(question_images[no-1].size[0]))
            new_hsize = int((float(question_images[no-1].size[1])*float(wpercent)))
            finalIMG = question_images[no-1].resize((new_width,new_hsize), Image.ANTIALIAS)   
            ex = ImageTk.PhotoImage(finalIMG)
            questionImage.configure(image=ex)
            questionImage.image = ex
            btnNUM.append(int(no)-1)
            lockedBTN.append(int(no)-1)
            CheckCOL()
            CalScrollbar()
            Check_CheckBTN()


        def omrBTN_EN(event):
            ab = event.widget
            no = int(ab.cget("text"))-1
            if endTEST[-1] == 0:
                opt1 = int(mahaOPT1[no])
                opt2 = int(mahaOPT2[no])
                opt3 = int(mahaOPT3[no])
                opt4 = int(mahaOPT4[no])
                if no != int(lockedBTN[-1]):
                    if opt1 == 1 or opt2 == 1 or opt3 == 1 or opt4 == 1:
                        ab.configure(cursor='hand2', image=omrBtn_answered_hover)
                    elif visitCHK[no] == 1:
                        ab.configure(cursor='hand2', image=visited_unanwered_hover)
                    else:
                        ab.configure(cursor='hand2', image=omrBtn_Hover)
                else:
                    ab.configure(cursor='hand2', image=omrBtn_selected)

            #-----------------------AFTER TEST ENDS
            if endTEST[-1] == 1:
                length = int(len(mahaOPT1))
                if no != int(lockedBTN[-1]):
                    if int(EntertimeQ[no]) == 1:
                        ab.configure(cursor='hand2', image=omrBtn_answered_hover)
                    elif int(EntertimeQ[no]) == 0:
                        ab.configure(cursor='hand2', image=visited_unanwered_hover)
                    else:
                        ab.configure(cursor='hand2', image=omrBtn_Hover)
                else:
                    ab.configure(image=omrBtn_selected)

        def omrBTN_LEAVE(event):
            ab = event.widget
            no = int(ab.cget("text"))-1
            if endTEST[-1] == 0:
                opt1 = int(mahaOPT1[no])
                opt2 = int(mahaOPT2[no])
                opt3 = int(mahaOPT3[no])
                opt4 = int(mahaOPT4[no])
                if no != int(lockedBTN[-1]):
                    if opt1 == 1 or opt2 == 1 or opt3 == 1 or opt4 == 1:
                        ab.configure(cursor='hand2', image=omrBtn_answered)
                    elif visitCHK[no] == 1:
                        ab.configure(cursor='hand2', image=visited_unanwered)
                    else:
                        ab.configure(image=omrBtn_unanswer)
                else:
                    omrBtnList[no].configure(image=omrBtn_selected)

            #------------------AFTER TEST ENDS
            if endTEST[-1] == 1:
                length = int(len(mahaOPT1))
                if no != int(lockedBTN[-1]):
                    if int(EntertimeQ[no]) == 1:
                        ab.configure(image=omrBtn_answered)
                    elif int(EntertimeQ[no]) == 0:
                        ab.configure(image=visited_unanwered)
                    else:
                        ab.configure(image=omrBtn_unanswer)
                else:
                    ab.configure(image=omrBtn_selected)
        def Zoom_In():
            del btnNUM[0:-2]
            num = int(btnNUM[-1])
            # ------------------------------------------------------------>   RESIZING THE IMAGES
            new_width = int(round(resize_list[num]))+100
            resize_list[num] = new_width
            wpercent = (new_width/float(question_images[num].size[0]))
            new_hsize = int((float(question_images[num].size[1])*float(wpercent)))
            img = question_images[num].resize((new_width,new_hsize), Image.ANTIALIAS)
            exam = ImageTk.PhotoImage(img)
            questionImage.configure(image=exam)
            questionImage.image = exam
            
        def Zoom_In2(event):
             Zoom_In()

        def Zoom_Out(event):
            del btnNUM[0:-2]
            num = int(btnNUM[-1])
            if resize_list[num] > 60:
                # ------------------------------------------------------------>   RESIZING THE IMAGES
                new_width = int(round(resize_list[num]))-100
                resize_list[num] = new_width
                wpercent = (new_width/float(question_images[num].size[0]))
                new_hsize = int((float(question_images[num].size[1])*float(wpercent)))
                img = question_images[num].resize((new_width,new_hsize), Image.ANTIALIAS)
                exam = ImageTk.PhotoImage(img)
                questionImage.configure(image=exam)
                questionImage.image = exam
            else:
                messagebox.showerror("WARNING", "CAN'T ZOOM IN MORE!+++")
                quizWin.focus_force()
                Zoom_In()
                Zoom_In()
                Zoom_In()
                Zoom_In()

        quizWin.bind("<+>", Zoom_In2)
        quizWin.bind("-", Zoom_Out)

        def Next_In(event):
            nextButton.configure(image=nextBTNH, cursor='hand2', bg='#262c72')
        def Next_Out(event):
            nextButton.configure(image=nextBTN, bg=omrRowCol)
        def Previous_In(event):
            previousButton.configure(image=previousBTNH, cursor='hand2', bg='#262c72')
        def Previous_Out(event):
            previousButton.configure(image=previousBTN, bg=omrRowCol)

        # ======================= -------> This runs when you the previous button    
        def PREVIOUS(event):
            if (OPT1GIF_CHK[-1] == 0 and OPT1GIF_CHK2[-1] == 10 and OPT2GIF_CHK[-1] == 0 and OPT2GIF_CHK2[-1] == 10 and
            OPT3GIF_CHK[-1] == 0 and OPT3GIF_CHK2[-1] == 10 and OPT4GIF_CHK[-1] == 0 and OPT4GIF_CHK2[-1] == 10):
                del btnNUM[0:-2]
                del lockedBTN[0:-2]
                no = int(btnNUM[-1])-1
                if endTEST[-1] == 0:
                    Totaltime = (int(hour[-1])*60*60)+(int(minute[-1])*60)+(int(second[-1]))
                    EntertimeQ[no] = Totaltime               
                if no >= 0:
                    if visitCHK[int(no)] == 0:
                        visitCHK[int(no)] = 1
                    qLabelT.set(str(no+1)+')')
                    new_width = int(round(resize_list[no]))
                    wpercent = (new_width/float(question_images[no].size[0]))
                    new_hsize = int((float(question_images[no].size[1])*float(wpercent)))
                    finalIMG = question_images[no].resize((new_width,new_hsize), Image.ANTIALIAS)   
                    ex = ImageTk.PhotoImage(finalIMG)
                    questionImage.configure(image=ex)
                    questionImage.image = ex
                    btnNUM.append(int(no))
                    lockedBTN.append(int(no))
                    CheckCOL()
                    AutoBackward()
                    Check_CheckBTN()
        # ======================= -------> This runs when you the next button
        def NEXT(event):
            if (OPT1GIF_CHK[-1] == 0 and OPT1GIF_CHK2[-1] == 10 and OPT2GIF_CHK[-1] == 0 and OPT2GIF_CHK2[-1] == 10 and
            OPT3GIF_CHK[-1] == 0 and OPT3GIF_CHK2[-1] == 10 and OPT4GIF_CHK[-1] == 0 and OPT4GIF_CHK2[-1] == 10):
                del btnNUM[0:-2]
                del lockedBTN[0:-2]
                no = int(btnNUM[-1])+1
                if endTEST[-1] == 0 and no < getQNO:
                    Totaltime = (int(hour[-1])*60*60)+(int(minute[-1])*60)+(int(second[-1]))
                    EntertimeQ[no] = Totaltime
                if no < getQNO:
                    if visitCHK[int(no)] == 0:
                        visitCHK[int(no)] = 1
                    qLabelT.set(str(no+1)+')')
                    new_width = int(round(resize_list[no]))
                    wpercent = (new_width/float(question_images[no].size[0]))
                    new_hsize = int((float(question_images[no].size[1])*float(wpercent)))
                    finalIMG = question_images[no].resize((new_width,new_hsize), Image.ANTIALIAS)   
                    ex = ImageTk.PhotoImage(finalIMG)
                    questionImage.configure(image=ex)
                    questionImage.image = ex
                    btnNUM.append(int(no))
                    lockedBTN.append(int(no))
                    CheckCOL()
                    AutoForward()
                    Check_CheckBTN()
                
        # ==================== -----------------------------> BINDING NEXT/PREVIOUS FUNCTION TO QUIZWIN
        quizWin.bind("<Left>", PREVIOUS)
        quizWin.bind("<Right>", NEXT)
        # ===================================== SETTING OMR SCROLLBAR ======================================
        OPTION_BIND = Frame(toolBar, background=toolBarColor)
        OPTION_BIND.pack(side=TOP, fill=X)

        def onFrameConfigure(canvas):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))

        previousButton = Label(OPTION_BIND, image=previousBTN, cursor='hand2', height=63, bg=omrRowCol)
        if zoom_chk[-1] == 1:
            print(int(quizWin.winfo_width()))
            canvas = Canvas(OPTION_BIND, borderwidth=0, height=65, width=int(1306), highlightthickness=1, highlightbackground=omrRowCol, background=omrRowCol)
        else:
            canvas = Canvas(OPTION_BIND, borderwidth=0, height=65, width=1242, highlightthickness=1, highlightbackground=omrRowCol, background=omrRowCol)
        buttonFrame = Frame(canvas, background=omrRowCol)

        vsb = Scrollbar(toolBar, orient="horizontal", command=canvas.xview, width=12)
        canvas.configure(xscrollcommand=vsb.set)

        nextButton = Label(OPTION_BIND, image=nextBTN, cursor='hand2', height=63, bg=omrRowCol)
        previousButton.bind("<1>", PREVIOUS)
        nextButton.bind("<1>", NEXT)

        nextButton.bind("<Enter>", Next_In)
        nextButton.bind("<Leave>", Next_Out)
        previousButton.bind("<Enter>", Previous_In)
        previousButton.bind("<Leave>", Previous_Out)

        previousButton.grid(row=0, column=0, pady=4)

        vsb.pack(side=BOTTOM, fill=X)
        canvas.grid(row=0, column=1, pady=4)
        canvas.create_window((0,0), window=buttonFrame, anchor="nw")

        buttonFrame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

        nextButton.grid(row=0, column=2, pady=4)

        # ====================================================================== -----> CREATING TOTAL OMR BUTTONS AND APPENDING THE LIST
        row = 0
        column = 0
        for omr in range(int(getQNO )):
            tk = StringVar()
            omr_unanswer = Label(buttonFrame, textvariable=tk, bg=omrRowCol, image=omrBtn_unanswer, compound='center', font=("Bahnschrift Light", 20))
            omr_unanswer.grid(row=row, column=column, padx=2, pady=2)
            tk.set(str(int(omr)+1))
            omr_unanswer.configure(fg="white")
            omrBtnList.append(omr_unanswer)
            omr_unanswer.bind('<1>', SetImage)
            omr_unanswer.bind("<Enter>", omrBTN_EN)
            omr_unanswer.bind("<Leave>", omrBTN_LEAVE)
            #if column!=3:
            #    column += 1
            #if column == 3:
            #    column = 0
            #    row += 1
            column += 1

        omrBtnList[0].configure(image=omrBtn_selected)

        #### ------------------------------->>> THIS IS FOR OPTION 1
        def update_opt1():
            i = int(OPT1GIF_CHK[-1])+1
            if i == 11:
                OPT1GIF_CHK.clear()
                OPT1GIF_CHK.append(0)
            else:    
                frame = Opt1frames[i]
                option1.configure(image=frame)
                quizWin.after(10, update_opt1)
                OPT1GIF_CHK.append(i)        

        def reverse_opt1():
            i = int(OPT1GIF_CHK2[-1])-1
            if i == -1:
                OPT1GIF_CHK2.clear()
                OPT1GIF_CHK2.append(10)
            else:
                frame = Opt1frames[i]
                option1.configure(image=frame)
                quizWin.after(10, reverse_opt1)
                OPT1GIF_CHK2.append(i)

        #### ------------------------------->>> THIS IS FOR OPTION 2 
        def update_opt2():
            i = int(OPT2GIF_CHK[-1])+1
            if i == 11:
                OPT2GIF_CHK.clear()
                OPT2GIF_CHK.append(0)
            else:    
                frame = Opt2frames[i]
                option2.configure(image=frame)
                quizWin.after(10, update_opt2)
                OPT2GIF_CHK.append(i)
        def reverse_opt2():
            i = int(OPT2GIF_CHK2[-1])-1
            if i == -1:
                OPT2GIF_CHK2.clear()
                OPT2GIF_CHK2.append(10)
            else:
                frame = Opt2frames[i]
                option2.configure(image=frame)
                quizWin.after(10, reverse_opt2)
                OPT2GIF_CHK2.append(i)

        #### ------------------------------->>> THIS IS FOR OPTION 3
        def update_opt3():
            i = int(OPT3GIF_CHK[-1])+1
            if i == 11:
                OPT3GIF_CHK.clear()
                OPT3GIF_CHK.append(0)
            else:    
                frame = Opt3frames[i]
                option3.configure(image=frame)
                quizWin.after(10, update_opt3)
                OPT3GIF_CHK.append(i)
        def reverse_opt3():
            i = int(OPT3GIF_CHK2[-1])-1
            if i == -1:
                OPT3GIF_CHK2.clear()
                OPT3GIF_CHK2.append(10)
            else:
                frame = Opt3frames[i]
                option3.configure(image=frame)
                quizWin.after(10, reverse_opt3)
                OPT3GIF_CHK2.append(i)

        #### ------------------------------->>> THIS IS FOR OPTION 4
        def update_opt4():
            i = int(OPT4GIF_CHK[-1])+1
            if i == 11:
                OPT4GIF_CHK.clear()
                OPT4GIF_CHK.append(0)
            else:
                frame = Opt4frames[i]
                option4.configure(image=frame)
                quizWin.after(10, update_opt4)
                OPT4GIF_CHK.append(i)
        def reverse_opt4():
            i = int(OPT4GIF_CHK2[-1])-1
            if i == -1:
                OPT4GIF_CHK2.clear()
                OPT4GIF_CHK2.append(10)
            else:
                frame = Opt4frames[i]
                option4.configure(image=frame)
                quizWin.after(10, reverse_opt4)
                OPT4GIF_CHK2.append(i)

        def CalTime():
            no = btnNUM[-1]
            Totaltime = (int(hour[-1])*60*60)+(int(minute[-1])*60)+(int(second[-1]))
            timeQ[no] = Totaltime-EntertimeQ[no]
            #print(timeQ[no])

        def CalTime2():
            no = btnNUM[-1]
            Totaltime = (int(hour[-1])*60*60)+(int(minute[-1])*60)+(int(second[-1]))
            if mahaOPT1[no] == 1 or mahaOPT2[no] == 1 or mahaOPT3[no] == 1 or mahaOPT4[no] == 1:
                pass
            else:
                timeQ[no] = 0
            #print(timeQ[no])

        # ===============================================================> THIS RUNS WHEN YOU CLICK ON OPTION 1   
        def ClickOnA(event):
            if endTEST[-1] == 0:
                if mahaOPT1[int(btnNUM[-1])] == 0:
                    mahaOPT1[int(btnNUM[-1])] = 1
                    update_opt1()
                    CalTime()
                elif mahaOPT1[int(btnNUM[-1])] == 1:
                    mahaOPT1[int(btnNUM[-1])] = 0
                    reverse_opt1()
                    CalTime2()
                Update_ANS()

        # ===============================================================> THIS RUNS WHEN YOU CLICK ON OPTION 2
        def ClickOnB(event):
            if endTEST[-1] == 0:
                if mahaOPT2[int(btnNUM[-1])] == 0:
                    mahaOPT2[int(btnNUM[-1])] = 1
                    update_opt2()
                    CalTime()
                elif mahaOPT2[int(btnNUM[-1])] == 1:
                    mahaOPT2[int(btnNUM[-1])] = 0
                    reverse_opt2()
                    CalTime2()
                Update_ANS()

        # ===============================================================> THIS RUNS WHEN YOU CLICK ON OPTION 3
        def ClickOnC(event):
            if endTEST[-1] == 0:
                if mahaOPT3[int(btnNUM[-1])] == 0:
                    mahaOPT3[int(btnNUM[-1])] = 1
                    update_opt3()
                    CalTime()
                elif mahaOPT3[int(btnNUM[-1])] == 1:
                    mahaOPT3[int(btnNUM[-1])] = 0
                    reverse_opt3()
                    CalTime2()
                Update_ANS()

        # ===============================================================> THIS RUNS WHEN YOU CLICK ON OPTION 4
        def ClickOnD(event):
            if endTEST[-1] == 0:
                Update_ANS()
                if mahaOPT4[int(btnNUM[-1])] == 0:
                    mahaOPT4[int(btnNUM[-1])] = 1
                    update_opt4()
                    CalTime()
                elif mahaOPT4[int(btnNUM[-1])] == 1:
                    mahaOPT4[int(btnNUM[-1])] = 0
                    reverse_opt4()
                    CalTime2()
                Update_ANS()

        t = StringVar()
        ansVar = StringVar()
        unansVar = StringVar()
        correctOpt = StringVar()
        timetook = StringVar()
        accQ = StringVar()
        t.set("00:00:00")
        ansVar.set(str(0))
        unansVar.set(str(len(mahaOPT1)))

        ## -----------------> THIS IS THE GUI CONTROL WIDGETS
        IconLabel = Label(GuiControl, bg=GuiControlColor, image=Icon)
        IconLabel.pack(side=LEFT, pady=1, padx=1)
        TitleLabel = Label(GuiControl, width=80, textvariable=t, bg=GuiControlColor, font=("Bahnschrift Light", 18), fg="#6fa5fd")
        if int(zoom_chk[-1]) == 1:
            TitleLabel.pack(side=LEFT, padx=125)
        else:    
            TitleLabel.pack(side=LEFT, padx=91)

        ###STATUSFRAME--CONTAIN###
        answeredFrame = Frame(statusFrame, background=sFrameLabCol)
        unansweredFrame = Frame(statusFrame, background=sFrameLabCol)
        timetookFrame = Frame(statusFrame, background=sFrameLabCol)
        accFrame = Frame(statusFrame, background=sFrameLabCol)
        correctFrame = Frame(statusFrame, background=sFrameLabCol)
        answeredFrame.pack(side=LEFT, padx=8, pady=5)
        unansweredFrame.pack(side=LEFT, padx=4, pady=5)


        answeredLabel = Label(answeredFrame, bg=sFrameLabCol, text='ANSWERED:', font=("Bahnschrift Light", 15), fg='#2a2a2a')
        answeredLabel.pack(side=LEFT)
        answeredLabelShow = Label(answeredFrame, anchor='w', bg='#cdc1fe', textvariable=ansVar, font=("Bahnschrift Light", 15), fg='#3000ff')
        answeredLabelShow.pack(side=LEFT)
        unansweredLabel = Label(unansweredFrame, bg=sFrameLabCol, text='UNANSWERED:', font=("Bahnschrift Light", 15), fg='#2a2a2a')
        unansweredLabel.pack(side=LEFT)
        unansweredLabelShow = Label(unansweredFrame, anchor='w', bg='#cdc1fe', textvariable=unansVar, font=("Bahnschrift Light", 15), fg='#3000ff')
        unansweredLabelShow.pack(side=LEFT)

        timeAnLabel = Label(timetookFrame , bg=sFrameLabCol, text='TIME TOOK:', font=("Bahnschrift Light", 15), fg='#2a2a2a')
        timeAnLabel.pack(side=LEFT)
        timeAnLabelShow = Label(timetookFrame, anchor='w', bg='#cdc1fe', textvariable=timetook, font=("Bahnschrift Light", 15), fg='#3000ff')
        timeAnLabelShow.pack(side=LEFT)

        accAnLabel = Label(accFrame, bg=sFrameLabCol, text='ACCURACY:', font=("Bahnschrift Light", 15), fg='#2a2a2a')
        accAnLabel.pack(side=LEFT)
        accAnLabelShow = Label(accFrame, anchor='w', bg='#00ff30', textvariable=accQ, font=("Bahnschrift Light", 15), fg=statusFrameCol)
        accAnLabelShow.pack(side=LEFT)

        correctAnLabel = Label(correctFrame, bg=sFrameLabCol, text='CORRECT OPTION:', font=("Bahnschrift Light", 15), fg='#2a2a2a')
        correctAnLabel.pack(side=LEFT)
        correctAnLabelShow = Label(correctFrame, anchor='w', bg='#00ff30', textvariable=correctOpt, font=("Bahnschrift Light", 15), fg=statusFrameCol)
        correctAnLabelShow.pack(side=LEFT)

        ###OMR BUTTON
        omrt = StringVar()
        omrBtn = Label(statusFrame, textvariable=omrt, cursor='hand2', image=Endtestframes[0], bg=statusFrameCol)
        omrBtn.bind("<Enter>", omrBtnIn)
        omrBtn.bind("<Leave>", omrBtnOut)
        omrBtn.bind("<1>", EndTest)
        omrBtn.pack(side=RIGHT)
        ###EVERYTHING ABOUT QUESTION N OPTION
        questionFrame = Frame(questionFrameScroll.interior, background='white')
        optionFrame = Frame(questionFrameScroll.interior, height=500, background=optionFrameCol)
        questionFrame.pack(fill=BOTH, padx=5, pady=5)
        optionFrame.pack(fill=BOTH, padx=5, pady=5)

        newidth = int(round(resize_list[0]))
        wper = (newidth/float(question_images[0].size[0]))
        newhsize = int((float(question_images[0].size[1])*float(wper)))
        finalIMG = question_images[0].resize((newidth,newhsize), Image.ANTIALIAS)
        first_question = ImageTk.PhotoImage(finalIMG)
        
        qLabelT = StringVar()
        qLabelT.set('1)')
        questionHolderFrame = Frame(questionFrame, background='white', width= 1300)
        qLabel = Label(questionHolderFrame, textvariable=qLabelT, bg='#2A324A', fg="white", font=("Bahnschrift Light", 80))
        questionImage = Label(questionHolderFrame, anchor='w', image=first_question, bg='white')
        questionImage.image = first_question
        questionHolderFrame.pack(side=TOP, fill=X)
        qLabel.pack(side=LEFT, fill=Y)
        questionImage.pack(side=LEFT, fill=X, expand=1)


        catchAC = Frame(optionFrame, background=optionFrameCol)
        dividerOption = Frame(optionFrame, background='#2A324A')
        catchBD = Frame(optionFrame, background=optionFrameCol)
        catchAC.pack(side=LEFT, fill=BOTH)
        if int(zoom_chk[-1]) == 1:
            dividerOption.pack(side=LEFT, pady=10, padx=40, fill=Y)
        else:
            dividerOption.pack(side=LEFT, pady=10, fill=Y)
        catchBD.pack(side=RIGHT, fill=BOTH)
        
        option1 = Label(catchAC, cursor='hand2', image=Opt1frames[0], bg=optionFrameCol)
        option2 = Label(catchBD, cursor='hand2', image=Opt2frames[0], bg=optionFrameCol)
        option3 = Label(catchAC, cursor='hand2', image=Opt3frames[0], bg=optionFrameCol)
        option4 = Label(catchBD, cursor='hand2', image=Opt4frames[0], bg=optionFrameCol)
        option1.bind("<1>", ClickOnA)
        option2.bind("<1>", ClickOnB)
        option3.bind("<1>", ClickOnC)
        option4.bind("<1>", ClickOnD)

        option1.grid(row=0, column=0, padx=45, pady=2)
        option2.grid(row=0, column=1, padx=45, pady=2)
        option3.grid(row=2, column=0, padx=45, pady=1)
        option4.grid(row=2, column=1, padx=45, pady=1)

        CloseLabel = Label(GuiControl, bg=GuiControlColor, image=Close_Dis)
        CloseLabel.bind("<Enter>", Close_In)
        CloseLabel.bind("<Leave>", Close_Out)
        CloseLabel.bind("<Button-1>", Quit)
        CloseLabel.pack(side=RIGHT, pady=1, padx=1)
        ##---FADE---EFFECT
        FEn = [0.0]
        def FadeEntry():
            quizWin.focus_force()
            del FEn[0:-2]
            no = float(FEn[-1])+0.01
            FEn.append(no)
            mainWin.withdraw()
            quizWin.attributes("-alpha", no)
            if FEn[-1] < 1:
                quizWin.after(5, FadeEntry)
            elif FEn[-1] > 1:
                del FEn[0:-1]
                FEn.append(0.0)
                timer()
        FadeEntry()
        quizWin.focus_force()
    else:
        mainWin.withdraw()
        Back_Home()
        messagebox.showerror("DIR ERROR", "UNABLE TO FIND ENOUGH DATA TO START THE TEST!")
        mainWin.focus_force()

AnimLoadBar() #LOADBAR UPDATE
        
def StartTest(event):
    play_click()
    ab = event.widget
    no = selectnames.index(ab)
    _getChpName_.append(str(lblnames[no].cget("text")))
    print('====================================================')
    print('SELECTED ', SubjSel[-1], ' > LEVEL ', Tab_chk[-1], ' > ', _getChpName_[-1])
    Fade_Out()
    for pk in range(len(selectnames)):
        selectnames[pk].bind("<Enter>", Faltu)
        selectnames[pk].bind("<Leave>", Faltu)
        selectnames[pk].bind("<1>", Faltu)
        lblnames[pk].bind("<Enter>", Faltu)
        lblnames[pk].bind("<Leave>", Faltu)

    inputWin = Toplevel(mainWin)
    inputWin.configure(background=QuizControlColor)
    inputWin.overrideredirect(True)
    inputWin.geometry('500x400')
    inputWin.tk.call('wm', 'iconphoto', inputWin._w, icon)
    ###-IT COMES IN CENTER
    window_height = 156
    window_width = 152
    screen_width = mainWin.winfo_screenwidth()
    screen_height = mainWin.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    def Close_In(event):
        CloseLabel.configure(image=Close_Hover, cursor='hand2')
    def Close_Out(event):
        CloseLabel.configure(image=Close_Dis)
    def Quit(event):
        print('====================================================')
        print('RETURNED BACK TO HOME (CANCELLED)')
        Back_Home()
        inputWin.destroy()

    def FOCUSS():
        inputWin.focus_force()
        mainWin.after(100, FOCUSS)
    inputWin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    inputWin2 = Frame(inputWin, background=GuiControlColor, height=30)
    inputWin2.pack(fill=BOTH)
    CloseLabel = Label(inputWin2, bg=GuiControlColor, image=Close_Dis)
    CloseLabel.bind("<Enter>", Close_In)
    CloseLabel.bind("<Leave>", Close_Out)
    CloseLabel.bind("<Button-1>", Quit)
    CloseLabel.pack(side=RIGHT)
    inputWin1 = Frame(inputWin, background=QuizControlColor)
    inputWin1.pack(fill=BOTH)
    def only_numbers(char):
        return char.isdigit()
    validation = inputWin.register(only_numbers)
    def In(event):
        enterBTN.configure(bg='#00ff30', cursor='hand2')
    def Out(event):
        enterBTN.configure(bg='cyan')
    def Proceed(event):
        if str(SubjSel[-1]) == 'P':
            subj = 'physics'
        if str(SubjSel[-1]) == 'C':
            subj = 'chemistry'
        if str(SubjSel[-1]) == 'M':
            subj = 'maths'
        if str(SubjSel[-1]) == 'CUS':
            subj = 'custom'
        
        csvFile = str('_AppData_\\questions\\'+str(subj)+'\\'+str(_getChpName_[-1])+'\\LEVEL'+str(Tab_chk[-1])+'\\'+'solution.csv')
        csvSol = pandas.read_csv(csvFile)
        _toCheckMaxQ_ = csvSol['OPTION1'].values.tolist()
        MaxQ = int(len(_toCheckMaxQ_))
    
        if entry.get() != '' and str(entry.get()).isdigit() != False:
            if int(entry.get()) > 3 and int(entry.get()) < 500 and int(entry.get()) <= MaxQ :
                Fade_In()
                totalQuestions.append(int(entry.get()))
                inputWin.withdraw()
                StartQuizFinal()
            elif int(entry.get()) > 500:
                messagebox.showerror('ERROR', 'Max LIMIT IS 500 (IT CAN BE DANGEROUS)')
                inputWin.focus_force()
                entry.focus_force()
            elif int(entry.get()) > MaxQ:
                messagebox.showerror('ERROR', 'Only '+str(MaxQ)+' Questions are available!')
                inputWin.focus_force()
                entry.focus_force()
                startt.set(str(MaxQ))
            else:
                messagebox.showerror('ERROR', 'SOMETHING IS WRONG!!')
                inputWin.focus_force()
                entry.focus_force()
        else:
            inputWin.focus_force()
            entry.focus_force()

    def BringUp(event):
        inputWin.focus_force()

    if os.path.exists('_AppData_\\data\\fullscreen.csv'):
        sett = pandas.read_csv('_AppData_\\data\\fullscreen.csv')
        Full1 = sett['FULLSCREEN'].values.tolist()
        zoom_chk.append(int(Full1[0]))
    else:
        zoom_chk.append(int(0))

    def SETZOOM(event):
        del zoom_chk[0:-1]
        if int(zoom_chk[-1]) == 0:
            with open('_AppData_\\data\\fullscreen.csv', 'w', newline='') as fl:
                row_con = ['FULLSCREEN']
                append_list_as_row('_AppData_\\data\\fullscreen.csv', row_con)
                row_con2 = [1]
                append_list_as_row('_AppData_\\data\\fullscreen.csv', row_con2)
                fl.close()
            zoom_chk.append(1)
            setZOOM.configure(image=fullscreen)
        else:
            with open('_AppData_\\data\\fullscreen.csv', 'w', newline='') as fl:
                row_con = ['FULLSCREEN']
                append_list_as_row('_AppData_\\data\\fullscreen.csv', row_con)
                row_con2 = [0]
                append_list_as_row('_AppData_\\data\\fullscreen.csv', row_con2)
                fl.close()
            zoom_chk.append(0)
            setZOOM.configure(image=windowed)
        #print(zoom_chk)

    mainWin.bind("<F8>", BringUp)
    inputWin.bind("<Return>", Proceed)
    startt = StringVar()
    entry = ttk.Entry(inputWin1, textvariable=startt, justify=CENTER, font=("Bahnschrift Light SemiCondensed", 40), validate="key", validatecommand=(validation, '%S'))
    entry.focus_force()
    entry.pack(side=TOP, fill=X, padx=5, pady=5)

    if zoom_chk[-1] == 1:
        setZOOM = Label(inputWin1, image=fullscreen, font=("Bahnschrift Light", 16), background=GuiControlColor, fg=QuizControlColor)
    else:
        setZOOM = Label(inputWin1, image=windowed, font=("Bahnschrift Light", 16), background=GuiControlColor, fg=QuizControlColor)
    setZOOM.bind("<1>", SETZOOM)
    setZOOM.pack(side=RIGHT, fill=X, padx=5, pady=1)

    enterBTN = Label(inputWin1, text='START', width=30, bg='cyan', fg='gray20', font=("Bahnschrift Light SemiCondensed", 18))
    enterBTN.bind("<1>", Proceed)
    enterBTN.bind("<Enter>", In)
    enterBTN.bind("<Leave>", Out)
    enterBTN.pack(side=LEFT, fill=BOTH, padx=5, pady=1)
    


def ChangeSelect(event):  
    ab = event.widget
    ab.configure(bg='#00ff30', width=15, cursor='hand2', text='START TEST', fg='white', font=("Bahnschrift Light SemiCondensed", 25))
def DefaultSelect(event):
    ab = event.widget
    ab.configure(bg='#00ccff', width=1, text='')

def ChangeLbl(event):
    ab = event.widget
    glitchSol.append(ab)
    if glitchSol[-1] == ab:
        if ab in lblnames:
            no = lblnames.index(ab)
            selectnames[no].configure(width=15, text='START TEST', fg='white', font=("Bahnschrift Light SemiCondensed", 25))
            for i in range(len(lblnames)):
                if i != no:
                    selectnames[i].configure(width=1, text='')
                    lblnames[i].configure(bg='#2d325a')
        ab.configure(bg='#373d6e')
    glitchSol.append(ab)    

def OpenChapter():
    chp = []
    if SubjSel[-1] == 'P':
        for jk in range(len(phy_chp)):
            pathDIR = "_AppData_\\questions\\physics\\"+str(phy_chp[jk])+"\\LEVEL"+str(Tab_chk[-1])+"\\"
            if os.path.exists(pathDIR):
                chp.append(phy_chp[jk])
 
    elif SubjSel[-1] == 'C':
        for jk in range(len(chem_chp)):
            pathDIR = "_AppData_\\questions\\chemistry\\"+str(chem_chp[jk])+"\\LEVEL"+str(Tab_chk[-1])+"\\"
            if os.path.exists(pathDIR):
                chp.append(chem_chp[jk])

    elif SubjSel[-1] == 'M':
        for jk in range(len(maths_chp)):
            pathDIR = "_AppData_\\questions\\maths\\"+str(maths_chp[jk])+"\\LEVEL"+str(Tab_chk[-1])+"\\"
            if os.path.exists(pathDIR):
                chp.append(maths_chp[jk])

    elif SubjSel[-1] == 'CUS':
        for jk in range(len(custom_chp)):
            pathDIR = "_AppData_\\questions\\custom\\"+str(custom_chp[jk])+"\\LEVEL"+str(Tab_chk[-1])+"\\"
            if os.path.exists(pathDIR):
                chp.append(custom_chp[jk])  
    if len(chp) > 0:
        TabHolder.pack_forget()
        SubHolder.pack_forget()
        mainWin.attributes("-alpha", 0.0)
        border_thick = 2
        for i in range(len(chp)):
            Outline = Frame(ChapterHolder, background='white', width=1236, height=4)
            if i == 0:
                pre_border = Frame(ChapterHolder, background=QuizControlColor, height=border_thick)
                pre_border.pack(fill=X, side=TOP)
            select = Label(Outline, text='', width=1, bg='#00ccff', font=("Bahnschrift", 25))
            Lbl = Label(Outline, text=chp[i], width=134, anchor="w", justify=RIGHT, bg='#2d325a', fg='white', font=("Bahnschrift", 30))
            border = Frame(ChapterHolder, background=QuizControlColor, height=border_thick)
            Outline.pack(side=TOP)
            select.pack(side=LEFT, fill=BOTH)
            select.bind("<Enter>", ChangeSelect)
            select.bind("<Leave>", DefaultSelect)
            select.bind("<1>", StartTest)
            Lbl.bind("<Enter>", ChangeLbl)
            Lbl.pack(side=LEFT, fill=BOTH)
            border.pack(fill=X, side=TOP)
            OutlineFrames.append(Outline)
            OutlineFrames.append(pre_border)
            OutlineFrames.append(border)
            lblnames.append(Lbl)
            selectnames.append(select)
        play_whoosh()
        Fade_In()
    else:
        messagebox.showinfo('INSUFFICIENT DATA','Please select other subject!')
        mainWin.focus_force()
def PhyL_In(event):
    PhyL.configure(image=PhySel, cursor='hand2')
def ChemL_In(event):
    ChemL.configure(image=ChemSel, cursor='hand2')
def MathL_In(event):
    MathL.configure(image=MathSel, cursor='hand2')
def CustomL_In(event):
    CustomL.configure(image=CustomSel, cursor='hand2')
def PhyL_Out(event):
    PhyL.configure(image=PhyImg)
def ChemL_Out(event):
    ChemL.configure(image=ChemImg)
def MathL_Out(event):
    MathL.configure(image=MathImg)
def CustomL_Out(event):
    CustomL.configure(image=CustomImg)

def Add_Phy(event):
    print('====================================================')
    print('SELECTED PHYSICS LEVEL ', Tab_chk[-1])
    if len(Tab_chk) > 0:
        SubjSel.append('P')
        OpenChapter()
    else:
        messagebox.showinfo('INSUFFICIENT DATA','Please select DIFFICULTY LEVEL!')
        mainWin.focus_force()
def Add_Chem(event):
    print('====================================================')
    print('SELECTED CHEMISTRY LEVEL ', Tab_chk[-1])
    if len(Tab_chk) > 0:    
        SubjSel.append('C')
        OpenChapter()
    else:
        messagebox.showinfo('INSUFFICIENT DATA','Please select DIFFICULTY LEVEL!')
        mainWin.focus_force()
def Add_Math(event):
    print('====================================================')
    print('SELECTED MATHS LEVEL ', Tab_chk[-1])
    if len(Tab_chk) > 0:
        SubjSel.append('M')
        OpenChapter()
    else:
        messagebox.showinfo('INSUFFICIENT DATA','Please select DIFFICULTY LEVEL!')
        mainWin.focus_force()
def Add_Custom(event):
    print('====================================================')
    print('SELECTED CUSTOM LEVEL ', Tab_chk[-1])
    if len(Tab_chk) > 0:
        SubjSel.append('CUS')
        OpenChapter()
    else:
        messagebox.showinfo('INSUFFICIENT DATA','Please select DIFFICULTY LEVEL!')
        mainWin.focus_force()

AnimLoadBar() # AFTER CHECKING MAINWIN COMPLETE LOADBAR UPDATE

PADX = 2
PADY = 3
PhyL = Label(SubHolder, bg=QuizControlColor, image=PhyImg)
ChemL = Label(SubHolder, bg=QuizControlColor, image=ChemImg)
MathL = Label(SubHolder, bg=QuizControlColor, image=MathImg)
CustomL = Label(SubHolder, bg=QuizControlColor, image=CustomImg)
PhyL.bind("<Enter>", PhyL_In)
ChemL.bind("<Enter>", ChemL_In)
MathL.bind("<Enter>", MathL_In)
CustomL.bind("<Enter>", CustomL_In)
PhyL.bind("<Leave>", PhyL_Out)
ChemL.bind("<Leave>", ChemL_Out)
MathL.bind("<Leave>", MathL_Out)
CustomL.bind("<Leave>", CustomL_Out)
PhyL.bind("<1>", Add_Phy)
ChemL.bind("<1>", Add_Chem)
MathL.bind("<1>", Add_Math)
CustomL.bind("<1>", Add_Custom)
PhyL.grid(row=0, column=1, padx=PADX, pady=PADY)
ChemL.grid(row=0, column=2, padx=PADX, pady=PADY)
MathL.grid(row=0, column=3, padx=PADX, pady=PADY)
CustomL.grid(row=0, column=4, padx=PADX, pady=PADY)

print('================================')
print('STARTING MAINWIN...')

AnimLoadBar() # AFTER STARTING MAINWIN COMPLETE LOADBAR UPDATE
def FadeMAINWin():
    SplashWin.destroy()
    MainFrame.destroy()
    PhotoHolder.destroy()
    SIROLogo.destroy()
    IconFrame.destroy()
    LoadingFrame.destroy()
    ShowWaterMark.destroy()
    PhotoLabel.destroy()
    #mainWin.deiconify()
    Fade_In()
    mainWin.focus_force()

mainWin.after(50, FadeMAINWin)
AnimLoadBar()
mainWin.focus_force()
mainWin.mainloop()

