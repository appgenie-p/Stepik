class TreeObj:
    """для описания вершин и листьев решающего дерева"""

    def __init__(self, indx: int, value: str = None):
        self.indx = indx  # проверяемый в вершине дерева индекс вектора x
        self.value = value  # значение с данными (строка), хранящееся в вершине (принимает значение None для вершин, у которых есть потомки - промежуточных вершин)
        self.__left: TreeObj = (
            None  # ссылка на следующий объект дерева по левой ветви (изначально None);
        )
        self.__right: TreeObj = (
            None  # ссылка на следующий объект дерева по правой ветви (изначально None).
        )

    @property
    def left(self) -> "TreeObj":
        return self.__left

    @left.setter
    def left(self, left: "TreeObj") -> None:
        self.__left = left

    @property
    def right(self) -> "TreeObj":
        return self.__right

    @right.setter
    def right(self, right: "TreeObj") -> None:
        self.__right = right

    def __repr__(self) -> str:
        return f"{self.value}"


class DecisionTree:
    """для работы с решающим деревом в целом"""

    @classmethod
    def predict(cls, root: TreeObj, x: list) -> str:
        """для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root.
        x = [1, 1, 0]
        """
        obj = root
        if x[0] == 1:
            obj = obj.left
            if x[1] == 1:
                obj = obj.left
            else:
                obj = obj.right
        else:
            obj = obj.right
            if x[2] == 1:
                obj = obj.left
            else:
                obj = obj.right
        return obj.value

    @classmethod
    def add_obj(
        cls, obj: TreeObj, node: "TreeObj" = None, left: bool = True
    ) -> TreeObj:
        if node is None:
            return obj
        if left:
            node.left = obj
            return obj
        node.right = obj
        return obj


assert hasattr(DecisionTree, "add_obj") and hasattr(
    DecisionTree, "predict"
), "в классе DecisionTree должны быть методы add_obj и predict"

assert (
    type(TreeObj.left) == property and type(TreeObj.right) == property
), "в классе TreeObj должны быть объекты-свойства left и right"

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

assert (
    DecisionTree.predict(root, [1, 1, 0]) == "программист"
), "неверный вывод решающего дерева"
assert DecisionTree.predict(root, [0, 1, 0]) == "нет", "неверный вывод решающего дерева"
assert (
    DecisionTree.predict(root, [0, 1, 1]) == "посмотрим"
), "неверный вывод решающего дерева"
