const url_email = "http://139.155.89.156/";


function bindEmail() {
    const email = $('#emailToBind').val().replace(/(^\s*)|(\s*$)/g, '');
    if (!checkEmail(email)) {
        alert('请输入合法的邮箱');
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
            url_email + "api/bind_email", {
            method: 'POST',
            dataType: 'json',
            data: {
                token: token,
                email: email
            },
            success: function(data) {
                alert(data.message)
            },
            error: function (error) {
                const resData = error.responseJSON;
                alert(JSON.stringify(resData.message));
                console.log(error);

                if (resData.errcode == 2) {
                    localStorage.clear();
                    parent.location.href="userLogin.html";
                }
            }
        });
    }
}


function confirmEmail() {
    const emailToken = $('#emailToken').val().replace(/(^\s*)|(\s*$)/g, '');
    const token = localStorage.getItem('token');
    if (token == null) {
        alert('请先登录');
        localStorage.clear();
        parent.location.href="userLogin.html";
    }
    else {
        $.ajax(
            url_email + "api/confirm_email", {
            method: 'POST',
            dataType: 'json',
            data: {
                token: token,
                verify_token: emailToken
            },
            success: function(data) {
                alert(data.message);
                window.location.reload()
                // parent.location.href="personCenter.html";
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
