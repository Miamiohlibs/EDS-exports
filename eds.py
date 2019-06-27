from ftplib import FTP


ftp = FTP('host')
ftp.login(user='user', passwd='pass')
ftp.cwd('/full')
def upload():
    filename = 'MU EDS A.out'
    try:
        ftp.storbinary('STOR '+filename, open(filename, 'rb'), 1024)
    filename = 'MU EDS B.out'
    try:
        ftp.storbinary('STOR '+filename, open(filename, 'rb'), 1024)
    filename = 'MU EDS C.out'
    try:
        ftp.storbinary('STOR '+filename, open(filename, 'rb'), 1024)
