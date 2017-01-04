# Created by Bryan R Martinez on 1/4/2017
from ftplib import FTP
import sys


def session_loop(ftp):
    print(ftp.getwelcome())
    print("Enter '--exit' to quit")
    ftp.quit()


def main(argv):
    if len(argv) == 1 or len(argv) == 3:
        print("Error: Invalid number of args entered.")
        exit(1)
    elif len(argv) == 2:
        try:
            ftp = FTP(argv[1])
            session_loop(ftp)
        except TimeoutError:
            print("Error: Connection timed out.")
            exit(1)
    elif len(argv) == 4:
        try:
            ftp = FTP(argv[1], argv[2], argv[3])
            session_loop(ftp)
        except TimeoutError:
            print("Error: Connection timed out.")
            exit(1)
    else:
        print("Error: Invalid number of args.")
        exit(1)


if __name__ == "__main__":
    main(sys.argv)
