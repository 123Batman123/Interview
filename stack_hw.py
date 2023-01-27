from stack_class import Stack


def test_brecket(test):

    stack_list = Stack()
    check = True
    for bracket in test:

        if bracket in '([{':
            stack_list.stack_append_el(bracket)
        elif bracket in ')]}':
            if stack_list.stack_is_empty() == True:
                check = False
                break

            bracket_pop = stack_list.stack_pop_el()

            if bracket_pop == '(' and bracket == ')':
                continue
            if bracket_pop == '[' and bracket == ']':
                continue
            if bracket_pop == '{' and bracket == '}':
                continue
            check = False
            break

    if check and stack_list.stack_is_empty():
        res = "Сбалансированная"
    else:
        res = "Не сбалансированная"
    return res


def dict_check_bracket(bracket_list):

    requests_dict = {}
    for test in bracket_list:
        if test_brecket(test) not in requests_dict:
            requests_dict[test_brecket(test)] = [test]
        else:
            requests_dict[test_brecket(test)] += [test]
    return requests_dict


if __name__ == "__main__":
    test_list = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '}{{', '{{[(])}}',
                 '{{[()]}}', '(){}()', '[[{())}]', ')))', '()', '({})({})({})({})((']
    print(dict_check_bracket(test_list))
