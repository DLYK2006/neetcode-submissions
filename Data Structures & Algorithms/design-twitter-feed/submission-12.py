from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.following=defaultdict(set)
        self.posts=defaultdict(list)
        self.count=0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count+=1
        self.posts[userId].append([self.count,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        users=list(set([userId]+list(self.following[userId])))
        for i in users:
            if self.posts[i]:
                count,tid=self.posts[i][-1]
                index=len(self.posts[i])-1
                heapq.heappush(heap,(-count,tid,i,index))
        result=[]
        while heap and len(result)<10:
            count,tid,i,index=heapq.heappop(heap)
            result.append(tid)
            if index>0:
                p_count,p_id=self.posts[i][index-1]
                heapq.heappush(heap,(-p_count,p_id,i,index-1))
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
