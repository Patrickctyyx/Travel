import uuid
from flask import g
from flask_restful import Resource, reqparse
from app.models import User, db
from app.errors import InvalidToken


class LogoutApi(Resource):

    def post(self):
        post_parser = reqparse.RequestParser()
        post_parser.add_argument(
            'token',
            type=str,
            required=True
        )
        args = post_parser.parse_args()

        user = User.verify_auth_token(args['token'])
        if not user:
            raise InvalidToken()

        # 更新 uuid，这样原来的 token 解析出来的 uuid 是旧的
        # 判定此时 token 已经失效
        user.uid = str(uuid.uuid4())
        db.session.add(user)
        db.session.commit()

        g.current_user = None

        return {'msg': 'ok'}, 200
