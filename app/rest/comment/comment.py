from flask_restful import Resource
from .comment_parser import comment_post_parser, comment_delete_parser
from app.models import db, Comment, User
from app.errors import (
    InvalidToken,
    DuplicateInfo,
    LackOfInfo,
    ObjectNotFound
)


class CommentApi(Resource):

    def get(self, comment_id=None):
        if not comment_id:
            raise LackOfInfo('评论 id')

        comment = Comment.query.get(comment_id)
        if not comment:
            raise ObjectNotFound('评论')

        result = dict()
        result['id'] = comment.id
        result['user_id'] = comment.user_id
        result['article_id'] = comment.article_id
        result['content'] = comment.content
        result['cred_at'] = str(comment.cred_at)

        return result, 200

    def post(self):
        args = comment_post_parser.parse_args()
        user = User.verify_auth_token(args['token'])

        if not user:
            raise InvalidToken()

        dup_comment = Comment.query.filter_by(content=args['content']).first()
        if dup_comment and dup_comment.user_id == user.id:
            raise DuplicateInfo('评论重复')

        comment = Comment()
        comment.user_id = user.id
        comment.article_id = args['article_id']
        comment.content = args['content']

        db.session.add(comment)
        db.session.commit()

        return {'message': 'ok'}, 200

    def delete(self, comment_id=None):

        args = comment_delete_parser.parse_args()
        user = User.verify_auth_token(args['token'])
        if not user:
            raise InvalidToken()

        if not comment_id:
            raise LackOfInfo('评论 id')

        comment = Comment.query.get(comment_id)
        if not comment:
            raise ObjectNotFound('评论')

        db.session.delete(comment)
        db.session.commit()

        return {'message': 'ok'}, 200
