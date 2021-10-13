li = ['risk', 'clue', 'catan']
print("I like the following games: risk, clue, and catan.")
game = input('What is your favorite game? ')
li.append(game)
while(game != "no"):
    game = input('What is your favorite game (type no to stop): ')
    li.append(game)
for item in li:
    print(item)