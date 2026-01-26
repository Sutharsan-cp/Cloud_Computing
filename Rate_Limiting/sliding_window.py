import time
from collections import deque

class SlidingWindowLog:
    def __init__(self, limit, window_size):
        self.limit = limit  # max requests allowed
        self.window_size = window_size  # time window in seconds
        self.requests = deque()  # stores timestamps of requests

    def allow_request(self):
        current_time = time.time()

        # Remove requests outside the window
        while self.requests and self.requests[0] <= current_time - self.window_size:
            self.requests.popleft()

        if len(self.requests) < self.limit:
            self.requests.append(current_time)
            return True
        return False


# Example usage:
sliding_window = SlidingWindowLog(5, 10)  # 5 requests per 10 seconds

for _ in range(10):
    if sliding_window.allow_request():
        print("Request allowed")
    else:
        print("Request denied")
    time.sleep(2)  # Simulate request interval