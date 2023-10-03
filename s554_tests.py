from s554 import DatabaseConnection

c = DatabaseConnection()

try:
    c.connect("aaa", "bbb")
except ConnectionError:
    assert c._fl_connection_open
else:
    assert False, "не сгенерировалось исключение ConnectionError"

try:
    with DatabaseConnection() as conn:
        conn.connect("aaa", "bbb")
except ConnectionError:
    assert True
else:
    assert False, "не сгенерировалось исключение ConnectionError"
