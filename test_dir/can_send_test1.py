import can

with can.Bus(channel='can0', interface='socketcan') as bus:
    msg = can.Message(arbitration_id=0x200, data=[0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08], is_extended_id=False)
    
    try:
        bus.send(msg)
        print("CAN send success:", msg)
    except can.CanError:
        print("CAN send fail")
