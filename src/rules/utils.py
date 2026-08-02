import re


def contains_keywords(text, keywords):

    if not text:
        return False

    text = text.lower()

    return any(keyword in text for keyword in keywords)


def contains_link(text):

    if not text:
        return False

    pattern = r"(http://|https://|www\.)"

    return re.search(pattern, text.lower()) is not None