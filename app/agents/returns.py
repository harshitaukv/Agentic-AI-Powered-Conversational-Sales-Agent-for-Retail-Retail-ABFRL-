from app.fsm import ReturnFSM

fsm = ReturnFSM()

def handle_return():
    state = fsm.next("REQUEST_RETURN")
    return f"🔄 Return Status Updated → {state}"

