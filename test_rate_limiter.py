from rate_limiter import RateLimiter


def test_requests_under_limit():
    limiter = RateLimiter(3, 10)

    assert limiter.add_request("alice", 1) is True
    assert limiter.add_request("alice", 2) is True
    assert limiter.add_request("alice", 3) is True


def test_request_over_limit():
    limiter = RateLimiter(2, 10)

    assert limiter.add_request("alice", 1) is True
    assert limiter.add_request("alice", 2) is True
    assert limiter.add_request("alice", 3) is False


def test_users_are_independent():
    limiter = RateLimiter(1, 10)

    assert limiter.add_request("alice", 1) is True
    assert limiter.add_request("alice", 2) is False
    assert limiter.add_request("bob", 2) is True


def test_expired_requests_are_removed():
    limiter = RateLimiter(2, 10)

    assert limiter.add_request("alice", 1) is True
    assert limiter.add_request("alice", 2) is True

    assert limiter.add_request("alice", 12) is True


def test_remaining_requests():
    limiter = RateLimiter(5, 10)

    limiter.add_request("alice", 1)
    limiter.add_request("alice", 2)

    assert limiter.remaining_requests("alice", 2) == 3