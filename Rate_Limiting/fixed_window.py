import time

class FixedWindowCounter:
    def __init__(self, limit, window_size):
        self.limit = limit  # max requests allowed
        self.window_size = window_size  # time window in seconds
        self.count = 0  # current count of requests in the window
        self.start_time = time.time()

    def allow_request(self):
        current_time = time.time()
        if current_time - self.start_time > self.window_size:
            # Reset the window
            self.start_time = current_time
            self.count = 0
        if self.count < self.limit:
            self.count += 1
            return True
        return False


# Example usage:
window = FixedWindowCounter(5, 10)  # 5 requests per 10 seconds

for _ in range(10):
    if window.allow_request():
        print("Request allowed")
    else:
        print("Request denied")
    time.sleep(2)  # Simulate request interval