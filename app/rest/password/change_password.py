from flask_restful import Resource, reqparse
from app.models import User, db
from app.errors import InvalidToken, WrongInfo
from app.utils import password_type


class ChangePasswordApi(Resource):

    def post(self):
        verify_post_parser = reqparse.RequestParser()
        verify_post_parser.add_argument(
            'token',
            type=str,
            required=True
        )
        verify_post_parser.add_argument(
            'old_password',
            type=password_type,
            required=True
        )
        verify_post_parser.add_argument(
            'new_password',
            type=password_type,
            required=True
        )
        args = verify_post_parser.parse_args()

        user = User.verify_auth_token(args['token'])
        if not user:
            raise InvalidToken()

        if not user.verify_password(args['old_password']):
            raise WrongInfo('用户名或者密码错误')

        user.password = args['new_password']
        db.session.add(user)
        db.session.commit()

        return {'message': 'ok'}, 200
