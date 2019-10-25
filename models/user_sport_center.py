from google.cloud import ndb

class user_sport_center(ndb.Model):
    user_id = ndb.IntegerProperty()
    sport_center_id = ndb.IntegerProperty()
    admin = ndb.BooleanProperty(auto_now=True, default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)