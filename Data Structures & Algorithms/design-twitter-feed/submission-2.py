from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.count=0
        self.tweetMap=defaultdict(list)
        self.followMap=defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        self.tweetMap[userId].append([self.count,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        result=[]
        heap=[]
        post=[]
        count=0
        tweetId=0
        counter=10
        index=0
        following=set(self.followMap[userId])
        following.add(userId)
        for i in following:
            tweets=self.tweetMap[i]
            if tweets:
                index=len(tweets)-1
                count,tweetId=tweets[-1]
                heapq.heappush(heap,(-count,tweetId,index,tweets))
        
        while counter!=0 and heap:
            post=list(heapq.heappop(heap))
            prevCount=0
            prevTweetId=0
            grah=[]
            result.append(post[1])
            if(post[2]>0):
                grah=post[3]
                prevCount,prevTweetId=grah[post[2]-1]
                heapq.heappush(heap,(-prevCount,prevTweetId,post[2]-1,grah))
            counter-=1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
