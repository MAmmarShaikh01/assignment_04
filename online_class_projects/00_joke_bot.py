# Constants
PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Ammar GPT - Ammmar is heading out to the grocery store. A programmer tells him: get a liter of milk, and if they have eggs, get 12. Ammar returns with 13 liters of milk. The programmer asks why and Ammar replies: 'because they had eggs'"
SORRY: str = "Sorry I only tell jokes."

def main():
    
    user_input = input(PROMPT)
    
    if user_input == "Joke" or "joke" :
        print(JOKE)
    else:
        print(SORRY)
if __name__ == '__main__':
    main()
