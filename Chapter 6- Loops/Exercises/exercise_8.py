
Pasta_orders = ['Rotini', 'Penne', 'Fettuccine', 'Rigatoni']
finished_Pasta = []

while Pasta_orders:
    current_sandwich = Pasta_orders.pop()
    print("I'm working on your " + current_sandwich + " Pasta.")
    finished_Pasta.append(current_sandwich)

print("\n")
for Pasta_name in finished_Pasta:
    print("I made a " + Pasta_name + " Pasta.")