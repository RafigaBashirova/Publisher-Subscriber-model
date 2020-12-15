import zmq

HOST = '127.0.0.1'
PORT = '1234'


sock = zmq.Context().socket(zmq.PUB)
p = 'tcp://' + HOST + ':' + PORT

sock.bind(p)

while True:
    folder = input('Please enter the folder name: ')
    sock.send(folder.encode())
    print('Request sent!')

sock.close()