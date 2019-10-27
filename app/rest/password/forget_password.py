from flask_restful import Resource
from app.models import User, Verify, db
from app.errors import ObjectNotFound, WrongInfo, InvalidToken
from app.rest.password.password_parser import forget_post_parser


class ForgetPasswordApi(Resource):

    def post(self):

        args = forget_post_parser.parse_args()

        user = User.query.filter_by(nickname=args['nickname']).first()
        if not user:
            raise ObjectNotFound('用户不存在')

        if not user.confirmed:
            raise WrongInfo('邮箱未确认，无法重置密码')

        if user.email != args['email']:
            raise WrongInfo('邮箱或用户名错误')

        if Verify.confirm(args['forget_token'],
                          args['nickname'], args['email']):
            user.password = args['new_password']
            db.session.add(user)
            db.session.commit()
            return {'message': '密码重置成功'}, 200
        else:
            raise InvalidToken('verify token')
