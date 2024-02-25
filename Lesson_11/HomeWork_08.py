import random
from abc import ABC, abstractmethod
from collections import Counter
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Post:
    message: str
    timestamp: str


class SocialChannel(ABC):
    def __init__(self, network: str, follower: int) -> None:
        self.network: str = network
        self.follower: int = follower

    @abstractmethod
    def make_a_post(self, message: str) -> None:
        pass


class Youtube(SocialChannel):
    def make_a_post(self, message: str, timestamp: str) -> None:
        print(
            f"This post for {self.network} (current number of subscribers: {self.follower}) has message '{message}', and it should be publish before {timestamp}"
        )


class Facebook(SocialChannel):
    def make_a_post(self, message: str, timestamp: str) -> None:
        print(
            f"This post for {self.network} (current number of subscribers: {self.follower}) has message '{message}', and it should be publish before {timestamp}"
        )


class Twitter(SocialChannel):
    def make_a_post(self, message: str, timestamp: str) -> None:
        print(
            f"This post for {self.network} (current number of subscribers: {self.follower}) has message '{message}', and it should be publish before {timestamp}"
        )


def post_a_message(channel: SocialChannel, message: str, timestamp: str):
    channel.make_a_post(message, timestamp)


def subscripe():
    number = random.randint(700, 5000)
    return number


def time():
    timestamp_lst = []
    for p in posts:
        date_time_str = p.timestamp
        date_time_obj = datetime.strptime(date_time_str, "%d/%m/%y %H:%M")
        ts_plan = datetime.timestamp(date_time_obj)
        timestamp_lst.append(int(ts_plan))

    c = Counter(timestamp_lst)
    mydict = c.values()

    if not all(x == 1 for x in list(mydict)):
        raise Exception("Only one publication per unit of time")
    else:
        return timestamp_lst


def process_schedule(posts: list[Post], channels: list[SocialChannel]):
    dt = datetime.now()
    ts_now = int(datetime.timestamp(dt))
    for i in posts:
        message, timestamp = i.message, i.timestamp
        for k in channels:
            for ts_inc in time():
                if (
                    ts_inc > ts_now
                    and posts.index(i) == channels.index(k)
                    and time().index(ts_inc) == channels.index(k)
                ):
                    post_a_message(k, message, timestamp)


post_1 = Post(message="Some materials for YouTube", timestamp="26/02/28 21:15")
post_2 = Post(message="Some materials for Facebook", timestamp="26/08/10 17:00")
post_3 = Post(message="Some materials for Twitter", timestamp="15/02/21 01:55")

result_1 = Youtube(network="youtube", follower=subscripe())
result_2 = Facebook(network="facebook", follower=subscripe())
result_3 = Twitter(network="twitter", follower=subscripe())

posts = [post_1, post_2, post_3]
channels = [result_1, result_2, result_3]

process_schedule(posts=posts, channels=channels)
