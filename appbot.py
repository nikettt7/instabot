def target_comments(insta_username):
    user_id= get_user_id(insta_username)

    if user_id == None:
        print "User does not exist!"
    request_url = (BASE_URL + '/users/%s/media/recent/?access_token=%s') %s(user_id,APP_ACCESS_TOKEN)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']['text']['']):
            for x in range(0, len(user_media['data']['text'])):
                caption= user_media['data'][x]['text']
                split_caption = caption.split(" ")
                if split_caption == '#fun' or '#adventure' or '#trip'
                    payload = {"access_token": APP_ACCESS_TOKEN, "text": "https://goo.gl/Hq4SVe"}
                    print 'POST request url : %s' % (request_url)
                    make_comment = requests.post(request_url, payload).json()
                    if make_comment['meta']['code'] == 200:
                        print 'comment has been posted successfully!'
                    else:
                        print 'Your comment was unsuccessful. please Try again!'
                else:
                    print "Not our markettable person"
        else:
            print"No caption exists!"
    else:
        print"meta code other than 200 recieved."
