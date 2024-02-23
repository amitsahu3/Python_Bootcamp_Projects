from twilio.rest import Client

TWILIO_SID = 'AC5dec45cb5a0c6e55f07d37f2280f1a4a'
TWILIO_AUTH_TOKEN = '7b8e8b510589078763536dc097c33f7c'
TWILIO_VIRTUAL_NUMBER = '+14015371051'
TWILIO_VERIFIED_NUMBER = '+919373440165'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
