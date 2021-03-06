from ._internal_utils import is_bpython


class _Color(object):
    def __init__(self, color_code, bright=False):
        self.color_code = str(color_code)
        self.intensity = '1' if bright else '0'

    def wrap_text(self, text):
        if is_bpython():
            colored_text = '\033[%sm%s\033[0m' % (self.color_code, text)
            if self.intensity == '0':
                return colored_text
            else:
                return '\033[1m' + colored_text
        else:
            return '\033[%s;%sm%s\033[0m' % (self.intensity, self.color_code, text)

    def __eq__(self, other):
        return self.color_code == other.color_code

    def __repr__(self):
        return '\033[%sm%s\033[0m' % (self.color_code, 'color')


COLORS = {
    'black': _Color(30),
    'bright black': _Color(30, True),
    'grey': _Color(30, True),
    'red': _Color(31),
    'bright red': _Color(31, True),
    'green': _Color(32),
    'bright green': _Color(32, True),
    'yellow': _Color(33),
    'bright yellow': _Color(33, True),
    'blue': _Color(34),
    'bright blue': _Color(34, True),
    'magenta': _Color(35),
    'bright magenta': _Color(35, True),
    'cyan': _Color(36),
    'bright cyan': _Color(36, True),
    'white': _Color(37),
    'bright white': _Color(37, True),
}
