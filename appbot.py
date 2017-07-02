import requests, urllib
APP_ACCESS_TOKEN = '2280536012.dfab058.1e90d0f8b510437989565c370545926b'
BASE_URL = 'https://api.instagram.com/v1/'

def self_info():
    request_url= (BASE_URL + 'users/self/?access_token=%s')%(APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)

    user_info = requests.get(request_url).json()
    if user_info ['meta']['code']==200:
        if len(user_info['data']):
            print 'username %s'%(user_info['data']['username'])
            print 'followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'following: %s' % (user_info['data']['counts']['follows'])
            print 'posts: %s' % (user_info['data']['counts']['media'])
        else:
            print"user doesnt exist!"
    else:
        print "status other than 200 "
self_info()

def get_user_id(insta_username):

    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()

def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
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
insta_username = raw_input("Enter the username of the user: ")
get_user_info(insta_username)



def get_post_id(user_name):
    user_id = get_user_id(user_name)
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

def like_a_post(dimpleverma3830):
    media_id = get_post_id(dimpleverma3830)
    request_url = (BASE_URL + 'media/%s/likes')%(media_id)
    payload = {"access token": APP_ACCESS_TOKEN}
    print 'POST request url : %s'%(request_url)
    post_a_like = requests.post(request_url,payload).json()
    if post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'
