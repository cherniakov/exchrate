import datetime

from peewee import SqliteDatabase, Model, IntegerField, DoubleField, DateTimeField

db = SqliteDatabase('golden-eye.db')


class XRate(Model):
    """Курсы валют"""
    from_currency = IntegerField()
    to_currency = IntegerField()
    rate = DoubleField()
    update = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = "xrates"
        indexes = (
            (('from_currency', 'to_currency'), True),
        )

    def __str__(self):
        return "XRate(%s=>%s): %s" % (self.from_currency, self.to_currency, self.rate)


def init_db():
    db.drop_tables(XRate)
    XRate.create_table()
    XRate.create(from_currency=840, to_currency=980, rote=1)
    print("db_created!")
