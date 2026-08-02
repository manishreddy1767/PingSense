"""
Simple in-memory cache.

Later this can become disk cache.
"""


class MediaCache:

    def __init__(self):

        self.cache = {}

    def get(self, media_id):

        return self.cache.get(media_id)

    def put(self, media_id, value):

        self.cache[media_id] = value