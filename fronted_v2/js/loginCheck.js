function registcheck() {
	var sname = $("form").find("input[name=name]").val().replace(/(^\s*)|(\s*$)/g, '');
	var spwd = $("form").find("input[name=pwd]").val().replace(/(^\s*)|(\s*$)/g, '');
	var srepwd = $("form").find("input[name=repwd]").val().replace(/(^\s*)|(\s*$)/g, '');
	var birthDate = $("form").find("input[name=day]").val().replace(/(^\s*)|(\s*$)/g, '');
	if (sname == '' || sname == undefined || sname == null) {
		$("#name").css("display","inline-block");
		$("form").find("input[name=name]").focus();
		return false;
	}else{
		$("#name").css("display","none");
	}
	if (spwd == '' || spwd == undefined || spwd == null) {
		$("#pwd").css("display","inline-block");
		$("form").find("input[name=pwd]").focus();
		return false;
	}else if(!spwd.match(/^[a-zA-Z0-9\.\_]{9,16}$/)){
		$("#pwd").css("display","inline-block");
		$("#pwd").html("密码格式不正确");
		$("form").find("input[name=pwd]").focus();
		return false;
	}else{
		$("#pwd").css("display","none");
	}
	if (srepwd != spwd) {
		$("#repwd").css("display","inline-block");
		$("form").find("input[name=repwd]").focus();
		return false;
	}else{
		$("#repwd").css("display","none");
	}
	if (birthDate != '' && birthDate != undefined && birthDate != null) {
		if (!birthDate.match(/^[0-9]{4}-[0-9]{1,2}$/)) {
			$("#day").css("display","inline-block");
			$("form").find("input[name=day]").focus();
			return false;
		}
	}
	return true;
}

function logincheck() {
	var sname = $("form").find("input[name=username]").val().replace(/(^\s*)|(\s*$)/g, '');
	var spwd = $("form").find("input[name=password]").val().replace(/(^\s*)|(\s*$)/g, '');
	if (sname == '' || sname == undefined || sname == null) {
		$("form").find("input[name=username]").focus();
		return false;
	}
	if (spwd == '' || spwd == undefined || spwd == null) {
		$("form").find("input[name=password]").focus();
		return false;
	}

	return true;
}