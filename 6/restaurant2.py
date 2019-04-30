from meal import Meal


class Restaurant(Meal):

	def __init__(self, res_name):
		self.res_name = res_name
		self.meal_list = []

	def add_meal(self, meal):
		self.meal_list.append(meal)

	def order_menu_cost(self):
		total = float(0.0)
		for m in self.meal_list:
			total += m.cost
		print("If I ordered everything in the menu it would cost ${}".format(total))


if __name__ == '__main__':
	restaurant = Restaurant('The Mona Lisa Chip Shop')

	meal1 = Meal('Fish and chips', 8.5)
	meal2 = Meal('Pie and chips', 5.35)

	restaurant.add_meal(meal1)
	restaurant.add_meal(meal2)

	restaurant.order_menu_cost()

#or
"""
restaurant = Restaurant('The Mona Lisa Chip Shop')

meal1 = Meal('Fish and chips', 8.5)
meal2 = Meal('Pie and chips', 5.35)

restaurant.add_meal(meal1)
restaurant.add_meal(meal2)

restaurant.order_menu_cost()

"""
