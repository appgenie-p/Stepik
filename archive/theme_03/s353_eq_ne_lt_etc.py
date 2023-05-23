from typing import List, Tuple, Union


class Track:
    Coords = Union[int, float]

    def __init__(self, start_x: Coords, start_y: Coords) -> None:
        self.start_x, self.start_y = start_x, start_y
        self.tracks: List["TrackLine"] = []

    def add_track(self, tr: "TrackLine") -> None:
        self.tracks.append(tr)

    def get_tracks(self) -> Tuple["TrackLine", ...]:
        return tuple(self.tracks)

    def __len__(self) -> int:
        len1 = (
            (self.start_x - self.tracks[0].to_x) ** 2
            + (self.start_y - self.tracks[0].to_y) ** 2
        ) ** 0.5

        return int(len1 + sum(self.__get_length(i) for i in range(1, len(self.tracks))))

    def __get_length(self, indx: int) -> int:
        return (
            (self.tracks[indx - 1].to_x - self.tracks[indx].to_x) ** 2
            + (self.tracks[indx - 1].to_y - self.tracks[indx].to_y) ** 2
        ) ** 0.5

    def __eq__(self, other) -> bool:
        return len(self) == len(other)

    def __lt__(self, other) -> bool:
        return len(self) < len(other)


class TrackLine:
    Coords = Union[int, float]

    def __init__(self, to_x: Coords, to_y: Coords, max_speed: int) -> None:
        self.to_x, self.to_y, self.max_speed = to_x, to_y, max_speed


track1, track2 = Track(0, 0), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
print(len(track1))
print(len(track2))
res_eq = track1 == track2
