from flask import Flask, Response
from app.config import config
from app.models import db, photos
from app.emails import mail
from app.rest.comment.comment import CommentApi
from app.rest.user.upload_avatar import AvatarApi
from app.rest.user.user_info import UserInfoApi
from app.rest.user.login import LoginApi
from app.rest.user.logout import LogoutApi
from app.rest.user.register import RegisterApi
from app.rest.user.revise_user_info import ReviseUserInfoApi
from app.rest.email.bind_email import BindEmailApi
from app.rest.email.confirm_email import ConfirmEmailApi
from app.rest.password.change_password import ChangePasswordApi
from app.rest.password.send_verify_email import SendVerifyEmailApi
from app.rest.password.forget_password import ForgetPasswordApi
from flask_restful import Api
from flask_uploads import configure_uploads
from werkzeug.datastructures import Headers


class MyResponse(Response):
    def __init__(self, response=None, **kwargs):
        kwargs['headers'] = ''
        headers = kwargs.get('headers')
        # 跨域控制
        origin = ('Access-Control-Allow-Origin', '*')
        methods = ('Access-Control-Allow-Methods', 'HEAD, OPTIONS, GET, POST, DELETE, PUT')
        if headers:
            headers.add(*origin)
            headers.add(*methods)
        else:
            headers = Headers([origin, methods])
        kwargs['headers'] = headers
        return super().__init__(response, **kwargs)


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(config[object_name])
    app.response_class = MyResponse

    db.init_app(app)
    mail.init_app(app)

    rest_api = Api()
    rest_api.add_resource(
        CommentApi,
        '/api/comment',
        '/api/comment/<int:comment_id>'
    )
    rest_api.add_resource(
        RegisterApi,
        '/api/register'
    )
    rest_api.add_resource(
        LoginApi,
        '/api/login'
    )
    rest_api.add_resource(
        LogoutApi,
        '/api/logout'
    )
    rest_api.add_resource(
        UserInfoApi,
        '/api/user_info',
        '/api/user_info/<int:user_id>'
    )
    rest_api.add_resource(
        AvatarApi,
        '/api/upload_avatar'
    )
    rest_api.add_resource(
        BindEmailApi,
        '/api/bind_email'
    )
    rest_api.add_resource(
        ConfirmEmailApi,
        '/api/confirm_email'
    )
    rest_api.add_resource(
        ChangePasswordApi,
        '/api/change_password'
    )
    rest_api.add_resource(
        SendVerifyEmailApi,
        '/api/send_verify_email'
    )
    rest_api.add_resource(
        ForgetPasswordApi,
        '/api/forget_password'
    )
    rest_api.add_resource(
        ReviseUserInfoApi,
        '/api/revise_user_info'
    )
    rest_api.init_app(app)

    configure_uploads(app, photos)

    return app
