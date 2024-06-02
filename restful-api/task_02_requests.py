#!/usr/bin/python3
import requests
import json


def fetch_and_print_posts():
    """Def functions to fetch and print"""
    request = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status code: {}".format(request.status_code))

    if request.status_code == 200:
        posts = request.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Function to fetch and save posts"""
    request = request.get("https://jsonplaceholder.typicode.com/posts")
    
    if request.status_code == 200:
        posts = request.json()
        post_list = [{"id": post['id'], 'title': post['title'],
            'body': post['body']} for post in posts]
        csv_file = 'posts.csv'
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DicWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(post_list)
