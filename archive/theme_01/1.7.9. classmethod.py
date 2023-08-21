from typing import List


class Video:
    def __init__(self, name: str) -> None:
        self.create(name)

    def create(self, name: str) -> None:
        """для задания имени name текущего видео (метод сохраняет имя name в
        локальном атрибуте name объекта класса Video)
        """
        self.name = name

    def play(self) -> None:
        """для воспроизведения видео (метод выводит на экран строку
        "воспроизведение видео <name>").
        """
        print(f"воспроизведение видео {self.name}")


class YouTube:
    """Метод play() класса YouTube должен обращаться к объекту класса Video
    по индексу списка videos и, затем, вызывать метод play() класса Video.

    Методы add_video и play вызывайте напрямую из класса YouTube. Создавать
    экземпляр этого класса не нужно.
    """

    videos: List[Video] = []

    @classmethod
    def add_video(cls, video: Video) -> None:
        """для добавления нового видео (метод помещает объект video класса
        Video в список);
        """
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx: int) -> None:
        """для проигрывания видео из списка по указанному индексу (индексация
        с нуля).
        """
        cls.videos[video_indx].play()


"""
Создайте два объекта v1 и v2 класса Video, затем, через метод create()
передайте им имена "Python" и "Python ООП".
После этого с помощью метода
add_video класса YouTube, добавьте в него эти два видео и воспроизведите
(с помощью метода play класса YouTube) сначала первое, а затем, второе видео.
"""
v1 = Video("Python")
v2 = Video("Python ООП")
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)
