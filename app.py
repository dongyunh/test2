from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests


app = Flask(__name__)

client = MongoClient('localhost', 27017)
# client = MongoClient('13.125.245.197', 27017, username="test", password="test")
db = client.dbsparta_week1_project


@app.route('/')
def main():
    # DB에서 저장된 포스트 '좋아요'순으로 보여주기
    return render_template("index.html")


@app.route('/posts')
def posts():
    return render_template("posts.html")


@app.route('/api/save_post', methods=['POST'])
def save_post():
    # 게시글 저장하기
    img_url_receive = request.form['img_url_give']
    nickname_receive = request.form['nickname_give']
    title_receive = request.form['title_give']
    address_receive = request.form['address_give']
    review_receive = request.form['review_give']
    doc = {
           "img_url": img_url_receive,
           "nickname": nickname_receive,
           "title": title_receive,
           "address": address_receive,
           "review": review_receive
           }
    db.posts.insert_one(doc)
    return jsonify({'result': 'success', 'msg': f'{nickname_receive}님 저장!'})


@app.route('/api/delete_post', methods=['POST'])
def delete_post():
    # 게시글 삭제하기
    return jsonify({'result': 'success', 'msg': '게시글 삭제!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)