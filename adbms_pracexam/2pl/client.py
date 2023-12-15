import socket


def client():
    port = 8000
    host = "127.0.0.1"
    log = ""
    over = 0

    while 1:
        try:
            sock = socket.socket()
            sock.connect((host, port))
            rec_data = sock.recv(1024).decode().lower()
            print("Coordinator : ", rec_data)
            if rec_data == "abort":
                over = 1
                msg = "ok"
                print("trans ends as aborted")
            elif rec_data == "success":
                over = 1
                msg = "ok"
                print("trans complete")
            else:
                msg = input("System status : ").lower()
                log += " " + msg
            sock.send(msg.encode())
            if over == 1:
                break
            sock.close()
        except:
            print(f"Transaction ends log : {log}")
            break


client()


# import socket
# def ClientSoc():
#     host = "127.0.0.1"
#     port = 8000
#     log = ""
#     over = 0
#     while(1):
#         try:
#             s_soc = socket.socket()
#             s_soc.connect((host,port))
#             rec_data = s_soc.recv(1024).decode()
#             print("Coordinator: ", rec_data.upper())
#             if rec_data.upper() == "ABORT":
#                 msg = "OK"
#                 print("TRANSACTION ABORTED!")
#                 over = 1
#             elif rec_data.upper() == "SUCCESS":
#                 msg = "OK"
#                 print("TRANSACTION COMPLETED!")
#                 over = 1
#             else:
#                 msg = input("System Status: ").upper()
#                 log += " "+msg
#             s_soc.send(msg.encode())
#             if over == 1:
#                 break
#             s_soc.close()
#         except:
#             print("END OF TRANSACTION\n final log is: ",log+" "+rec_data.upper())
#             break
# ClientSoc()
