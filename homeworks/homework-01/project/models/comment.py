from datetime import datetime
import uuid

class Comment:
    def __init__(self, author_id: uuid, text: str):
        self.author_id = author_id
        self.text = text
        self.create_data = datetime.now()
        self.update_data = self.create_data
        self.like_count = 0

    def edit_comment(self, new_text: str) -> None:
        self.text = new_text
        self.update_data = datetime.now()

    def like(self) -> None:
        self.like_count += 1
        self.update_data = datetime.now()

    def dislike(self) -> None:
        self.like_count -= 1
        self.update_data = datetime.now()

    def __repr__(self) -> str:
        return "author_id={}, text={}, create_data={}, update_data={}, like_count={}".format(self.author_id, self.text, self.create_data, self.update_data, self.like_count)
