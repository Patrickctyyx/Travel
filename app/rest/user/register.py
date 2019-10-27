from flask import g
from flask_restful import Resource
from .register_parser import register_post_parser
from app.models import db, User
from app.errors import DuplicateInfo


class RegisterApi(Resource):

    def post(self):
        args = register_post_parser.parse_args()

        user = User.query.filter_by(nickname=args.get('nickname')).first()
        if user:
            raise DuplicateInfo('该用户名已存在')
        else:
            user = User(
                nickname=args.get('nickname'),
                password=args.get('password'),
                sex=args.get('sex'),
                birth_date=args.get('birth_date'),
                hobby=args.get('hobby')
            )

        db.session.add(user)
        db.session.commit()
        token = user.generate_auth_token().decode()

        g.current_user = user

        return {'token': token}, 200
