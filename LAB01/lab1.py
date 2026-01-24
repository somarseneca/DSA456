#  1
def wins_rock_scissors_paper(player, opponent):
    p = player.lower()
    o = opponent.lower()

    if p == o:
        return False

    if p == "rock" and o == "scissors":
        return True
    if p == "paper" and o == "rock":
        return True
    if p == "scissors" and o == "paper":
        return True

    return False

#  2
def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result


#  3
def Fibonacci(n):
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
        i += 1

    return b


#  4
def sum_to_goal(numbers, goal):
    i = 0
    while i < len(numbers):
        j = i + 1
        while j < len(numbers):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
            j += 1
        i += 1
    return 0


# objects
class UpCounter:
    def __init__(self, stepsize=1):
        self.stepsize = stepsize
        self.value = 0

    def count(self):
        return self.value

    def update(self):
        self.value += self.stepsize


class DownCounter(UpCounter):
    def __init__(self, stepsize=1):
        super().__init__(stepsize)

    def update(self):
        self.value -= self.stepsize



