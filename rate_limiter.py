print("rate_limiter.py loaded")

class RateLimiter:
    def __init__ (self, limit:int, window:int):
        self.limit = limit
        self.window = window


limiter = RateLimiter(5,10)
print(limiter.limit)
print(limiter.window)