# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define test = Character('Test', color="#c8ffc8")

define narrator = Character(None, kind=nvl)
define form = Character(None, kind=nvl, what_font="fonts/Liberation.ttf")
define titlecard = ImageDissolve("backgrounds/titlecard.png", 0.1)

init:
    #Custom flash fade
    $ flash = Fade(.25, 0, .75, color="#fff")
    #Background
    image black = "#000000"
    image white = "#FFFFFF"
    image IT = "backgrounds/colony_1.png"
    image ship = "backgrounds/ch1_1.png"
    image riot = "backgrounds/ch1_2.png"
    image title = "backgrounds/titlecard.png"
    image periscopeSight = "backgrounds/periscopeSight.png"
    image periscopeSightDark = "backgrounds/periscopeSightDark.png"
    image smallcraft = "backgrounds/menu_1.png"
    image barracks = "backgrounds/barracks.png"
    image barracks2 = "backgrounds/barracks2.png"
    image shipHall = "backgrounds/hall1.png"
    image shipHall2 = "backgrounds/hall2.png"
    image shipHall3 = "backgrounds/hall3.png"
    image shipHallDark = "backgrounds/halldark.png"
    image spaceDock = "backgrounds/spaceport.png"
    image space = "backgrounds/star.png"
    image spaceLight = "backgrounds/starlight.png"
    image bridge = "backgrounds/bridge.png"
    image armory = "backgrounds/armory.png"
    image shipAirlock = "backgrounds/airlock.png"
    image shipAirlockDark = "backgrounds/airlockdark.png"
    image pacificOcean = "backgrounds/pacific.png"
    image Hawaii = "backgrounds/hawaii.png"
    image HawaiiTown = "backgrounds/hawaiitown.png"
    image HawaiiTable = "backgrounds/hawaiitable.png"
    image bomb = "backgrounds/bomb.png"
    image colonyCafe = "backgrounds/cafe.png"
    image controlRoom = "backgrounds/controlroom.png"
    image sickbay = "backgrounds/sickbay.png"
    image badend = "backgrounds/badend.png"
    image goodend = "backgrounds/goodend.png"
    image interrogationRoom = "backgrounds/interrogation room.png"
    image warRoom = "backgrounds/warroom.png"
    
    #Titlecards
    image soldierChapter1 = "backgrounds/ch1 titlecard.png"
    image soldierChapter2 = "backgrounds/ch2 titlecard.png"
    image soldierChapter3 = "backgrounds/ch3 titlecard.png"
    image soldierChapter4 = "backgrounds/ch4 titlecard.png"
    image soldierChapter5 = "backgrounds/ch5 titlecard.png"
    
    # Principle skills
    $ marksmanship = 0
    $ pilotry = 0
    $ pt = 0
    $ engineering = 0
    $ math = 0
    $ social = 0
    $ drive = 0
    $ depression = 0 # 0 = suicidally depressed, 10 = indomitably happy
    
    #Pronouns
    $ gender_they = "he"
    $ gender_them = "him"
    $ gender_their = "his"
    $ gender_formal = "Mister"
    $ gender_formal_title = "sir"
    $ gender = "man"
    
    #Specializations
    $ soldier = False
    $ pilot = False
    $ engineer = False
    $ everyman = False
    
    #Age
    $ age = 20
    
    
