from flask_restful import Resource, reqparse
from app.models import User
from app.errors import LackOfInfo, ObjectNotFound, InvalidToken


class UserInfoApi(Resource):

    def get(self, user_id=None):
        if not user_id:
            raise LackOfInfo('缺少用户 id')

        user = User.query.get(user_id)
        if not user:
            raise ObjectNotFound('user')

        result = dict()
        result['id'] = user.id
        result['nickname'] = user.nickname
        result['email'] = user.email
        result['avatar_url'] = user.avatar_url
        result['sex'] = user.sex
        result['birth_date'] = user.birth_date
        result['hobby'] = user.hobby

        return result, 200

    def post(self):  # 获得自己的信息
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

        result = dict()
        result['id'] = user.id
        result['nickname'] = user.nickname
        result['email'] = user.email
        result['avatar_url'] = user.avatar_url
        result['sex'] = user.sex
        result['birth_date'] = user.birth_date
        result['hobby'] = user.hobby

        return result, 200
