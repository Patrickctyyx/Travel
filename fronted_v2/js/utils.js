function registerHandler(){
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
            "http://localhost:5000/api/register", {
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
                console.log(data);
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