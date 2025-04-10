import csv
import random
from locust import task
from core.base_user import BaseUser

class UserTasks(BaseUser):

    def on_start(self):
        self.user_data = self.load_users()

    def load_users(self):
        with open("data/users.csv", newline='') as csvfile:
            return list(csv.DictReader(csvfile))

    @task
    def get_users(self):
        self.client.get("/api/users?page=2")

    @task
    def create_user(self):
        user = random.choice(self.user_data)
        self.client.post("/api/users", json=user)
