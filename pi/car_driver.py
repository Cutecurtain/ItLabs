import socket

class car_driver:


    def __init__(self,pwm_ecu_ID):
        self.pwm_ecu_ID = pwm_ecu_ID

    def run(self):
        try:
            serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serversocket.bind((socket.gethostname(), 9003))
            serversocket.listen(5)

            while True:
                (clientsocket, address) = serversocket.accept()

            
        except IOError as e:
            print(e)


