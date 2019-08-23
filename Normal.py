#Задание "Normal"
# Задание - 1

worker = ["Леонид", "Станислав", "Илья", "Николай", "Сергей"]
worker_bax = [30000, 34000, 25000, 78000, 83000]
salary = dict(zip(worker, worker_bax))

print(salary)

for i in salary:
    salary[i] = round(int(salary[i]) * 0.87)
    if salary[i] > 50000:
        continue
    salary_2 = i.upper() + " - " + str(salary[i])
    print(salary_2)

file = open("salary.txt", 'w')

for key, val in salary.items():
    file.write(f"{key} - {val}\n")    

file_read = open("salary.txt")
for line in file_read:
    list_line = line.split("-")
    print(list_line)

file.close()
file_read = open("salary.txt")
for line in file_read:
    list_line = line.split("-")
    print(list_line)
file.close()    