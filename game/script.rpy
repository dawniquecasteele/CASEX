init python:

    # Mitosis Match 
        def RandomizeCards():
            global cards
            cards = []

            #for i in range(int(cardAmount / 2)):
                #rand_card_num = renpy.random.randint(1,6) 
                #cards.append(["Cards/cardname-%s" % rand_card_num, "deselected", "visible"])
                #cards.append(["Cards/cardimage-%s" % rand_card_num, "deselected", "visible"])

            cards.append(["Cards/cardname-1", "deselected", "visible", "1"])
            cards.append(["Cards/cardimage-1", "deselected", "visible", "1"])

            cards.append(["Cards/cardname-2", "deselected", "visible", "2"])
            cards.append(["Cards/cardimage-2", "deselected", "visible", "2"])

            cards.append(["Cards/cardname-3", "deselected", "visible", "3"])
            cards.append(["Cards/cardimage-3", "deselected", "visible", "3"])

            cards.append(["Cards/cardname-4", "deselected", "visible", "4"])
            cards.append(["Cards/cardimage-4", "deselected", "visible", "4"])

            cards.append(["Cards/cardname-5", "deselected", "visible", "5"])
            cards.append(["Cards/cardimage-5", "deselected", "visible", "5"])

            cards.append(["Cards/cardname-6", "deselected", "visible", "6"])
            cards.append(["Cards/cardimage-6", "deselected", "visible", "6"])




            renpy.random.shuffle(cards)
        
        def SelectCard(cardIndex):
            global selectedCards
            global matchFound

            cards[cardIndex][1] = "selected"
            selectedCards.append(cardIndex)

            

            if len(selectedCards) == 2 and (cards[selectedCards[0]][3] == cards[selectedCards[1]][3]):
                matchFound = True 
                

        def HideMatches():
            global selectedCards
            global matchFound
            global hiddenCards

            cards[selectedCards[0]][2] = "hidden"
            cards[selectedCards[1]][2] = "hidden"
            hiddenCards += 2
            DeselectCards()
            matchFound = False

        def DeselectCards():
            global selectedCards

            if len(selectedCards) == 2:
                for card in cards:
                    if card[1] == "selected":
                        card[1] = "deselected"
            
            selectedCards = []

        def ResetGame():
            global matchFound
            global hiddenCards

            matchFound = False
            hiddenCards = 0
            RandomizeCards()

    # DNA Drag

        def SetupPuzzle():
            for i in range(pieces):
                startX = 800
                startY = 200
                endX = 1000
                endY = 800
                randLoc = (renpy.random.randint(startX, endX), renpy.random.randint(startY, endY))
                initPiecesCoords.append(randLoc)

        def PieceDrop(droppedOn, draggedPiece):
            global finishedPieces

            if draggedPiece[0].drag_name == droppedOn.drag_name:
                draggedPiece[0].snap(droppedOn.x, droppedOn.y)
                draggedPiece[0].draggable = False
                finishedPieces += 1

                if finishedPieces == pieces:
                    renpy.jump("day2")
      

        
# People 
define c = Character("Clifton")
define a = Character("Alaric")
define s = Character("Samira")
define e = Character("Emery")

define who = Character("???")
define yn = Character("[name]")

# Backgrounds

image home = "homeBG.png"
image lab = "lab.png"

# Sprites

# clifton
image cneutral = "clifton_neutral.png"
image chappy = "clifton_happy.png"
image cscared = "clifton_scared.png"
image cupset = "clifton_upset.png"
image cthinking = "clifton_thinking.png"

# alaric
image aneutral = "alaric_neutral.png"
image ahappy = "alaric_happy.png"
image ascared = "alaric_scared.png"
image aupset = "alaric_upset.png"
image athinking = "alaric_thinking.png"

# samira
image sneutral = "samira_neutral.png"
image shappy = "samira_happy.png"
image sscared = "samira_scared.png"
image supset = "samira_upset.png"
image sthinking = "samira_thinking.png"

