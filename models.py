from peewee import (SqliteDatabase, Model, IntegerField, DoubleField, DateTimeField,
                    datetime as peewee_datetime, CharField, TextField)
from config import DB_NAME

db = SqliteDatabase(DB_NAME)


class _Model(Model):
    class Meta:
        database = db


class XRate(_Model):
    """Курсы валют"""
    from_currency = IntegerField()
    to_currency = IntegerField()
    rate = DoubleField()
    updated = DateTimeField(default=peewee_datetime.datetime.now)

    class Meta:
        db_table = "xrates"
        indexes = (
            (("from_currency", "to_currency"), True),
        )

    def __str__(self):
        return "XRate(%s=>%s): %s" % (self.from_currency, self.to_currency, self.rate)


class ApiLog(_Model):
    request_url = CharField()
    request_data = TextField(null=True)
    request_method = CharField(max_length=100)
    request_headers = TextField(null=True)
    response_text = TextField(null=True)
    created = DateTimeField(index=True, default=peewee_datetime.datetime.now)
    finished = DateTimeField()
    error = TextField(null=True)

    class Meta:
        db_name = "api_logs"


class ErrorLog(_Model):

    request_data = TextField(null=True)
    request_url = TextField()
    request_method = CharField(max_length=100)
    error = TextField(null=True)
    traceback = TextField(null=True)
    created = DateTimeField(index=True, default=peewee_datetime.datetime.now)

    class Meta:
        db_name = "error_logs"


def init_db():
    for m in (XRate, ApiLog, ErrorLog):
        m.drop_table()
        m.create_table()

    XRate.create(from_currency=840, to_currency=980, rate=1)
    XRate.create(from_currency=840, to_currency=643, rate=1)

    print("db_created!")
