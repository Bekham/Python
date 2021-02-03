c = int(input("Введите вермя в секундах:"))
hour = c//3600
min = c//60 - hour*60
sec = c - min*60 - hour*3600
print (f"Текущще время: {hour}:{min}:{sec}")