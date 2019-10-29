const url_password = "http://localhost:5000/";

function sendForgetToken() {
    const nickname = $('#nicknameForget').val().replace(/(^\s*)|(\s*$)/g, '');
    if (nickname == '' || nickname == null) {
        alert('昵称不能为空');
        return false
    }
    const email = $('#emailForget').val().replace(/(^\s*)|(\s*$)/g, '');
    if (!checkEmail(email)) {
        alert('请输入合法的邮箱');
        return
    }
    $.ajax(
        url_password + "api/send_verify_email", {
        method: 'POST',
        dataType: 'json',
        data: {
            nickname: nickname,
            email: email
        },
        success: function(data) {
            alert(data.message)
        },
        error: function (error) {
            const resData = error.responseJSON;
            alert(JSON.stringify(resData.message));
            console.log(error);
        }
    });
}


function forgetPasswordHandler() {
    const nickname = $('#nicknameForget').val().replace(/(^\s*)|(\s*$)/g, '');
    if (nickname == '' || nickname == null) {
        alert('昵称不能为空');
        return false
    }
    const email = $('#emailForget').val().replace(/(^\s*)|(\s*$)/g, '');
    if (!checkEmail(email)) {
        alert('请输入合法的邮箱');
        return
    }
    const forgetToken = $('#tokenForget').val().replace(/(^\s*)|(\s*$)/g, '');
    const newPwd1 = $('#passwordForget1').val().replace(/(^\s*)|(\s*$)/g, '');
    const newPwd2 = $('#passwordForget2').val().replace(/(^\s*)|(\s*$)/g, '');
    if (newPwd1 != newPwd2) {
		alert("两次密码不一致");
		return
	}
    if (!checkPassword(newPwd1)) {
        alert('密码中只能包含大小写数字和._，且长度为 9~16 位');
        return
    }
    $.ajax(
        url_password + "api/forget_password", {
        method: 'POST',
        dataType: 'json',
        data: {
            nickname: nickname,
            email: email,
            forget_token: forgetToken,
            new_password: newPwd1
        },
        success: function(data) {
            alert(data.message);
            window.location.href = "userLogin.html"
        },
        error: function (error) {
            const resData = error.responseJSON;
            alert(JSON.stringify(resData.message));
            console.log(error);

            if (resData.message.indexOf('未确认')) {
                window.location.href = "homepage.html"
            }
        }
    });
}


function changePasswordHandler() {
    const oldPwd = $('#changeOldPassword').val().replace(/(^\s*)|(\s*$)/g, '');
    const newPwd1 = $('#changeNewPassword1').val().replace(/(^\s*)|(\s*$)/g, '');
    const newPwd2 = $('#changeNewPassword2').val().replace(/(^\s*)|(\s*$)/g, '');
    if (newPwd1 != newPwd2) {
		alert("两次密码不一致");
		return
	}
    if(!newPwd1.match(/^[a-zA-Z0-9\.\_]{9,16}$/)) {
        alert('密码中只能包含大小写数字和._，且长度为 9~16 位');
        return
    }
    const token = localStorage.getItem('token');
    if (token == null) {
        alert('请先登录');
        localStorage.clear();
        parent.location.href="userLogin.html";
    }
    else {
        $.ajax(
            url_password + "api/change_password", {
            method: 'POST',
            dataType: 'json',
            data: {
                token: token,
                old_password: oldPwd,
                new_password: newPwd1
            },
            success: function(data) {
                // console.log(data);
                alert('密码改变，请重新登录');
                localStorage.clear();
                parent.location.href="userLogin.html";
            },
            error: function (error) {
                const resData = error.responseJSON;
                alert(JSON.stringify(resData.message));

                if (resData.errcode == 2) {
                    console.log(error);
                    localStorage.clear();
                    parent.location.href="userLogin.html";
                }
            }
        });
    }
}
