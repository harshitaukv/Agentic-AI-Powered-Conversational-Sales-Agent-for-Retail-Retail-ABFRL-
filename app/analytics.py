analytics_data = {
    "recommendations": 0,
    "payments": 0,
    "returns": 0,
    "support_requests": 0
}

def log_event(event: str):
    if event in analytics_data:
        analytics_data[event] += 1

def get_analytics():
    return analytics_data
