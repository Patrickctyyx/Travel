# 上传图片
import hashlib
import time
from flask import request
from flask_restful import Resource, reqparse
from app.models import photos, db, User
from app.errors import InvalidToken


class AvatarApi(Resource):

    def post(self):
        eval_imgs_post_parser = reqparse.RequestParser()
        eval_imgs_post_parser.add_argument(
            'token',
            type=str,
            required=True
        )
        args = eval_imgs_post_parser.parse_args()

        user = User.verify_auth_token(args['token'])

        if not user:
            raise InvalidToken()

        if 'photo' in request.files:
            filename = hashlib.md5(str(user.nickname).encode('utf-8') +
                                   str(time.time()).encode('utf-8')).hexdigest()[:10]
            # If it ends with a dot, the file’s extension will be appended to the end.
            img = photos.save(request.files['photo'], name=filename + '.')
            img_url = photos.url(img)

            user.avatar_url = img_url
            db.session.add(user)
            db.session.commit()

            return {'avatar_url': img_url}, 200
