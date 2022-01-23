import csv
import json

#1 calculates function values
def func_1(x):
  y = x/(x+100)
  #print(y)
  return y

def func_2(x):
    y = 1/x
    #print(y)
    return y

h = 5
while h <= 6:
    func_1(h)
    func_2(h)
    h += 1

#2 calculates the function value
def func_3(x):
    y = 20*(func_1(x) + func_2(x))/x
    #print(y)
    return y

h = 5
while h <= 90:
    func_3(h)
    h += 1

#3 represents the result as a dictionary
dict = {}
h = 5
while h <= 90:
    el_1 = func_1(h)
    el_2 = func_2(h)
    el_3 = func_3(h)
    el = [el_1, el_2, el_3]
    key = h
    h += 1
    dict.setdefault(key, el)
#print(dict)

#4 saves the calculation result to a CSV file
with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        ("x", "f1(X)", "f2(X)", "f3(X)")
    )

h = 5
while h <= 90:
    el_1 = func_1(h)
    el_2 = func_2(h)
    el_3 = func_3(h)
    data = [
        [h, el_1, el_2, el_3]
    ]
    for i in data:
        with open("data.csv", "a", newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(i)
    h += 1

#5 reads the written CSV file and presents the result as a list
with open("data.csv", newline='') as file:
    reader = csv.DictReader(file, delimiter=";")
    l = []
    for row in reader:
        lst = [row["x"], row["f1(X)"], row["f2(X)"], row["f3(X)"]]
        l.append(lst)
print(l)

#6 saves the list to a JSON file
count = 0

with open('data.json', encoding='utf8') as file:
    data = json.load(file)
    for i in l:
        lst = l[count]
        data['function'].append(lst)
        count += 1
    with open('data.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)