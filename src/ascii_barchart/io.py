def load_rows(file):
    l=[]
    f=open(file)
    for line in f:
        l.append(line.strip().split(","))
    return l 


