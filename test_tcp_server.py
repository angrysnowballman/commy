from django.test import TestCase
import Communizm.management.commands.communizm as comm
import time
import os

import threading


class TestCommunizm(TestCase):

    @staticmethod
    def send_coords():
        os.system("python coordinates_sender.py")

    def test_communizm(self):
        from subprocess import Popen, PIPE

        process = Popen(["python", "manage.py", "communizm"], stdout=PIPE)

        time.sleep(2)

        thread = threading.Thread(target=self.send_coords, args=())
        thread.daemon = True
        thread.start()

        time.sleep(5)
        print "*****************************************************"


        if os.path.exists("test_data.txt"):
            with open("test_data.txt", "r") as f:
                self.assertTrue("{'event_type': 12, 'time': 1527139132, 'lat': 0.0, 'control_id': 'EyGeDCfJ', 'lon': 0.0, 'height': -267}" in f.read())


