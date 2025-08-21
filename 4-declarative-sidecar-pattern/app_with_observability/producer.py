import redis
import json
import time
import random
import uuid

# Connect to the Redis instance defined in docker-compose
r = redis.Redis(host='redis', port=6379, db=0)
print("✅ Producer connected to Redis.")


def create_user_signup_event():
    """Generates a random user signup event."""
    return {
        "event_name": "user_signup",
        "user_id": str(uuid.uuid4()),
        "email": f"user_{random.randint(1000, 9999)}@example.com",
        "age": random.randint(18, 70),
        "country_code": random.choice(["US", "DE", "GB", "CA", "FR", "AU"]),
        "timestamp": time.time()
    }


print("🚀 Starting data production...")
while True:
    try:
        event = create_user_signup_event()
        # Publish the event as a JSON string to the 'events_channel'
        r.publish('events_channel', json.dumps(event))
        print(f"Sent event for user: {event['user_id']}")

        # Simulate variable load by sleeping for a random interval
        time.sleep(random.uniform(0.5, 2.5))

    except redis.exceptions.ConnectionError as e:
        print(f"❌ Could not connect to Redis: {e}. Retrying in 5 seconds...")
        time.sleep(5)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        time.sleep(5)