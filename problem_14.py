class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         #edgecase where there's only 1 word in the string list, then just
        #return that word
        if len(strs) == 1:
            return strs[0]
        
        #sorts the strs list in order from smallest word to biggest
        sorted_list = sorted(strs, key=len)

        
        #so this goes through all the letters of the first word in sorted list
        #but we're using pointers, starting at index 0 of the word
        for letter_pos in range(len(sorted_list[0])):
            curr_letter = sorted_list[0][letter_pos]
            print(sorted_list)
            
            #formatting variable inside print
            #print(f"Name: {name}, Age: {age}")
            
            #this is going through all the words in sorted list
            for word in sorted_list:
                if(curr_letter == word[letter_pos]):
                    print(f"the {letter_pos+1}th letter for {sorted_list[0]} is matching the {letter_pos+1} for the word {word}")
                else:
                    print("the letter is no longer matching")

                #print(word[letter_pos], end="")
            #print("")
        
        return sorted_list
        