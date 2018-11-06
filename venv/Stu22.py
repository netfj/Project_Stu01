# -*- coding: UTF-8 -*-
"""
deque模块是python标准库collections中的一项，
它提供了两端都可以操作的序列，这意味着，
在序列的前后你都可以执行添加或删除操作。
"""

from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)

queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)

queue.popleft()                 # The first to arrive now leaves
print(queue)

queue.popleft()                 # The second to arrive now leaves
print(queue)

vec = [2, 4, 6]
print([3*x for x in vec])

a=dict(sape=4139, guido=4127, jack=4098)
print(a)