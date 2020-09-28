from locust import HttpUser, TaskSet, task

class UserTasks(TaskSet):
    def on_start(self): # WebsiteUser 開始任務需要執行的步驟
        """ on_start is called when a Locust start before any task is scheduled """
        self.login(url)

    def on_stop(self): # 為結束
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("/login", {"username":"ellen_key", "password":"education"})

    def logout(self):
        self.client.post("/logout", {"username":"ellen_key", "password":"education"})

    # decorator
    @task(1)  # 亦即在過程中要執行的指令，後面的數字是執行比例
    def index(self):
        self.client.get("/")

    @task(2)
    def about(self):
        self.client.get("/about")


class WebUser(HttpUser):
    task_set = UserTasks

    # min_wait 則定義 max_wait 測試過程中兩次任務的間隔為 5-15 秒的隨機數。
    min_wait = 5000
    max_wait = 15000
