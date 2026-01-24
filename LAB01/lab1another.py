#  1
def wins_rock_scissors_paper(player, opponent):
    player = player.lower()
    opponent = opponent.lower()

    if player == opponent:
        return False

    if player == "rock" and opponent == "scissors":
        return True
    if player == "paper" and opponent == "rock":
        return True
    if player == "scissors" and opponent == "paper":
        return True

    return False


#  2
def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result = result * i
        i = i + 1
    return result


#  3 
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    i = 2
    while i <= n:
        c = a + b
        a = b
        b = c
        i = i + 1

    return b


#  4
def sum_to_goal(numbers, goal):
    i = 0
    while i < len(numbers):
        j = i + 1
        while j < len(numbers):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
            j = j + 1
        i = i + 1
    return 0


# 5
class UpCounter:
    def __init__(self, stepsize=1):
        self.stepsize = stepsize
        self.value = 0

    def count(self):
        return self.value

    def update(self):
        self.value = self.value + self.stepsize


class DownCounter(UpCounter):
    def __init__(self, stepsize=1):
        UpCounter.__init__(self, stepsize)

    def update(self):
        self.value = self.value - self.stepsize
