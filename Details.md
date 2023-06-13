 ![image](https://github.com/YomnaEskander/MiniMax-Algorithm/assets/136505151/a5f4bc8e-e57e-46eb-a73c-9299faa93e3c)


This method printBoard is the one that creates the board. The board is a dictionary.

![image](https://github.com/YomnaEskander/MiniMax-Algorithm/assets/136505151/ba294e05-d993-48b1-ba2b-45c6e88e6f16)

The play is a dictionary.

![image](https://github.com/YomnaEskander/MiniMax-Algorithm/assets/136505151/4cd9c706-c7a4-49a7-aad3-a26475214e73)




  

 

This method “spaceIsFree” uses an if statement to check if current position is free and returns true. Else returns false. 
 ![image](https://github.com/YomnaEskander/MiniMax-Algorithm/assets/136505151/a7894846-768b-48ce-9554-780d65f13322)

And now it's time to insert X or O and choose the position
So we have to check first if the chosen position is free or not 
If yes we have to check if the players draw (then print draw) or win (print win)

 

Now it’s time for the user (X) to choose whither to play with the computer or with another player 
If the user chooses to play with the computer then print "Bots win"
If the user chooses to play with the a player then print "Player1 win"


 

If the position wasn't free then print "can't insert here" and the user have to insert a new value

 

This method is to check if the players draw or not
If the key is free then return false 
If the key isn't free then return true
 
The method “checkForWin” checks if there are consecutively same letters, whether is X or O, in the same row, in keys 1 and 2 and 3, and if they’re all not empty, returns true. Else If, checks 2nd row 3rd row 4th and so on then checks both diagonals and then columns. Else returns false.  
The method “checkWhichMarkWon” checks if there are consecutively same letters, but are of the same mark X or O, in the same row, in keys 1,2, 3 and if they’re all not empty, returns true. Else If, checks 2nd row 3rd row 4th and so on then checks both diagonals and then columns. Else returns false.






 
This two methods give the move to the players 1 or 2 to insert the position of their letter 
 
This method is that the best move the computer can move with his best score to make him win quickly
 
This method checks if computer won or the player did won or if there is a draw.
If any condition of those conditions is done it will stop and if not it will check the maximizing method if its maximizing it will be computer’s turn then it will call MiniMax method to let the player play . And the score is updated every turn.
 
Now we call the method to print the board empty 
Then ask the user to choose player 1 vs player 2 or player 1 vs computer
  
This method :
If the user’s choice is one .The game will be between P1 and P2 till one of them beat the other.
If the user’s choice is two .The game will be between P1 and the bot till one of them beat the other.
If the user’s choice is neither one nor two it will print ”sorry ” then it will call the method again.
 
We call this method to ask the user which game mode to play.
 
