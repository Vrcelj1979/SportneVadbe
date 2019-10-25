from google.cloud import ndb

class sport_center(ndb.Model):
    title = ndb.StringProperty()
    email_address = ndb.StringProperty()
    street = ndb.TextProperty()
    city = ndb.TextProperty()
    zip_number = ndb.StringProperty()
    country = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)