# The game starts here.
label start:

    scene black
    
    play ambiance "sounds/ambiance.mp3"
    play music "sounds/music1.mp3"
    
    ##Lobby
    narrator "Why did you come here?"
    narrator "To serve? To protect? To see the Terrasphere?"
    
    scene IT
    
    narrator "You're waiting, perhaps anxiously, sitting in the lobby of the Terrasphere Space Forces recruitment center."
    narrator "The length of the O'Neill Cylinder is visible from where you sit."
    narrator "There's little but the sound of those in the other rooms, hard at work. Bureaucrats."
    narrator "There are a handful of other people. Young people, most no older than eighteen. They seem fairly anxious."
    narrator "The door into the interior of the recruitment center swings open with a creak, and a young man steps out."
    narrator "He gestures to you, saying you're next."
    
    nvl clear
    
    ##Recruiter room
    narrator "You head into the room. It's a small cubicle, no larger than three by three meters. At its center is a desk, complete with a computer."
    narrator "\"Please, have a seat,\" he says, gesturing to the chair on your side of the desk. He is an older man, perhaps mid-forties, his cheeks round and his belly plump."
    narrator "The face of a grandfather."
    narrator "But he is sharply dressed and very well-kempt, despite it."
    narrator "He taps away at the keyboard on his computer as you take your seat, and then adjusts his glasses."
    narrator "\"I'm lieutenant Jacobsen,\" he said. \"I'm the lead recruiter here and senior officer of this facility.\""
    narrator "The old man across from you hands you a red slip of paper."
    narrator "\"I have a form for you to fill out, if you're really set on this job,\" he said. \"Military isn't for the faint of heart, especially the Space Force. This form will get you on the right track. It's mostly a formality, nothing too difficult, nothing like the ASVAT.\""
    narrator "He points at it with his pen, gesturing where he wants you to sign."
    
    nvl clear
    narrator "You glance at it."
    form " "
    form "OFFICIAL CORRESPONDENCE"
    form " "
    form "PROPERTY OF TERRASPHERE FEDERATION SPACE FORCES"
    form " "
    form "DO NOT DUPLICATE"
    form " "
    narrator "The form has a number of lines asking for various details. You fill them out dutifully."
    $ player_name = renpy.input("Print name in the field below.") or "Amuro"
    $ player_name = player_name.strip()
    
    narrator "You check one of the options for your sex."
    
    #Determines pronouns
    menu:
        "Male":
            $ female = False
        "Female":
            $ female = True
            $ gender_they = "she"
            $ gender_them = "her"
            $ gender_their = "hers"
            $ gender_formal = "Miss"
            $ gender_formal_title = "ma'am"
            $ gender = "woman"
    
    nvl clear
    
    narrator "The form asks for your age."
    $ age = renpy.input("Print age in the field below.") or age
    $ age = int(age)
    nvl clear
    
    if age > 50:
        narrator "Jacobsen shakes his head. \"I think you're a bit beyond what we're looking for, [gender_formal_title].\""
        return
    
    if age < 16:
        narrator "Jacobsen shakes his head. \"I thought you looked too young to be here.\" He snatches the form back from you. \"Where the fuck are your parents? Go home, get out of my office.\""
        return

    nvl clear
    
    narrator "The form asks for special skills and experiences."
    
    #Determines base skillpoint allocation
    menu:
        "Marksman.":
            $ soldier = True 
            $ frontline = True
            $ rearline = False
            $ marksmanship = 7 #5 = average
            $ pt = 6
            $ pilotry = 3
            $ math = 5
            $ drive = 6
            $ social = 3
            $ depression = 7
            $ cowardice = 0
            $ RaiBond = 0
            $ RossBond = 0
            $ isInjured = False
        "Pilot.":
            $ pilot = True
            $ frontline = True
            $ rearline = False
            $ marksmanship = 3 #5 = average
            $ pt = 4
            $ pilotry = 7
            $ math = 7
            $ drive = 4
            $ social = 6
            $ depression = 4
            $ cowardice = 0
            $ RaiBond = 0
            $ RossBond = 0
            $ isInjured = False
        "Engineer.":
            $ engineer = True
            $ rearline = True
            $ frontline  = False
            $ marksmanship = 2 #5 = average
            $ pt = 8
            $ pilotry = 4
            $ math = 8
            $ drive = 6
            $ social = 2
            $ depression = 4
            $ RaiBond = 0
            $ RossBond = 0 
            $ isInjured = False
        "Student.":
            $ everyman = True
            $ rearline = True
            $ frontline = False
            $ marksmanship = 4 #5 = average
            $ pt = 4
            $ pilotry = 2
            $ math = 5
            $ drive = 8
            $ social = 8
            $ depression = 8
            $ RaiBond = 0
            $ RossBond = 0
            $ isInjured = False
        
    nvl clear
    
    #First choice-based branch shows a little backstory for each specialization.
    if soldier == True:
        narrator "You think back. You always had a good sense of depth, and superb hand-eye coordination. When you were a teenager your parents bought you a handgun, with which you often went to the gun range."
        narrator "You were always in good health, as well, if a little introverted. You could fly, but it was never your forte, although that didn't stop you from trying."
        narrator "To your parents, the most admirable thing about you was your passion and drive. No matter what it was, if  you put your mind to it you would succeed."
    if pilot == True:
        narrator "From a young age your passion was flying."
        narrator "At every possible opportunity, you would find a way to get behind the stick of a VTOL or better yet, a smallcraft."
        narrator "A keen eye for depth and superb calculative abilities made you one of the best pilots for your age."
        narrator "You struggled with maintaining functional relationships for much of your life. Constantly being alone, preferring the company of a warm engine, and general disinterest in \"normal\" extracurricular activities made it hard."
        narrator "That being said, there was nothing you liked more than showboating. Any chance to show off your skills could make your heart rise above the clouds of loneliness."
    if engineer == True:
        narrator "Robotics. Car repair. Ship repair. Manufacturing. Weapons maintenance. It didn't matter what it was, if it involved taking things apart and putting them back together, you jumped on it."
        narrator "Human contact paled in comparison to your tactile skills. On top of that, the heavy lifting that came with particularly complex machines kept your physique honed."
        narrator "Fixing things and building things, that was what you did and you loved it. It took a great deal of study and learning to get there, and while your social skills have certainly suffered as a result, it's not a passion you would ever give up."
    if everyman == True:
        narrator "You're just another young [gender]."
        narrator "Your reasons for enlisting are your own, but in any case you don't really have all that much to offer the TFSF."
        narrator "Your proficiencies are average, at best. You've only rarely flown a smallcraft, rarely shot a gun. You exercise regularly and eat well, but never went the extra mile."
        narrator "On the upshot, your averageness makes you appear quite stable compared to a lot of people. You are \"normal\", for better or worse."
    
    nvl clear
    narrator "You continue filling out the form to the best of your ability."
    narrator "The lieutenant wasn't lying, it's no test. It's purely personal and professional questions."
    narrator "Your level of education, your criminal record, the date of your last physical. Things of that nature. Your pen flies over the paper, the sound of ballpoint on paper competing with the clacking of the recruiter's computer."
    narrator "When you finish up the form, you hand it, and the pen, back to him. He grabs it, and begins looking it over, checking, doublechecking. Perhaps ensuring you didn't miss any of the fields."
    narrator "\"Very good, [gender_formal] [player_name],\" Jacobsen says, giving it one final once-over." 
    
    play sound "sounds/stamp.ogg"
    
    narrator "He take out a stamp, and presses it down on the paper."
    
    narrator "Jacobsen stands, and offers his hand, and you mimic his motions."
    
    nvl clear
    
    narrator "\"Welcome to the TFSF, Ensign. In a few days' time, we'll contact you regarding potential stationing and other accoutrements.\" He points toward the door. \"Now, would you kindly send in the next enlistee on your way  out?\""
    narrator "You exit the room and do as the lieutenant asked of you before heading out on your own."

    nvl clear
    
    stop ambiance

    scene ship
    
    narrator "This model O'Neill cylinder colony is fairly ancient. No less than three centuries old. Its construction makes that apparent -- it still has that kind of 'rough' aesthetic, unpolished. The catwalk onto which you exit is no different."
    narrator "You walk along, clanking over steel. It's nighttime, but the earth is still gleaming in the distance like a blue marble. The colony is part of the L2 group -- the one between the Earth and the Moon."
    narrator "You were born here, on this colony. You are, sure enough, a colonial citizen. Not entitled to vote in Terran politics, but still guaranteed some rights and liberties."
    narrator "The L2 group has been among the most loyal colony group in recent days. Perhaps because it plays host to one of the largest Terrasphere Federation Space Forces shipyards in existence."
    narrator "The colony is in the wrong position to see the shipyard, though."
    narrator "There are other benefits, though. Being a hub for the TFSF means they recruit quite a bit from the colonials here."
    narrator "Which is the easiest path for Terran citizenship."
    narrator "Perhaps that's why you enlisted."
    
    nvl  clear
    
    scene riot
    
    narrator "The year so far hadn't exactly been out to a great start, either."
    narrator "Agitators in the L4 and L5 colony groups had been escalating what was already a bad situation. Food was scarce, even on Terra itself, but those dissidents seemed to believe that they deserved food more than anyone else."
    narrator "They were even exporting their terrorism to the more calm of the colony groups."
    narrator "And things were just getting worse every day. The annual remembrance day for Leonard Chauchat, who had been a major Terran supporter for the Colonial Rights Movement, was marked by major riots across dozens of cities in all of the colony groups. Even the Solar colony groups."
    narrator "A group of school-aged children ran past you on the catwalk, barely keeping from knocking you over the bannister."
    
    scene ship
    
    narrator "A bad situation, rapidly deteriorating into anarchy, especially on the more distant colonies. And with the terrorists gaining speed, all it would take to set off the keg was one spark."
    
    scene black
    
    nvl clear
    
    narrator "You could feel the hair on the back of your neck sear off before you realized what had happened."
    
    play sound "sounds/explosion.wav"
    play tinnitus "sounds/tinnitus.ogg"
    
    nvl clear
    
    scene title
    
    $ renpy.pause()
    
    window hide
    stop sound
    stop tinnitus
    stop music
    nvl clear
    ##The following is mostly from the Soldier line.
        
