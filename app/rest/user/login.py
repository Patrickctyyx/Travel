from flask import g
from flask_restful import Resource
from .register_parser import register_post_parser
from app.models import User
from app.errors import ObjectNotFound


class LoginApi(Resource):

    def post(self):
        args = register_post_parser.parse_args()

        user = User.query.filter_by(nickname=args.get('nickname')).first()
        if not user:
            raise ObjectNotFound('用户名不存在')

        g.current_user = user
        token = user.generate_auth_token().decode()

        return {'token': token}, 200
