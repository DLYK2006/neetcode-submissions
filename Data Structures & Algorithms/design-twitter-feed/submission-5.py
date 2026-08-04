from collections import defaultdict

class Twitter:

    def __init__(self):
        self.posts=defaultdict(list)
        self.following=defaultdict(set)
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        self.posts[userId].append((self.count,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets=[]
        users=list(set([userId]+list(self.following[userId])))
        for i in users:
            tweets+=self.posts[i]
        tweets.sort(reverse=True)
        return [tid for count, tid in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