label SoldierLine:
    scene soldierChapter1
    $ renpy.pause()
    ##CH1: The One Day War begins.
    scene barracks
    play war "sounds/war.wav" #klaxons and explosions.
    play music "sounds/tense.mp3"
    narrator "Klaxons wailing jolt you up from your sleep. It's been several months since the attack on colony and a few weeks since the end of basic training."
    narrator "The lights flicker, the ship shudders; either the armory has detonated or the ship is under attack."
    narrator "There's a cacaphony going on outside of your barracks' door, people clambering by and shouting at the tops of their lungs."
    narrator "Your training comes flooding back at full volume, compelling you out of your bed and on your feet, and before long out the door despite having no time to change."
    scene shipHall
    play sound "sounds/shudder.wav"
    narrator "People push you out of their way as they hurry down the tight corridors of the ship."
    narrator "The Lion-class vessels are medium-sized cruisers, nothing like the Daedalus-class battleships that make up the TFSF line of battle."
    
    nvl clear
    
    narrator "The ship was docked in L2 colony cluster shipyard, the principle refuelling station for all of the Terrasphere's major fleets."
    narrator "The terrorist attacks had been steadily intensifying over the last weeks... but this was different."
    narrator "Terrorist attacks are typically one-off bombings. This sounded more like a concerted effort by several space warships."
    narrator "The comms system comes alive with a crackle and the sharp sound of feedback. \"All hands, general quarters; this is not a drill. Repeat, all hands, general quarters; this is not a drill.\""
    narrator "The Executive Officer of the ship, who had just been on the comms, pushed his way past you."
    narrator "\"Sir?\" you ask. \"What's going on?\""
    narrator "The XO looks at you and cocks his head."
    narrator "\"We're at war, soldier,\" he says. \"Get to your station and ready for battle.\""
    
    nvl clear
    
    narrator "War."
    narrator "War?"
    narrator "The notion was incomprehensible. There hadn't been a serious war in centuries."
    narrator "Terrorist attacks weren't war, they were some messed up way of trying to get attention."
    narrator "You start walking toward your station. Dust is kicked up with every shudder, and the seriousness of the situation becomes readily apparent."
   
    narrator "Your principle battlestation was the bowmost gun. The barracks, unfortunately, are situated quite far from the bow, right in the very heart of the ship itself."
    scene shipHall2
    narrator "Despite the labyrinthine layout of the Lion-class, you faithfully make your way toward the battle station even as the ship seems to be coming apart around you."
    narrator "Rivets strip from plates of metal, ricocheting like shrapnel and just as lethal. You watch as an engineer catches one with his neck."
    narrator "The fountain of blood that results just barely misses you as he crumples to the floor."
    nvl clear
    narrator "You carefully step around him."
    narrator "Not long after, you find yourself at the entrance to the battery that is your assigned station."
    narrator "Only one other person is there -- Jake Marlow, the battery commander."
    narrator "\"Well!\" he shouts after he notices you standing near the door, busy with prepping the magazine with new tungsten darts. \"So glad you finally decided  to show up, [player_name].\""
    narrator "He points at one of the several empty seats at a control panel."
    narrator "\"You know how to operate the targeting systems right?\""
    narrator "\"Yes, sir!\" you say instinctively. Marlow grimaces."
    narrator "\"I work for a living, kid.\" he says, irately. \"Just get on the console and start zeroing our gun.\""
    nvl clear
    scene periscopeSight
    narrator "You do as you're told."
    narrator "The gunner's seat has the most important controls for the gun. A periscope allows the gunner to view the outside universe, with an electronic laser rangefinder."
    narrator "The trajectory and range calculations are done automatically by a computerized system. The mathematics involved fly far over your head, so there is a degree of trust involved with the device."
    narrator "You peer through it."
    narrator "It's a black void."
    narrator "You flip through the settings -- IR radiation detection is the most useful in this case, given that all spacecraft put off huge amounts of the stuff in reflection."
    narrator "The three-dimensional radar system gives a bearing on where potential contacts are, and you attempt to dial them in individually with the periscope."
    narrator "\"Ten darts loaded,\" Marlow says."
    nvl clear
    narrator "Marlow has his own periscope, as well, and he finds a target quite faster than you do. He barks the coordinates and you make your own corrections."
    narrator "It's a kind of ship you've never seen before. Much larger, armed with no less than ten railguns and maybe as many missile batteries. The Daedalus-class has just eight guns and six missile batteries."
    narrator "\"AP's loaded, you're clear to fire,\" Marlow says. You check the periscope's tolerances margin-of-error indicator, waiting for it to fall below 5\%."
    narrator "You take the trigger mechanism in one hand, its 'ready' indicator flashing yellow -- ready to fire, but not quite a perfect shot."
    narrator "The indicator ticks down."
    narrator "7\%."
    narrator "6\%."
    narrator "5\%."
    narrator "You pull the trigger once."
    nvl clear
    narrator "It's the first time you've ever live-fired a railgun before. The whole ship shudders in response and the lights dim momentarily -- an issue more modern ships don't suffer from."
    narrator "Marlow hops up and starts messing with the loader's lever, preparing another shot."
    narrator "The dart seems to travel instantaneously from your gun to their ship. It strikes one of their guns, but very little surface damage is done."
    narrator "\"We hit it,\" you say, looking back at Marlow. \"I don't think it did much.\""
    narrator "Marlow shakes his head."
    narrator "\"It's an AP dart, it's not meant to tear up the outside, it's meant to rip through the inside.\""
    narrator "You open your mouth to make a comment, but before you can form your words the ship rattles, this time much harder than before."
    narrator "The lights go out completely."
    nvl clear
    scene black
    $ renpy.pause()
    scene periscopeSightDark with fade
    narrator "The emergency light systems come on just moments afterward."
    narrator "\"Sergeant?\" You ask. Marlow is shaking his head."
    narrator "\"The ship lost all power,\" he says."
    play sound "sounds/shudder.wav"
    narrator "The ship shudders again."
    narrator "It strikes you that, defenseless and without power, it might be best to try to leave the ship."
    narrator "And thankfully, Marlow agrees."
    nvl clear
    scene shipHallDark
    narrator "A dull orange glow fills the corridor just outside of the battery. You poke your head through just in time to see three crewmen shutting a bulwark door."
    narrator "Sparks fly from every exposed wire, threatening to light off the high-oxygen environment."
    narrator "Worse still, the artificial gravity system finally shut down -- meaning you have to hold onto metal railing right near where those same sparks continually arc."
    narrator "You follow behind Marlow as you head toward the docking bay. Most of the other crew don't seem to have this same idea, and are more busy attempting to do damage control than survive."
    narrator "Marlow and you cross paths with the XO, who has been assisting the midshipmen in combat. He doesn't say a word to either of you."
    nvl clear
    scene spaceDock
    narrator "Beyond the airlocks the space port opens up to you. It's predictably abandoned -- everybody has either fled or gone to their posts."
    narrator "The sounds of combat continue even in the space port."
    narrator "It also strikes you too late that it might have been worth it to grab a pressurized spacesuit before fleeing the ship."
    scene black
    stop music
    stop war
    nvl clear
    narrator "However, nothing happens in the end. The enemy ship gets driven off."
    narrator "But the skirmish at the L2 space docks left fully half the First Fleet crippled, and was just one small part of a far larger conflagration that had unfolded that day."
    narrator "Some time later it was announced by the TFSF high command that the Colonial Liberation Front and many other terrorist organizations advocating Colonial liberation had joined forces and started a space and ground war."
    narrator "Much larger forces had attacked the more far-flung outposts, and many of those outposts were destroyed wholesale. The incident quickly became known as the One-Day War because of its sheer scale..."
    nvl clear
    narrator "But it was merely the beginning."
    
    #CH2: Daedalus slips the seige/Skirmish over America
    scene soldierChapter2
    $ renpy.pause()
    nvl clear
    play music "sounds/music1.mp3"
    scene ship
    narrator "A brusque, deep voice called out over the intercom. It had been just under a week since the One-Day War and your transfer to the Daedalus. The namesake of the Daedalus-class. \"Crew of the Daedalus, this is your new Executive Officer speaking.  I am Captain Neil Wright.\""
    narrator "He paused. \"I know these are unusual circumstances we find ourselves in, but in the midst of hardship I believe we better ourselves as a people. I will do my best to prove my worth as Captain of this ship, and I hope you all help me along the way.\""
    narrator "And with that the announcement ended."
    narrator "The Daedalus had been en route back to Earth, as part of a general withdrawal from the farther reaches of the Terrasphere."
    narrator "The idea was to reorganize and prepare for a counterattack, but the exact details were privileged information."
    if rearline == True:
        narrator "The head technician of the Daedalus stumbles upon you and introduces himself."
        narrator "\"I'm Adam Ross,\" he said, smiling. He's an older guy, tall, with greying hair. \"I'm the head technician around here, and I heard you're my new protege.\""
        narrator "The two of you talk shop about the state of the ship as well as your responsibilities as a member of the maintenance crew. Ross is an alright guy."
    nvl clear
    scene space
    narrator "The vast expanse of space was all that was visible besides the incipient Earth."
    narrator "It isn't at all like in the movies you remember as a kid. Nor is it like those heavily doctored-up ancient photos you used to see in science textbooks."
    narrator "It's empty. Besides the Earth and Sun only the far-off pinpricks of light break up the darkness."
    narrator "It might be lonesome."
    narrator "But as you gaze out into that abyss you see a glint."
    nvl clear
    scene spaceLight
    narrator "It might have been a satellite of ancient times, were it not for the fact that the glint's trajectory was mismatched with any kind of natural orbit."
    scene bridge
    narrator "You head up toward the bridge where Captain Wright commands the ship from. Up on his pedastal, overlooking no less than two dozen assistant crewmen, he looks incredibly bored."
    narrator "\"Sir,\" you say, climbing up onto the platform. \"I think I saw a ship, coming from the port side.\""
    narrator "Wright perks up and scratches his head. His short, curly hair ruffles under his fingers."
    narrator "\"Navigator, bring up the port camera array,\" Wright says. The holo display, the most cutting edge in media technology, brings up a series of cameras. Wright scans each one, looking for the glint."
    narrator "He sees it, and points toward it. It expands in response to his gesture, displaying additional information about the camera  watching that part of the ship."
    nvl clear
    narrator "Perhaps against expectations, Wright begins issuing orders rapidly, trying to mask some evasive maneuver."
    narrator "He tries to avoid combat, but the enemy ship is already too close -- within just a few miles -- and upon noticing the sudden change in bearing the enemy ship dispatches a handful of small craft."
    narrator "These craft hightail it at a speed that would likely be supersonic in an atmosphere."
    narrator "Boarding craft."
    if frontline == True:
        narrator "Hand to hand combat was a focus in basic training, but the idea of facing off against real opponents in a life or death situation seemed dangerous. Even moreso than fighting them in ship to ship duels; that at least was impersonal."
        narrator "So it comes down to a decision."
        nvl clear
        menu:
            "Prepare to repel boarders":
                jump ShipMelee
            "Hide in your quarters":
                jump ShipHide
    
    else:
        jump EngiSkirmish
            
