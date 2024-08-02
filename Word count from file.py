count= {}
with open(input("Enter the file path: "),"r") as f:
    for text in f:
     clear_text= ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
     words= clear_text.split()
     for word in words:
        if word in count:
         count[word]+=1
        else:
         count[word]=1
     
count= sorted(count.items(),key= lambda x:x[1],reverse=True)
print("\nThe words and there counts are:-\n")
for x in count:
 print(f"{x[0]}: {x[1]}")
