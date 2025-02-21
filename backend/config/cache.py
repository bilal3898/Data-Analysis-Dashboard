import redis
import os

class Cache:
    def __init__(self):
        """Initialize Redis cache connection"""
        self.redis_client = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            db=0,
            decode_responses=True  # Ensures stored values are in string format
        )

    def set_cache(self, key, value, expiration=3600):
        """Store data in Redis cache with expiration time (default: 1 hour)"""
        self.redis_client.setex(key, expiration, value)

    def get_cache(self, key):
        """Retrieve data from Redis cache"""
        return self.redis_client.get(key)

    def delete_cache(self, key):
        """Remove specific data from cache"""
        self.redis_client.delete(key)

    def flush_cache(self):
        """Clear all cached data"""
        self.redis_client.flushall()

# Initialize cache instance
cache = Cache()
