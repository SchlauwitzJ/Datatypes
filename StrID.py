from __future__ import annotations
from typing import Union
import random
import string


def strid(len_lim: int = None, exclusions: Union[list, dict] = None):
    if exclusions is None:
        taken_str = []
    elif isinstance(exclusions, dict):
        taken_str = exclusions.keys()
    else:
        taken_str = exclusions

    while True:
        new_strid = ''.join(random.choice(string.ascii_letters + string.digits)
                            for _ in range(random.choice(range(1, len_lim))))
        if new_strid not in taken_str:
            break
    return new_strid
