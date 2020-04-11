import datetime

from peewee import SqliteDatabase, Model, IntegerField, DoubleField, DateTimeField

db = SqliteDatabase('golden-eye.db')


class BaseModel(Model):
    class Meta:
        database = db


class XRate(BaseModel):
    """Курсы валют"""
    from_currency = IntegerField()
    to_currency = IntegerField()
    rate = DoubleField()
    update = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = "xrates"
        indexes = (
            (('from_currency', 'to_currency'), True),
        )
