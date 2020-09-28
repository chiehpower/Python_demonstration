import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task(1)
    def view_item(self):
        for item_id in range(10):
            print("view_item: This is {} time.".format(item_id))
            files  = {'file': open('test.png', 'rb')}
            model = '(model name)'
            url = "(link)"
            result = self.client.post(url, files=files, data={'model':model, 'web':'web'})
            time.sleep(1)
    @task(1)
    def get_item(self):
        for item_id1 in range(10):
            print("get_item: This is {} time.".format(item_id1))
            files  = {'file': open('test.png', 'rb')}
            model = '(model 2 name)'
            url = "(link)"
            result = self.client.post(url, files=files, data={'model':model, 'web':'web'})
            time.sleep(1)