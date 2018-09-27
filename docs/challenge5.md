# Challenge 5

You have a basketball hoop and someone says that you can play one or two games.

* Game 1: You get one shot to make the hoop.
* Game 2: You get three shots and you have to make two out of three.

If p is the probability of making a particular shot, for which values of p should you pick one game or the other?

### Function prototype:
    def pick_bball_game(p)
 
p (float): probability of making a shot, range 0 to 1
 
### Return values
game (int): the game number with the higher chance of winning 
 
### Example
##### Sample Input
    0.9
 
##### Sample Output
    1
 
### Explanation
With probability p = 0.9, you have a better chance of winning by playing Game 1.
