import time

employees = ["srini", "joseph", "vamsi", "bharath", "keerthi", "bhargav"]
print (employees)

time.sleep(2)

employees.pop()
print (employees)

time.sleep(2)

employees.extend(["unknown"])
print (employees)
