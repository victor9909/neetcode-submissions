import heapq

class Twitter:

    def __init__(self):
        self.follows = {}
        self.posts = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []

        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):
        users = set()

        if userId in self.follows:
            users = self.follows[userId]

        users.add(userId)

        heap = []

        for user in users:
            if user in self.posts:
                for time, tweetId in self.posts[user]:
                    heapq.heappush(heap, (time, tweetId))

                    if len(heap) > 10:
                        heapq.heappop(heap)

        return [tweetId for time, tweetId in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)