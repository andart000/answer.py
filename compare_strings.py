input1 = input()
input2 = input()
def compare_strings(string1, string2):
	if string1 == string2:
		print(1)
	elif len(string1) > len(string2):
		print(2)
	elif string1 != string2 and string2 == 'learn':
		print(3)
compare_strings(input1, input2)