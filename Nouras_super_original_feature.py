"""HVNGMVN

Spooky hangman game.

"""
from time import sleep
from tqdm import tqdm
import random

HANGMAN = (
"""
     ----
    |    |
    |
    |
    |
    |
    |
    |
----------
""",
"""
     ----
    |    |
    |    0
    |
    |
    |
    |
    |
----------
""",
"""
     ----
    |    |
    |    0
    |   -+-
    |
    |
    |
    |
----------
""",
"""
     ----
    |    |
    |    0
    |  /-+-/
    |
    |
    |
    |
----------
""",
"""
     ----
    |    |
    |    0
    |  /-+-/
    |    |
    |    |
    |
    |
----------
""",
"""
     ----
    |    |
    |    0
    |  /-+-/
    |    |
    |    |
    |   | |
    |
----------
""")


"""The word bank will be updated over time."""

WORDS = ("AS_SILENT_AS_THE_GRAVE", "MAUSOLEUM", "MEMENTO_MORI", "PRETERNATURAL", "POLTERGEIST", "NECRONOMICON", "SEANCE", "DEVILS_ADVOCATE", "OVER_MY_DEAD_BODY", "DROP_DEAD_GORGEOUS", "SPILL_YOUR_GUTS", "GHOST_OF_A_CHANCE", "SKELETON_IN_THE_CLOSET", "SIX_FEET_UNDER", "IN COLD BLOOD", "BAT_OUT_OF_HELL", "SCARED_STIFF", "PHANTASMAGORIA", "TRISKAIDEKAPHOBIA")

print("I N I T I A L I Z I N G. . . . . . . . . .")

for i in tqdm(range(100)):
    sleep(0.01)

print("""
    |\     ____
    | \.-./ .-'
     \ _  _(
     | .)(./
     |   \(
     |     \   |
     |  +vvv   |
     |  |__    |
   /      `-.  |
""")
print("Welcome to HVNGMVN.EXE \n")
print("Please wait for your host.")

sleep(10)

print("""
    |\     ____
    | \.-./ .-'
     \│_  _(
     |¡^  ^/
     |   \(
     |     \   |
     |  +vvv   |
     |  |__    |
   /      `-.  |
""")
print("Eheheheh....Apologies...")
sleep(3)
print("Lord MALEK will be with you shortly.")

sleep(5)

print("""\n
   ,    ,    /\   /\ 
  /( /\ )\  _\ \_/ /_
  |\_||_/| < \_   _/ >
  \______/  \|0   0|/
    _\/_   _(_  ^  _)_
   ( () ) /`\|V^V^V|/`\ 
     {}   \  \_____/  /
     ()   /\   )=(   /\ 
     {}  /  \_/\=/\_/  \ 
""")
print("\n Ugh! I'll never know why I thought THIS particular contract was worth my time.")
sleep(5)
print("\n Another group of mortals dares to challenge me to a game of HVNGMVN? Fine, let's get this over with.")
input('\n Press the enter key to continue.')
print(""" \n 
Welcome to my personal little slice of Hell, where your pitiful guessing skills will be tested. You have only five--yes,
five--chances to guess the word or phrase. I don't have all eternity you know... Well, actually, I do, but I already
waste enough of it as it is.
""")
input('\n Press the enter key to continue.')
print("""\n
The utterances I've chosen are dark and dreadful, pulled from the depths of forgotten nightmares. Each incorrect guess 
draws the noose tighter. It's tiresome, really, how predictable your struggles will be... *yawn*
""")
input('\n Press the enter key to continue.')
print("""
So... scramble to guess letters if you must, but remember, with each misstep my patience wears thin and your doom draws
near. Can you succeed, or will you, like so many before you, fall into the abyss of failure?
""")
input('\n Press the enter key to continue.')

print("""
    |\     ____
    | \.-./ .-'
     \ _  _(
     | .)(./
     |   \(
     |     \   |
     |  +vvv   |
     |  |__    |
   /      `-.  |
""")

print("[NOTE: Choose a champion to play against MALEK. If you lose, you will be consigned to torture until such time as MALEK is defeated. Upon failure, a new champion must be chosen.]")

input('\n Press the enter key to continue.')

win = False

