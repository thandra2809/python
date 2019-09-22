import time

employees = ["srini", "joseph", "vamsi", "bharath", "keerthi", "bhargav"]
print (employees)

count = 0

while count < len(employees):
    print(employees[count])
    time.sleep(2)
    count = count + 1
