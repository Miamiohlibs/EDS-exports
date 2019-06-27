from ftplib import FTP

ftp = FTP('')
ftp.login(user='', passwd='')

def upload():
    ftp.cwd('/full')
    filename = 'MU EDS A.out'
    try:
        ftp.storbinary('STOR '+filename, open(filename, 'rb'), 1024)
    ftp.cwd('../update')
    filename = 'MU EDS B.out'
    try:
        ftp.storbinary('STOR '+filename, open(filename, 'rb'), 1024)
    filename = 'MU EDS C.out'
    try:
        ftp.storbinary('STOR '+filename, open(filename, 'rb'), 1024)
