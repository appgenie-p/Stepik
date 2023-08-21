import sys


class MailItem:
    def __init__(self, mail_from: str, title: str, content: str) -> None:
        self.mail_from, self.title, self.content = mail_from, title, content
        self.is_read = False

    def set_read(self, fl_read: bool) -> None:
        self.is_read = fl_read

    def __bool__(self) -> bool:
        return self.is_read


class MailBox:
    def __init__(self) -> None:
        self.inbox_list: list = []

    def receive(self) -> None:
        # lst_in = list(map(str.strip, sys.stdin.readlines()))
        lst_in = [
            "sc_lib@list.ru; От Балакирева; Успехов в IT!",
            "mail@list.ru; Выгодное предложение; Вам одобрен кредит.",
            "Python ООП; Балакирев С.М.; 2022",
            "mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.",
        ]
        for item in lst_in:
            self.inbox_list.append(MailItem(*item.split(";")))


mail = MailBox()
mail.receive()

# Get first and last elements of mail.inbox_list and set them as read
# by using list slicing. Slise first and last elements of list with step equal to
# list length minus 1 (4-1=3 in the case). Then set them as read.
for i in mail.inbox_list[:: len(mail.inbox_list) - 1]:
    i.set_read(True)

inbox_list_filtered = list(filter(bool, mail.inbox_list))
