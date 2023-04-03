import itertools

dishes = itertools.product(main_courses, desserts, drinks)
prices = itertools.product(price_main_courses, price_desserts, price_drinks)
lst = list(zip(dishes, prices))
result = [f"{meal[0]} {meal[1]} {meal[2]} {sum(price)}" for meal, price in lst if sum(price) <= 30]
print("\n".join(result))
