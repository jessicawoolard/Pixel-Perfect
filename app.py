import csv

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    # 1. Open the post html and get the contents as a string
    post_file = open('post.html', 'r')
    post_html = post_file.read()
    post_file.close()

    # 2. Create a new list that will hold all the html for your blog posts
    blog_posts = []

    # 3. Open the csv file and read it using the CSV library. This will give you a list of rows.
        # See: https://docs.python.org/3/library/csv.html#csv.DictReader
    with open("data.csv", newline="") as cvsfile:
        reader = csv.DictReader(cvsfile)

        # 4. Loop over each row in the CSV. Each row is a blog post.
        for row in reader:
            current_post_html = post_html
            # 4. Loop over each row in the CSV. Each row is a blog post.
            current_post_html = current_post_html.replace("{{category}}", row['category'])
            current_post_html = current_post_html.replace("{{title}}", row['title'])
            current_post_html = current_post_html.replace("{{body}}", row['body'])
            current_post_html = current_post_html.replace("{{author}}", row['author'])
            current_post_html = current_post_html.replace("{{date}}", row['date'])
            current_post_html = current_post_html.replace("{{image}}", row['image'])


    # 6. Add the post_html to the new list you created above.

            blog_posts.append(current_post_html)

    # 7. Join all the items in your new list together into a single string. Name this string "blog_post_html".
    blog_posts_html = "".join(blog_posts)
    # 8. Open the index.html file and replace {{blog_posts}} with the blog post string you just created.
    index_file = open('index.html', 'r')
    index_html = index_file.read()

    index_html = index_html.replace('{{blog_posts}}', blog_posts_html)

    index_file.close()

    return index_html
