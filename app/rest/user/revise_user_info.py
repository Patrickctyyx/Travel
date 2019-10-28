from flask_restful import Resource
from .revise_user_info_parser import user_info_post_parser
from app.models import db, User
from app.errors import InvalidToken


class ReviseUserInfoApi(Resource):

    def post(self):
        args = user_info_post_parser.parse_args()

        user = User.verify_auth_token(args['token'])
        if not user:
            raise InvalidToken()

        user.sex = args['sex']
        user.birth_date = args.get('birth_date')
        user.hobby = args.get('hobby')

        db.session.add(user)
        db.session.commit()

        return {'message': 'ok'}, 200
