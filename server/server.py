import socket

adapter_addr = '18:ce:94:1a:72:b7'

port = 3  # Normal port for rfcomm? (for now 3)
print(adapter_addr + '\t:\t' + str(port) +'\n')

buf_size = 1024

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((adapter_addr, port))
s.listen(1)
try:
    print('Listening for connection...')
    client, address = s.accept()
    print(f'Connected to {address}')

    while True:
        data = client.recv(buf_size)
        if data:
            print(data)
except Exception as e:
    print(f'Something went wrong: {e}')
    client.close()
    s.close()