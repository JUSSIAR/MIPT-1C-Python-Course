def get_ordered_comments_by_likes(comments):
    return sorted(comments, key=lambda x: -x.like_count)
