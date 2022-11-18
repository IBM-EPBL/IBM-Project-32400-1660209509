import time
from locust import HttpUser, task, between
#from locust import HttpLocust, TaskSet, between

class QuickstartUser(HttpUser):
    wait_time = between(1,2)
   

    @task
    def getting(self):
        self.client.post("/login")
        
    def posting(self):
        self.client.get("/dashboard")