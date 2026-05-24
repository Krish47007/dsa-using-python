
class Solution:
    def profession(self, level, pos):

        if pos == 1:
            return 'e'

        parentProf = self.profession(level - 1, (pos + 1) // 2)

        if parentProf == 'e':
            if pos % 2 != 0:
                return 'e'
            else:
                return 'd'
        else:
            if pos % 2 != 0:
                return 'd'
            else:
                return 'e'