while not win:
    MAX_WRONG = len(HANGMAN) - 1
    # INITIALIZE VARIABLES
    word = random.choice(WORDS) # word to be guessed
    so_far = '_' * len(word) # one dash for each word to be guessed
    wrong = 0 # number of wrong guesses by player
    used = [] # letters already guessed

    while wrong < MAX_WRONG and so_far != word:
        print(HANGMAN[wrong])
        print("""\n
       ,    ,    /\   /\  
      /( /\ )\  _\ \_/ /_ 
      |\_||_/| < \_   _/ >
      \______/  \|0   0|/ 
      ==========================
        """)
        print("\n So far, you've used the following letters:\n", used)
        print("\n :\n", so_far)
        
        guess = input("\n\n Enter your guess:")
        guess = guess.upper()
        
        while guess in used:
            print("""\n
             ,    ,    /\   /\  
            /( /\ )\  _\ \_/ /_ 
            |\_||_/| < \_   _/ >
            \______/  \|¿   ¿|/ 
            ==========================
              """)
            print("You've already guessed the letter", guess)
            guess = input("Enter your guess:")
            guess = guess.upper()
            
            
        used.append(guess)
        
        if guess in word:
            print("""\n
                 ,   ,
                /(   )\ 
                \ \_/ /   , /\ ,
                /_   _\  /| || |\ 
                |  \> |  \| || |/
            ===========================       
            """)
            print("\n Yes...", guess, "is correct. Lucky you.")
            
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]
            so_far = new
            sleep(3)
        else:
            print("""\n
                     ,    ,    /\   /\  
                    /( /\ )\  _\ \_/ /_ 
                    |\_||_/| < \_   _/ >
                    \______/  \|^   ^|/ 
                    ==========================
                      """)
            print("\n Fool!", guess, "is incorrect.")
            wrong += 1
            sleep(3)
            if wrong == 4:
                print("""
                Ah, the suspense is almost palpable. One last guess stands between you and your inevitable demise.
                 Can you feel the weight of your impending failure pressing down upon you, mortal?
                """)
                input('Press the enter key to continue')
            
    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("""\n
           ,    ,    /\   /\ 
          /( /\ )\  _\ \_/ /_
          |\_||_/| < \_   _/ >
          \______/  \|^   ^|/
            _\/_   _(_  ^  _)_
           ( () ) /`\|V-V-V|/`\ 
             {}   \  \_^_^_/  /
             ()   /\   )=(   /\ 
             {}  /  \_/\=/\_/  \ 
        """)
        print("""\n
        Well, well, well... look who couldn't handle a simple game of HVNGMVN. I must say, your failure was as predictable
        as I said it would be, but not as boring. How delightful it was to watch you fumble in the dark, grasping at straws 
        and missing the mark entirely.
        """)
        input('\n Press the enter key to continue.')
        print("""\n
           ,    ,    /\   /\ 
          /( /\ )\  _\ \_/ /_
          |\_||_/| < \_   _/ >
          \______/  \|0   0|/
            _\/_   _(_  ^  _)_
           ( () ) /`\|V^V^V|/`\ 
             {}   \  \_____/  /
             ()   /\   )=(   /\ 
             {}  /  \_/\=/\_/  \ 
        """)
        print("""\n
        Your five chances have come and gone, and now YOU must join the ranks of the countless other lost souls who thought they could best me.
        Take solace in knowing you've provided a brief moment of amusement in my otherwise monotonous eternity.
        """)
        input('\n Press the enter key to continue.')
        print("""\n
           ,    ,    /\   /\ 
          /( /\ )\  _\ \_/ /_
          |\_||_/| < \⋋   ⋌/ >
          \______/  \|⊚   ⊚|/
            _\/_   _(_  ^  _)_
           ( () ) /`\|V-V-V|/`\ 
             {}   \  \_^_^_/  /
             ()   /\   )=(   /\ 
             {}  /  \_/\=/\_/  \ 
        """)
        print("Wish the next victim luck--by the looks of it they'll need it. Now, be gone.")
        input('\n Press the enter key to continue.')
    else:
        win = True
        print("""\n
           ,    ,    /\   /\ 
          /( /\ )\  _\ \_/ /_
          |\_||_/| < \_   _/ >
          \______/  \|X   X|/
            _\/_   _(_  ^  _)_
           ( () ) /`\|  ■  |/`\ 
             {}   \  \_____/  /
             ()   /\   )=(   /\ 
             {}  /  \_/\=/\_/  \ 
        """)
        print("""\n
        Well, well, it seems even the dimmest candles can flicker brightly from time to time. Against all odds, you've
        managed to infer my arcane inscription. How delightfully infuriating.
        """)
        input('\n Press the enter key to continue.')
        print("""\n
        Enjoy your fleeting triumph, for in the grand scheme of things, you are still just a play thing in the hands of an
        indifferent Universe.
        """)
        input('\n Press the enter key to continue.')
        print("""\n
       ,    ,    /\   /\ 
      /( /\ )\  _\ \_/ /_
      |\_||_/| < \_   _/ >
      \______/  \|0   0|/
        _\/_   _(_  ^  _)_
       ( () ) /`\|V^V^V|/`\ 
         {}   \  \_____/  /
         ()   /\   )=(   /\ 
         {}  /  \_/\=/\_/  \ 
    """)
        print("As my contract requires, here is the prize you seek. The combination...")
        input('\n Press the enter key to continue.')
        print("\n ■■■■■■■ G E N E R A T I N G ■■■■■■■ C O M B I N A T I O N ■■■■■■■ ")
        
        for i in tqdm(range(100)):
            sleep(0.01)
            
        print("""\n
         9999
        99  99
         99999
            99
         9999
        """)
        sleep(3)
        print("""\n
         3333   1111
        33  33    11
           333    11
        33  33    11
         3333   111111
        """)
        sleep(3)
        print("""\n
        1111
          11
          11
          11
        111111
        """)

sleep(3)

print("""\n
    |\     ____
    | \.-./ .-'
     \ _  _(
     | .)(./
     |   \(
     |     \   |
     |  +vvv   |
     |  |__    |
   /      `-.  |
""")
print("Hehehe... thanks for playing! Now that you've entertained Master he'll beat me less tonight.")
input("\n\n Press the enter key to exit.")
