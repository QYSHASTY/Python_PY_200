Наш `LinkdeList` теперь может конкатенировать к себе `list`,  
но вот в обратную сторону к сожалению не работает.

Хотим пойти дальше и научить встроенный `list` складываться с нашим `LinkdeList`.  
Для этого есть специальный метод `__radd__`.

1. Определить метод `__radd__` для сложения `list` с `LinkdeList`.