label ShipMelee:
    scene shipHall3
    play music "sounds/tense.mp3"
    play war "sounds/war.wav"
    narrator "You head down toward the armory."
    narrator "There are no klaxons this time, and the corridors are much more tolerably sized, so the cacophany isn't nearly as noticeable as it was aboard the Lion-class."
    scene armory
    narrator "The quartermaster sees you and points toward a line of racks, each clad with a suit of body armor -- the standard for infantry protection both in space and on Earth."
    narrator "You quickly toss on the gear and tighten it up, ensuring that the straps are taut but not overtightened."
    narrator "And to top it off, you pick up one of the M79 laser rifles -- the standard infantry small arm."
    narrator "Your stomach turns uncontrollably as you prepare. The boarding vessels rely on the airlocks just as much as any other smallcraft, so throughout the docking bay area other members of the crew prepare for their first hand to hand."
    scene shipAirlock
    narrator "You took a place behind a makeshift barrier, at one of the airlocsk taht seemed undermanned, and leveled your rifle at the door."
    scene black
    scene shipAirlockDark with fade
    play sound "sounds/doors.wav"
    narrator "The airlock's override mechanism activated and its pneumatic pistons forced it open at an incredible speed."
    narrator "No less than a dozen Colonial troops were waiting on the other side, and after a tense split second, both sides opened fire."
    play laserfire "sounds/laserfire.wav"
    nvl clear
    narrator "Laser bolts scorched the metal of the barrier. One of your crewmates gets hit, falling to the floor with a screaming and severe burns on his face."
    if pt < 6:
        nvl clear
        $ isInjured = True
        $ pt = pt - 2
        $ drive = drive - 2
        narrator "You yourself feel the scorch of a laser bolt as it strikes your chest. Although it has no mass, the burning energy the bolt transfers to your body is more than enough to lay you out."
        narrator "You fall to the floor, clutching at the wound. The armor was practically worthless for it."
        narrator "As you lay on the floor, certain you will die from the overwhelming pain, you eventually pass out."
        jump Reentry
    
    narrator "You fight valiantly in spite of your comrades being gunned down. Your bolts may or may not strike home, but despite being shot no less than three times, you remain standing."
    narrator "At one point, the Colonials attempt to charge out of the airlock, bashing one of your crewmates over the head with their rifles."
    narrator "But once they get to you, your superior physical training enables you to beat them back repeatedly."
    narrator "The burns can't even be felt until well after the battle is over and the adrenaline has subsided, but they are fairly small and not life threatening. However, the exhaustion hits you all at once and you pass out immediately after being reviewed for injury."
    nvl clear
    jump Reentry
    return
    
label ShipHide:
    narrator "Despite the cacophony outside, you lock the doors to your quarters and hope for the best."
    if pilot == True:
        narrator "You're a pilot anyway, not really a fighter. Trying to get involved would be a death wish, or so you think."
    if everyman == True:
        narrator "You're not really a fighter anyway, getting involved in a melee would be like a death wish."
    narrator "Eventually, the fighting subsides and an all-clear is given over the intercom."
    narrator "Thankfully, nobody saw your cowardice."
    jump Reentry
    return
label Reentry:
    #CH3: Intermission
    stop sound
    stop music
    stop laserfire
    stop war
    scene soldierChapter3
    $ renpy.pause()
    scene pacificOcean
    play music "sounds/hawaii.mp3"
    play surf "sounds/surf.wav" fadein 1.0
    nvl clear
    narrator "The re-entry went smoother than anticipated. The melee over America had resulted in the enemy ship fleeing from the fight when it realized its troops had been massacred."
    narrator "The two-day journey from the re-entry point to San Francisco began with a stopover in Hawaii."
    if isInjured == True:
        narrator "While you can move about and be active like you used to, your body resists your every motion."
        narrator "Rai Shimizu, the head medic, told you to stay in bed and get rest, but that ain't you."
        narrator "You'll keep a bandage wrapped around your chest, but you won't let a flesh wound keep you down."
    nvl clear
    scene Hawaii
    narrator "While the 301st Transport Corps refuels and refits the Daedalus, you and some other crewmates headed down to the beaches. For most of the crew, it was their first time on Earth, let alone their first time in such a place as Hawaii."
    narrator "Marble-white beaches stretch for miles in either direction, presenting on a silver platter the real ocean. Its rhythmically crashing surf, glassy teal gently reflecting an orange sun -- who knew the sun was orange on earth? While rivers and lakes were simulated in the colonies, few had ever seen such a mass amount of water in one place. And for the colonies, the sun is white. There are no atmospheric effects."
    narrator "One of the other crew stuck her feet into the water and yelped at the surprising cold. Despite being fairly mild, right in the range of the colony cylinders' optimal temperature, the water was practically freezing."
    narrator "A breeze kicked up. It was warm, and fairly dry, despite the proximity to the water. It's the first time you've ever felt natural wind, rather than something generated by a fan."
    narrator "Growing up in the colonies is different."
    nvl clear
    stop surf fadeout 10.0
    scene HawaiiTown
    if rearline == True:
        jump Friends
label Strangers:
    narrator "You, the lead technician on the ship, and the head medic, all head up to the little village just up the road from the beach, to take in the sights before the Transport Corps finishes their work."
    narrator "\"It's nice,\" Adam Ross, the technician, spoke up over the otherwise silent walk. \"It's nice that for once I'm not having to fix everything.\""
    narrator "\"I bet.\" You say. Ross is an older fellow. His hair  shows off  his age, greying steadily from the roots, while his face would suggest a younger man."
    narrator "\"At least the injured can get some proper medical care here,\" Rai Shimizu, the head medic, said. \"We've been so swamped down in the infirmary the last few weeks.\""
    if isInjured == True:
        narrator "\"And no thanks to you, [gender_formal] [player_name].\" She tacked  on. As if it was  your fault you got shot."
    jump nonFriends
