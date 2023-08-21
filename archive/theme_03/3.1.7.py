class SmartPhone:
    def __init__(self, model) -> None:
        self.model = model
        self.apps = []

    def add_app(self, app):
        try:
            if next(i for i in self.apps if i.name == app.name):
                return
        except StopIteration:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    name = "ВКонтакте"


class AppYouTube:
    name = "YouTube"

    def __init__(self, memory_max) -> None:
        self.memory_max = memory_max


class AppPhone:
    name = "Phone"

    def __init__(self, contacts: dict) -> None:
        self.phone_list = []
        contacts_lst = contacts.items()
        self.phone_list.append(contacts_lst)


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
