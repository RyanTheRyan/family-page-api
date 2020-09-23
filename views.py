from flask import Blueprint, jsonify, request
from . import db
from .models import Blog, Announcement, User
import bcrypt

main = Blueprint('main', __name__)

@main.route('/new_blog', methods=['POST'])
def add_blog():
    blog_data = request.get_json()

    new_blog = Blog(title=blog_data['title'], banner_image_url=blog_data['banner_image_url'], content=blog_data['content'], status=blog_data['status'], published_date=blog_data['published_date'])

    db.session.add(new_blog)
    db.session.commit()

    return 'Done', 201

@main.route('/blogs', methods=['GET'])
def blogs():
    blog_list = Blog.query.all()
    blogs = []

    for blog in blog_list:
        blogs.append({'title' : blog.title, 'banner_image_url' : blog.banner_image_url, 'content' : blog.content, 'status' : blog.status, 'published_date' : blog.published_date})

    return jsonify({'blog posts' : blogs})

@main.route('/create-announcment', methods=['POST'])
def add_announcment():
    announcement_data = request.get_json()

    if announcement_data == None:
        new_announcement = Announcement(title=announcement_data['title'], content=announcement_data['content'])
        print(new_announcement)

        db.session.add(new_announcement)
        db.session.commit()
    else:
        alldata = Announcement.query.all()

        for a in alldata:
            db.session.delete(a)

            new_announcement = Announcement(title=announcement_data['title'], content=announcement_data['content'])

            db.session.add(new_announcement)
            db.session.commit()
    return 'Done', 201

@main.route('/announcment')
def announcment():
    announcement_list = Announcement.query.all()
    print(announcement_list)
    announcement_item = []

    for announcement in announcement_list:
        announcement_item.append({'title' : announcement.title, 'content' : announcement.content})

    return jsonify("announcement" : announcement_item)

# @main.route('/register_user', methods=['POST'])
# def user():
#     user_data = request.get_json()

#     password = user_data['password']
#     hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(10))

#     new_user = User(username=user_data['username'], name=user_data['name'], password=f'{hashed}')

#     db.session.add(new_user)
#     db.session.commit()

#     return 'Done', 201

# @main.route('/users')
# def users():
#     user_list = User.query.all()
#     users = []

#     for user in user_list:
#         users.append({'title' : user.username, 'name' : user.name, 'password' : user.password})

#     return jsonify({'announcments' : users})