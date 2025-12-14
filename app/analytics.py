import datetime
def log_event(event_type: str, value: str):
    timestamp = datetime.datetime.now().isoformat()
    print(f"[ANALYTICS] {timestamp} | {event_type} | {value}")

