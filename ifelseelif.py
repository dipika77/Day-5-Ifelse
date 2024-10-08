# if, else and elif in python
#instructions
'''Examine the if statement that prints out "looking around in the kitchen." if room equals "kit".
Write another if statement that prints out "big place!" if area is greater than 15.'''

# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15:
    print("big place!")



#instructions
'''Add an else statement to the second control structure so that "pretty small." 
is printed out if area > 15 evaluates to False.'''

# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else:
    print("pretty small.")



#instructions
'''Add an elif to the second control structure such that "medium size, nice!" is printed 
out if area is greater than 10.'''

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print('medium size, nice!')
else :
    print("pretty small.")