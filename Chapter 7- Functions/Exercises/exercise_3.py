#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 

#should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 

#argum0ents to make a shirt. Call the function a second time using keyword arguments.


def make_shirt(size, text):
    print("t-shirt size is ", size)
    print("t-shirt text is ", text)

make_shirt('M', "The size of the shirt is Medium")

make_shirt(text="The size of the shirt is Medium", size='M')

