import os
import urllib

from django.conf import settings
from urllib.error import URLError


def get_static_file(app_label, filename):
    path = os.path.join(
        settings.STATIC_ROOT, app_label, filename)
    try:
        with open(path, "r"):
            pass
    except FileNotFoundError:
        url = os.path.join(
            f"https://{settings.STATIC_URL}", app_label, filename)
        try:
            path, _ = urllib.request.urlretrieve(url)
        except URLError as e:
            raise FileNotFoundError(
                f"Static file not found. "
                f"Tried STATIC_ROOT ({settings.STATIC_ROOT}) and "
                f"STATIC_URL ({settings.STATIC_URL}). "
                f"Got {app_label}/{filename}.")
    return path