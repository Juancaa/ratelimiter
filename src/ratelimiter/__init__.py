
'''
Function decorator for bursty and steady rate limiting

This module provides a functon decorator that can be used to wrap a function
such that it will raise an exception if the number of calls to that function
exceeds a maximum within a specified time window.

This code is a modified version of below repo
https://github.com/tomasbasham/ratelimt
'''
from decorators import SlidingWindowRateLimiter, FixedWindowRateLimiter, rate_limiter
from utilities import batch_generator

fixed_rate = FixedWindowRateLimiter
sliding_rate = SlidingWindowRateLimiter
rate_limiter = rate_limiter

__all__ = [
  'fixed_rate',
  'sliding_rate',
  'batch_generator',
  'rate_limiter',
]

__version__ = '0.1.1'
