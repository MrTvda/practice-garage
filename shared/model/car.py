from google.cloud import ndb
from shared.system.base.model import BaseModel
import logging


class Car(BaseModel):
    """The Car model"""

    garage_id = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty(required=True)
    brand = ndb.StringProperty()

    note = ndb.TextProperty(indexed=False)

    @classmethod
    def list(cls, garage_id=None, name=None, brand=None, limit=20):
        """
        example normal query with filter.

        """

        with cls.ndb_context():
            query = Car.query()
            if garage_id:
                query = query.filter(Car.garage_id == garage_id)
            elif name:
                query = query.filter(Car.name == name)
            elif brand:
                query = query.filter(Car.brand == brand)
            if limit:
                return query.fetch(limit)
            return query.fetch()
