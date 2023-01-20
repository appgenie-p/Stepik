import sys


class MailItem:
    # item = MailItem(mail_from, title, content)
    def __init__(self, mail_from: str, title: str, content: str) -> None:
        self.mail_from, self.title, self.content = mail_from, title, content
        self.is_read = False

    def set_read(self, fl_read: bool) -> None:
        self.is_read = fl_read

    def __bool__(self) -> bool:
        return self.is_read


class MailBox:
    def __init__(self) -> None:
        # список из принятых писем
        self.inbox_list: list = []

    def receive(self) -> None:
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        # lst_in = [
        #     'sc_lib@list.ru; От Балакирева; Успехов в IT!',
        #     'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
        #     'Python ООП; Балакирев С.М.; 2022',
        #     'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.'
        # ]
        # iterrate over list ->
        for item in lst_in:
            # each item separate on 3 parts "от кого; заголовок; текст письма" ->
            parts = item.split(';')
            # and create MailItem object ->
            obj = MailItem(*parts)
            # append this object to self.inbox_list
            self.inbox_list.append(obj)
            

mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
# Сформируйте в программе список (глобальный) с именем inbox_list_filtered.
# В этот список поместите только те письма, которые прочитаны.
# Используя стандартную функцию filter() совместно с функцией bool() языка Python.
inbox_list_filtered = list(filter(bool, mail.inbox_list))