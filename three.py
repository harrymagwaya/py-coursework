# Write a Python program using dictionary to manage the scores of n players in a game. Each player has a name and a score (runs scored). The program should provide tasks:
# Add a player's name and score.
# Update the score of an existing player.
# Find and display the score of a particular player.
# Display a scoreboard showing all players and their scores, along with the total score.
# Exit the program.

players = {}

while True:
    print("1. Adding a player")
    print("2. Updating a player")
    print("3. Find and display score of player")
    print("4. Show score ")

    option = int(input("Enter an option 1...4: "))
    if option == 1:
        name = input("Enter a players name: ")
        score = int(input("Enter a score: "))
        if name in players:
            print("Name exists")
        else:
            players[name] = score
    elif option ==2:
       name = input("Enter a players name: ")
       new_score = int(input("Enter a score: ")) 
       if name in players:
            players[name] = new_score
       else:
           print(name , " doesnt exist")
    elif option == 3:
         name = input("Enter a players name: ")
         if name in players:
             score = players[name]
             print("Score of ", name, "is ", score)
         else:
             print("Nmae doesnt exist")
    elif option == 4:
        total = 0
        for i in players.items():
            name, score = i
            print(name, score)
            total = total + score
        print("total is", total)
    elif option == 5:
        break    
        
           
        
    