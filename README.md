# Travel

高级软件测试实践作业一，“红色记忆”旅游网站。后端为 Flask REST API，前端未使用开发框架。[运行 Demo](http://www.jnugeek.cn/static/homepage.html) 已部署到服务器上。

## 小组成员
- Ying Cheng
- Tianyang Cheng
- Jia Tang
- Junxia Li
- Heng Ge
- Congyan Xia

## 功能列表
- 首页
- 登录页
- 注册页
- 景点页面
    - 景点介绍
    - 参观指南
    - 门票攻略
    - 专题巡展
- 红色记忆页面
- 游客留言页面
    - 登录之后发表留言
- 个人中心页面
    - 查看/修改个人信息
    - 绑定邮箱
    - 修改密码
    
## 运行代码
- 配置环境
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
- 数据库初始化
```
python manage.py db init
# 这时候会创建 app/migrations 文件夹
python manage.py db upgrade
# 这个时候应该能在 app 目录下看到 prod.sqlite 文件
```
- 启动服务器
```
python mange.py server
```
- 打开 fronted_v2/homepage.html
- 修改 app/config.py 里面的邮箱信息

## 运行截图
- 首页
![image](https://github.com/Patrickctyyx/Travel/blob/master/posts/homepage.png)
- 登录
![image](https://github.com/Patrickctyyx/Travel/blob/master/posts/login.png)
- 注册
![image](https://github.com/Patrickctyyx/Travel/blob/master/posts/register.png)
- 景点介绍
![image](https://github.com/Patrickctyyx/Travel/blob/master/posts/introduction.png)
- 参观指南
![image](https://github.com/Patrickctyyx/Travel/blob/master/posts/guidance.png)
- 红色记忆
![image](https://github.com/Patrickctyyx/Travel/blob/master/posts/red_memory.png)
- 留言板
![image](https://github.com/Patrickctyyx/Travel/blob/master/posts/discuss.png)
- 个人中心
![image](https://github.com/Patrickctyyx/Travel/blob/master/posts/personal_center.png)
