from stacks.linked_list_stack import Stack


class BalancedParenthesis:
    matching_brackets = {')': '(', '}': '{', ']': '['}

    def __init__(self):
        self.simulator = Stack()

    def get_matching_parenthesis(self, item):
        return self.matching_brackets.get(item, None)

    def is_balanced(self, input_str):
        for item in input_str:
            if (item == '[') or (item == '(') or (item == '{'):
                self.simulator.push(item)
            elif self.simulator.peek() == self.get_matching_parenthesis(item):
                self.simulator.pop()
            else:
                return False

        return self.simulator.is_empty()


bp = BalancedParenthesis()
print(bp.is_balanced("(((((((((([[[[[[[[{{{{{{{{}}}}}}}}]]]]]]]]))))))))))"))
