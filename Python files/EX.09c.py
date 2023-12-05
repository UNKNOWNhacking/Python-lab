sentence = input("Enter Sentence : ")
longest = max(sentence.split(), key=len)
print("longest words is : ", longest)
print("any its length is : ", len(longest))
