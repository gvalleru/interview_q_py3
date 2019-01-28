class Solution(object):
    def toGoatLatin(self, S):
        out = ''
        for index, word in enumerate(s.split()):
            if word[0].lower() in 'aeiou':
                out = out+word+'ma'+'a'*(index + 1)+' '
            else:
                out = out+word[1:]+word[0]+'ma'+'a'*(index + 1)+' '
        return out[:len(out)-1]
