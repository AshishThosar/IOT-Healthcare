from ftplib import FTP

from sshtunnel import SSHTunnelForwarder
from time import sleep

# ssh tunnneling code
server = SSHTunnelForwarder(
    '13.76.2.219',
    ssh_username="adminuser",
    ssh_password="4^zv>!_d$M3B{Z-D",
    remote_bind_address=('127.0.0.1', 1026)
)
server.start()
port = server.local_bind_port
print("Assign port - ",server.local_bind_port)  # show assigned local port



ftp = FTP('')
ftp.connect('127.0.0.1',port)
ftp.login()
ftp.cwd('download') #replace with your directory
#ftp.retrlines('LIST')

def uploadFile():
 filename = '3.jpg' #replace with your file in your home folder
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def downloadFile():
 filename = 'testfile.txt' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

uploadFile()

