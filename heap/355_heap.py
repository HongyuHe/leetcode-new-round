from collections import defaultdict
import heapq as hq

class Twitter:
    # Attemp 1: 29min
    def __init__(self):
        self.N_POSTS = 10
        # Tracking time
        self.ts = 0
        # subs: user id -> followers + itself
        self.subs = {}
        # posts: user id -> posts in chronological order
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.subs:
            self.subs[userId] = set([userId])
        self.ts += 1
        self.posts[userId].append((-self.ts, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        if userId not in self.subs:
            self.subs[userId] = set([userId])
            return self.posts[userId]
        feeds = []
        for fid in self.subs[userId]:
            feeds += self.posts[fid][-self.N_POSTS:]
        # O(logN)
        hq.heapify(feeds)
        # Get the 10 most recent
        feed = []
        for _ in range(self.N_POSTS):
            if not feeds:
                break
            feed.append(hq.heappop(feeds)[1])
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.subs:
            self.subs[followerId] = set([followerId])
        self.subs[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.subs:
            self.subs[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)