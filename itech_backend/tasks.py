from celery import shared_task
import datetime
from Accounting.models import Invoice, BillingAccount
from Users.models import User


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


@shared_task
def generate_invoices():
    with open('date.txt') as file:
        lines = file.readlines()
        if str(datetime.datetime.now()) == lines[0]:
            with open('date.txt', 'w') as f:
                f.write(str(first_day_of_next_month(datetime.datetime.now())))
