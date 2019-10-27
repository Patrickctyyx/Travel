from flask_restful import reqparse
from app.utils import password_type

register_post_parser = reqparse.RequestParser()
register_post_parser.add_argument(
    'nickname',
    type=str,
    required=True
)
register_post_parser.add_argument(
    'password',
    type=password_type,
    required=True
)
register_post_parser.add_argument(
    'sex',
    type=str,
    required=True
)
register_post_parser.add_argument(
    'birth_date',
    type=str,
    required=False
)
register_post_parser.add_argument(
    'hobby',
    type=str,
    required=False
)
