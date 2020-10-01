import words
import hangman_draw

def hangman():
    F = 7 #Max failed attempt.
    att = 0 #Count the attempt.
    secret_word = words.get_words() #Secret_word pick random word from import words.
    word = list(secret_word) #It choose one from the list.
    hangman_draw.hang(att)
    msg = ("Help I cant breath")


    hid_let = [] #Hidden letter in the word. 
    for letter in word: #Look for a letter in word.
        hid_let.append("_") #The blank space in letter.

    Win = True
    while Win: #Making a loop. It keep replaying itself until game over. 
        print(f"You have {F - att} tries remaining.") #Print the ramaining tries left. 
        print(f"Your current word is: {' '.join(hid_let)}") #Print out the correct words. 
        Guessed = input("Guess a letter: ") #Ask the player to guess the letter.


        if att == 0: # Will draw the head after first failed attempt and it goes on...
            hangman_draw.draw_head()
        if att == 1:   
            hangman_draw.draw_left_leg()
        if att == 2:
            hangman_draw.draw_right_leg()
        if att == 3:
            hangman_draw.draw_left_arm()
        if att == 4:
            hangman_draw.draw_right_arm()
        if att >= 5: 
            hangman_draw.draw_face() # Draws the last pieces from the import hangman_draw. 
            hangman_draw.print_message(msg) # Print out message under the drawing. 


        if Guessed in word: #If player guessed the correct letter.
            print(f"\nLetter {Guessed} is correct. Good job!\n") #Print out the guessed letter.
            for i in range(len(word)): #It look for the letter, in the current word list.
                letter = word[i] #Word is picked and is given a new value.
                if letter == Guessed: #If letter is same as Guessed = True. 
                    hid_let[i] = word[i]
                    word[i] = "_"
                
            #If missing letter is filed up, you won.    
            if all ("_" == guessed_letter for guessed_letter in word): 
                print("Congratulation. You won!\nYou completed the missing letters.")
                return Win #Stops the game loop after winning. 

        
        else: #If player picked the wrong letter.
            print("\nYou guessed the wrong letter!\nTry again.\n") 
            att += 1 #It adds +1 on each failed attempt. 
            if att == F: #If True = Game over. 
                print("Game over\nBetter luck next time.\nGoodbye!") 
                break              
hangman()








