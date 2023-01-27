class Stack:
    def __init__(self):
        self.stack = []

    def stack_is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def stack_append_el(self, el):
        self.stack.append(el)

    def stack_pop_el(self):
        return self.stack.pop()

    def stack_print_last_el(self):
        return self.stack[-1]

    def stack_print_len_el(self):
        return len(self.stack)