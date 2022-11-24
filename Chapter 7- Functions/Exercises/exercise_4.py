#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

#medium shirt with the default message, and a shirt of any size with a different message.



def make_shirt(size='L', text='I love Python'):
    print("t-shirt size is ", size)
    print("t-shirt text is ", text)

make_shirt()
make_shirt(size= 'M')
make_shirt(size= 's')
make_shirt(size= 'XL', text= 'this is hard')

