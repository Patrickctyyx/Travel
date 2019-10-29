from flask_restful import Resource, reqparse
from app.models import Verify, User
from app.emails import send_email
from app.errors import WrongInfo


class SendVerifyEmailApi(Resource):

    def post(self):
        verify_post_parser = reqparse.RequestParser()
        verify_post_parser.add_argument(
            'nickname',
            type=str,
            required=True
        )
        verify_post_parser.add_argument(
            'email',
            type=str,
            required=True
        )
        args = verify_post_parser.parse_args()

        user = User.query.filter_by(nickname=args['nickname']).first()
        if not user or not user.email or user.email != args['email']:
            raise WrongInfo('邮箱或用户名错误')

        verify_token = Verify.generate_confirmation_token(
            args['nickname'], args['email']).decode()

        send_email(args['email'], '查收重置密码的 token',
                   'email/confirm', token=verify_token)

        return {'message': '邮件已发送'}, 200
