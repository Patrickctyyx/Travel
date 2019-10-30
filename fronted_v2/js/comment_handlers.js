const url_comment = "http://139.155.89.156/";


function commentPostHandler() {
    const content = $('#commentContent').val().replace(/(^\s*)|(\s*$)/g, '');
    if (content == '' || content == null) {
        alert('评论不能为空');
        return
    }
    const token = localStorage.getItem('token');
    if (token == null) {
        alert('请登录以发表评论');
        localStorage.clear();
        parent.location.href="userLogin.html";
    }
    else {
        $.ajax(
            url_comment + "api/comment", {
            method: 'POST',
            dataType: 'json',
            data: {
                token: token,
                content: content
            },
            success: function(data) {
                alert('评论成功');
                window.location.reload();
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


function commentGetHandler() {
    
}
