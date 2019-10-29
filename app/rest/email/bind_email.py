from flask_restful import Resource
from app.models import User, db
from app.errors import InvalidToken, DuplicateInfo
from app.utils import email_type
from app.emails import send_email
from app.rest.email.bind_email_parser import email_post_parser


class BindEmailApi(Resource):

    def post(self):
        args = email_post_parser.parse_args()

        email = email_type(args['email'])

        user = User.verify_auth_token(args['token'])
        if not user:
            raise InvalidToken()

        dup_email = User.query.filter_by(email=email).first()
        if dup_email:
            raise DuplicateInfo('该邮箱已被绑定')

        if user.email:
            user.confirmed = False

        user.email = email
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token().decode()

        send_email(email, '确认你的邮件',
                   'email/confirm', token=token)

        return {'message': '确认邮件已发送'}, 200
