#Задание "Easy"

#Задание - 1
def Player(Name, age, city = "Moscow"):
	print(Name, age, "лет" ,"г.", city)

#Задание - 2
def my_max(One, Two, Three):
	Answer = max(One, Two, Three)
	print("Максимальное число: ", Answer)

#Задание - 3 
def max_len(*args):
	answer_max = max(args, key=len)
	print("Самая длиная строка: ", answer_max)

	
#Задание - 1
Player(input("Ваше имя: "),input("Ваш возраст: "),input("Ваш город: "))

#Задание - 2
my_max(input("Введите первое число: "),input("Введите второе число: "),input("Введите третье число: "))

#Задание - 3
max_len(input("1 строка: "), input("2 строка: "), input("3 строка: "))

