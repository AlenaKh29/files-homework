cook_book = {}                                               # Задача 1
with open('recipes.txt', 'r', encoding='utf-8') as file:
	for line in file:
		dish_name = line.rstrip()
		quantity_ing = int(file.readline().rstrip())
		ingredients = []
		for i in range(quantity_ing):
			string = file.readline().rstrip()
			product, quantity, measure = string.split(' | ')
			quantity = int(quantity)
			ingredients.append({'ingredient_name': product, 'quantity': quantity, 'measure': measure})
		file.readline()
		cook_book[dish_name] = ingredients

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):           # Задача 2
	list_by_dishes = {}
	for dish in dishes:
		if dish in cook_book:
			ingredients = cook_book[dish]
			for ingredient in ingredients:
				product = ingredient.pop('ingredient_name')
				if product not in list_by_dishes:
					quantity = ingredient.pop('quantity') * person_count
					ingredient['quantity'] = quantity
					list_by_dishes[product] = ingredient
				else:
					list_by_dishes[product]['quantity'] += ingredient['quantity'] * person_count
		else:
			print('Мы такое не готовим')
	print(list_by_dishes)

get_shop_list_by_dishes(['Фахитос', 'Суп', 'Утка по-пекински'], 3)
