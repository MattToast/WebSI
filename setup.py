import json
import os
import hashlib
import getpass


def main():
    FileStructureSetUp().set_up_files()

class ScheduleTable:
    class Row:
        def __init__(self, block_type="NA", day="NA", place="NA", time="NA"):
            self.__type = block_type
            self.__day = day
            self.__place = place
            self.__time = time

        def to_dict(self):
            row_dict = {
                "type": self.__type,
                "day": self.__day,
                "place": self.__place,
                "time": self.__time
            }
            return row_dict

    def __init__(self, title=""):
        if title == "":
            title = "Schedule"
        self.__title = title
        self.__rows = {}

    def add_row(self, block_type, day, place, time):
        self.__rows["r" + str(len(self.__rows.keys()))] = self.Row(block_type, day, place, time).to_dict()

    def to_dict(self):
        schedule_dict = {
            "title": self.__title,
            "rows": self.__rows
        }
        return schedule_dict


class FileStructureSetUp():
    def __init__(self):
        pass

    def set_up_files(self):
        self.create_missing_dirs()
        self.set_admin()
        self.design_site()

    def create_missing_dirs(self):
        self.attmept_to_make_dir("./static/res/share/")
        self.attmept_to_make_dir("./static/json")

    def attmept_to_make_dir(self, path):
        # check that a dir exists, if it doesn't attempt to create it
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except Exception:
                print("Something went wrong creating" + path)

    def set_admin(self):
        admin_json = {}
        admin_json['path'] = self.set_path()
        (admin_json['username'], admin_json['password']) = self.set_credentials()
        with open('./static/json/admin.json', 'w') as admin:
            json.dump(admin_json, admin, indent=2)

    def set_path(self):
        newPath = os.getcwd()
        print("Your current working directory is:")
        print(newPath + "\n")
        choice = input("Would you like to use this path (y/n): ")
        if choice != 'y' and choice != 'Y' and choice != 'yes':
            newPath = input('Please enter your new path:\n')
        return newPath

    def set_credentials(self):
        username = str(hashlib.sha256(
            input('Please enter an admin username: ').encode()).hexdigest())
        password = getpass.getpass('Please enter an admin password: ')

        while len(password) < 8:
            print("Password should be 8 or more characters long")
            password = getpass.getpass('Please enter an admin password: ')

        password = str(hashlib.sha256(password.encode()).hexdigest())
        passeord_re_enter = str(hashlib.sha256(getpass.getpass(
            'Please re-enter the password: ').encode()).hexdigest())

        if password == passeord_re_enter:
            print("Username and password have been updated")
            return (username, password)
        else:
            print("Passwords do not match, changes are being ignored")
            exit()

    def design_site(self):
        design_json = {}
        design_json['title'] = input("Please enter a title for your site: ")
        schedule_table = ScheduleTable(input("Please enter a schedule title: "))
        add_rows = 'y'
        while add_rows == 'y' or add_rows == 'Y' or str(add_rows).lower() == 'yes':
            block_type = input("Enter block type (Usually 'SI Session' or 'Office Hours'): ")
            day = input("Enter day of this block: ")
            place = input("Enter place where the block occurs: ")
            time = input("Enter time when the block occurs (ex, 5:30-6:20): ")
            schedule_table.add_row(block_type, day, place, time)
            add_rows = input('Add another row? (y/n): ')
        design_json['schedule_table'] = schedule_table.to_dict()
        with open('./static/json/design.json', 'w') as design:
            json.dump(design_json, design, indent=2)


if __name__ == "__main__":
    main()
