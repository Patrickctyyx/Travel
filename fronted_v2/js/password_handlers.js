const url_password = "http://localhost:5000/";

function forgetPasswordHandler() {
    // todo
}


function changePasswordHandler() {
    const oldPwd = $('#changeOldPassword').val().replace(/(^\s*)|(\s*$)/g, '');
    const newPwd1 = $('#changeNewPassword1').val().replace(/(^\s*)|(\s*$)/g, '');
    const newPwd2 = $('#changeNewPassword2').val().replace(/(^\s*)|(\s*$)/g, '');
    if (newPwd1 != newPwd2) {
		alert("两次密码不一致");
		return false;
	}
    if(!newPwd1.match(/^[a-zA-Z0-9\.\_]{9,16}$/)) {
        alert('密码中只能包含大小写数字和._，且长度为 9~16 位');
        return false;
    }
    const token = localStorage.getItem('token');
    if (token == null) {
        alert('请先登录');
        localStorage.clear();
        parent.location.href="userLogin.html";
    }
    else {
        $.ajax(
            url_user + "api/change_password", {
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
