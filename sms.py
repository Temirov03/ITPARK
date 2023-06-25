# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['api.mobizon.kz']
auth_token = os.environ['kz683c9ee4133d6a30fbbfc08d042cd16825227e319b7699e0df68af664f7f966cfc85']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there',
                              from_='+15017122661',
                              to='+15558675310'
                          )

print(message.sid)