def is_event_cancelled(event):
    for p in event.property_items():
        (name, value) = p
        if name == 'STATUS' and value == 'CANCELLED':
            print("The event was cancelled")
            return True
    return False
