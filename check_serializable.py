def isConflicting(op1, op2):
    isConflicting = False
    if (op1['data'] == op2['data']) and (op1['action'] == 'w' or op2['action'] == 'w'):
        # print(op1['action'] + str(op1['tid']) + "(" + op1['data'] + ") < ", end=" ")
        # print(op2['action'] + str(op2['tid']) + "(" + op2['data'] + ")")
        # print('possibly conflicting')
        isConflicting = True
    return isConflicting


# ---------------------
# |   | 1 | 2 | 3 | 4 |
# ---------------------
# | 1 | F | F | F | T |
# ---------------------
# | 2 | F | F | F | T |
# ---------------------
# | 3 | F | T | F | T |
# ---------------------
# | 4 | T | F | T | F |
# ---------------------
def check_dependency(history, t_graph):
    for i in range(1, len(history)):
        for j in range(0, i):
            r = history[i]['tid']
            c = history[j]['tid']
            # if there is an existing True (Dependency info), we will not over-write
            if t_graph[r][c] is False:
                t_graph[r][c] = isConflicting(history[j], history[i])
    return t_graph


def cyclic(tg):
    exists = False
    # number of transactions
    n = len(tg)
    # exploring tg
    for i in range(0, n):
        for j in range(i + 1, n):
            if tg[i][j] is True and tg[i][j] == tg[j][i]:
                # cycle exists,
                # i.g. transaction i depends on transaction j and vice-versa
                exists = True
                break
    return exists


def manage_input():
    input_history = input('Enter History: ').split(' ')
    history = []
    transactions = set()
    for i in range(0, len(input_history), 3):
        instance = {
                    'action': input_history[i],
                    'transaction': int(input_history[i+1]),
                    'data': input_history[i+2],
                    'tid': int(input_history[i+1]) - 1,
                    }
        transactions.add(instance['tid'])
        history.append(instance)
    # print(instance['action'] + str(instance['tid']) + "(" + instance['data'] + ") < ", end=" ")
    return history, sorted(transactions)


def main():
    history, transactions = manage_input()
    t_graph = []
    n = len(transactions)
    for i in range(0, n):
        t_graph.append([])
        for j in range(0, n):
            t_graph[i].append(False)

    print(t_graph)
    t_graph = check_dependency(history, t_graph)
    print(not cyclic(t_graph))


if __name__ == '__main__':
    # w 1 x r 2 x w 2 y r 3 y w 3 z r 1 z
    main()
