list1 = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
def find_person(name):
	while list1:
		person = list1.pop()
		if person == name:
			print(name + " тута")
			break
find_person(input("Введите имя:"))
