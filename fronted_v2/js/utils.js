const url = "http://139.155.89.156/";

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


function checkEmail(email) {
    if (email == '' || email == null) {
        alert('邮箱不能为空');
        return false
    }
    const regex = /^\w+((.\w+)|(-\w+))@[A-Za-z0-9]+((.|-)[A-Za-z0-9]+).[A-Za-z0-9]+$/;
    return email.match(regex)
}


function checkBirthDate(birthDate) {
    return birthDate.match(/^[0-9]{4}-[0-9]{1,2}$/)
}


function checkPassword(password) {
    return password.match(/^[a-zA-Z0-9\.\_]{9,16}$/)
}

