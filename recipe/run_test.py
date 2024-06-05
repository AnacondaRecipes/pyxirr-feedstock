# Code snippet from README and using as a smoke test.
from datetime import date
from pyxirr import xirr

dates = [date(2020, 1, 1), date(2021, 1, 1), date(2022, 1, 1)]
amounts = [-1000, 750, 500]

# feed columnar data
xirr(dates, amounts)
# feed iterators
xirr(iter(dates), (x / 2 for x in amounts))
# feed an iterable of tuples
xirr(zip(dates, amounts))
# feed a dictionary
xirr(dict(zip(dates, amounts)))
# dates as strings
xirr(['2020-01-01', '2021-01-01'], [-1000, 1200])
