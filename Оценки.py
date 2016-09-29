school = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class2' : '4b', 'scores2' : [6, 7, 8, 9, 10]}]
scores_class1 = school[0]
scores_class1 = scores_class1['scores']
scores_class2 = school[1]
scores_class2 = scores_class2['scores2']
def arith_mean(x):
	print(sum(x) / len(x))
arith_mean(scores_class1)
arith_mean(scores_class2)
arith_mean(scores_class1 + scores_class2)