import uuid

import pytest

from models.comment import Comment


class TestComment:
    def setup(self):
        self.uuid = uuid.uuid4()
        self.comment = Comment(self.uuid, 'comment_text')

    def test_edit_comment(self):
        self.comment.edit_comment('new_comment_text')
        assert self.comment.text == 'new_comment_text'
        assert self.comment.create_data != self.comment.update_data

    @pytest.mark.parametrize('like_count', [0, 1, 2, 5])
    def test_like(self, like_count):
        for i in range(like_count):
            self.comment.like()
        assert self.comment.like_count == like_count

    @pytest.mark.parametrize('dislike_count', [0, 1, 2, 5])
    def test_dislike(self, dislike_count):
        for i in range(dislike_count):
            self.comment.dislike()
        assert self.comment.like_count == -dislike_count
