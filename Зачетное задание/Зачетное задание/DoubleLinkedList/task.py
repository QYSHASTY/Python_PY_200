from typing import Any, Iterable, Optional, Iterator

from collections.abc import MutableSequence

from node import Node


class LinkedList(MutableSequence):


    def __init__(self):
        """Конструктор связного списка"""
        super().__init__()

    def __getitem__(self, index: int):
        """ Метод возвращает значение узла по указанному индексу. """
        super().__getitem__()

    def __setitem__(self, index: int, value: Any):
        """ Метод устанавливает значение узла по указанному индексу. """
        super().__setitem__()

    def __delitem__(self, index: int):
        super().__delitem__()
        if not 0 <= index < self.len:  # проверка индекса
            raise IndexError

    def __len__(self) -> int:
        """ Метод возвращает длину последовательности. """
        super().__len__()
        return self.len

    def __str__(self) -> str:
        return f" В списке {self.to_list()} для узла Nodename следующим элементом является Value  "

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"


    def insert(self, index: int, value: Any) -> None:
        super().insert()
        if not isinstance(index, int):
            raise TypeError()


    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        super().append()

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node


    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def nodes_iterator(self) -> Iterator[Node]:
        current_node = self.head  # функция-генератор для перебора всех узлов
        for _ in range(self.len):
            yield current_node
            current_node = current_node.next



class DoubleLinkedList(LinkedList):
    ...


if __name__ == "__main__":


