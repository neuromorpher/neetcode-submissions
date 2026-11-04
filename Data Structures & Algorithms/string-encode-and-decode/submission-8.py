class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:

            return "-" 

        encoded_string = "\0".join(strs) 

        return encoded_string

    def decode(self, s: str) -> List[str]:

        if s=="-":

            return [] 

        if not s:

            return [""]

        decoded_string = s.split("\0")

        return decoded_string 