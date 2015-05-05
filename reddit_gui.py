import requests
import json
import time
from Tkinter import *


def get_sub(subreddit):
    url = "http://www.reddit.com/r/%s/hot/.json" % subreddit
    headers = {'User-Agent': "API Testing Project 0.2"}
    r = requests.get(url, headers=headers)
    json_data = json.loads(r.text)
    return json_data


def get_posts(sub_data):

    all_posts = []

    for item in sub_data['data']['children']:

        post_spacer = "-------------------------------------------"
        post_title = "Title: %s" % (item['data']['title'])
        post_author = "Author: %s" % (item['data']['author'])
        post_upvotes = "UpVotes: %i" % (item['data']['ups'])
        post_url = "URL: %s" % (item['data']['url'])
        posted_epoch_time = int(item['data']['created'])
        posted_date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(posted_epoch_time))
        post_posted = "Posted: %s" % posted_date_time

        post_data = "%s\n%s\n%s\n%s\n%s\n%s\n" % (post_spacer, post_title, post_author, post_upvotes, post_url, post_posted)

        all_posts.append(post_data)

    return all_posts


#def main():
#    user_input = top_frame_entry.get()
#    data = get_posts(get_sub(user_input))
#    text_frame.insert(END, data)

def main():
    user_input = top_frame_entry.get()
    for post in get_posts(get_sub(user_input)):
        text_frame.insert(END, post)

root_window = Tk()
root_window.title("Reddit App")
root_window.geometry("800x500")

top_frame = Frame(root_window)
top_frame.pack(side=TOP)
top_frame_title = Label(top_frame, text="Which Subreddit would you like to list?")
top_frame_title.pack()
top_frame_entry = Entry(top_frame)
top_frame_entry.pack()

get_posts_button = Button(top_frame, text="Get posts!", command=main)
get_posts_button.pack()

bottom_frame = Frame(root_window)
bottom_frame.pack(side=BOTTOM)
bottom_frame_title = Label(bottom_frame, text="Top 25 hot stories")
bottom_frame_title.pack()
bottom_frame_content = Label(bottom_frame)

text_frame = Text(bottom_frame)
text_frame.pack()


root_window.mainloop()