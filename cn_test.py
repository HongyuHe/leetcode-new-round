import socket
import threading
import select
import time

def getData(sock):
    data = sock.recv(4096).decode("utf-8")
    if not data:
        print("Socket is closed")
        exit()

    if data == "BAD-RQST-HDRi\n":
        raise "bad request header"
    elif data == "BAD-RQST-BODY\n":
        raise "bad request body"

    return data

def getUsers(data):
    users = []
    expectedMsg = "WHO-OK"
    if data[0:6] == expectedMsg:
        users = data[7:-1].split(",")
        return users
    else:
        return None

def listenForMessages(sock):
    t = threading.currentThread()
    while getattr(t, "run", True):
        listen = getattr(t, "listen", True)
        if listen:
            try:
                data = getData(sock)
                if data[0:8] == "DELIVERY":
                    fromUser = data[9:].split(" ")[0]
                    print("[%s]\t\t %s" % (fromUser, data[10 + len(fromUser):-1]))
            except socket.timeout:
                pass
            except Exception as e:
                print("An exception occurred")
                print(e)

def lockThread(t, sock):
        t.listen = False
        time.sleep(socketTimeout)
        sock.settimeout(None)

def unlockThread(t, sock):
        sock.settimeout(socketTimeout)
        t.listen = True
        time.sleep(socketTimeout)

socketTimeout = 0.1
sock = None
host = ("18.195.107.195", 5378)

# Log in
user = ""
while user == "":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(host)

    print("Choose a username")
    user = input()
    helloMsg = "HELLO-FROM %s\n" % user
    sock.sendall(helloMsg.encode("utf-8"))
    try:
        data = getData(sock)
            
        expectedMsg = "HELLO %s\n" % user
        if data == expectedMsg:
            print("Log in successful!")
        elif data == "IN-USE\n":
            print("Username already taken\n")
            user = ""
            sock.close()
        elif data == "BUSY\n":
            print("Maximum number of users reached on the server, try again later")
            exit()
        else:
            print("Unexpected response %s" % data)
    except Exception as e:
        print(e)

sock.settimeout(socketTimeout)

t = threading.Thread(target=listenForMessages, args=(sock,))
t.start()

print("\n")

quit = False
while quit == False:
    try:
        command = input("[YOU]\t\t")

        if command == "!quit":
            # Handle !quit command
            quit = True
        elif command == "!who":
            # Handle !who command
            whoMsg = "WHO\n"
            
            lockThread(t, sock)

            sock.sendall(whoMsg.encode("utf-8"))
            data = getData(sock)
            
            unlockThread(t, sock)

            users = getUsers(data)
            if users == None:
                print("Unexpected response %s" % data)
                exit()
            print("Online users:", end="\n\t")
            print("\n\t".join(users))
        elif command[0] == "@":
            # Handle sending message
            userDst = command[1:].split(" ")[0]
            message = command[2 + len(userDst):]

            sendMsg = "SEND %s %s\n" % (userDst, message)

            lockThread(t, sock)

            sock.sendall(sendMsg.encode("utf-8"))
            data = getData(sock)

            unlockThread(t, sock)

            if data != "SEND-OK\n":
                if data == "UNKNOWN\n":
                    print("User '%s' offline" % userDst)
                else:
                    print("Unexpected response %s" % data)
                    exit()

    except Exception as e:
        print(e)

t.run = False
t.join()

sock.close()
