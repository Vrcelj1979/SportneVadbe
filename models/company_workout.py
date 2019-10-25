from google.cloud import ndb

class company_workout(ndb.Model):
    workout_id = ndb.IntegerProperty()
    company_id = ndb.IntegerProperty()
    contract_number = ndb.IntegerProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)