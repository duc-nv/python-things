from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    host = 'http://localhost:5001/sync'

    @task
    def hello_world(self):
        self.client.get("/")

# locust --headless -u5 -r5 -t10s --stop-timeout 2
