import pytz
from dateutil.tz import UTC


def is_event_cancelled(event):
    for p in event.property_items():
        (name, value) = p
        if name == 'STATUS' and value == 'CANCELLED':
            print("The event was cancelled")
            return True
    return False


def get_timezone(calendar):
    # Keep track of the timezones defined in the calendar
    timezones = {}
    for c in calendar.walk('VTIMEZONE'):
        name = str(c['TZID'])
        try:
            timezones[name] = c.to_tz()
        except IndexError:
            # This happens if the VTIMEZONE doesn't
            # contain start/end times for daylight
            # saving time. Get the system pytz
            # value from the name as a fallback.
            timezones[name] = pytz.timezone(name)

    # If there's exactly one timezone in the file,
    # assume it applies globally, otherwise UTC
    if len(timezones) == 1:
        cal_tz = pytz.timezone(list(timezones)[0])
    else:
        cal_tz = UTC
    return cal_tz
