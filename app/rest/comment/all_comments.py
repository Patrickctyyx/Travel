from flask_restful import Resource
from app.models import Comment, User


class AllCommentsApi(Resource):

    def get(self):

        comments = Comment.query.order_by(Comment.cred_at.desc()).all()
        if not comments:
            return []

        result_list = list()

        for comment in comments:
            result = dict()
            result['id'] = comment.id
            user = User.query.get(comment.user_id)
            result['nickname'] = user.nickname
            result['avatar_url'] = user.avatar_url
            result['sex'] = user.sex
            result['article_id'] = comment.article_id
            result['content'] = comment.content
            result['cred_at'] = str(comment.cred_at)
            result_list.append(result)

        return result_list, 200
