from flask import Flask, Blueprint, jsonify, request
from . import db
from .models import Blog, Announcement

main = Blueprint('main', __name__)

@main.route('/new-blog', methods=['POST'])
def add_blog():
    blog_data = request.get_json()

    new_id = Blog.query.all()

    new_blog = Blog(title=blog_data['title'], banner_image_url=blog_data['banner_image_url'], content=blog_data['content'], status=blog_data['status'], published_date=blog_data['published_date'])

    db.session.add(new_blog)
    db.session.commit()

    return 'Done', 201

@main.route('/delete-blogs', methods=['DELETE'])
def delete_blogs():
    all_blogs = Blog.query.all()

    for blog in all_blogs:
        db.session.delete(blog)
        db.session.commit()
    return "Done"


@main.route('/blogs', methods=['GET'])
def blogs():
    blog_list = Blog.query.all()
    blogs = []

    for blog in blog_list:
        blogs.append({'title' : blog.title, 'banner_image_url' : blog.banner_image_url, 'content' : blog.content, 'status' : blog.status, 'published_date' : blog.published_date})

    return jsonify({'blog posts' : blogs})

@main.route('/new-announcement', methods=['POST'])
def new_announcement():

    old_announcement_data = Announcement.query.all()

    announcement_data = request.get_json()

    for old_announcement in old_announcement_data:
        db.session.delete(old_announcement)
        db.session.commit()

    add_announcement = Announcement(title=announcement_data['title'], content=announcement_data['content'])

    db.session.add(add_announcement)
    db.session.commit()

    return "done", 201

@main.route('/announcement', methods=['GET'])
def get_announcment():
    announcement_item = Announcement.query.all()

    announcements = []

    for announcement in announcement_item:
        announcements.append({'title' : announcement.title, 'content' : announcement.content})

    return jsonify({'announcement' : announcements})

    if __name__ == '__main__':
        main.run()