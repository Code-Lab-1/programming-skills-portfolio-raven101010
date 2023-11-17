
prompt = "What type of pants?"
prompt += "Enter 'quit' when you are finished: "

while True:
    pants = input(prompt)
    if pants != 'quit':
        print("  I'll get a  " + pants + " pants for you.")
    else:
        break