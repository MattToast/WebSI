import json
import os
import hashlib
import getpass


def main():
    FileStructureSetUp().set_up_files()


class ScheduleTable:
    # Describes a schedule table
    class Row:
        def __init__(self, block_type: str = "NA", day: str = "NA", place: str = "NA", time: str = "NA"):
            """
            Describes a row in the schedule table
            :param block_type: String, meeting type label 
            :param day: String, name of the day of the week of the meeting
            :param place: String, name of the place of the meeting 
            :param time: String, times avilble (ex. 5:30-6:30) 
            """
            self.__type = block_type
            self.__day = day
            self.__place = place
            self.__time = time

        def to_dict(self) -> dict:
            """
            Converts a row into a dictionary to be converted to json
            :return: dict that represents the contents of the row
            """
            row_dict = {
                "type": self.__type,
                "day": self.__day,
                "place": self.__place,
                "time": self.__time
            }
            return row_dict

    def __init__(self, title: str = ""):
        """
        Makes a schedule tabel
        :param title: String, title of the table
        """
        if title == "":
            title = "Schedule"
        self.__title = title
        self.__rows = []

    def add_row(self, block_type: str, day: str, place: str, time: str):
        """
        Creates a new row in the table
        :param block_type: String, meeting type label 
        :param day: String, name of the day of the week of the meeting
        :param place: String, name of the place of the meeting 
        :param time: String, times avilble (ex. 5:30-6:30) 
        """
        self.__rows.append(self.Row(block_type, day, place, time).to_dict())

    def to_dict(self) -> dict:
        """
        Converts table into a dict to be made into a json
        :return: dictionary representation of the table
        """
        schedule_dict = {
            "title": self.__title,
            "rows": self.__rows
        }
        return schedule_dict


class FileStructureSetUp():
    def __init__(self):
        pass

    def set_up_files(self):
        """Sets up the file structure for the website"""
        self.create_missing_dirs()
        self.set_admin()
        self.design_site()

    def create_missing_dirs(self):
        """Creates any missing dirs"""
        self.attmept_to_make_dir("./static/res/share/")
        self.attmept_to_make_dir("./static/json")

    def attmept_to_make_dir(self, path: str):
        """Check that a dir exists, if it doesn't attempt to create it"""
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except Exception:
                print("Something went wrong creating" + path)

    def set_admin(self):
        """Creates and writes out the admin json"""
        admin_json = {}
        admin_json['path'] = self.set_path()
        (admin_json['username'], admin_json['password']) = self.set_credentials()
        with open('./static/json/admin.json', 'w') as admin:
            json.dump(admin_json, admin, indent=2)

    def set_path(self) -> str:
        """
        Asks the user to confirm that the path provided is where the website isrun from.
        If not they can provide their own path. The path is then returned as a string
        :return: String, path to current working dir
        """
        newPath = os.getcwd()
        print("Your current working directory is:")
        print(newPath + "\n")
        choice = input("Would you like to use this path (y/n): ")
        if choice != 'y' and choice != 'Y' and choice != 'yes':
            newPath = input('Please enter your new path:\n')
        return newPath

    def set_credentials(self):
        """Gets and hashes the credentials"""
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
        """Creates a json that describes the general layout of the website"""
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