label Friends:
    narrator "You, Ross, and Rai all head up to the little village just up the road from the beach, to take in the sights before the Transport Corps finishes their work."
    if RossBond < 1:
        narrator "\"It's nice,\" Ross said. \"It's nice that for once I'm not having to fix everything.\" It's unclear if he's referring to you or the Transport Corps. So you stay silent."
    if RossBond == 1:
        narrator "\"It's nice,\" Ross said. \"It's nice that for once I'm not having to fix everything.\""
        narrator "\"You can thank me with a drink later,\" you joke in response. Ross laughs." 
    narrator "\"At least the injured can get some proper medical care here,\" Rai said. \"We've been so swamped down in the infirmary the last few weeks.\""
    if RaiBond > 0:
        narrator "\"You've helped a lot, [player_name],\" she added after a split second. \"Made my life tolerable anyway.\""
    narrator "And all of this was true. Both the ship and her crew were practically coming apart as a result of the stresses they were under. It was borderline unimaginable the degree to which there were failures aboard the ship."
    narrator "Even you, as a technician, were feeling it. Not only because you have to deal with the mental and physical aspects of combat, but because you have to help keep the machines up and running in those conditions. You knew first hand what kind of stresses are at play."
    narrator "It was hard to believe, but the war had only been going on for about a month. Probably less."
   
label nonFriends:    
    nvl clear
    

    narrator "You stop over a small cafe in the town. All three of you get lemonade -- the first non-government-issued food you have had in weeks and the first time you've ever bought something on Earth."
    scene HawaiiTable
    narrator "You take a seat and enjoy your drinks as you take in the view."
    narrator "\"How long do you think we're going to stay here?\" Rai asks."
    narrator "\"Hawaii, or Earth as a whole?\" Ross asks."
    narrator "\"Earth.\""
    if RossBond == 1:
        jump Friends2
    narrator "\"It can't be long,\" Ross answers. \"Things have been falling apart pretty badly. I'm not really supposed to talk about this stuff with enlisted personnel, though. It's bad for morale.\""
    narrator "Rai frowns but doesn't pursue the conversation."
    jump EndLemonade
label Friends2:
    narrator "\"It can't be long,\" Ross answers. \"Things have been falling apart pretty badly.\" He froze for a second, as if having an internal conflict about something. He opens and closes his mouth several times."
    narrator "\"We're losing the war,\" he says at last. \"The brass have been going on about some Christmas Offensive, but you have to understand, half the forces they think they're commanding don't even exist anymore. They're so loose-lipped about it all, as well. I knew we haven't seen a war in ages, but you  would think they would realize that compromising our own secrets like this would backfire.\""
    nvl clear
    narrator "Rai swallows audibly. You think back. Ever since you'd transferred to the Daedalus you don't think you've seen her smile genuinely at all."
    narrator "\"It gets worse, too,\" Ross continued. \"Don't make me regret being your friend, [player_name], Rai.\" He leaned in and spoke more softly. \"The brass have been developing a WMD for the last few years. Something dangerous, capable of vaporizing entire colonies, and if it's turned on the earth it could even destroy the ozone layer. How do I know all this? They fuckin' sent me a copy of the technical manual for the thing by accident. I had to study it for a while but it's grim.\""
label EndLemonade:
    nvl clear
    narrator "Before long, you all finish your drinks, and the time to return to the ship draws near."
    scene HawaiiTown
    narrator "\"Where are we going next?\" You ask Ross as the three of you head back toward the ship."
    narrator "\"San Francisco,\" Ross says. \"Stopping over and linking up with the TFSF command there.\""
    scene black
    nvl clear
    narrator "Without any fanfare, the Transport Corps and the Daedalus ready to depart."
    narrator "The entire crew looks on with sadness, having been unable to really fully experience what the little island chain has to offer."
    nvl clear
    stop music fadeout 0.5

label Saboteurs:
    #CH4 - Saboteur
    scene soldierChapter4
    $ renpy.pause()
    scene shipHall3
    narrator "That same dreadful sound you heard months ago at the Academy rears its ugly head again just a few hours after having gotten into port at San Francisco."
    narrator "An explosion tore through the air. The ship shuddered and it shifted in its mooring."
    narrator "You had been in your quarters at the time, getting shuteye after pulling an overnight watch on the lower decks. An inspection of the site of the explosion revealed that the target was most likely the ship's powerplant -- the nuclear reactor."
    narrator "You were up and at 'em immediately, however. Together with several other members of the crew, the culprit was found hiding away in the kitchen cupboard of the ship's galley. He was a young man, probably not out of his teens; but he also wasn't a member of the crew."
    narrator "Wright had him hauled out of there and thrown in the brig, where he awaited interrogation, which would be done by a member of the TFSF's elite Ghost Wolves special operations unit."
    narrator "Wright himself, on the other hand, indicated that he wanted to head off to meet  with General Manstein as soon as possible for the officers' briefing. He invited you to go with him."
    if RaiBond > 0:
        narrator "Rai and Ross had both been there during the conflagration, but had disappeared not long after."
    menu:
        "Help interrogate the POW?":
            jump interrogation
            $ drive = drive - 2
            $ depression = depression + 2
        "Go with Wright.":
            jump Manstein
    
        "Look around for your friends" if RaiBond > 0:
            jump RaiColony
        
label interrogation:
    nvl clear
    scene interrogationRoom
    narrator "The suspect was brought into the interrogation room at the TFSF headquarters main office. It was a subterranean facility, so there were no windows and lighting was poor at best, but that made it perfect  for what the Ghost Wolves did in their interrogations. They were, for all intents and purposes, the Terrasphere Federation's secret police."
    narrator "The Geneva Convention was a distant memory. There were no rules as to what comprised a human right, no restrictions on what weapons and tactics could be employed in the waging of war."
    narrator "But even knowing these things from your history books could not have prepared you for what the Ghost Wolves did. What began as an attempt to 'assist' the interrogators very quickly turned into horror as the prisoner of war was progressively brutalized."
    nvl clear
    narrator "It started with the typical good-cop bad-cop routine. He was offered to be spared if he complied with what the Ghost Wolves wanted. The 'bad cop' on the other hand started beating the kid with bare fists."
    narrator "It only got worse from there. The secret police went from a simple beating to more complex rituals as the event dragged on and on. Waterboarding. Electroshock. Critical asphyxiation. Any pretense of gathering information went out the window as it became increasingly clear that the Wolves lives up to their namesake. They were  doing what  they did  for the hell of it."
    scene black
    narrator "And then they crossed a line."
    narrator "When they crossed that line, you had to leave. Or else your stomach might have come up out of your throat."
