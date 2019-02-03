from collections import deque

class message:
    def __init__(self,name,date_time,msg):
        self.name=name
        self.date_time=date_time
        self.msg=msg
    def display(self):
        print(self.name)


d=deque(maxlen=5)
for i in range(5):
    dumm=message("rajat",i,"hello"+str(i))
    d.append(dumm)
print("Old:")
for item in d:
    print(item.name)
    print(item.msg)
    print(item.date_time)

chumm=message("vish",100,"bye")
d.append(chumm)
print("new:")
for item in d:
    print(item.name)
    print(item.msg)
    print(item.date_time)
