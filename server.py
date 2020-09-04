# first of all import the socket library
import socket
import pyautogui
import io

# next create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")


# reserve a port on your computer in our
# case it is 12345 but it can byte anything
port = 20001

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network

s.bind(('', port))
print("socket binded to %s" % port)

# put the socket into listening mode


s.listen(10)
print("socket is listening")

if s is None:
    print('could not open socket')

# a forever loop until we interrupt it or
# an error occurs

pyautogui.FAILSAFE = False

# Any duration less than this is rounded to 0.0 to instantly move the mouse.
pyautogui.MINIMUM_DURATION = 0  # Default: 0.1
# Minimal number of seconds to sleep between mouse moves.
pyautogui.MINIMUM_SLEEP = 0  # Default: 0.05
# The number of seconds to pause after EVERY public function call.
pyautogui.PAUSE = 0  # Default: 0.1

while True:

    # Establish connection with client.
    # print('Got connection from', addr)

    c, addr = s.accept()

    # Receive data
    temp = c.recv(100)
    data = str(temp, 'utf-8').split(",")

    if data[0] == "0":  # Move mouse at (data[1],data[2]) coords
        try:
            pyautogui.moveRel(round(float(data[1])/7, 0), round(float(data[2])/7, 0,))
        except:
            pass
    elif data[0] == "1":
        try:
            pyautogui.click(button=data[1])
        except:
            pass
    elif data[0] == "2":    # press keyboard keys
        try:
            pyautogui.press(data[1])
        except:
            pass
    elif data[0] == "3":
        try:
            pyautogui.typewrite(data[1])
        except:
            pass
    elif data[0] == "4":    # Take and send screenshot
        try:
            im = pyautogui.screenshot()
            im_resize = im.resize((1920, 1080))
            buf = io.BytesIO()
            im_resize.save(buf, format='PNG')
            byte_im = buf.getvalue()
            c.send(byte_im)
        except:
            pass
    elif data[0] == "5":    # Break the loop
        break
    elif data[0] == "6":
        try:
            pyautogui.press(data[1:])
        except:
            pass
    elif data[0] == "7":
        try:
            pyautogui.moveTo(float(data[1]), float(data[2]))
        except:
            pass
    c.detach()
    # Close the connection with the client
c.close()
s.close()

print('Server Stopped', end="\n")


