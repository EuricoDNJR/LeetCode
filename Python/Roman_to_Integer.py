class Solution:
    def romanToInt(self, s: str) -> int:
        acumulate = 0
        i = 0
        while i < len(s):
            if s[i] == "I":
                acumulate += 1
                if i < len(s) - 1:
                    if s[i + 1] == "V":
                        acumulate += 3
                        i += 1
                    elif s[i + 1] == "X":
                        acumulate += 8
                        i += 1
            elif s[i] == "V":
                acumulate += 5
            elif s[i] == "X":
                acumulate += 10
                if i < len(s) - 1:
                    if s[i + 1] == "L":
                        acumulate += 30
                        i += 1
                    elif s[i + 1] == "C":
                        acumulate += 80
                        i += 1
            elif s[i] == "L":
                acumulate += 50
            elif s[i] == "C":
                acumulate += 100
                if i < len(s) - 1:
                    if s[i + 1] == "D":
                        acumulate += 300
                        i += 1
                    elif s[i + 1] == "M":
                        acumulate += 800
                        i += 1
            elif s[i] == "D":
                acumulate += 500
            elif s[i] == "M":
                acumulate += 1000
            i += 1
        return acumulate