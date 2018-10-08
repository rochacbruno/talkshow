from flask import current_app as app
from slugify import UniqueSlugify


def slug_unique_check(text, uids):
    ''' Checks the database for a matching text'''
    if text in uids:
        return False
    return not app.db['events'].find_one({'slug': text})


# Creates a Unique Slugify
slugify = UniqueSlugify(unique_check=slug_unique_check, to_lower=True)
