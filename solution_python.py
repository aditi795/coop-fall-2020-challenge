from collections import deque
class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self._undoStack = deque()
        self._redoStack = deque()

    def add(self, num: int):
        self._undoStack.append(num)
        self.value += num

    def subtract(self, num: int):
        self._undoStack.append(-num)
        self.value -= num

    def undo(self):
        if self._undoStack:
            popped = self._undoStack.pop()
            self.value -= popped
            self._redoStack.append(popped)

    def redo(self):
        if self._redoStack:
            popped = self._redoStack.pop()
            self.value += popped

    def bulk_undo(self, steps: int):
        for i in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        for i in range(steps):
            self.redo()