import requests
import datetime
# import schedule
# import time

#       for the meme
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 \
    Safari/537.36'

URL = 'https://api.imgflip.com/caption_image'

d1 = datetime.date.today() + datetime.timedelta(days=1)
d2 = d1.strftime("%a %d %B")
params = {
    'username': '065AH',
    'password': '0passBOToto',
    'template_id': '25901141',
    'font': 'courier',
    'text0': f'tomorrow is {d2}',
    'text1': ''
}

#       for the fb post
token = 'your token here'
pageID = 'your page ID here'
msg = ''


def log(text):
    with open('log.txt', 'a') as f:
        # f.write(datetime.date.today())
        f.write(str(text))


def postingdaily():

    imgflip = requests.request('POST', URL, params=params).json()

    log(
        f'\n----{datetime.date.today()}---- \nimgflip response : \n{imgflip}')

    url = imgflip['data']['url']

    fb_post = requests.post(
        f"https://graph.facebook.com/{pageID}/photos?url={url}&message={msg}&access_token={token}")

    log(f'\nfacebook response : \n{fb_post.json()}\n --------')



# # schedule.every(24).hours.do(postingdaily)
# schedule.every().day.at("12:17").do(postingdaily)

# while True:
#     schedule.run_pending()
#     time.sleep(10)

postingdaily() #I only kept this function because the
#server I hosted this script on had their own schedule system to minimize cpu usage 
#basically I was free plan