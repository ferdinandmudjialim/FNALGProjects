# Ferdinand Mudjialim
# Lab 05: ParenMatch
from pythonds.basic.stack import Stack

matching = {'(':')', '{':'}', '[':']'}

def ParenMatch(x):
    s = Stack()
    for i in range(0, len(x)):
        if x[i] in matching.keys():
            s.push(x[i])
        elif x[i] in matching.values():
            if s.isEmpty():
                return False
            if matching[s.pop()] != x[i]:
                return False

    return s.isEmpty()

if __name__ == '__main__':
    print(
    "A*B+C*D",
    ParenMatch("A*B+C*D"),
    "(A+B)*(C-(D-E))*(F+G)",
    ParenMatch("(A+B)*(C-(D-E))*(F+G)"),
    "((A+{B+C}-[D-E])+[F]-[G]",
    ParenMatch("((A+{B+C}-[D-E])+[F]-[G]"),
    "(A+B)*(C+D)",
    ParenMatch("(A+B)*(C+D)"),
    "A/B-C+D*E-A*C",
    ParenMatch("A/B-C+D*E-A*C"),
    "(((A/B)-C)+(D*E))-A*C)",
    ParenMatch("(((A/B)-C)+(D*E))-A*C)"),
    "A/(B-C+D))*(E-A)*C",
    ParenMatch("A/(B-C+D))*(E-A)*C"),
    sep="\n"
    )