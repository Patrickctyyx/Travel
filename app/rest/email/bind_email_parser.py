from flask_restful import reqparse
from app.utils import email_type

email_post_parser = reqparse.RequestParser()
email_post_parser.add_argument(
    'token',
    type=str,
    required=True
)
email_post_parser.add_argument(
    'email',
    type=email_type,
    required=True
)
