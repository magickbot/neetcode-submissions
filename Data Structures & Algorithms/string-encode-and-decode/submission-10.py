class Solution:

    def encode(self, strs: list[str]) -> str:
        if not strs: 
            return "__EMPTY_LIST__"

        return "::##::".join(strs)

    def decode(self, s: str) -> list[str]:
        if s == "__EMPTY_LIST__":
            return []
            

        return s.split("::##::")