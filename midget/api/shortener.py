import uuid

import redis


redis_instance = redis.StrictRedis(host='localhost', port=6379, db=0)


def generate_random_string(string_length=7):
    """
    Returns a random string of length string_length.

    This will be appended to the shortened link and stored on redis as a key to
    a url.
    """
    # Convert UUID format to a Python string.
    random = str(uuid.uuid4())

    # Make all characters uppercase.
    # random = random.upper()

    # Remove the UUID '-'.
    random = random.replace("-", "")

    # Return the random string.
    return random[0:string_length]


def check_random_string(random_string):
    """
    Check if a string is already in use on the redis server and create a new
    one if needed.

    If it exists, return true, else return false
    """
    if redis_instance.get(random_string):
        return True
    else:
        return False


def get_url(random_string):
    """
    Find a url from the redis server and return it
    """
    return redis_instance.get(random_string)


def create_url(url_to_be_shortened):
    """
    Create the shortened URL and save it on Redis
    """
    strng = generate_random_string()

    if check_random_string(strng):
        create_url(url_to_be_shortened)

    elif not check_random_string(strng):
        redis_instance.set(strng, url_to_be_shortened)
        return strng

