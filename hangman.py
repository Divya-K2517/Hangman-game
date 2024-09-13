import pygame
import sys

#lists, dictionaries
word_dict = {} #contains the letters to be guessed
wrong_guesses = [] #contains all wrongly guessed letters
right_guesses = {} #contains all the correct guess and their index number in the word
body_parts = ["head", "body", "right arm", "left arm", "right leg", "left leg"] #contains all the not drawn body parts
game_over = False
game_won=False

#ask for word
print()
print("=====WELCOME TO HANGMAN=====")
word = input("What is the word you want others to guess(single world only)? " )
for i in range(40):
    print()

for i in range (len(word)):
    word_dict[i] = word[i]


pygame.init() #starts up pygame
screen = pygame.display.set_mode((1000, 300)) #creates a screen of width 350 and length 600
clock = pygame.time.Clock() #sets up an FPS(frames per second)
surface = pygame.Surface((1000,300))
font=pygame.font.Font(None, 24)
bigfont = pygame.font.Font(None, 48)

#functions
        
def guess_letter():
    global game_over
    guess = input("Guess a letter(lowercase): " )
    if game_won ==False and game_over==False:
        if guess in word_dict.values() and guess not in right_guesses: # if guess is right and hasnt been guessed before
            for key, value in word_dict.items():
                if value == guess:
                    right_guesses[key] = guess

        elif guess not in wrong_guesses and guess not in right_guesses: #if guess is wrong and hasnt been guessed before
            wrong_guesses.append(guess)
            if body_parts[0] == "head":
                pygame.draw.circle(surface, (250,250,250), (140,100), 20)
                body_parts.remove("head")

            elif body_parts[0] == "body":
                pygame.draw.line(surface, (250,250,250), (140,120), (140,180), width=2)
                body_parts.remove("body")

            elif body_parts[0] == "right arm":
                pygame.draw.line(surface, (250,250,250), (140,120), (170,170), width=2)
                body_parts.remove("right arm")

            elif body_parts[0] == "left arm":
                pygame.draw.line(surface, (250,250,250), (140,120), (110,170), width=2)
                body_parts.remove("left arm")

            elif body_parts[0] == "right leg":
                pygame.draw.line(surface, (250,250,250), (140,180), (160,220), width=2)
                body_parts.remove("right leg")

            elif body_parts[0] == "left leg":
                pygame.draw.line(surface, (250,250,250), (140,180), (120,220), width=2)
                body_parts.remove("left leg")
                game_over = True
                
        elif guess in wrong_guesses: #guess has already been guessed
            print()
            print("You've already guessed this letter, try again")
            guess = input("Guess a letter(lowercase): " )

        print()


#texts
already_guessed = font.render("Already guessed: ", True, (250,250,250))

#Drawing on-screen constants
pygame.draw.line(surface, (250,250,250), (20,270), (160,270), width=3)
pygame.draw.line(surface, (250,250,250), (70,50), (70,270), width=3)
pygame.draw.line(surface, (250,250,250), (70,50), (140,50), width=3)
pygame.draw.line(surface, (250,250,250), (140,50), (140,80), width=3)
startx = 200
endx=230
for i in range(len(word)):
    pygame.draw.line(surface, (250,250,250), (startx,270), (endx, 270),  width=8)
    startx += 80
    endx += 80

#main code 
running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #above 4 lines make it so the user has a way to close the screen
    screen.fill((0,0,0)) #makes the screen black
    screen.blit(surface, (0,0)) #puts the surface on the screen
    screen.blit(already_guessed, (180, 40))

    #showing right letters
    for i, letter in right_guesses.items():
        right_letter = font.render(letter, True, (250,250,250))
        screen.blit(right_letter, (200+(i*80),250))

    #showing wrong guesses
    wrong_text = font.render(" ".join(wrong_guesses), True, (250,250,250))
    screen.blit(wrong_text, (180,60))

    if game_over:
        game_over_text = bigfont.render("GAME OVER YOU KILLED THE GUY", True, (250,0,0))
        screen.blit(game_over_text, (200,150))
        
    elif len(right_guesses) == len(word_dict.keys()):
        game_won=True
        game_won_text = bigfont.render("GOOD JOB YOU WON", True, (0,250,0))
        screen.blit(game_won_text, (400,150))

        
    elif not running:
        pygame.mixer.get_busy(20)
        sys.exit()

    pygame.display.flip() #updates display
    #player guess letter
    if not game_won and not game_over:
        guess_letter()


