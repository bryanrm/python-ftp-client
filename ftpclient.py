# Created by Bryan R Martinez on 1/4/2017
from ftplib import FTP
import sys

ftp = None


def session_loop():
    print(ftp.getwelcome())
    print(ftp.dir())
    ftp.quit()


def main(argv):
    if len(argv) == 1 or len(argv) == 3:
        print("Error: Invalid number of args entered.")
        exit(1)
    elif len(argv) == 2:
        try:
            global ftp
            ftp = FTP(argv[1])
            session_loop()
        except TimeoutError:
            print("Error: Connection timed out.")
            exit(1)


if __name__ == "__main__":
    main(sys.argv)
