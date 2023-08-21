from typing import Any


class Router:
    def __init__(self) -> None:
        self.buffer: list["Data"] = []
        self.linked_servers: list["Server"] = []

    def link(self, server: "Server"):
        self.linked_servers.append(server)

    def unlink(self, server: "Server"):
        self.linked_servers.remove(server)

    def send_data(self):
        """Find ip in added server list and send data to the server"""
        for data in self.buffer:
            for server in self.linked_servers:
                if data.ip == server.ip:
                    server.buffer.append(data)
                    break
        self.buffer.clear()


class Server:
    counter: int = 0

    def __new__(cls, *args, **kwargs):
        """Create new server instance with unique ID"""
        instance = super().__new__(cls)
        instance.ip: int = cls.counter
        cls.counter += 1
        return instance

    def __init__(self) -> None:
        self.buffer: list["Data"] = []

    def send_data(self, data: "Data") -> None:
        router.buffer.append(data)

    def get_data(self) -> list["Data"] | list[Any]:
        packets_received = self.buffer[:]
        self.buffer.clear()
        return packets_received

    def get_ip(self) -> int:
        return self.ip


class Data:
    def __init__(self, data: str, ip: int) -> None:
        self.data = data
        self.ip = ip  # IP-адрес назначения

    def __str__(self) -> str:
        return f"{self.data}"


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
