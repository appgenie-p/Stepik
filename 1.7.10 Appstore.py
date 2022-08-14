class AppStore:
    apps: list = []

    @classmethod
    def add_application(cls, app: 'Application'):
        cls.apps.append(app)

    @classmethod
    def remove_application(cls, app: 'Application'):
        cls.apps.remove(app)

    @classmethod
    def block_application(cls, app: 'Application'):
        indx = cls.apps.index(app)
        if not indx:
            return False
        cls.apps[indx].blocked = True
        return True

    @classmethod
    def total_apps(cls):
        return len(cls.apps)


class Application:
    def __init__(self, name: str, blocked: bool = False) -> None:
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.block_application(app_youtube)
store.remove_application(app_youtube)
