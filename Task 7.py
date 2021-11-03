import json

with open('company.json', 'w') as w:
    with open('company.txt',encoding='utf - 8') as f:
        prof = {line.split()[0]:int(line.split()[2])-int(line.split()[3]) for line in f}
        result = [prof, {'av_prof': round(sum([int(i) for i in prof.values() if int(i)>0])/len([int(i) for i in prof.values() if int(i>0)]))}]
    json.dump(result, w)