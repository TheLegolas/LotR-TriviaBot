import praw

class RedditClient():
    '''
    Reddit Client for fetching memes.
    '''
    def __init__(self, info, meme_log):
        self.meme_log = meme_log
        client_id, client_secret, username, password = info
        self.reddit = praw.Reddit(client_id=client_id,
                                  client_secret=client_secret,
                                  password=password,
                                  user_agent='reddit post yoinker by /u/_LegolasGreenleaf',
                                  username=username)

    def get_meme(self, server, subreddit):
        '''
        finds unseen meme for the given server
        '''
        if server.id in self.meme_log.keys():
            used_ids = self.meme_log[server.id]
        else:
            used_ids = []

        meme = ''
        step = 5
        limit = 0
        while not meme:
            limit += step
            for submission in list(self.reddit.subreddit(subreddit).hot(limit=limit))[limit-step:]:
                if submission.id in used_ids:
                    continue
                meme = submission
                used_ids.append(submission.id)
                break

        self.meme_log[server.id] = used_ids
        return meme
