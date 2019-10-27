from flask_restful import Resource, reqparse
from app.models import User
from app.errors import InvalidToken, DuplicateInfo


class ConfirmEmailApi(Resource):

    def post(self):
        verify_post_parser = reqparse.RequestParser()
        verify_post_parser.add_argument(
            'token',
            type=str,
            required=True
        )
        verify_post_parser.add_argument(
            'verify_token',
            type=str,
            required=True
        )
        args = verify_post_parser.parse_args()

        user = User.verify_auth_token(args['token'])
        if not user:
            raise InvalidToken()

        if user.confirmed:
            raise DuplicateInfo('邮箱已确认')

        if user.confirm(args['verify_token']):
            return {'message': '邮箱绑定成功'}, 200
        else:
            return InvalidToken('verify token')
