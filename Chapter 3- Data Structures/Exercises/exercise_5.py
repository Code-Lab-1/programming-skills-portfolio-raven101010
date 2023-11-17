
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
