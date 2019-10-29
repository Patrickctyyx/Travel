from flask_restful import Resource
from .register_parser import login_post_parser
from app.models import User
from app.errors import ObjectNotFound, WrongInfo


class LoginApi(Resource):

    def post(self):
        args = login_post_parser.parse_args()

        user = User.query.filter_by(nickname=args.get('nickname')).first()
        if not user:
            raise ObjectNotFound('用户名不存在')

        if not user.verify_password(args.get('password')):
            raise WrongInfo('用户名或者密码错误')

        token = user.generate_auth_token().decode()

        return {'token': token, 'avatar_url': user.avatar_url}, 200
