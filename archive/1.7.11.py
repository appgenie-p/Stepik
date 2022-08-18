class Viber:
    MSGS: list = []

    @classmethod
    def add_message(cls, msg: 'Message') -> None:
        cls.MSGS.append(msg)

    @classmethod
    def remove_message(cls, msg: 'Message') -> None:
        try:
            cls.MSGS.remove(msg)
        except ValueError:
            print('There is no such a message')

    @classmethod
    def set_like(cls, msg: 'Message') -> None:
        try:
            indx = cls.MSGS.index(msg)
        except ValueError:
            print('There is no such a message')
        cls.MSGS[indx].fl_like = not cls.MSGS[indx].fl_like

    @classmethod
    def show_last_message(cls, number):
        last_msgs = cls.MSGS[-number:]
        all(print(msg) for msg in last_msgs)

    @classmethod
    def total_messages(cls):
        return len(cls.MSGS)


class Message:
    def __init__(self, text: str, fl_like: bool = False) -> None:
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)
