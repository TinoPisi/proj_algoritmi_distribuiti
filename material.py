import uuid
import time


class Material(object):
    def __init__(self, name, name_person):
        self.id = uuid.uuid4()
        self.name = name
        self.arrive_date = time.strftime("%Y%m%d %H.%M")
        self.inserted_by = name_person

    def get_info(self):
        print("{0} - {1} - {2}, Inserted by: {3}.".format(self.name, self.id, self.arrive_date, self.inserted_by))