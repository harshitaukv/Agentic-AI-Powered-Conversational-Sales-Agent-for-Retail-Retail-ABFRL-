from app.agents.returns import handle_return

def post_purchase():
    return (
        "🚚 Order Delivered\n"
        "Options:\n"
        "1. Track Order\n"
        "2. Request Return\n\n"
        f"{handle_return()}"
    )
