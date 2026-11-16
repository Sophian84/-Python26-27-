from MyFunctions import *
#turtle.bgpic("M_Maze1.gif")
bob.speed(0)
#rainbow(0,0) 
# Starts at 2, stops before 10, jumps by 2 (Prints: 2, 4, 6, 8)
for i in range(2, 10, 2):
    print(i)

for num in range (20):
    rainbow(num*30-200,num*30-200)
    
for num in range (20):
    polygon(3,200,   "turquoise")
    jump(num*-30,num-30)
