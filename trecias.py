l = (['Valdas', 'programuotojas', 2000],
['Adomas', 'direktorius', 3000],
['Remigijus', 'programuotojas', 1400],
['Jogaila', 'vadybininkas', 2000]),

pozijos = []
atlyginimai = []
for el in l:
    pozijos.append(el[1])
    atlyginimai.append(el[2])

programuotoju_sk = pozijos.count('programuotojas')
suma = sum(atlyginimai)

print("Atlyginimų suma yra", suma)
