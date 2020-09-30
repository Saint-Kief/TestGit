import words
import hangman_draw     

def hangman():
    N = 7 # max number of stage
    stage = 0 
    secret_word = words.get_words() #in secret_word a randomly chosen word
    #...Continue writing the code of your game. Have fun!
    hangman_draw.hang(stage) #Hangman stage show up.
    word = list(secret_word) #Chooses random word from import words.
    msg = ("Help I cant breath")


    attempts = []
    for letter in word:
        attempts.append("_")   


    Result = True
    while Result: #Making a loop, so it keep replaying itself until game over. 
        print(f"You have {N - stage} chance remaining") #Print the ramining tries left.
        print(f"Your current word is: {' ' .join(attempts)}") #Print out the correct words.
        letters_guessed = input("Guess a letter: ") #Ask the player to guess the letter.

        if stage == 0: # Will draw the head after first failed attempt and so it goes on. 
            hangman_draw.draw_head()
        if stage == 1:   
            hangman_draw.draw_left_leg()
        if stage == 2:
            hangman_draw.draw_right_leg()
        if stage == 3:
            hangman_draw.draw_left_arm()
        if stage == 4:
            hangman_draw.draw_right_arm()
        if stage == 5: 
            hangman_draw.draw_face() # Draws the last pieces from the import hangman_draw. 
            hangman_draw.print_message(msg) # Print out message under the drawing. 

        if letters_guessed in word: #If the player guessed the correct letter.
            print(f"Good job! The {letters_guessed} is the correct letter!\n")
            for i in range(len(word)):
                letter = word[i]
                if letter == letters_guessed:
                    attempts = word[i]
                    word[i] = "_"
            
        elif letters_guessed not in word:
            #If the player picked the wrong letter. 
            print("\nYou guessed the wrong letter!\nTry again.\n")
            stage += 1 #Add 1 more number in 'stage' string. 

        if all("_" == letters_guessed for letters_guessed in word): #Won the game, it stops here. 
            print("Congratulation, You won!\nYou finished all the missing letters")
            return Result

        if stage >= N: #If stage is greater/eqaul to 'N' max attempt.
            print(f"Game over!\nBetter luck next time.\nGoodbye!") #Stops the game. Gamer over. 
            break

hangman()