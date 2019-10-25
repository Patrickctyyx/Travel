import re


def email_type(email):
    if re.match('^[0-9a-zA-Z\_]+@[0-9a-zA-Z\_]+\.com$', email):
        return email
    else:
        raise ValueError('邮箱不合法')


def password_type(password):
    if re.match('[0-9a-zA-Z\.\_]{9,16}', password):
        return password
    else:
        raise ValueError('密码中只能包含大小写数字和._，且长度为 9~16 位')


def level_type(level):
    if level != 'college' and level != 'master' and level != 'doctor':
        raise ValueError('Not a proper level!')
    return level


def status_type(status):
    if status != 'pending' and status != 'processing' and status != 'ended':
        raise ValueError('Not a proper status!')
    return status


def apply_status_type(status):
    if status != 1 and status != 0 and status != -1:
        raise ValueError('Not a proper status!')
    return status
