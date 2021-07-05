import os 
from twilio.rest import Client  
 
account_sid = "AC7d5317a4303136a24b145c640eef0622"
auth_token = "157b164a48974a4b30d5c4b5fe627b4b"
client = Client(account_sid, auth_token)

call = client.calls.create( twiml='<Response><Say>Ahoy, World!</Say></Response>',
						   to="+330608962192",
						    from_ ="+330671826346"
						    )



print (call.sid)