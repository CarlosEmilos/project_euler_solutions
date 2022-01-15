with open("p022_names.csv") as f:
    data = f.read().lower()
    data = data.replace('"', '')
    data = data.split(",")
    data = list(data)
    data = sorted(data)

name_scores = []
letter_scores = {}
#print(data)
#should be done with list comprehension i think
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for index, i in enumerate(alphabet):
    letter_scores.update({i: index+1})

sorted_data = {}

for index, i in enumerate(data):
    sorted_data.update({i:index+1})

for i in sorted_data.keys():
    sum = 0
    for j in i:
        sum += letter_scores[j]
    name_scores.append(sum * sorted_data[i])

newsum = 0
for i in name_scores:
    newsum += i

print(newsum)
