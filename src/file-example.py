order_file = open("orders.csv", "r")

for order in order_file.readlines():
    print(order)

order_file.close()
