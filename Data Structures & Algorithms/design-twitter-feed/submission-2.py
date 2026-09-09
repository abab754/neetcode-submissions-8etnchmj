
import time
class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-time.time(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follows[userId]
        users.add(userId)
        heap = []
        for user in users:
            for tweet in self.tweets[user]:
                heapq.heappush(heap, tweet)
        res = []
        while heap and len(res) < 10:
            t, tweet = heapq.heappop(heap)
            print(t, tweet)
            res.append(tweet)        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
