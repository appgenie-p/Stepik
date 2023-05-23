class FileAcceptor:
    def __init__(self, *exts: str):
        self.__exts = exts

    def __call__(self, filename: str) -> bool:
        return filename.endswith(self.__exts)

    def __add__(self, other: "FileAcceptor") -> "FileAcceptor":
        return FileAcceptor(*(self.__exts + other.__exts))


filenames = [
    "boat.jpg",
    "ans.web.png",
    "text.txt",
    "www.python.doc",
    "my.ava.jpg",
    "forest.jpeg",
    "eq_1.png",
    "eq_2.xls",
]

acceptor = FileAcceptor("jpg", "jpeg", "png")
# filenames = list(filter(acceptor, filenames))
filenames = [filename for filename in filenames if acceptor(filename)]

acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2  # ("jpg", "jpeg", "png", "bmp")
