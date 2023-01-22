dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
dict2 = {}
for i in dict:
    if dict.get(i) >= 3:
        dict2[i] = dict.get(i)
print(dict2)