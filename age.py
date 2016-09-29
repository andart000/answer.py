age = int(input('Введите свой возраст в цифрах: '))
if age >= 0:
	if 0 <= age <= 6:
		print("В САД")
	elif 7 <= age <= 16:
		print("ШКОЛОЛО")
	elif 17 <= age <= 22:
		print("УНИВЕР")
	else:
		print("работать")
else:
	print("возраст не может быть отрицательным")