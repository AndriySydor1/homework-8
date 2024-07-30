import mongoengine as me

class Contact(me.Document):
    fullname = me.StringField(required=True)
    email = me.EmailField(required=True)
    phone = me.StringField()
    sent = me.BooleanField(default=False)
    preferred_contact_method = me.StringField(choices=['email', 'sms'], default='email')
    
    