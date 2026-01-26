import time

class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity  # max number of tokens
        self.tokens = capacity  # current number of tokens
        self.refill_rate = refill_rate  # tokens added per second
        self.last_refill_time = time.time()

    def refill(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_refill_time
        # Refill the bucket based on elapsed time
        new_tokens = elapsed_time * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill_time = current_time

    def allow_request(self):
        self.refill()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False


# Example usage:
bucket = TokenBucket(5, 1)  # 5 tokens max, refill 1 token per second

for _ in range(10):
    if bucket.allow_request():
        print("Request allowed")
    else:
        print("Request denied")
    time.sleep(0.5)  # Simulate request interval