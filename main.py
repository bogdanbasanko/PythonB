#import snastik as avgGrade
#opilane = {
#    "nimi": "Thomas",
#    "vanus": 18,
#    "klass": "12A"
#}
#print(opilane["nimi"])
#print(opilane.get("vanus"))

#opilane["adress"] = "Tallinn"
#opilane.pop("nimi")
#del opilane["klass"]

#print(opilane.values())
#print(opilane.keys())

#for elem in opilane.keys():
  #  print(elem)
   
#for key, value in opilane.items():
  #  print("see on võtti", key, "see on väärtus", value)

#grades = {
  #  "Mari": [4,5,3,4]
   # "Jaan": [2,2,3,2]
#}
#avgGrade.arvutaKeskmineHinne(grades)
#}
#result = avgGrade.arvutaKeskmineHinne(grades)
#print(result)


from snastik import letter_frequency

word = input("Введите слово: ")
result = letter_frequency(word)
print("Частота букв в слове:", result)
