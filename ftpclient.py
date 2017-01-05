# Created by Bryan R Martinez on 1/4/2017
import ftplib
import sys


def session_loop(ftp):
    print(str(ftp.getwelcome()).split(None, 1)[1])
    try:
        ftp.dir()
        print("Directory completely listed.")
    except ftplib.all_errors as e:
        print("Error: "+str(e).split(None, 1)[1])
        exit(1)
    while True:
        text = input()
        if text.lower() == "dir":
            ftp.dir()
            print("Directory completely listed.")
        elif text.lower().startswith("cd"):
            try:
                r = ftp.cwd(text.split()[1])
                print(str(r).split(None, 1)[1])
                ftp.dir()
                print("Directory completely listed.")
            except ftplib.all_errors as e:
                print("Error: "+str(e).split(None, 1)[1])
            except IndexError:
                print("Error: Directory name not specified.")
        elif text.lower().startswith("dl"):
            try:
                name = text.split()[1]
                r = ftp.retrbinary("RETR "+name, open(name, "wb").write)
                print(str(r).split(None, 1)[1])
            except ftplib.all_errors as e:
                print("Error: "+str(e).split(None, 1)[1])
            except IndexError:
                print("Error: File name not specified.")
            except IOError:
                print("Error: Unable to write to file.")
        elif text == "exit" or text == "quit":
            break
        else:
            print("Error: Command not recognized.")
    ftp.quit()


def main(argv):
    if len(argv) == 1 or len(argv) == 3:
        print("Error: Invalid number of args entered.")
        exit(1)
    elif len(argv) == 2:
        try:
            ftp = ftplib.FTP(argv[1])
            session_loop(ftp)
        except ftplib.all_errors as e:
            print(str(e).split(None, 1)[1])
            exit(1)
    elif len(argv) == 4:
        try:
            ftp = ftplib.FTP(argv[1], argv[2], argv[3])
            session_loop(ftp)
        except ftplib.all_errors as e:
            print(str(e).split(None, 1)[1])
            exit(1)
    else:
        print("Error: Invalid number of args.")
        exit(1)


if __name__ == "__main__":
    main(sys.argv)
