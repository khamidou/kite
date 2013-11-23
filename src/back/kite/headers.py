# various functions which works on headers
import re

def cleanup_subject(subject_str):
    """Returns a cleaned up string.
    For instance, 'Re: Re: Re: Birthday party' becomes 'Birthday party'"""

    cleanup_regexp = "^((Re:|RE:|fwd:|FWD:)\s+)+"
    return re.sub(cleanup_regexp, "", subject_str)

