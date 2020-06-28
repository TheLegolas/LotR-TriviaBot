from apiclient.discovery import build

class GoogleClient():
    def __init__(self, config, credentials):
        self.config = config
        self.credentials = credentials
        self.youtube = build('youtube', 'v3', developerKey=credentials[0])

    def get_video_from_channel(self, channel_id, query, maxResults):
        request = self.youtube.search().list(q=query, channelId=channel_id, part='snippet', type='video', maxResults=maxResults)
        return request.execute()
    
    def get_video_info(self, video_id):
        request = self.youtube.videos().list(part="snippet", id=video_id)
        return request.execute()
