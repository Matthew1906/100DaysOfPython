# Import module
import pandas as pd

# Create dataframe and dictionary
nato_df = pd.read_csv("Project/nato_phonetic_alphabet.csv")
nato_dict = {nato_df.at[index,'letter']:nato_df.at[index,'code'] for index,row in nato_df.iterrows()}

# Driver code
running = True
while running:
    print([nato_dict[letter] for letter in input("Enter a word: ").upper()])
    if not input("Type 'y' to play again\n>> ") =='y':
        running = False