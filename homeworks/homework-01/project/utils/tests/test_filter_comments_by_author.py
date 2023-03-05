from models.comment import Comment
from models.user import User
from utils.filter_comments_by_author import filter_comments_by_author


def test_filter_comments_by_author():
    author1 = User('a')
    author2 = User('b')
    comments = [
        Comment(author1.id, 't1'),
        Comment(author2.id, 't2'),
        Comment(author1.id, 't3'),
    ]

    received = filter_comments_by_author(comments, author1)

    assert len(received) == 2
    assert received[0].author_id == author1.id
    assert received[1].author_id == author1.id
