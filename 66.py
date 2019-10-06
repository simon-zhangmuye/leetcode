# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/10/6 9:23'


# 使用栈实现队列的下列操作：
#
# push(x) -- 将一个元素放入队列的尾部。
# pop() -- 从队列首部移除元素。
# peek() -- 返回队列首部的元素。
# empty() -- 返回队列是否为空。
# 示例:
#
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # 两个栈倒，新来的元素总是在栈底（队尾进）
        if self.stack1 == None:
            self.stack1.append(x)
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
            self.stack1.append(x)
            while self.stack2:
                self.stack1.append(self.stack2.pop(-1))

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # 直接弹出，因为本来就是队头出
        return self.stack1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack1:
            return self.stack1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # 因为队列１存储了所有元素，所以只需要判断队列１
