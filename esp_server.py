

# echo-server.py



import socket

HOST = "100.66.175.29"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)



lat_cords= []

long_cords= []



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")
        lats=[]
        longs=[]
        while len(lats)<=20:
            lat = conn.recv(1024)
            long=conn.recv(1024)
            lats.append(lat)
            longs.append(long)

            print(lat,long)
            #if not data:
            #    break
            #other=b'other data'
            #conn.sendall(other)

        lat_sum=0
        long_sum = 0
        for i in lats:
            lat_sum += int(i)

        for j in longs:
            long_sum += int(j)

        lat_avg= lat_sum/len(lats)
        print(lat_avg)

        long_avg= long_sum/len(longs)
        print(long_avg)

        lat_cords.append(lat_avg)

        long_cords.append(long_avg)




