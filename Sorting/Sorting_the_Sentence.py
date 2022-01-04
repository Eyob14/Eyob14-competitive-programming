class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = s.split()
        ordered = []
        for i in range(len(sentence)):
            for j in range(len(sentence)-1):
                if sentence[j][-1] > sentence[j+1][-1]:
                    sentence[j], sentence[j+1] = sentence[j+1], sentence[j]
        for i in range(len(sentence)):
            temp = sentence[i][:-1]
            if i != len(sentence)-1:
                ordered.append(temp)
                ordered.append(" ")
            else:
                ordered.append(temp)
        return ''.join(ordered) 