from datetime import datetime
from dateutil.tz import gettz
from math import ceil
from uuid import uuid4

from .age import age, get_dob, formatted_age, get_age_in_days, AgeValueError  # noqa
from .date import get_utcnow, to_arrow_utc, to_utc  # noqa
from .disable_signals import DisableSignals  # noqa
from .get_static_file import get_static_file  # noqa
from .show_urls import show_urls, show_url_names  # noqa
from .text import (  # noqa
    safe_allowed_chars,  # noqa
    get_safe_random_string,  # noqa
    convert_php_dateformat,  # noqa
    convert_from_camel,  # noqa
    formatted_datetime,  # noqa
)  # noqa


def get_uuid():
    return uuid4().hex


def round_up(value, digits):
    ceil(value * (10 ** digits)) / (10 ** digits)


def get_datetime_from_env(
    year, month, day, hour, minute, second, time_zone, closing_date=None
):
    if closing_date:
        hour = hour or 23
        minute = minute or 59
        second = second or 59
    else:
        hour = hour or 0
        minute = minute or 0
        second = second or 0
    return datetime(
        int(year),
        int(month),
        int(day),
        int(hour),
        int(minute),
        int(second),
        0,
        gettz(time_zone),
    )
