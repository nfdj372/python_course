import random

def hangman():
    words = ["cat","dog","book","tree","car","house","chair","apple","ball","flower","hello","goodbye","sorry","please","yes","no","friend","family","time","travel","music","school","work","city","weather","hobby","exercise","food","holiday","friendship","shopping","restaurant","conversation","health","language","meeting","job","culture"]
    word = random.choice(words) 
    guessed_letters = []
    tries = 6 

    while tries > 0:
        guessed_word = ''
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += '_ '

        print('Current word:', guessed_word)
        print('Tries left:', tries)

        if guessed_word == word:
            print('Congratulations! You guessed the word!')
            return

        guess = input('Enter a letter: ').lower()

        if guess in guessed_letters:
            print('You already guessed that letter.')
        elif guess in word:
            print('Correct guess!')
            guessed_letters.append(guess)
        else:
            print('Wrong guess!')
            tries -= 1
            guessed_letters.append(guess)

    print('Game over! You ran out of tries.')
    print('The word was:', word)

hangman()
 
