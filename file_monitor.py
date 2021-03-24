import os.path
import time


csv_file = open("users.txt", "r")
current_time = time.strftime("%d")


class Monitoring:
    def __init__(self):
        self.modyfy = ""

    def checkmodfy(self, file, filename, user):
        self.modyfy = time.ctime(os.path.getmtime(file))
        return "last modified: {} -- {} -- {}, \n".format(self.modyfy, filename, user)
    # created = time.ctime(os.path.getctime(file))
    # print("created: %s" % created)


class Finaloperation:

    def __init__(self, current_time):
        self.current_time = current_time
        self.documents_name = "Dokumenty"
        self.desktop_name = "Pulpit"
        self.desktop = ""
        self.documents = ""
        self.separator = ""
        self.check_one = ""
        self.check_two = ""

    def writingtofile(self):
        for user in csv_file.read().splitlines():
            try:
                self.desktop = "//192.168.1.1/{}/Pulpit".format(user)
                self.documents = "//192.168.1.1/{}/Dokumenty".format(user)
                self.separator = "*" * 20, user, "*" * 20
                self.check_one = data_info.checkmodfy(self.desktop, self.desktop_name, user)
                self.check_two = data_info.checkmodfy(self.documents, self.documents_name, user + "\n")
                if data_info.modyfy[9:10] is str(self.current_time[1]) or\
                        data_info.modyfy[8:10] == str(self.current_time):
                    pass
                else:
                    text_file.write(str(self.separator) + "\n")
                    text_file.write(str(self.check_one))
                    text_file.write(str(self.check_two))

            except Exception as e:
                message = "Użytkownik {} nie posiada odpowiednich katalogów".format(user)
                full_message = e, message
                text_file.write(str(full_message) + "\n\n")


text_file = open("backup_monitor.txt", "w")
data_info = Monitoring()
final = Finaloperation(current_time)
final.writingtofile()
text_file.close()
csv_file.close()
