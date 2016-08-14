from enum import Enum


class Color(Enum):

    DEFAULT = 0
    BLACK   = 30
    RED     = 31
    GREEN   = 32
    YELLOW  = 33
    BLUE    = 34
    MAGENTA = 35
    CYAN    = 36
    WHITE   = 37
    GRAY    = 90

    def __str__(self):
        return self.name.lower()

    def _escape(self, string, value):
        escape_sequence_template = '\033[{}m'
        return '{}{}{}'.format(
            escape_sequence_template.format(value),
            string,
            escape_sequence_template.format(Color.DEFAULT.value),
        )
        
    def fore(self, string):
        return self._escape(string, self.value)

    def back(self, string):
        return self._escape(string, self.value + 10)
