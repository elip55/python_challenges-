# given a datatype (list, string), return it backwards


 

def backwards(data):

    ticker = len(data) -1
    data2 = []
    for i in data:
        data2.append(data[ticker])
        ticker -= 1
    return data2

