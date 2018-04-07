import shodan
import json

print("Insert Shodan Key : ")
key = input()
print("Insert the search query : ")
query = input()

api = shodan.Shodan(key)

results = api.search(query)

i = 0

print("Saving "+str(results['total'])+" banners")
for result in results['matches']:
    print("saving banner "+str(i))
    with open("banner_"+str(i)+".txt",'w') as f:
        f.write(result['data'])
    i=i+1

print("D O N E")
    
