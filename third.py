temperature_input = input("Введите температуру (например, 12C или 100F): ")
try:
	value = float(temperature_input[:-1])
	if temperature_input[-1].upper() == "C":
		celsius = float(temperature_input[:-1])
		fahrenheit = celsius * 1.8 + 32
		print(f"{celsius}C = {fahrenheit}F")
	elif temperature_input[-1].upper() == "F":
		fahrenheit = float(temperature_input[:-1])
		celsius = (fahrenheit - 32) / 1.8
		print(f"{fahrenheit}F = {celsius}C")
	else:
		print("Ошибка: ввод должен заканчиваться на 'C' или 'F'.")
except ValueError as e:
	print("Ввод должен начинаться с числа")
	print (e)