# emery
image eneutral = "emery_neutral.png"
image ehappy = "emery_happy.png"
image escared = "emery_scared.png"
image eupset = "emery_upset.png"
image ethinking = "emery_thinking.png"


# other 
#image phone = ""
image splash = "splash logo.png"
image white = "white.png"
image phone = "phone.png"

# Other
transform cardFadeIn:
    alpha 0.0
    easein 0.5 alpha 1.0

# Mitosis Match

default cardAmount = 12
default cardRows = 3
default cards = []
default selectedCards = []
default hiddenCards = 0
default matchFound = False
default isDone = False

screen mitosisMatch:
    image "minigameBG.png"
    grid int(cardAmount / cardRows) cardRows:
        align (0.5, 0.5)
        spacing 5
        
        for i, card in enumerate(cards):
            if card[1] == "deselected" and card[2] == "visible":
                imagebutton idle "cardback.png" sensitive If(len(selectedCards) != 2, True, False) action Function(SelectCard, cardIndex = i)  #at cardFadeIn
            
            elif card[1] == "selected" and card[2] == "visible":
                image "%s.png" % card[0]  #at cardFadeIn

            else:
                null

    if matchFound:
        timer 0.8 action Function(HideMatches) repeat True
        
    elif len(selectedCards) == 2:
        timer 0.8 action Function(DeselectCards) repeat True

    elif hiddenCards == cardAmount:
        textbutton "Return" action Jump("afterMitosis") align (0.5, 0.5)
    
      

# DNA Drag

default pieces = 12
default fullPageSize = (711, 996) # change this
default piecesCoords = []
default initPiecesCoords = []
default finishedPieces = 0

