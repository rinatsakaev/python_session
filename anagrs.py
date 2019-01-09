import inspect
def classmethod2(f):
    def inner(*args, **kwargs):
        _cls = None
        if inspect.isfunction(f):
            cls = getattr(inspect.getmodule(f),
                          f.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0])
            if isinstance(cls, type):
                _cls = cls
        return f(_cls, *args, **kwargs)
    return inner

class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod2
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')