label Manstein:
    play ambiance "sounds/ambiance.mp3"
    nvl clear
    scene warRoom
    narrator "You link up with Wright heading into Manstein's office."
    narrator "Inside, the meeting has already been proceeding at full speed despite Wright's absence."
    narrator "\"Ah!\" an elderly voice said. \"I'm so glad to finally meet the famous Captain Wright!\" It was General Manstein himself. He appeared in quite a number of propaganda films in the last several weeks. Tall and slender, with greying hair, but  his most  prominent feature was the bushy mustache he sported."
    narrator "\"Thank you, sir.\" Wright said, giving a very slight bow."
    narrator "After cursory introductions, the entire general staff got right down to brass tacks. Much of the details was privileged information, so you didn't get to hear anything specific, besides the word 'icarus' as the name for some secret weapon. Besides from that, Wright was briefed on the situation at large. The Colonials had launched a massive global invasion during the One-Day War and in the following days, very quickly seizing a large proportion of major cities as well as innumerable high-importance resources, in particular the mines of Odessa."
    narrator "On the space front, the situation was even bleaker: large parts of the TFSF fleets had defected to the Colonial cause, leaving only three principle fleets operational on the fringes: Admiral George Pettit's Fifth Fleet, Admiral Grant's Second Fleet, and the Solar Patrol Fleet at the farthest Solar lagrange point."
    nvl clear
    narrator "Furthermore, Colonial space tech had far outstripped the TFSF's. The Colonial Liberation Front, which had been largely funded by corporate investors using under-the-table payments, had developed ship technology that could beat even the best TFSF ship. Active camouflage, spaced ceramic armor, and a larger array of weapons that were smaller than but also more powerful than their TFSF counterparts."
    narrator "There was a rough plan known as the 'Christmas Campaign' that seeks to unroot the Colonial hold on key regions. The precise degree of investment into this plan, which boiled down to little more than a headlong charge, illustrated how desperate the situation had gotten for the TFGF."
    nvl clear
    if rearline == True:
        narrator "But you knew that was bullshit."
        narrator "If what Ross said was true, the campaign was doomed to fail. And the irony was, this kind of open meeting was the perfect example of precisely how stupid TFSF brass was. They let some random noncom walk into a meeting with privileged information being thrown around, and nobody batted an eye."
        narrator "But you're not an officer. So you kept your tongue held tight. No rocking the boat."
    scene shipHall3
    narrator "You and Wright returned to the ship after the briefing ended. Because the damage to the ship from the attempted sabotage was so minimal, it was deemed a strategic necessity that the ship be immediately returned to space on its new mission to acquire the superweapon. From how Wright's face blanched after reading  the technical specifications of the device, it was easy to tell that it was immensely powerful."
    if rearline == True:
        narrator "As it sould be. If Wright doesn't know what the brass are doing, then that means that he's as innocent as they come. Which could be good or bad."
    jump leave
label RaiColony:
    scene shipHall3
    nvl clear
    narrator "Instead of going to the meeting or helping with the Prisoner of War, you head down to the infirmary, looking for Rai or Ross wasn't back yet."
    narrator "The medic is nowhere to be found, and neither is Ross."
    menu:
        "Look for Rai":
            narrator "So you do something you've never done before and seek out her quarters."
            $ RaiBond = RaiBond + 1
            $ depression = depression + 2 
            jump RaiColony2
        "Forget it, go hang out in your quarters":
            $ depression = depression + 3
            jump leave
            
label RaiColony2:
    narrator "You knock on her door and wait."
    scene barracks2
    narrator "Eventually, she opens up her door, looking bleary-eyed and exhausted."
    narrator "\"Need something, [player_name]?\" she asks, rubbing her eyes."
    narrator "\"I was bored,\" you say. \"Didn't feel like going to some boring old mens' meeting, and definitely didn't feel like watching a torture session.\""
    narrator "Her room is noticeably different from the much more barren barracks most of the ship's crew are stuck with. It's got wood paneling, and its own restroom. You had never seen a room like this before on a warship."
    narrator "\"Were you sleeping?\" You ask."
    narrator "\"Nope. Just tired from all this crap today.\" She huffed. \"Why don't you come in and take a seat?\" she asked."
    narrator "You take a seat in her desk chair while she sits on the edge of her bed."
    nvl clear
    narrator "\"I heard about what they did to that poor kid,\" she said. \"It's awful.\""
    narrator "Since you opted not to assist interrogation, you don't know what she's talking about -- the torture session comment was a joke."
    narrator "\What'd they do?\" You ask after some time."
    narrator "She shakes her head. \"Awful things. They ruined him, for the rest of his life -- assuming he even recovers from his injuries. I'm not even allowed to tend to them, the bastard Ghost Wolves refused me.\""
    narrator "She is silent for several long moments."
    narrator "\"Don't you realize how fucked up this is?\" she said. \"The level of incompetence we're serving under goes beyond what I originally thought back when I first became a medic. The overwhelming amount of power given to a handful of individuals  is borderline insane.\""
    narrator "You have to think of a response."
    menu:
        "Agree":
            $ RaiBond = RaiBond + 1
            "\"I think you're right,\" you say, after careful contemplation. \"I'm not sure how I feel about the TFSF anymore. I always just saw it as a way  out of the colonies, which it certainly is. My timing is just bad.\""
            nvl clear
            narrator "She laughs. \"That goes for all of us I think.\""
            narrator "Eventually she goes on at length the colonies she grew up in. It was one of the 'core' colonies  of the nascent colonial liberation movements. \"I even protested with my family on that colonial holiday. The movement became so violent though, that even we had to move elsewhere.\" she says. \"Our own people were getting hurt. So we looked to the TFSF to counterbalance that and restore some semblance of order. There's a saying: empires toppled from without will always get back up, but empires toppled from within are dead.\""
            narrator "\"I thought I could stay out of the conflict, too, by becoming somebody who heals people for a living. But I started looking at how my actions connect. All I'm doing is healing people so they can fight more. Even when I'm saving lives, I'm furthering the violence that injured these people in the first place.\""
            narrator "\"Listen to me ramble,\" she says after an hour or so. \"Thanks for  hearing me out. I've been stressed a lot recently with all these revelations regarding the TFSF.\""
            narrator "You smile. \"It's no problem.\" you say."
        "Disagree":
            $ RaiBond = RaiBond - 1
            narrator "\"I think that you may be overreacting. A handful of individuals doesn't represent the entire Terrasphere Federation, Rai.\""
            narrator "She shakes her head. Even though the conversation continues, it quickly becomes hollow and uncomfortable, and eventually you make an excuse to leave."
label leave:
    stop ambiance
    scene black
    nvl clear
    narrator "The ship's engines roar to life as you head to your quarters again to catch up on that sleep you'd missed  out on because of the sabotage."
    narrator "As you make your way, you hear talk among the crew about the Christmas Campaign. Spirits are high. Things seem to be looking up, for the moment."
    if rearline == True and drive > 7:
        narrator "You try your best to tell them not to get their  hopes up, without compromising your own standing by making too much of a ruckus."
    if rearline == True and not drive > 7:
        narrator "You know they're getting their hopes up for no good reason. But you don't have the heart to tell them as much."

