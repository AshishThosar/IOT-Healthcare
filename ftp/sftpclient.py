import pysftp
import sys

# Defines the name of the file for download / upload
remote_file = "3.jpg"#sys.argv[1]

srv = pysftp.Connection(host="13.76.2.219", username="adminuser",
password="4^zv>!_d$M3B{Z-D")

# Download the file from the remote server
#srv.get(remote_file)

# To upload the file, simple replace get with put. 
srv.put(remote_file)

# Closes the connection
srv.close()
