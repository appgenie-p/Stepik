from typing import Tuple, Union

CURRENT_OS = 'windows'  # 'windows', 'linux'

FileExts = Tuple[str, ...]


class WindowsFileDialog:
    def __init__(self, title: str, path: str, exts: FileExts):
        self.__title = title
        self.__path = path
        self.__exts = exts


class LinuxFileDialog:
    def __init__(self, title: str, path: str, exts: FileExts):
        self.__title = title
        self.__path = path
        self.__exts = exts


class FileDialogFactory:
    def __new__(
        cls, *args: ..., **kwargs: ...
    ) -> Union[WindowsFileDialog, LinuxFileDialog]:
        file_dialogs = {'windows': WindowsFileDialog, 'linux': LinuxFileDialog}
        instance = super().__new__(file_dialogs[CURRENT_OS])
        instance.__init__(*args, **kwargs)
        return instance
