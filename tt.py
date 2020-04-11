import re


name= input("hello, What is your name? ")
print ("Hello " + name)

print("""
You wake up in the middle of a cave! 
There is a lantern here. 
You can see a tunnel to the north and a door to the south. 
Behind the door, you hear flowing liquid.""")

command = input("What do you want to do? ")
print("You said "+ command)

if re.search('north', command, re.IGNORECASE):
	print ("You walk north through the tunnel. You come to an intersection.")
	print ("There is a tunnel to the North East, a tunnel to the North West and a tunnel to the south.")
	print ("It's very dark here.")
elif re.search('south', command, re.IGNORECASE):
	print ("You open the door and cautiously step inside.")
	print ("It is suprisingly warm in here.")
	print ("There is a door to the North, and a tunnel to the South and a tunnel to the South East")
	print ("Behind the door to the North, there is a bright light.")
	print ("In the tunnel to the South, there is an intense heat.")
	print ("In the tunnel to the South East, there is a weird moaning noise.")