label ColonyL7:
    #Chapter 5: L7 - Climax and Finale
    scene soldierChapter5
    $ renpy.pause()
    scene barracks
    nvl clear
    narrator "Two uneventful weeks have passed since the Daedalus set out for colony L7, on the far side of the moon."
    narrator "You've spent most of those days like this. Staring up at the ceiling, wondering what's going to happen next."
    if RaiBond > 1:
        narrator "On the  flip side, you've hung out with Rai and Ross quite a lot whenever you felt the desire for human companionship."
    narrator "And yet this is the longest you've gone with nothing happening since the war began."
    narrator "It's already being dubbed the \"Terrasphere Civil War\", but it's more accurately the \"Terrasphere Collapse\"."
    scene black
    narrator "The Christmas Campaign was a total failure."
    narrator "The losses on both sides number in the hundreds of millions."
    narrator "The TFGF made some initial gains, but once the Colonials began reacting the operation began to drag. The hope was, as per the name, to oust the Colonials from key locations by Christmas."
    narrator "Instead, just a few days after the operation commenced, a nuclear exchange ensued."
    scene bomb with fade
    nvl clear
    narrator "It was devastating for both sides, but especially for the Terrasphere Federation. Huge amounts of resources were rendered inaccessible for the near future, countless civilians were killed when their cities were demolished, and vast tracts of arable land was ruined."
    narrator "Most of the Colonial losses were military personnel. Admittedly, a disproportionate amount of Colonials are directly involved in the war, so they still did lose a  significant portion of their total population."
    narrator "But ultimately, nothing really changed. The situation in space has remained more or less static -- the Fifth and Second fleets linked up to create the Joint Fleet, but not major gains were made for either side. The Luna Base has been under seige since essentially the conflict began."
    scene barracks
    narrator "Morale sank to the lowest it had probably ever been. Few among the crew ever speak anymore, including you."
    if drive >=4 or depression < 7:
        narrator "Your spirit hasn't quite been broken, however. Something is driving you to keep pushing even in the face of the most intense adversity you had ever faced."
        narrator "You do your job. You don't slack. Even though discipline is practically nonexistant on the Daedalus anymore, you've kept up with your work. You've done your part."
    if drive < 4 or depression > 7:
        narrator "Your spirit has been broken. Along the way, something happened that caused you to lose hope. For you, it doesn't matter whether or not you, or anybody else, survives. For you, your life feels like a walking trainwreck in progress. Always on the road to self-destruction."
    play sound "sounds/shudder.wav"
    narrator "The ship shuddered, evidence that it had finally docked on L7 after close to two weeks en route."
    nvl clear
    narrator "You took your place in the queue to go out to the colony. Cabin fever was getting to everybody aboard and getting out would be good."
    narrator "L7 is a neutral colony, so you throw on some civilian clothes rather than your standard issue uniform."
    scene IT
    narrator "It's familiar."
    play ambiance "sounds/ambiance.mp3" fadein 10.0
    play music "sounds/non_canon_end.mp3" fadein 5.0
    narrator "The colony looks identical to L2, your home. The only difference is the immediate surroundings, visible through the side ports."
    narrator "You walk for some time, heading into the capitol city well before the rest of the Daedalus' crew has disembarked. While the 'fresh' air is nice compared to the air  aboard the Daedalus, it still can't quite beat the Earth's."
    scene colonyCafe
    narrator "Eventually, you find a friendly-looking mom and pop cafe, get a coffee, and sit down to relax."
    if RaiBond > 1:
        narrator "Rai finds you."
        narrator "She came looking for you from the ship, accompanied by Ross."
        narrator "Ross is from L7 -- even has a  smallcraft in port."
        narrator "\"Hear me out, [player_name].\" Rai prefaces her argument with. \"You know how we've  been discussing  how incompetent the TFSF high command is?\""
        narrator "You nod, slowly, seeing exactly where this is going."
        narrator "\"We want to go back, [player_name]. To Hawaii. To Earth.\""
        menu:
            "Defect":
                narrator "\"You're right,\" you say after some time. \"We have a golden opportunity to leave, and we should take it.\""
                jump defector
            "Stay loyal":
                narrator "\"I can't,\" you say, after heavy contemplation. \"This is my life. I can't just abandon my crewmates.\""
                narrator "\"So you'd rather abandon your friends?\" she returns, accusatively."
                narrator "You can only shrug. She mutters something along the lines of 'un-fucking-believable' before dragging Ross off.\""
                jump loyalist
    narrator "History lessons always told you that people come from many different places and cultures. And yet, with the Colonials, they would seem to beof the same kind. They share a common heritage, common history, common desires, common hopes. Hopes that have been repeatedly quashed by the Terrasphere Federation and Colonial Liberation Front alike. Hopes that play a formative role. And yet..."
    narrator "You  wile away an hour or two at the cafe."
label loyalist:
    play colonyKlaxon "sounds/klaxons.wav"
    stop ambiance fadeout 10.0
    stop music fadeout 5.0
    play music "sounds/tense.mp3"
    narrator "Klaxons sound."
    narrator "Everybody's head perks up at the sudden assault of noise against what had otherwise been a still and quiet day."
    nvl clear
    narrator "From the public spaceport lift, hundreds of smallcraft begin flooding the air."
    narrator "The Colonials are invading L7."
    nvl clear
    narrator "Without bothering to pay, you start heading back toward the ship."
    narrator "You're stopped short, however, when you start seeing Colonial troops dropping from the smallcraft in great numbers."
    narrator "It's tense and unclear exactly what's going to happen. The Colonials haven't been known to treat their conquests well, by any stretch, so the civilians for the most part have turned tail and run."
    narrator "You, on the other hand, have to go through these people."
    narrator "You unholster a sidearm, and begin picking your way through the city back toward the hidden spaceport on the far side of the cylinder."
    narrator "It is a lucky thing that colony cylinders aren't particularly large by necessity, even though they can support hundreds of thousands or even millions of people. The walk is slow, but tolerable, and thankfully nobody objects when you break into their  houses during a crisis like this."
    narrator "You skirt around the enemy who have begun sweeping the city."
    narrator "This could either be pure coincidence, or more likely, the Daedalus was tailed."
    nvl clear
    stop colonyKlaxon fadeout 5.0
    scene shipHall3
    
    narrator "When you finally make it back to the Daedalus, you're nearly shot by guards with itchy trigger fingers. They apologize, before rushing you to Captain Wright, assuming you have some information. But you don't. You're as oblivious to the situation as Wright or anybody else on the crew is."
    narrator "\"Ensign [player_name], it's highly likely they learned about the secret weapon and came here to stop us. More than likely, they wanted to get to it before we could leave the colony, because it's a lot harder to board a ship from space than it is to board it from a space port.\" Wright said"
    narrator "He shook his head and paced back and forth down the hall."
    narrator "\"We need to unmoor  the ship and get underway, now.\""
    narrator "You salute. You and a handful of your shipmates head back out of the ship and into the spaceport."
    scene controlRoom
    narrator "After some brief searching, you eventually find the control room for the moorings. One of the others posts up as a lookout incase any Colonials happen upon the spaceport."
    narrator "You set about undoing the moorings, taking great care to input the proper commands..."
    narrator "Jettison support arms. The icons on the monitors that indicate statuses of various apparati blink and change with each press of a button and turn of a lever. The arm supports disengage, although the Daedalus still sits on top of them."
    nvl clear
    narrator "Disable artificial gravity well. Again, another flip of a switch and turn of a knob and the Daedalus begins to levitate at its slot."
    narrator "Set depressurization timer... with a text input from a keypad, you give yourself five minutes to leave before the depressurization sequence begins."
    narrator "A spaceport is basically a giant airlock. You have to give yourselves time to escape as well."
    narrator "Set airlock door opening timer... And again, using a keypad you input just over 5 minutes."
    narrator "Set launch sequence timer... this one is  different. When the timer expires, the launch sequence begins -- the catapult attached to the stern of the ship will be rocketed out toward the airlock door. And with it, the ship will go. That has to happen just after the airlock door actually opens."
    narrator "With all parameters set, you and the team you came out with start making your way back toward the ship."
    nvl clear
    scene shipHall3
    narrator "The bunch of you hightail it, knowing time is ticking down. After the timers expire, the port will be depressurized, opened to the vaccuum of space, and subequently the ship will be launched without you, if you can't get back on board."
    stop music
    narrator "But you make it, and with no incidents on the way. The ship's hatches are all buttoned up, and with all heads accounted for, the ship prepares for launch."
