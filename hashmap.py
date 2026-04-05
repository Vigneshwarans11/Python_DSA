#frequency of items or count the items
items=["pen", "book", "pen", "pencil", "book", "pen"]
count={}
for products in items:
    if products in count:
        count[products]+=1
    else:
        count[products]=1
print(count)

