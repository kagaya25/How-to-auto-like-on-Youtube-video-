from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from apikey import apikey
# Step 1 : API key
# Step 2 : outh 2.0 name it  client_secret.json
# Step 3 : channelId to your youtube channels id 
# Step 4 : maxResults how many video you will likes 


class YoutubeBot:
    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', credentials=credentials)

    def getVids(self):
        ids = [] #stores the video ids
        youtube = build('youtube', 'v3', developerKey=apikey)
        channelId = "UCiBfuUreTbKvBKtQbb6SIWQ" # Step 3 : channelId to your youtube channels id
        maxResults = 20 # Step 4 : maxResults how many video you will likes 
        request = youtube.search().list(part="snippet",channelId=channelId,maxResults=maxResults,order="date",type="video")
        response = request.execute()
        for item in response['items']:
            print(item['snippet']['title'])
            ids.append((item['id']['videoId'], item['snippet']['channelId']))
        print(response)
        return ids
    def likeVids(self):
        ids = self.getVids()
        for videoId in ids:
            self.youtube.videos().rate(rating='like', id=videoId[0]).execute()
	
	
        
bot = YoutubeBot()
bot.likeVids()
