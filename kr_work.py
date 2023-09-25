from node import Node


class BinaryTree:
    """
       BinaryTree class.
       Implements Binary tree

       Attributes:
             Manage what objects allowed to be stored inside tree elements
             Objects must implement at least __lt__ and __gt__ methods

       Methods:
           __init__(self)
             Constructor, create empty tree, or set root element as Node, or create root element with $root as value
           add(self, value)
             Add elements to tree.
           search(self, value)
             Search element in tree and return it or None
           countNodes(self)
             Counting the number of elements of a binary tree
           print(self)
             Print tree starting from $node or tree.root
           delete(self, value)
             Search element in tree by $value and delete it

       """

    def __init__(self):
        self.root = None

    def add(self, value):
        """
            Добавление значения в бинарное дерево

            Parameters:
                value: Значение для добавления
        """
        if not self.root:
            self.root = Node(value)
        else:
            self.add_(value, self.root)

    def add_(self, value, current_node):
        """
            Вспомогательная функция добавления значения в бинарное дерево

            Parameters:
                value: Значение для добавления
                current_node: Текущий узел
        """
        if value < current_node.value:
            if not current_node.left:
                current_node.left = Node(value)
            else:
                self.add_(value, current_node.left)
        elif value > current_node.value:
            if not current_node.right:
                current_node.right = Node(value)
            else:
                self.add_(value, current_node.right)

    def search(self, value):
        """
        Нахождение элемента в дереве и возвращение результата
        Поиск всегда начинается с корня дерева

        Parameters:
            value: Значение для поиска
        """
        return self.search_(value, self.root)[0]

    def search_(self, value, node, parent=None):
        """
        Метод внутреннего поиска
        Поиск узла с $value и его родительского элемента
        Поиск начинается с $node

        Parameters:
            value: Значение для поиска
            node: С какого узла начать поиск
            parent(optional): Точки на текущем родительском узле, используемые для целей рекурсии
        """
        if node is None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search_(value, node.right, node)
        if value < node.value:
            return self.search_(value, node.left, node)

    def countNodes(self):
        """
            Подсчёт количества элементов бинарного дерева
        """
        counter = 0
        current = self.root
        while current is not None:
            counter += 1
            current = current.right
        return counter

    # Функция для удаления узла с заданным значением данных из двоичного дерева
    def delete(self, value):
        """
              Нахождение элемента $data в дереве и удаление его

              Parameters:
                  value: Значение для удаления

        """
        self.root = self.delete_(self.root, value)

    def delete_(self, current_node, value):
        """
              Вспомогательная функция для метода удаления

              Parameters:
                  value: Значение для удаления
                  current_node: Текущий узел

        """
        if not current_node:
            return current_node
        elif value < current_node.value:
            current_node.left = self.delete_(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.delete_(current_node.right, value)
        else:
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            else:
                min_node = self.find_min_(current_node.right)
                current_node.value = min_node.data
                current_node.right = self.delete_(current_node.right, min_node.data)
        return current_node

    def find_min_(self, current_node):
        """
              Функция для нахождения минимального значения узла с заданным значением данных из бинарного дерева

              Parameters:
                  current_node: Текущий узел

           """
        while current_node.left:
            current_node = current_node.left
        return current_node
