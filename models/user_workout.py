from google.cloud import ndb

class user_workout(ndb.Model):
    user_id = ndb.IntegerProperty()
    workout_id = ndb.IntegerProperty()
    price_paid = ndb.IntegerProperty()
    company_id = ndb.IntegerProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)