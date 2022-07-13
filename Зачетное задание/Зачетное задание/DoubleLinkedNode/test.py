import unittest

from task import Node

class TestCase(unittest.TestCase):
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node("node_without_next")

        msg = "Следующий узел не ожидается (значение None)"
        self.assertIsNone(node.next, msg)


    def test_str(self):
        some_value = 3
        node = Node(some_value)

        self.assertEqual(str(node), str(some_value))