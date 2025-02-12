class Node(object):
    def __init__(self, child=None, leaf=None):
        self.child = child
        self.leaf = leaf


class Section(object):
    def __init__(self, id):
        self.id = id


class Op(object):
    def __init__(self, opcode):
        self.opcode = opcode


class BinOp(Op):
    def __init__(self, opcode, left, right):
        Op.__init__(self, opcode)
        self.left, self.right = left, right


class TernaryOp(Op):
    def __init__(self, opcode, one, two, three):
        Op.__init__(self, opcode)
        self.first, self.second, self.third = one, two, three


class Jump(object):
    def __init__(self, opcode, reg, num, label):
        self.opcode = opcode
        self.reg = reg
        self.num = num
        self.label = label


class Call(object):
    def __init__(self, procedure):
        self.procedure = procedure


class Label(object):
    def __init__(self, name):
        self.name = name


class Phv(object):
    def __init__(self, shift):
        self.shift = shift


class Portmask(object):
    pass


class Hdr(object):
    def __init__(self, shift):
        self.shift = shift


class Reg(object):
    def __init__(self, name):
        self.name = name
