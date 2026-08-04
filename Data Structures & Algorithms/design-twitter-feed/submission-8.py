from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.posts=defaultdict(list)
        self.following=defaultdict(set)
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        self.posts[userId].append((self.count,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result=[]
        heap=[]
        users=list(set([userId]+list(self.following[userId])))
        for i in users:
            tweets=self.posts[i]
            if tweets:
                index=len(tweets)-1
                count,tweetId=tweets[index]
                heapq.heappush(heap,(-count,tweetId,i,index))
        while heap and len(result)<10:
            negCount,tweetId,userId,index=heapq.heappop(heap)
            result.append(tweetId)
            if index>0:
                newIndex=index-1
                count,tid=self.posts[userId][newIndex]
                heapq.heappush(heap,(-count,tid,userId,newIndex))
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
