# Python Rate Limiter

A lightweight rate limiter built in Python that controls how frequently individual clients can make requests within a configurable period of time.

This project was created to explore rate-limiting algorithms, object-oriented programming, request tracking, and automated testing in Python.

## Features

* Per-client request tracking
* Configurable request limits
* Configurable time windows
* Sliding-window request limiting
* Automatic removal of expired request timestamps
* Independent limits for different clients
* Successful and rejected request tracking
* Remaining-request calculation
* Support for real-time and manually supplied timestamps
* Unit tests using `pytest`

## How It Works

The rate limiter uses a **sliding-window** approach.

Each client has a list containing the timestamps of their recent successful requests.

For example:

```text
alice: [12, 15, 18]
bob:   [14, 19]
```

When a new request is received:

1. The start of the current time window is calculated.
2. Request timestamps outside that window are removed.
3. The number of remaining requests is compared with the configured limit.
4. If the client has reached the limit, the request is rejected.
5. Otherwise, the request is recorded and allowed.

For a rate limiter configured with a limit of `5` and a window of `10` seconds, each client may have up to five successful requests within the active ten-second window.

## Example Usage

```python
from rate_limiter import RateLimiter

limiter = RateLimiter(limit=5, window=10)

if limiter.add_request("alice"):
    print("Request allowed")
else:
    print("Request denied")

print(limiter.remaining_requests("alice"))
```

Timestamps can also be supplied manually, which is useful for testing:

```python
limiter = RateLimiter(limit=3, window=10)

print(limiter.add_request("alice", 1))
print(limiter.add_request("alice", 2))
print(limiter.add_request("alice", 3))
print(limiter.add_request("alice", 4))
```

The fourth request is rejected because Alice has already reached the configured limit within the current window.

## Running the Tests

The project uses `pytest` for automated testing.

Install pytest:

```bash
py -m pip install pytest
```

Run the test suite:

```bash
py -m pytest -v
```

The tests cover behaviour including:

* Requests below the configured limit
* Requests exceeding the limit
* Independent limits for different clients
* Expiration of old requests
* Remaining-request calculations

## Project Structure

```text
rate-limiter/
├── rate_limiter.py
├── test_rate_limiter.py
├── README.md
├── LICENSE
└── .gitignore
```

## Current Limitations

This is an initial implementation intended for learning and experimentation.

Request data is currently stored in memory, meaning it is local to a single running Python process and is lost when the application stops. It is therefore not designed for distributed or production-scale systems.

## Future Improvements

Potential future versions could explore:

* Token-bucket and other rate-limiting algorithms
* Thread-safe request handling
* FastAPI or other web-framework integration
* Persistent or shared storage
* Redis-backed distributed rate limiting
* Configurable rate limits for different endpoints
* Usage statistics and monitoring
* Performance benchmarking

## License

This project is available under the MIT License. See `LICENSE` for details.
