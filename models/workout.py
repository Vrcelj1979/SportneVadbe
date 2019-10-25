from google.cloud import ndb

class workout(ndb.Model):
    title = ndb.StringProperty()
    description = ndb.TextProperty()
    start_date = ndb.DateTimeProperty()
    end_date = ndb.DateTimeProperty()
    sport_center_id = ndb.IntegerProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)