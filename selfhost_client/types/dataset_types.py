from typing import List

try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class DatasetType(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for this dataset.
        name: Name of the resource. Does not have to be unique.
        format: File format of the data set.
        checksum: The sha256 checksum of the content.
        size: The size of the content in number of bytes.
        thing_uuid: A UUID reference to a Thing as a way to track data-sets to things.
        created: Date-time when created, as defined by RFC 3339, section 5.6.
        created_by: User UUID reference.
        updated: Date-time of last change, as defined by RFC 3339, section 5.6.
        updated_by: User UUID reference.
        tags: Tags pinned on this dataset.

    Example::

        {
            'uuid': '5e029cdf-4fee-42d2-9196-afbdfbdb9d8f'
            'name': 'ML model yTgvX7z',
            'format': 'ini',
            'checksum': '853ff93762a06ddbf722c4ebe9ddd66d8f63ddaea97f521c3ecc20da7c976020',
            'size': 0,
            'thing_uuid': 'f36834fb-8d96-4c01-b0e4-0bd85906bc25',
            'created': '2017-07-21T17:32:28+02:00',
            'created_by': 'f36834fb-8d96-4c01-b0e4-0bd85906bc25',
            'updated': '2017-07-21T17:32:28+02:00',
            'updated_by': 'A36834fb-8d96-4c01-b0e4-0bd85906bc25',
            'tags': [
                'tag1',
                'tag2'
            ],
        }

    """
    uuid: str
    name: str
    format: str
    checksum: str
    size: int
    thing_uuid: str
    created: str
    created_by: str
    updated: str
    updated_by: str
    tags: List[str]
