from locust import HttpUser, between
from config.settings import get_config

config = get_config()

class BaseUser(HttpUser):
    wait_time = between(1, 3)
    host = config.host