screen DNADrag:
    image "minigameBG.png"
    frame:
        # background " .png"
        xysize fullPageSize
        anchor(0.5, 0.5)
        pos(650, 535)

    draggroup:
        # Paper Pieces
        for i in range(pieces):
            drag:
                drag_name i
                pos initPiecesCoords[i]
                anchor(0.5, 0.5)
                focus_mask True
                drag_raise True
                # image "Pieces/piece-%s.png" % (i + 1)


        # Snappable Spots

        for i in range(pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped PieceDrop
                pos piecesCoords[i]
                anchor(0.5, 0.5)
                focus_mask True
                # image "Pieces/piece=%s.png" % (i + 1) alpha 0.0
                


    

# START

label splashscreen:
    show white
    with Pause(1)

    show splash with dissolve
    with Pause(2)

    hide splash with dissolve
    with Pause(1)

    return

    
label start:
    
    # Get Name
    $ name = renpy.input("What would you like to be called?")
    $ name = name.strip()
    if name == "":
        $ name = "Doc"

        jump mitosis

    

label exposition:

    show home with fade
    

    "The bills were beginning to stack up. After graduating college, you couldn't seem to find a job in your field."

    "You kept applying to everywhere you thought you'd be a good fit, but you never recieved a response."

    "Your rent was due soon, and your current part-time job was not gonna cut it."

    "You needed another job, fast."

    "*buzz buzz!*"
    
    show phone with hpunch

    "Your phone rang, pulling you out of your thoughts."

    yn "Hello?"

    who "Hello, may I speak with [name]?"

    yn "This is them."

    who "Oh great! We're pleased to inform you that we've reviewed your application at Helix Laboratories, and we think you'll be a good fit in one of our human resources positions!"

    "Human resources? Helix Laboratories? You don't remember applying to that company. They were a well-known lab in your state, focusing in DNA testing and research."

    yn "May I have some more information about this position you're offering? I can't recall the position listing."

    who "Yes of course. Makes sense."

    who "As a human resources officer, you'll be responsible for handling conduct and other issues in our company. Not too hard, I think. A perfect entry level job!"

    "Do recruiters usually speak like this, like they're trying to sell you on the job?"

    "You didn't even study human resources in college. This feels like a mistake."

    yn "I'm sorry, I don't think I can accept this position."

    "Those words hurt to say. It hurt your wallet, mostly. Yeah, you needed money, but this feels sketchy."

    who "But you are the perfect candidate! We've seen your resume, your education- you'll fit right in!"

    yn "But I didn't study human resources in college."

    who "The base salary is $70,000, and we'll send you your first paycheck upfront."

    who "We really need to fill this position, and you're our top choice. Will you accept this position?"

    menu: 
        "Will you take the job?"

        "Yes": 
            "A job is a job, right?"
        
        "No":
            jump avoidance_ending

    who "Great! We'll email you the details later. Have a great day and welcome to Helix Laboratories!"

    hide phone with easeoutbottom
    "The recruiter hung up the phone. You pinched your nosebridge- what did you get yourself into?"

    hide home
    jump day1

label mitosis:
    $RandomizeCards()
    call screen mitosisMatch
    return


label dna:



label day1:

show lab with fade 

"You arrived at Helix Laboratories, ready for your first day."

show sneutral with dissolve

who "Hey, are you the new hire?"

yn "Yes, I am. My name's [name] and I'm pretty sure I was assigned to your team?"

"You looked at the woman in front of you. She was wearing a white coat. Aren't you supposed to be on a team with other HR officers?"

hide sneutral
show shappy

s "Well it's nice to meet you [name]! My name is Dr. Samira Bahar and  I'm so glad to have another doctor on the team!"

yn "Doctor? I-"

"*buzz buzz!*"



show phone with hpunch

"I'm so sorry, my recruiter is calling me?"

hide phone

show shappy

s "Yes, of course. They tend to be a bit chatty on the first day. I'll be over there when you're done."

hide shappy with dissolve

show phone

yn "Hello?"

who "Hi there! I think I forgot to disclose some information the other day."

yn "Yeah I believe so. Why does the team think that I'm a doctor?"

who "Well, because you first case is to investigate this team. Undercover."

who "We have reason to believe that one of the members of the team is a criminal."

"You went silent. You did not sign up for this."

yn "I thought being a HR officer meant investigating disorderly conduct, not actual crimes!"

who "This is extremely important. It's vital that we find out who is the criminal, quickly."

yn "Can't you get the police involved, or even a more experienced HR officer?"

who "As I said earlier, we need this to be done as quick as possible. You're the best candidate for this."

who "And there's no backing out. You've already signed our contract, [name]."

"You sighed."

yn "Well, is it bad? Murder?"

who "We're not sure. There are employees in our company that have been dissapearing. After reviewing the evidence found, the genome has been labelled as CASE X."

yn "CASE X?"

who "Yes. Case X. And one of the four people has that genome. It's your job to find them. Now good luck!"

hide phone with easeoutbottom

"What are you going to do? This is so out of your field! This is -"

show aneutral

who "Ah, the new doctor."

hide aneutral
show aupset

who "Do you think you have what it takes to join our team?"

yn "Huh!"

who "Play this game, and we'll see how you'll fare in our team."

jump mitosis

label afterMitosis:

who "Well, I guess you're smarter than it seems."

hide aupset with easeoutleft

"This was going to be a rough job. Are you going to be able to handle it?"

hide lab with dissolve

show text "To Be Continued"
with Pause(2)

hide text

return

label day2:





label day3:





label day4:




label day5:






label avoidance_ending:

    "You declined the job. You are absolutely sure that it was a scam."

    hide phone with easeoutbottom

    "It's alright. You'll find another job, right?"
    
    hide home with dissolve

    show text "Ending 1 - Avoidance" 
    with Pause(2)

    hide text 

    return



label c_ending:

    c "..."

    return

label a_ending:

    a "Are you kidding me?"


    return

label s_ending:

    s "Do you even realize what you just said?"

    return

label e_ending:

    e "What?"
    return

label x_ending:

    return

    # This ends the game.

    return