label inAtTheDeath:
    ##The final act
    scene space
    nvl clear
    narrator "The ship lurches as the launch catapult goes."
    narrator "But it wasn't part of the plan to run directly into a ship."
    narrator "It's what the Captain referred to as an Orlov-class. One of the Colonials' line of battle ships."
    scene periscopeSight
    narrator "You get on the periscope at your station."
    scene space
    narrator "Everywhere, you see twinkling. But those aren't stars. Every direction you look, your view is filled up with an innumerable amount of glints, the glinting of metal, warships. It's the entire Colonial Third Fleet."
    play music "sounds/creep.mp3"
    narrator "The realization of just how outgunned and outnumbered you are hits like a rock to the face."
    narrator "You look around at your crew. None of them even realize yet. So you walk out."
    narrator "You numbly amble through the corridors of your ship. The ship you called your home for several months. The ship that carried you through your hardest and most trying time."
    narrator "Yet it was ultimately a drifting iron coffin."
    nvl clear
    scene black
    
    narrator "Your steps become rhythmic to your ears as you head up toward the bridge, wanting just to see."
    play war "sounds/war.wav"
    narrator "It's a wonder it took so long for things to escalate."
    narrator "It's a wonder you even survived as long as you did."
    narrator "If you had just stayed in the colony, couldn't you have lived to see the end of the war?"
    narrator "Or if you had stayed on Earth."
    narrator "Or transferred to any other ship."
    narrator "Maybe you could have lived."
    nvl clear
    scene bridge
    narrator "Captain Wright stared at his holo displays. The bridge crew stared at him. You stared at him."
    narrator "His face was empty."
    narrator "\"Ready the Icarus.\" He spoke only three words."
    narrator "The ship was coming apart. There were so many missiles hitting the hull, and darts piercing from every angle, there were failures  on all systems across the board. The ship was practically screaming in agony."
    narrator "You watch as the weapon, Icarus, came up on an elevator platform."
    nvl clear
    narrator "It was so small, so innocuous. At first you didn't think that could possibly be the superweapon that had been mentioned."
    narrator "But it charged up. Every color under the  sun was generated from its center."
    play sound "sounds/icarus.wav"
    narrator "And with a burning white light, half the colonial fleet disappeared."
    narrator "But... it was far  too late."
    scene white with flash
    nvl clear
    scene badend
    
    $ renpy.pause()
    window hide
    
    scene title
    
    $ renpy.pause()
    
    window hide
    return 
##Everything under here is for the noncombatant line only.
label EngiSkirmish:
    scene shipHall2
    nvl clear
    narrator "While the rest of the crew battled the boarders, you and Ross helped to keep systems running. The enemy ship was constantly pelting the Daedalus with darts and missiles, and while the ship's Close-In Weapons Systems managed to shoot down most of the missiles, the few hits the Daedalus took came close to taking important systems offline."
    narrator "Ross showed you how to deal with electrical fires in a high-oxygen environment, as well as giving a live demonstration of the wiring system hidden behind the ship's walls. He pointed out particularly important circuits, where their easiest access points are. And how to mend them using tools found in the technician storehouse."
    narrator "He even showed you where the 'heart' of the ship is -- the singular path through which all circuits pass at least one time."
    narrator "However, beyond a certain point, he seemed to have everything handled on his own."
    scene shipHall3
    narrator "So he decided to let you loose, and asked  you to go make yourself useful as the skirmish wound down."
    menu:
        "Continue to assist Ross":
            $ RossBond = RossBond + 1
            $ RaiBond = RaiBond + 1
            narrator "Despite him giving you explicit permission to do as you wished, you chose to continue helping Ross out around the ship."
            narrator "The two of you shoot the breeze as you clean up in the aftermath of the mess."
            nvl clear
            narrator "Topics vary wildly, but center mostly around home and Earth, and the Terrasphere at large. 'Earth Nostalgia', nostalgia for something you have never even been to, is surprisingly common among Colonial citizens, who often dream of moving to Earth some day."
            narrator "The chief medic on the ship, Rai Shimizu, came by with a list of damages. Specific casualty reports. It made me curious as to what exactly Ross's role was aboard the ship. He was clearly a high-ranking officer."
            narrator "But you don't sweat it. It's been a hard day and you've earn some rest."
            jump Reentry
        "Help the gun crews finish off the enemy":
            narrator "You head on over to the gun batteries, specifically Battery #1, which is the lead gun."
            narrator "The resulting workout from learning how to use the loading system is both fun and makes you feel pretty good about yourself."
            $ pt = pt + 2
            narrator "But at the end of the day, the activity seems rather pointless in hindsight, because the enemy ship was already fleeing. The guns didn't even manage to destroy it when all was said and done."
            nvl clear
            narrator "You see Ross talking with one of the medics, a woman by the name of Rai. It's easy to tell the medics from other midshipmen given that they always end up covered in blood at the end of any major conflagration. Whether it was  a riot, a freak accident, or combat, you could bet they'd be wading knee-deep in blood by the end of it."
            narrator "\"Hey, [player_name].\" Ross said."
            narrator "\"Sir?\" You ask."
            narrator "\"Good work out there,\" he said. He smiled and placed a hand on your shoulder. \"We need flexible people like you.\""
            narrator "\"Rai, where's Marlow?\" you ask, realizing that one of the other few survivors of your old Lion-class had seemingly disappeared in the cacophony."
            narrator "Rai's eyes flitted toward the door. \"He got shot with a laser bolt to the chest,\" she said. Her voice quaked. \"The chance he's going to pull through are... slim, at best.\""
            narrator "You blink. It takes a moment to process. You hardly even knew Marlow that well, but he had been a capable battery commander and a reasonable man."
            jump Reentry
        "Go see about tending to wounded":
            $ RaiBond = RaiBond + 1
            narrator "You follow the trails of blood through the halls toward where the medics are tending to the wounded."
            nvl clear
            narrator "Eventually, it leads you to the sickbay, where you see a young woman, Rai Shimizu cauterizing a  soldier's wounds."
            scene sickbay
            narrator "\"Is there some way  I can be of assistance?\" you ask."
            narrator "\"Oh thank God,\" she says, exasperated. \"We're flooded with injuries here, if you couldn't tell. Do you know first aid?\""
            narrator "You nod. \"What needs to be done?\" you ask."
            narrator "\"The guy on the gurney by the door needs his wounds cleaned and bandaged,\" she says. \"The three by the medical cabinet need an IV bloodbag ASAP. Or you can go and bring more injured soldiers in.\""
            narrator "You carry out the bloody tasks that are assigned of you."
            narrator "It's exhausting and disgusting, and gives you a much greater appreciation for the fragility of human life. Rai seems to have greatly appreciated the assistance, however -- some of her own medics were among those killed or wounded, so she was both understaffed and overloaded with patients."
            narrator "By the time you were done, you just threw yourself on your bunk and passed out."
            jump Reentry
label defector:  
    play music "sounds/canon_end.mp3"
    scene black
    nvl clear
    narrator "You follow the two toward the spaceport. The walk is fairly quick -- colony cylinders aren't too large."
    scene smallcraft
    narrator "With Ross's guidance, you power up the old smallcraft, and all three of you get settled in."
    narrator "You have this odd feeling. It's as if you can hear klaxons in the distance, like the chaos of the One-Day War."
    narrator "A distant memory."
    narrator "You come out of the port on the opposite side of the colony to the Daedalus."
    scene goodend
    
    $ renpy.pause()
    
    window hide
    
    scene title
    
    $ renpy.pause()
    
    window hide
    
    
return

label Death:
    nvl clear
    narrator "You have died."
    
    return