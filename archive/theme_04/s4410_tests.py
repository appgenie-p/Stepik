import s4410
from s4410 import FileDialogFactory, LinuxFileDialog, WindowsFileDialog


def test_windows_factory() -> None:
    fial_dialog = FileDialogFactory(
        "Изображения", "d:/images/", ("jpg", "gif", "bmp", "png")
    )
    assert isinstance(fial_dialog, WindowsFileDialog)


def test_linux_factory() -> None:
    s4410.CURRENT_OS = "linux"
    fial_dialog = FileDialogFactory(
        "Изображения", "d:/images/", ("jpg", "gif", "bmp", "png")
    )
    assert isinstance(fial_dialog, LinuxFileDialog)
