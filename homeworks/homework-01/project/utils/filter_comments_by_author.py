def filter_comments_by_author(comments, author):
    return list(filter(lambda x: x.author_id == author.id, comments))
