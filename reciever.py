import socket
import time

from ucl.common import byte_print, decode_version, decode_sn, getVoltage, pretty_print_obj, lib_version
from ucl.highCmd import highCmd
from ucl.highState import highState
from ucl.lowCmd import lowCmd
from ucl.unitreeConnection import unitreeConnection, HIGH_WIFI_DEFAULTS, HIGH_WIRED_DEFAULTS
from ucl.enums import MotorModeHigh, GaitType
from ucl.complex import motorCmd

from spin_dog import spin_right, spin_left, strafe_right, strafe_left, go_forward, go_backward, turn_around, lie_down, stand_up
# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the address and port to receive the data
address = 'localhost'
port = 12345

# Bind the socket to the address and port
sock.bind((address, port))

# Listen for incoming connections
sock.listen(1)

# Accept the connection from the sender script
conn, addr = sock.accept()

while True:
    # Receive the variable
    data = conn.recv(1024).decode()

    if not data:
        break

    # Print the received variable
    # print("Received:", data)
    if data == "D1va, Spin Right":
        print("Poggers")
        spin_right()

    if data == "D1va, Spin Left":
        print("monkaS")
        spin_left()

    if data == "D1va, Strafe Right":
        print("monkaS")
        strafe_right()

    if data == "D1va, Strafe Left":
        print("monkaS")
        strafe_left()

    if data == "D1va, Go Forward":
        print("monkaS")
        go_forward()

    if data == "D1va, Go Backward":
        print("monkaS")
        go_backward()

    if data == "D1va, Turn Around":
        print("monkaS")
        turn_around()

    if data == "D1va, Lay Down":
        print("monkaS")
        lie_down()

    if data == "D1va, Stand Up":
        print("monkaS")
        stand_up()
    
    time.sleep(2)

# Close the connection and socket
conn.close()
sock.close()