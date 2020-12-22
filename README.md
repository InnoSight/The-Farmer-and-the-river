# Farmer-and-river
This project presents graph search for the widely known game of Farmer, Fox, Goose and Beans. 
The Farmer has to move all participants across the river taking into account that 
the Fox can eat the Goose and the Goose can eat the Beans being unsupervised. The boat holds
only two passengers and can't sail without the Farmer.

The central idea of this solution is to find a right path in the graph where a vertex - 
is an arrangement of all characters - each one on it's own position. For example, an arrangement 
where Fox and Beans are on the left shore, Farmer is on the boat and Goose is on the right shore - 
is one of all vertexes of the graph. 

Example1:
Left shore: Fox, Beans
Boat: Farmer
Right shore: Goose

Obviously we have 81 arrangements in total. (It's the number of ways we could place 4 characters
on 3 positions: 3^4 = 81).

All these arrangements are connected to each other by edges. Each edge - is one movement of
the Farmer. For example, arrangement where Fox and Beans are on the left shore and Goose and Farmer
are on the right - is an arrangement that connected with our first example by one move. Of course, 
Farmer can move alone or take one character with him on the boat. 

Example2:
Left shore: Fox, Beans
Boat:
Right shore: Goose, Farmer


It's important to notice that not all of the arrangements meet conditions described in rules 
of the game. So, in graph we have desirable and undesirable arrangements. 

Example3:
Left shore: Fox, Goose
Boat: Beans
Right shore: Farmer

In this Example3 the Fox can eat the Goose being unsupervised, and Beans are on the boat without 
the Farmer.

Now closer to algorithm.
I used a class Arrangement which corresponds to arrangement (vertex of graph). There's a class
variable "desirable" which shows if the arrangement is desirable or not. Also was created 
class Location suits to possible positions: left shore, boat, right shore. Location 
class has a variable of class List - the list of characters on it.

Example4:
Left_shore.creatures_lst = ['Fox', 'Goose']

We don't have to see all the graph during the game. For each iteration (as we go through the 
graph) we need to know our current arrangement and find all the arrangements that are connected
to this current one by one move. So the whole algorithm could be described by these steps:

 - If the current arrangement is the one where all characters are on the right shore, then
   we're finished.
 - Finding all the arrangements connected to the current arrangement by a single move.
 - Of those arrangements we eliminate a previous arrangement (if there's one).
 - Further we eliminate all the connected arrangements that are undesirable.
 - Picking one of the remaining connected arrangements. (If there aren't any remaining, we give up).
 - Making it the new current arrangement; the current arrangement is now the previous arrangement.
 
However the algorithm doesn't necessarily find the solution. The reason of that is that the number
of desirable arrangements on each step could be more than one. Moreover, it's known that there's
a cycle of desirable arrangements. So, the algorithm could go that way and get stuck in the cycle,
following it around forever without finishing. The are a number of algorithms that find paths in
a graph with cycle, but they are not covered in this project.

In this implementation I used class Arrangement, and each arrangement or vertex of the graph 
was an object of this class. I used method deepcopy() of the copy library to create an object of 
new arrangement which is connected with current arrangement by one move. Without using deepcopy()
all references would lead to the same object that will change all the time.

All graphics was made via turtle module designed to implement simple graphics.
