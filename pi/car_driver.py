import socket

class car_driver:


    def __init__(self,pwm_ecu_ID):
        self.pwm_ecu_ID = pwm_ecu_ID

    def run(self):
        try:
            server = socket.socket()
            server.bind(('',9001))
            
        except IOError as e:
            print(e)


