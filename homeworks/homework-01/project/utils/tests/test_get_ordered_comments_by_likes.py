import uuid

from models.comment import Comment
from utils.get_ordered_comments_by_likes import get_ordered_comments_by_likes


def test_get_ordered_comments_by_likes():
    comments = [
        Comment(uuid.UUID(), 't1'),
        Comment(uuid.UUID(), 't2'),
        Comment(uuid.UUID(), 't3'),
    ]
    comments[0].like()
    comments[1].dislike()
    comments[2].like()
    comments[0].like()

    received = get_ordered_comments_by_likes(comments)

    assert received[0].likes_count == 2
    assert received[1].likes_count == 1
    assert received[2].likes_count == -1
