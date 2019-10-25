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
