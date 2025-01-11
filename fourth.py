from random import randint
snum = randint(0, 100)
print("Отгадай число от 0 до 100")
unum = 0
while unum != snum:
	unum = input("Введите число: ")
	try:
		value = int(unum)
		if value < snum:
			print("Мое число больше")
		elif value > snum:
			print("Мое число меньше")
		elif value == snum:
			print(f"Ты угадал! Мое число: {snum}")
			break
	except ValueError as e:
		print("Некорректный ввод. Введите ЧИСЛО от 0 до 100")
		
