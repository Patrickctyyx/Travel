from flask_restful import reqparse

comment_post_parser = reqparse.RequestParser()
comment_post_parser.add_argument(
    'token',
    type=str,
    required=True
)
comment_post_parser.add_argument(
    'article_id',
    type=str,
    required=True
)
comment_post_parser.add_argument(
    'content',
    type=str,
    required=True
)

comment_delete_parser = reqparse.RequestParser()
comment_delete_parser.add_argument(
    'token',
    type=str,
    required=True
)
