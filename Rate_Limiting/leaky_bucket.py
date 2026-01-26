import time

class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity  # max bucket size
        self.water = 0  # current amount of "water" in the bucket
        self.leak_rate = leak_rate  # rate at which water leaks per second
        self.last_time = time.time()

    def leak(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_time
        self.water = max(0, self.water - elapsed_time * self.leak_rate)
        self.last_time = current_time

    def allow_request(self):
        self.leak()
        if self.water < self.capacity:
            self.water += 1  # Add 1 unit of "water" for each request
            return True
        return False


# Example usage:
bucket = LeakyBucket(5, 1)  # max 5 requests, leak 1 per second

for _ in range(10):
    if bucket.allow_request():
        print("Request allowed")
    else:
        print("Request denied")
    time.sleep(0.5)  # Simulate request interval