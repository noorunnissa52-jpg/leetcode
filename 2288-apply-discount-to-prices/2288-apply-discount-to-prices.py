class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words=sentence.split()
        result=[]
        for word in words:
            if word.startswith('$') and word[1:].isdigit():
                price=int(word[1:])
                price=price*(100-discount)/100
                result.append('$'+format(price,'.2f'))
            else:
                result.append(word)
        return ' '.join(result)