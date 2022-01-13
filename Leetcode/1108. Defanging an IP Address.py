# https://leetcode.com/problems/defanging-an-ip-address/

def defangIPaddr(self, address: str) -> str:
    defangedIP = ""
    for i in address:
        if i != ".":
            defangedIP = defangedIP + i
        else:
            defangedIP = defangedIP + "[.]"
    return defangedIP