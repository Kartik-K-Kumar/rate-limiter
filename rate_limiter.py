import time


class RateLimiter:
    def __init__(self, limit: int, window: int):
        self.limit = limit
        self.window = window
        self.requests = {}
        self.successful = 0
        self.unsuccessful = 0

    def remove_expired_requests(self, user: str, timestamp: float):
        window_start = timestamp - self.window

        self.requests[user] = [
            t for t in self.requests[user]
            if t >= window_start
        ]

    def add_request(self, user: str, timestamp=None) -> bool:
        if timestamp is None:
            timestamp = time.time()

        if user not in self.requests:
            self.requests[user] = []

        self.remove_expired_requests(user, timestamp)

        if len(self.requests[user]) >= self.limit:
            self.unsuccessful += 1
            return False

        self.requests[user].append(timestamp)
        self.successful += 1
        return True

    def remaining_requests(self, user: str, timestamp=None) -> int:
        if timestamp is None:
            timestamp = time.time()

        if user not in self.requests:
            return self.limit

        self.remove_expired_requests(user, timestamp)

        return self.limit - len(self.requests[user])


# Test execution
requestLimit = RateLimiter(5, 10)

print(requestLimit.add_request("alice"))
print(requestLimit.add_request("alice"))
print(requestLimit.add_request("alice"))
print(requestLimit.add_request("alice"))
print(requestLimit.add_request("alice"))
print(requestLimit.add_request("alice"))
print(requestLimit.add_request("alice"))
print(requestLimit.add_request("alice"))
print(requestLimit.add_request("alice"))

print("\n--- Testing Bob (Fails on 4th continuous request) ---")
print(requestLimit.add_request("bob"))
print(requestLimit.add_request("bob"))
print(requestLimit.add_request("bob"))
print(requestLimit.add_request("bob"))

print("\n--- Testing Charlie (All valid, old requests drop out) ---")
print(requestLimit.add_request("charlie"))
print(requestLimit.add_request("charlie"))
print(requestLimit.add_request("charlie"))
print(requestLimit.add_request("charlie"))
print(requestLimit.add_request("charlie"))
print(requestLimit.add_request("charlie"))



print(requestLimit.request)
print(f"Successful requests: {requestLimit.successful}")
print(f"Unsuccessful requests: {requestLimit.unsuccessful}")

total_requests = requestLimit.successful + requestLimit.unsuccessful

print(f"Total Requests: {total_requests}")