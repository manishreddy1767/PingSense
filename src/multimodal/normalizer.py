"""
Multimodal Normalizer

Converts every message into effective_text.
"""

from src.multimodal.cache import MediaCache
from src.multimodal.image_processor import ImageProcessor
from src.multimodal.audio_processor import AudioProcessor


class MultimodalNormalizer:

    def __init__(self):

        self.cache = MediaCache()

        self.image = ImageProcessor()

        self.audio = AudioProcessor()

    def normalize(self, context):

        message = context.message

        # Plain text
        if message.media_type is None:

            context.effective_text = message.message_text

            return context

        # Cached result
        cached = self.cache.get(message.media_id)

        if cached is not None:

            context.effective_text = cached

            return context

        # Image
        if message.media_type == "image":

            text = self.image.process(
                context.media.file_path
            )

        # Voice
        elif message.media_type == "voice":

            text = self.audio.process(
                context.media.file_path
            )

        else:

            text = message.message_text

        self.cache.put(message.media_id, text)

        context.effective_text = text

        return context