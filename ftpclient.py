# Created by Bryan R Martinez on 1/4/2017
import ftplib, sys, os


# primary loop, runs until exit or quit entered by user
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
        if text.lower().startswith("dir"):
            ftp.dir()
            print("Directory completely listed.")
        elif text.lower().startswith("cd"):
            try:
                r = ftp.cwd(text.split(None, 1)[1])
                print(str(r).split(None, 1)[1])
                ftp.dir()
                print("Directory completely listed.")
            except ftplib.all_errors as e:
                print("Error: "+str(e).split(None, 1)[1])
            except IndexError:
                print("Error: Directory name not specified.")
        elif text.lower().startswith("dl"):
            try:
                name = text.split(None, 1)[1]
                r = ftp.retrbinary("RETR "+name, open(name, "wb").write)
                print(str(r).split(None, 1)[1])
            except ftplib.all_errors as e:
                print("Error: "+str(e).split(None, 1)[1])
            except IndexError:
                print("Error: File name not specified.")
            except IOError:
                print("Error: Unable to write file.")
        elif text.lower().startswith("ul"):
            try:
                path = text.split(None, 1)[1]
                name = os.path.basename(path)
                r = ftp.storbinary("STOR "+name, open(path, "rb"))
                print(str(r).split(None, 1)[1])
            except ftplib.all_errors as e:
                print("Error: " + str(e).split(None, 1)[1])
            except IndexError:
                print("Error: File name not specified.")
            except IOError:
                print("Error: Unable to open file.")
        elif text.lower().startswith("rn"):
            try:
                names = text.split(None, 1)
                names = names[1].split("  ")
                r = ftp.rename(names[0], names[1])
                print(str(r).split(None, 1)[1])
            except ftplib.all_errors as e:
                print("Error: " + str(e).split(None, 1)[1])
            except IndexError:
                print("Error: File names not correctly specified.")
        elif text.lower().startswith("del"):
            try:
                r = ftp.delete(text.split(None, 1)[1])
                print(str(r).split(None, 1)[1])
            except ftplib.all_errors as e:
                print("Error: "+str(e).split(None, 1)[1])
            except IndexError:
                print("Error: File name not specified.")
        elif text == "help":
            print("""
            'exit' or 'quit' - exits program
            'dir' - list directory contents
            'cd [dir_name]' - moves to specified directory (.. returns to previous directory)
            'dl [file_name]' - downloads specified file to default program directory
            'ul [file_name' - uploads specified file to current server directory
            'rn [name]  [new_name]' - renames file on server to new_name (note: double space between names)
            'del [file_name]' - deletes specified file on server
            """)
        elif text == "exit" or text == "quit":
            break
        else:
            print("Error: Command not recognized.")
            print("Enter 'exit' or 'quit' to exit the program or 'help' for help.")
    ftp.quit()


# validates program args
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


# runs script if called directly
if __name__ == "__main__":
    main(sys.argv)
