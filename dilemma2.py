#Dilemma - An Original Work of Fiction
#CQ CQ CQ DE WAAK1A7 BK EMRG CX II EMRG CX BK SFR EAST US SIGS SK BK QRN QRM BK CQ UNCLR BK DC GONE II DC GONE RPT
from tkinter import *
from PIL import *
from winsound import *

#Ends program.

def end():
    global root
    root.destroy()

#Swaps from one screen to the next
def skipToBranch1():
    storyLeave1()
    canvas.delete(button_window)
    canvas.delete(button1_window)
    canvas.delete(button2_window)
    canvas.delete(button3_window)
    canvas.delete(button4_window)
    canvas.delete(button5_window)
    canvas.delete(button7_window)
def skipToBranch2():
    storyStay1()
    canvas.delete(button_window)
    canvas.delete(button1_window)
    canvas.delete(button2_window)
    canvas.delete(button3_window)
    canvas.delete(button4_window)
    canvas.delete(button5_window)
    canvas.delete(button7_window)
    
def skipToDeath():
    storyLeaveBadEnd()
    canvas.delete(button9_window)
    canvas.delete(button10_window)
    canvas.delete(button11_window)
    canvas.delete(button12_window)
    canvas.delete(button13_window)
    canvas.delete(button14_window)
    

#Awakening
def story1():
    global button1_window
    label.configure(text="You awaken in the bunker to the sound of morse over your HAM radio. \n There is no other sound -- the worst has passed.")
    button1 = Button(text="Continue.", command = story2)
    button1_window = canvas.create_window(400, 400, window=button1)
    PlaySound("C:/Users/Austin/Documents/emergency.wav", SND_ASYNC)
def story2():
    global button2_window
    label.configure(text="You were dreaming again. Five days ago the world went to hell, but every time you close your eyes you can \n still see the way it was before. Safe, quiet, happy.")
    button2 = Button(text="Continue.", command = story3)
    button2_window = canvas.create_window(400, 400, window=button2)
def story3():
    global button3_window    
    label.configure(text="The message from the radio is the same.")
    button3 = Button(text="Continue.", command = story4)
    button3_window = canvas.create_window(400, 400, window=button3)
def story4():
    global button4_window
    label.configure(text="It's a message from another survivor. \"Calling all stations, calling all stations...\"\nBut you don't know enough morse to try and reach out to them. They might have even died since they started broadcasting.")
    button4 = Button(text="Continue.", command = story5)
    button4_window = canvas.create_window(400, 400, window=button4)
def story5():
    global button5_window
    global button7_window
    #Opt1
    label.configure(text="It crosses your mind to take a walk. You've been sitting at the desk keeping track of the radio for almost a week, with only intermittent sleep.\n One can only mope for so long, yeah? But if there's an update you might miss it. What would you like to do?")
    button5 = Button(text="Stretch your legs.", command = skipToBranch1)
    button5_window = canvas.create_window(400, 400, window=button5)
    #opt2
    button7 = Button(text="Stay seated.", command = skipToBranch2)
    button7_window = canvas.create_window(400, 350, window=button7)

#Begin branched story
def storyLeave1():
    global bgHallwaya
    global bgHallway
    canvas.delete(bgBunkera)
    bgHallway = PhotoImage(file="C:/Users/Austin/Documents/bunker hall.gif")
    bgHallwaya = canvas.create_image(10,10,image = bgHallway, anchor=NW)
    PlaySound("C:/Users/Austin/Documents/emergency muted.wav", SND_ASYNC)
    label.configure(text="You step into the main part of your bunker -- the hallway. It's empty. \nYou were the only one who managed to make it to the shelter before the bombs really started falling.\n You can hear your own echo now. It reminds you about the first few days -- the bombs wouldn't stop.\n The whole bunker was filled with the sound of the explosions above.")
    button8 = Button(text="Continue", command = storyLeave2)
    button8_window = canvas.create_window(400, 350, window = button8)

def storyLeave2():
    global button9_window
    label.configure(text="There's no breeze. You can still hear the radio in the other room, though it's muffled.\nThe only other sound comes from the air filtration system.")
    button9 = Button(text="Continue", command = storyLeave3)
    button9_window = canvas.create_window(400, 350, window = button9)

