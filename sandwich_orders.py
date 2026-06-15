sandwich_orders = ["Tuna", "BLT", "Grilled Cheese", "Club"]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print("I made your " + sandwich)
    finished_sandwiches.append(sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)