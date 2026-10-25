import json
with open("detions.txt",'r',encoding="utf-8") as f:
    counts = {}
    for line in f:
        parts = line.split("|")
        pairs = parts[1].split(',')
        for p in pairs:
            k,v = p.split(':')
            v = int(v)
            k = k.strip()
            counts[k] = counts.get(k,0) + v
counts_list = counts.items()
counts_out = sorted(counts_list,key=lambda item: item[1],reverse=True)
print(counts_out)
with open ("stats.json","w",encoding="utf-8") as f:
    json.dump(counts_out,f)

