def average_value1_by_type(rows):
    l=[]
    for c in ["A","B","C","D"]:
        l.append(average_by_letter(rows,c))
    return l 

def average_by_letter(rows,x):
    summe=0
    anzahl=0
    for row in rows:
        if row[0]==x:
            summe=summe+float(row[1])
            anzahl=anzahl+1
    median=summe/anzahl
    return (x,median)
