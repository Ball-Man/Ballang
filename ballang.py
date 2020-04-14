from operator import add


ADD = '+'
SUB = '-'
CLOCK = '/'
CCLOCK = '\\'
UP = '^'
DOWN = '_'
LEFT = '<'
RIGHT = '>'
START = '*'
OUTPUT = '.'
GTZ = '?'
STOP = '|'


INTERP_DICT = {
    ADD: lambda ball: ball.add(),
    SUB: lambda ball: ball.sub(),
    CLOCK: lambda ball: ball.clockwise(),
    CCLOCK: lambda ball: ball.countclockwise(),
    UP: lambda ball: ball.up(),
    DOWN: lambda ball: ball.down(),
    LEFT: lambda ball: ball.left(),
    RIGHT: lambda ball: ball.right(),
    START: lambda ball: ball.start(),
    OUTPUT: lambda ball: ball.output(),
    GTZ: lambda ball: ball.set_gtz_flag(),
    STOP: lambda ball: -1
}

PROG_FILENAME = 'program.txt'
INPUT_FILENAME = 'input.txt'


def checkgtz(fun):
    def wrapper(*args, **kwargs):
        ball = args[0]
        if not ball.gtz_flag or ball.val > 0:
            return fun(*args, **kwargs)
        ball.gtz_flag = False

    return wrapper


class Ball:

    def __init__(self, pos, direction, val=0):
        self.pos = list(pos)
        self._start_dir = list(direction)
        self._direction = list(direction)
        self.val = val
        self.gtz_flag = False

    @checkgtz
    def up(self):
        self._direction = [0, -1]

    @checkgtz
    def down(self):
        self._direction = [0, 1]

    @checkgtz
    def left(self):
        self._direction = [-1, 0]

    @checkgtz
    def right(self):
        self._direction = [1, 0]

    @checkgtz
    def add(self, val=1):
        self.val += val

    @checkgtz
    def sub(self, val=1):
        self.val = max(0, self.val - val)

    @checkgtz
    def clockwise(self):
        self._direction = [-self.direction[1], self.direction[0]]

    @checkgtz
    def countclockwise(self):
        self._direction = [self.direction[1], -self.direction[0]]

    @checkgtz
    def start(self):
        self._direction = list(self._start_dir)

    def update(self):
        self.pos = list(map(add, self._direction, self.pos))

    @checkgtz
    def output(self):
        return self.val

    def set_gtz_flag(self):
        self.gtz_flag = True

    @property
    def direction(self):
        return self._direction


class Interpreter:

    def __init__(self, matrix, direction=(1, 0), initval=0):
        self._matrix = matrix
        self._ball = Ball(self._get_ball_pos(), direction, initval)

    @staticmethod
    def matrix_from_file(fin):
        return fin.read().split('\n')

    def update(self):
        self._ball.update()

        fun = None
        try:
            fun = INTERP_DICT.get(self._matrix[self._ball.pos[1]]
                                  [self._ball.pos[0]])
        except IndexError:
            pass

        if fun is not None:
            return fun(self._ball)

    @property
    def matrix(self):
        return self._matrix

    def _get_ball_pos(self):
        for y in range(len(self._matrix)):
            if START in self._matrix[y]:
                return self._matrix[y].index(START), y


def main():
    with open(INPUT_FILENAME) as fin:
        initval = int(fin.read())

    with open(PROG_FILENAME) as fin:
        matrix = Interpreter.matrix_from_file(fin)
    interp = Interpreter(matrix, initval=initval)

    while True:
        res = interp.update()
        if res == -1:
            break
        if res is not None:
            print(res)


if __name__ == '__main__':
    main()
