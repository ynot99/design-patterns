from milk import Milk
from simple_coffee import SimpleCoffee
from sugar import Sugar
from vanilla import Vanilla


coffee = SimpleCoffee()
print("Description: ", coffee.get_description())
print("Cost: $", coffee.get_cost())

coffee_with_milk_and_sugar = Milk(Sugar(coffee))
print("Description: ", coffee_with_milk_and_sugar.get_description())
print("Cost: $", coffee_with_milk_and_sugar.get_cost())

coffee_with_milk_sugar_and_vanilla = Vanilla(coffee_with_milk_and_sugar)
print("Description: ", coffee_with_milk_sugar_and_vanilla.get_description())
print("Cost: $", coffee_with_milk_sugar_and_vanilla.get_cost())
