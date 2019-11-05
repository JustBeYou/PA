import datetime

data = input()
data = datetime.datetime.strptime(data, "%d %m %Y")
print (data.strftime("%A"))
