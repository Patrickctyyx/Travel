const url = "http://localhost:5000/";


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
