import time
from locust import HttpUser, task, between,constant,SequentialTaskSet

class QuickstartUser(SequentialTaskSet):
   

    @task
    def getting(self):
       res= self.client.get("/login")
        
    @task
    def posting(self):
         res=  self.client.post("/dashboard")
         
class Task(HttpUser):
    wait_time=constant(1)
    
    host="/http://localhost:5000"
    tasks=[QuickstartUser]
    


    