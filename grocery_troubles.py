#Obligatory
print("Hello World!")

#Variables
munny = 50

print("$" + str(munny))

#Printing stuff
print("I like...")
print("New lines!")

print("I", end="")
print(" do not.")

print("And I'm weird ", end="0w0\n")

#Printing Variables
print("There has to be a better way to print my munny... ", end="")
print("$" + str(munny))

print("There is! ${}".format(munny))

#Lists

shopping_list = ["eggs", "milk", "human souls"]

print("I have to buy {}, {} and {} at the store today.".format(shopping_list[0], shopping_list[1], shopping_list[2]))
print("I wonder if {}, {} or {} are on sale today.".format(*shopping_list))
print("Why am I saying {1}, {0} and {2} so much?".format(*shopping_list))

print("Wait, I also need to buy oranges...")
shopping_list.append("oranges")

print("That's better, {}, {}, {} and {}.".format(*shopping_list))

#Dictionaries

prices = {"eggs" : 199.99, "milk" : 2.99, "oranges" : 4.99, "human souls" : 0.99}

print("One car ride later...")
print("I have ${} to spend...".format(munny))
print("How much are eggs... ${}?!?!?!?!".format(prices["eggs"]))
print("I guess I can just eat toast for breakfast.")
print("At least everything else is reasonably priced..., milk is ${}, oranges are {} and human souls are only {}.".format(prices["milk"], prices["oranges"], prices["human souls"]))

#Iteration

print("So if I skip the eggs, ", end="")
shopping_list.remove("eggs")
print("my total is...")

total = 0

for item in shopping_list:
  total += prices[item]
  
print("${} before taxes...".format(total))

tax = 1.13
tax_total = tax * total

print("And ${:.2f} after tax".format(tax_total))
