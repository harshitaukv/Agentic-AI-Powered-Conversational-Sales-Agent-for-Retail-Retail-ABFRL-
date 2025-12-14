class ReturnFSM:
    def __init__(self):
        self.state = "ORDER_DELIVERED"

    def next(self, action):
        transitions = {
            "ORDER_DELIVERED": ["REQUEST_RETURN"],
            "REQUEST_RETURN": ["PICKUP_SCHEDULED"],
            "PICKUP_SCHEDULED": ["REFUND_INITIATED"],
            "REFUND_INITIATED": ["REFUND_COMPLETED"]
        }

        if action in transitions.get(self.state, []):
            self.state = action
        return self.state