def storyLeave3():
    global button10_window
    label.configure(text="There's next to nothing to do. The first two days, you worried about being killed by either a direct hit, or radiation. \n The days after, you kept up with the survivors over the radio. One by one the signals began to drop off, replaced by static.\nToday might be a good time as any to check the geiger counters in the airlocks.")
    button10 = Button(text="Continue", command = storyLeave4)
    button10_window = canvas.create_window(400, 350, window = button10)
def storyLeave4():
    global button11_window
    label.configure(text="There are lethal levels of radiation beyond the walls of your small shelter.")
    button11 = Button(text="Continue", command = storyLeave5)
    button11_window = canvas.create_window(400, 350, window=button11)
def storyLeave5():
    global button12_window
    label.configure(text="Something that never really crossed your mind was what would happen after the fact. Sure, you've survived -- but what happens when the fallout clears?\n How will you survive? You know of no other survivors nearby, nor do you have the supplies for much of anything.\nWas it all for naught?")
    button12 = Button(text="Continue", command = storyLeave6)
    button12_window = canvas.create_window(400, 350, window = button12)
def storyLeave6():
    global button13_window
    global button14_window
    label.configure(text="...perhaps it would be best to simply walk out and die.")
    #Game over.
    button13 = Button(text="Walk outside?", command = skipToDeath)
    button13_window = canvas.create_window(400, 350, window=button13)   

##Branch option 2
def storyStay1():
    label.configure(text="You continue to listen to the droning of the radio. It makes you think -- virtually no other channels have remained online.\nHas everybody else really died?")
    button17 = Button(text="Contine", command = storyStay2)
    button17_window = canvas.create_window(400, 350, window=button17)
def storyStay2():
    label.configure(text="The stress is getting to you. The days of isolation, the fear of death. Your pantry will eventually run down.\n Do you really have the guts to try and persevere in the face of those odds?")
    button18 = Button(text="Continue", command = storyStay3)
    button18_window = canvas.create_window(400, 350, window=button18)
def storyStay3():
    label.configure(text="There's a gun in your desk. You take it out, check the ammo. It was bought with the purpose of home defense, but... as you hold it, you realize it might be your escape.\n You press the barrel to your temple.")
    button19 = Button(text="Do it.", command = end)
    button19_window = canvas.create_window(400, 350, window=button19)
    
##Bad Ends
def storyLeaveBadEnd():
    global bgCitya
    global bgCity
    global button15_window
    canvas.delete(bgHallwaya)
    bgCity = PhotoImage("C:/Users/Austin/Documents/nuked city.gif")
    bgCitya = canvas.create_image(10,10,image = bgCity, anchor=NW)
    label.configure(text="This was a bad idea. As radiation floods the airlock you immediately feel nausea overtaking your senses. \n You barely make it out of the bunker before you set eyes on the remains of the city that once was your home. \n Irradiated and sick with regret, you curl into a ball and await your death.")
    button15 = Button(text="Game over.", command = end)
    button15_window = canvas.create_window(400, 350, window=button15)

def storyStayBadEnd():
    label.configure(text="You press the gun to your head and take a deep breath.\n Squeeze the trigger.")
    button16 = Button(text="Oh no!", command = end)
    button16_window = canvas.create_window(400, 350, window=button15)
    
##Good ends
    
root= Tk()
##Canvas
canvas = Canvas(width=800, height=450, bg='black')
canvas.grid()

##Label
label=Label(text="...")
label_window = canvas.create_window(400, 100, window=label)
#label.grid(row=1, column=0)

##Background
bgBunker = PhotoImage(file="C:/Users/Austin/Documents/bunker radio.gif")
bgBunkera = canvas.create_image(10,10, image = bgBunker, anchor=NW)

##Button
button = Button(text="Continue.", command = story1)
button_window = canvas.create_window(400, 400, window=button)






root.geometry("800x450+0+0")

##Begin background music
PlaySound("C:/Users/Austin/Documents/bg music.wav", SND_ASYNC) #It took like an hour before I realized it wasn't working because it was 'waiting' for the music to finish.

    
mainloop()

