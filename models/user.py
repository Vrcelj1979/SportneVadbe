from google.cloud import ndb

class user(ndb.Model):
    first_name = ndb.TextProperty()
    last_name = ndb.TextProperty()
    email_address = ndb.StringProperty()
    street = ndb.TextProperty()
    city = ndb.TextProperty()
    zip_number = ndb.StringProperty()
    country = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)
