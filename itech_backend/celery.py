import pandas as pd
import datetime
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itech_backend.settings')
app = Celery('itech_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
import datetime
with open('date.txt','w') as f:
    f.write(str(datetime.datetime.now()))

def first_day_of_next_month(dt):
    """Get the first day of the next month. Preserves the timezone.

    Args:
        dt (datetime.datetime): The current datetime

    Returns:
        datetime.datetime: The first day of the next month at 00:00:00.
    """
    if dt.month == 12:
        return datetime.datetime(year=dt.year + 1,
                                 month=1,
                                 day=1,
                                 tzinfo=dt.tzinfo)
    else:
        return datetime.datetime(year=dt.year,
                                 month=dt.month + 1,
                                 day=1,
                                 tzinfo=dt.tzinfo)


def generate_invoices():
    data = pd.read_csv('itech_backend/data.csv')
    next_execution_date = data['NEXT_MONTH'][0]
    if datetime.datetime.now() == next_execution_date:
        pass
    print(data)
