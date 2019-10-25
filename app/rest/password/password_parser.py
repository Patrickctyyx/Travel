from flask_restful import reqparse


forget_post_parser = reqparse.RequestParser()
forget_post_parser.add_argument(
    'forget_token',
    type=str,
    required=True
)
forget_post_parser.add_argument(
    'nickname',
    type=str,
    required=True
)
forget_post_parser.add_argument(
    'email',
    type=str,
    required=True
)
forget_post_parser.add_argument(
    'new_password',
    type=str,
    required=True
)