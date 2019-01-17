class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        one = []
        two = ['a', 'b', 'c']
        three = ['d', 'e', 'f']
        four = ['g', 'h', 'i']
        five = ['j', 'k', 'l']
        six = ['m', 'n', 'o']
        seven = ['p', 'q', 'r', 's']
        eight = ['t', 'u', 'v']
        nine = ['w', 'x', 'y', 'z']
        number = [one, two, three, four, five, six, seven, eight, nine]

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return number[int(digits[0]) - 1]

        digitsComb = []
        digitsCombFlag = []
        for s in digits:
            digitsComb.append(number[int(s) - 1])
            digitsCombFlag.append(0)

        length = len(digitsComb)

        returnArr = []
        curStr = ''
        for i in range(length):
            curStr += str(digitsComb[i][digitsCombFlag[i]])
        returnArr.append(curStr)

        flag = True
        while flag == True:
            i = len(digitsCombFlag) - 1
            digitsCombFlag[i] += 1
            if digitsCombFlag[i] == len(digitsComb[i]):
                digitsCombFlag[i] = 0
                digitsCombFlag[i - 1] += 1
                k = i
                proce = True
                while proce == True:
                    k = k - 1
                    if digitsCombFlag[k] == len(digitsComb[k]):
                        if k == 0:
                            return returnArr
                        else:
                            digitsCombFlag[k] = 0
                            digitsCombFlag[k - 1] += 1
                    else:
                        proce = False
                curStr = ''
                for i in range(length):
                    curStr += str(digitsComb[i][digitsCombFlag[i]])
                returnArr.append(curStr)
            else:
                curStr = ''
                for i in range(length):
                    curStr += str(digitsComb[i][digitsCombFlag[i]])
                returnArr.append(curStr)