#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

#•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

#•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

#•Print a message to each of the two people still on your list, letting them know they’re still invited.

#•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.



invites = ['Michael Jackson','Ryan Reynolds', 'Brad Pitt', 'Tom Hardy']

print("original invites")
print(invites)


print("I invite you to my dinner party Mr.{}".format(invites[0]))
print("I invite you to my dinner party Mr.{}".format(invites[1]))
print("I invite you to my dinner party Mr.{}".format(invites[2]))
print("I invite you to my dinner party Mr.{}".format(invites[3]))

invites[1] = "Ryan Gosling"
invites[3] = "Tom Hiddleston"

print("new invites")
print(invites)

print("I invite you to my dinner party Mr.{}".format(invites[0]))
print("I invite you to my dinner party Mr.{}".format(invites[1]))
print("I invite you to my dinner party Mr.{}".format(invites[2]))
print("I invite you to my dinner party Mr.{}".format(invites[3]))


remove_value = invites.pop(3)