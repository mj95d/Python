order1 = "Pizza"
order1qut = 1
order1price = 20 


order2 = "cola"
order2qut = 2
order2price = 5


order3 = "water"
order3qut = 2
order3price = 1.5




order1cost = order1qut * order1price
order2cost = order2qut * order2price
order3cost = order3qut * order3price


total = order1cost + order2cost + order3cost 
tax = total * 0.15
total_cost = total + tax 

'''
fainal bill
'''

print("SEHHA & HANAA\n""Restaurant")
print(f"1: {order1} = {order1qut} x {order1price} = {order1cost}SR")
print(f"2: {order2} = {order2qut} x {order2price} = {order2cost}SR")
print(f"3: {order3} = {order3qut} x {order3price} = {order3cost}SR")


print("----------------")
print(f"Total = {total}SR")
print(f"Tax = {tax}SR")
print("--------------")

print(f"Total Cost = {total_cost}SR")


print("Tank you")
