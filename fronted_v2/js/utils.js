const url = "http://localhost:5000/";

function registerHandler() {
	const sname = $("input[name=name]").val().replace(/(^\s*)|(\s*$)/g, '');
	const spwd = $("input[name=pwd]").val().replace(/(^\s*)|(\s*$)/g, '');
	const sex = $("input[name=sex]").val().replace(/(^\s*)|(\s*$)/g, '');
	let ssex;
	if (sex === 0) {
	    ssex = '男';
    }
	else {
	    ssex = '女';
    }
	const birthDate = $("input[name=day]").val().replace(/(^\s*)|(\s*$)/g, '');
	const hobby = $("input[name=hobby]").val().replace(/(^\s*)|(\s*$)/g, '');

	if (registcheck()) {
	    $.ajax(
            url + "api/register", {
            method: 'POST',
            dataType: 'json',
            data: {
                nickname: sname,
                password: spwd,
                sex: ssex,
                birth_date: birthDate,
                hobby: hobby
            },
            success: function(data) {
                // console.log(data);
                localStorage.setItem('token', data.token);
                alert('注册成功');
                window.location.href="homepage.html";
            },
            error: function (error) {
                const resData = error.responseJSON.message;
                alert(JSON.stringify(resData));
                console.log(error);
            }
	    });
    }
}


function forgetPasswordHandler() {
    // todo
}


function loginHandler() {
    const sname = $("input[name=username]").val().replace(/(^\s*)|(\s*$)/g, '');
	const spwd = $("input[name=password]").val().replace(/(^\s*)|(\s*$)/g, '');

    if (logincheck()) {
        $.ajax(
            url + "api/login", {
            method: 'POST',
            dataType: 'json',
            data: {
                nickname: sname,
                password: spwd
            },
            success: function(data) {
                // console.log(data);
                localStorage.setItem('token', data.token);
                alert('登录成功');
                window.location.href="homepage.html";
            },
            error: function (error) {
                const resData = error.responseJSON.message;
                alert(JSON.stringify(resData));
                console.log(error);
            }
	    });
    }
}


function logoutHandler() {
    const token = localStorage.getItem('token');
    if (token == null) {
        alert('请先登录')
    }
    else {
        $.ajax(
            url + "api/logout", {
            method: 'POST',
            dataType: 'json',
            data: {
                token: token
            },
            success: function(data) {
                // console.log(data);
                alert('登出成功');
                localStorage.removeItem('token');
                $("#loginBtn").css('display', 'inline-block');
                $("#registerBtn").css('display', 'inline-block');
                $("#userBlock").css('display', 'none');
                window.location.href="homepage.html";
            },
            error: function (error) {
                const resData = error.responseJSON.message;
                alert(JSON.stringify(resData));
                console.log(error);
            }
        });
    }
}


function homepageLoaded() {
    const token = localStorage.getItem('token');
    if (token == null) {
        $("#loginBtn").css('display', 'inline-block');
        $("#registerBtn").css('display', 'inline-block');
        $("#userBlock").css('display', 'none');
    }
    else {
        $("#loginBtn").css('display', 'none');
        $("#registerBtn").css('display', 'none');
        $("#userBlock").css('display', 'inline-block');
    }
}
