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
        const avatar_url = localStorage.getItem('avatar_url');
        if (avatar_url != null) {
            $('#userAvatar').attr('src', avatar_url)
        }
    }
}


function personalPageLoaded() {
	const token = localStorage.getItem('token');
    if (token == null) {
        alert('请先登录');
        window.location.href="homepage.html";
    }
    else {
        $.ajax(
            url + "api/user_info", {
            method: 'POST',
            dataType: 'json',
            data: {
                token: token
            },
            success: function(data) {
                // console.log(data);
                localStorage.setItem('avatar_url', data.avatar_url);
                localStorage.setItem('nickname', data.nickname);
                $("#avatarAndName").children("a").children("img").attr('src', data.avatar_url);
                $("#avatarAndName").children("span").text(data.nickname);
                $("#detailInfo").children("div").children('input:eq(0)').attr('value', data.nickname);
                if (data.sex === '男') {
                    $("input[name=sex].boy").attr('checked', 'checked');
                    $("input[name=sex].girl").removeAttr('checked');
                }
                else {
                    $("input[name=sex].girl").attr('checked', 'checked');
                    $("input[name=sex].boy").removeAttr('checked');
                }
                $("#detailInfo").children("div").children('input:eq(1)').attr('value', data.sex);
                $("#detailInfo").children("div").children('input:eq(3)').attr('value', data.email);
                $("#detailInfo").children("div").children('input:eq(4)').attr('value', data.birth_date);
                $("#detailInfo").children("div").children('input:eq(5)').attr('value', data.hobby);
            },
            error: function (error) {
                const resData = error.responseJSON.message;
                alert(JSON.stringify(resData));
                console.log(error);
            }
        });
    }
}


function userInfoHandler() {
    const sex = $("input[name=sex]:checked").val().replace(/(^\s*)|(\s*$)/g, '');
    let ssex;
    if (sex == 0) {
        ssex = '女';
    }
    else {
        ssex = '男';
    }
    const hobby = $("input[name=hobby]").val().replace(/(^\s*)|(\s*$)/g, '');
    const birthDate = $("input[name=birth_date]").val().replace(/(^\s*)|(\s*$)/g, '');
    if (birthDate !== '' && birthDate !== undefined) {
		if (!birthDate.match(/^[0-9]{4}-[0-9]{1,2}$/)) {
			$("input[name=birth_date]").focus();
			alert("出生年月格式应为YYYY-MM");
			return false;
		}
	}
    const token = localStorage.getItem('token');
    if (token == null) {
        alert('请先登录');
        window.location.href="homepage.html";
    }
    else {
        $.ajax(
            url + "api/revise_user_info", {
            method: 'POST',
            dataType: 'json',
            data: {
                token: token,
                sex: ssex,
                hobby: hobby,
                birth_date: birthDate
            },
            success: function(data) {
                // console.log(data);
                location.reload();
            },
            error: function (error) {
                const resData = error.responseJSON.message;
                alert(JSON.stringify(resData));
                console.log(error);
            }
        });
    }
}
