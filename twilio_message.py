from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "AC7795b373d9a799dfe05d9acc8ccc20dd"   # "your account sid"
# Your Auth Token from twilio.com/console
auth_token  = "f64a55d8e68d04fcf3f3223eda3964de"
client = Client(account_sid, auth_token)
message = client.messages.create(
# 这里中国的号码前面需要加86
to="+8613811567456",
from_="+15156048281",
body="这里一个python学习发出来的短信!")
print(message.sid)