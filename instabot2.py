import requests, urllib
#  access token owner : md.pup
#   sandbox users : kajalangural , dimpleverma3803

# For Sentiment Analysis the library TextBlob is used
from textblob import TextBlob
# imported the classifier for sentiment analysis
from textblob.sentiments import NaiveBayesAnalyzer

# App access token is imported from key file
from client_id import APP_ACCESS_TOKEN
from termcolor import colored,cprint
import colorama
from termcolor import *



# BASE URL in global variable
BASE_URL = 'https://api.instagram.com/v1/'


# Function declaration to get your own info
def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % APP_ACCESS_TOKEN

    # this will print the request url
    print 'GET request url : %s' % request_url

    # .json is used while handling json data .it act as a json decoder.
    user_info = requests.get(request_url).json()


    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'


# Function declaration to get the ID of a user by username

def get_user_id(insta_username):
    request_url = (BASE_URL + 'user''s/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    user_info = requests.get(request_url).json()


    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()


# Function declaration to get the info of a user by username

def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % request_url
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):


            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'


#function to own's recent post
def get_own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % APP_ACCESS_TOKEN
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print('Your image has been downloaded!', 'blue')
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


# function to get user recent post id
def get_user_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s' % (user_id, APP_ACCESS_TOKEN))
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            # image is saved in a variable image_name
            image_name = user_media['data'][0]['id'] + '.jpeg'
            # url of the image is provided to be downloaded
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            # urllib is used to fetch data across world wide web .

            urllib.urlretrieve(image_url, image_name)
            print('user image has been downloaded!', 'blue')
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'


# get_post_id function to get media id to add like or comment
def get_post_id(insta_username):

    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()

# function to get the recent media liked by the user
def recent_media_liked():
    request_url = (BASE_URL + 'users/self/media/liked?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    liked_post = requests.get(request_url).json()
    if liked_post['meta']['code'] == 200:
        if len(liked_post['data']):
            image_name = liked_post['data'][0]['id'] + '.jpeg'
            image_url = liked_post['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'image has been downloaded'
        else:
            print('no post liked')
    else:
        print('status code error')


# let us create a function to like a post on instagram
def like_a_post(insta_username):
    # HERE WE ARE CALLING GET_POST_ID FUNCTION
    # SO AS TO GET POST ON WHICH WE CAN ADD LIKE
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)

    #  Access Token is sent in payload to authenticate the like that we're making.
    # payload act as a data handler  from where data is passed
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like has been made successfully!'
    else:
        print 'Your like was unsuccessful.please Try again!'


# function declaration to get list of likes on a media
def list_of_likes(insta_username):
    # here we are fetching media id from which we will get like list
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'get request url : %s' % request_url
    likes_info = requests.get(request_url).json()
    if likes_info['meta']['code'] == 200:
        if len(likes_info['data']):
            for x in range(0, len(likes_info['data'])):
                print likes_info['data'][x]['username']
        else:
            print 'no existing like'
    else:
        print 'status code error'


# function declaration to post a comment on user media
def comment_on_post(insta_username):
    media_id = get_post_id(insta_username)

    # here we are entering the comment we waant to postt by using RAW_INPUT
    comment_text = raw_input('enter your comment : ')
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)

    # while adding a comment payload will consist of access token and text we want to enter
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    print 'POST request url : %s' % (request_url)
    make_comment = requests.post(request_url, payload).json()
    if make_comment['meta']['code'] == 200:
        print 'comment has been posted successfully!'
    else:
        print 'Your comment was unsuccessful. please Try again!'


# function declaration to get list of comments on a media
def list_of_comments(insta_username):
    # here we are fetching media id from which we will get comment list
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'get request url : %s' % request_url
    comment_info = requests.get(request_url).json()
    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            for x in range(0, len(comment_info['data'])):
                print comment_info['data'][x]['text']
        else:
            print 'no existing comment'
    else:
        print 'status code error'


# function to delete negative comments on recent posts
def delete_negative_comment(insta_username):
    # here we are  calling get post id function
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):

            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())

                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    # url is passed and saved which is used for deleting a comment from post
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (
                        media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()
                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'


# function to fetch users any post
def get_media_of_your_choice(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'user does not exist'
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):

            post_number = raw_input("enter no of post which you want : ")
            post_number = int(post_number)

            x = post_number - 1
            image_name = user_media['data'][x]['id'] + '.jpeg'
            image_url = user_media['data'][x]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print'user media does not exist'
    else:
        print 'status code error'

def target_comments(insta_username): #takes argument as insta username
    user_id = get_user_id(insta_username)    #url of tags has been used
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    caption_info = requests.get(request_url).json()

    if caption_info['meta']['code'] == 200:

        if len(caption_info['data']):

            for y in range(0, len(caption_info['data'])):

                caption_text = str(caption_info['data'][y]['caption'])
                caption = caption_text.split(" ")
                if "Park" in caption:
                    print 'Read Caption: %s' % (caption)
                    media_id = get_post_id(insta_username)
                    comment_text = "Get more exciting offers at"
                    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
                    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
                    print 'POST request url : %s' % (request_url)

                    make_comment = requests.post(request_url, payload).json()

                    if make_comment['meta']['code'] == 200:
                        print "Successfully Posted Targetted Comment!"
                    else:
                        print "Unable to add comment. Try again!"
                else:
                    print 'There is no caption on the post!'

        else:

            print 'Status code other than 200 received!'
    exit()


def main_function():#main function which will start

    while True:
        print '\n'
        colorama.init()
        # cprint is used for colored printing of a string
        cprint( 'Hello! Welcome to instaBot!\n', 'blue')
        cprint('You have following options: \n', 'red')
        print "a.Get your own details.\n"
        print "b.Get details of a user by username.\n"
        print "c.Get your own post.\n"
        print "d.Get users recent post.\n"
        print "e.Like user recent post.\n"
        print "f.get list of likes on post\n"
        print "g.Comment on user recent post.\n "
        print "h.get list of comments on post\n"
        print "i.get the recent media liked by the user.\n "
        print "j.Delete negative comment.\n "
        print "k.get post of yor choice.\n"
        print "l.Do some Marketing\n "
        print "m.Exit\n"
        choice = raw_input("Enter you choice: ")
        if choice == "a":
            self_info()

        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "c":
            get_own_post()
            print get_own_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice == 'e':
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice == 'f':
            insta_username = raw_input('enter username : ')
            list_of_likes(insta_username)
        elif choice == 'g':
            insta_username = raw_input("Enter the username of the user: ")
            comment_on_post(insta_username)
        elif choice == 'h':
            insta_username = raw_input('enter username : ')
            list_of_comments(insta_username)
        elif choice == 'i':
            recent_media_liked()
        elif choice == 'j':
            insta_username = raw_input("Enter the username of the user: ")
            delete_negative_comment(insta_username)
        elif choice == 'k':
            insta_username = raw_input("enter username of the user : ")
            get_media_of_your_choice(insta_username)
        elif choice == 'l':
            insta_username = raw_input("Enter the username: \n")
            target_comments(insta_username)
        elif choice == 'm':
            exit()
        else:
            cprint("wrong choice", 'green')


main_function() #finally executing