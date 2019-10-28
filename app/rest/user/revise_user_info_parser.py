from flask_restful import reqparse

user_info_post_parser = reqparse.RequestParser()
user_info_post_parser.add_argument(
    'token',
    type=str,
    required=True,
)
user_info_post_parser.add_argument(
    'sex',
    type=str,
    required=True
)
user_info_post_parser.add_argument(
    'birth_date',
    type=str,
    required=False
)
user_info_post_parser.add_argument(
    'hobby',
    type=str,
    required=False
)
