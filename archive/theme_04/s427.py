from typing import Protocol


class Video(Protocol):
    title: str
    descr: str
    path: str
    rating: "VideoRating"


class VideoItem(Video):
    def __init__(self, title: str, descr: str, path: str) -> None:
        self.title = title
        self.descr = descr
        self.path = path
        self.rating: VideoRating = self.get_rating()

    def get_rating(self):
        return rating_fabric(self)


def rating_fabric(video_item: Video):
    return VideoRatingImplementation(video_item, 0)


class VideoRating(Protocol):
    video: Video

    @property
    def rating(self) -> int:
        ...

    @rating.setter
    def rating(self, value: int) -> None:
        ...


class VideoRatingImplementation:
    def __init__(self, video: Video, rating: int) -> None:
        self.video = video
        self.__rating = rating

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, value: int) -> None:
        self._is_rating_in_range(value)
        self.__rating = value

    def _is_rating_in_range(self, value: int):
        if value not in range(1, 6):
            raise ValueError("Rating must be between 1 and 5")


v = VideoItem(
    "Курс по Python ООП",
    "Подробный курс по Python ООР",
    "D:/videos/python_oop.mp4",
)

print(v.rating.rating)  # 0
v.rating.rating = 5
print(v.rating.rating)  # 5
title = v.title
descr = v.descr
v.rating.rating = 6  # ValueError
