import random
import time

word_list = ['python', 'hangman', 'programming', 'developer', 'algorithm', 'computer', 'puzzle', "aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "baboon", "badger",
            "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois", "cheetah", "chicken",
             "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach", "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur", "dog", "dogfish", "dolphin", "donkey",
             "dormouse", "dotterel", "dove", "dragonfly", "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant",  "elk", "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly",
             "fox", "frog", "gaur", "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose", "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", 
             "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human", "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher",
             "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark", "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird", "magpie", "mallard", "manatee", "mandrill", "mantis",
             "marten", "meerkat", "mink", "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt", "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter", "owl", "ox", 
             "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin", "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail", "quelea", "quetzal", "rabbit", 
             "raccoon", "rail", "ram", "rat", "raven", "red-deer", "red-panda", "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sand-dollar", "sandpiper", "sardine", "scorpion", "seahorse", "seal", "shark", 
             "sheep", "shrew", "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid", "squirrel", "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir", "tarsier", "termite", "tiger", "toad",
             "trout", "turkey", "turtle", "viper", "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodcock", "woodpecker", "worm", "wren", "yak", "zebra"]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def give_clue(word, guessed_letters):
    unguessed_letters = [letter for letter in word if letter not in guessed_letters]
    clue = random.choice(unguessed_letters)
    return clue

def hangman():
    print("Welcome to Hangman!")
    
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 5 
    guessed_word = display_word(word, guessed_letters)
    clue_given = False  
    
    print(f"Word to guess: {guessed_word}")
    
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()
      
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Incorrect! '{guess}' is not in the word.")
            print(f"You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses remaining.")
        
        guessed_word = display_word(word, guessed_letters)
        print(f"Word to guess: {guessed_word}")
        
        if incorrect_guesses == 3 and not clue_given:
            clue_request = input("Would you like a clue? (yes/no): ").lower()
            if clue_request == 'yes':
                clue = give_clue(word, guessed_letters)
                print(f"Here's your clue: One of the letters is '{clue}'.")
                clue_given = True
        
        if guessed_word == word:
            print("Congratulations, you won!")
            for i in range(3):
                print("You guessed the word!", end="")
                time.sleep(0.5)
                print(".", end="")
                time.sleep(0.5)
                print(".", end="")
                time.sleep(0.5)
                print(".", end="")
                time.sleep(0.5)
                print("\n")
            break
    else:
        print(f"You've been hanged! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
