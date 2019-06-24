from collections import deque
from datetime import datetime
channels={"main":deque(maxlen=100)}
class message:
    def __init__(self,name,date_time,msg):
        self.name=name
        self.date_time=date_time
        self.msg=msg

def post_msg(msg,channel):
    channels[channel].append(msg)

def make_json(channel_msgs,channel):
    json_form=dict()
    json_form[channel]=list()
    for all in channel_msgs:
        new=dict()
        new["name"]=all.name
        new["date_time"]=all.date_time
        new["msg"]=all.msg
        json_form[channel].append(new)
    return json_form

first=message("rajat",datetime.now(),"Hello")
post_msg(first,"main")
print(make_json(channels["main"],"main"))
