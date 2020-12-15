import zmq, os

HOST = '127.0.0.1'
PORT = '1234'

sock = zmq.Context().socket(zmq.SUB)

p = 'tcp://' + HOST + ':' + PORT # how and where to communicate
sock.connect(p) # connect to the server
sock.setsockopt(zmq.SUBSCRIBE, b'') # all topics


while True:

    folder = sock.recv().decode()
    print(f'Requesting folder {folder}...')

    for file in os.listdir(folder):
        print(f'Folder {folder} has {file}')

    print('---END OF CONTENT---')



sock.close()