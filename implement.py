import csv
import matplotlib.pyplot as plt

class Tools:
    
    def extract_list_of_lists(lists):
        final_list = []
        for i in lists:
            for x in i:
                final_list.append(x)
        return final_list
    
    
    def count_em_up(lists):
        a=b=c=d=e=f=g=h=j=k=l=m=n=0
        for i in lists:
            if 'Pale Ale' in i:
                a +=1
            if 'Brown' in i:
                b +=1
            if 'Saison' in i:
                c += 1
            if 'Cider' in i:
                d +=1
            if 'Tripel' in i:
                e +=1
            if 'Blonde' in i:
                f += 1
            if 'Amber' in i:
                g +=1
            if 'Wheat' in i:
                h +=1
            if 'Gose' in i:
                j += 1
            if 'Lager' in i:
                k +=1
            if 'Stout' in i:
                l +=1
            if 'IPA' in i:
                m += 1
            if 'Pilsner' in i:
                n += 1
            final_dict = {'Pale Ale':a,'Brown':b, 'Saison':c, 'Cider':d, 'Tripel':e,
                      'Blonde': f, 'Amber':g, 'Wheat':h, 'Gose':j, 'Lager':k, 'Stout': l,
                     'IPA': m, 'Pilsner': n}
        return final_dict
    
    def show_the_graph(dictionary,x):
    
        labels = []
        sizes = []
        title = x
        for x, y in dictionary.items():
            labels.append(x)
            sizes.append(y)
        plt.pie(sizes,labels=labels, autopct='%1.1f%%',radius = 4,labeldistance=1.1,
                shadow={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9}, startangle=90)
        plt.title(title,bbox={'facecolor':'.5', 'pad':20})
        plt.show()
    
    
def gather_all():
    rows = []
    with open("beers.csv", 'r') as file:
        header_reader = csv.reader(file)
        header = next(header_reader) # header is the name of the accounts
        rowboat = csv.reader(file)
        for row in rowboat:
            rows.append(row) # rows import data as floats using quote_nonnumeric
    return header, rows

v,j = gather_all() # v = header, j = rows

for i in range(len(j)):
    del(j[i][0]) # delete unwanted first index
state_list = []
state_type_dict = {}

for i in range(len(j)):
    state_type_dict[j[i][12]] = []
    state_list.append(j[i][12])
state_list.sort()
state_list = list(set(state_list))
for i in range(len(j)):
    if j[i][12] in state_list:
        state_type_dict[j[i][12]].append(j[i][5])
        
west = ['WA', 'OR', 'CA', 'ID', 'NV', 'AZ', 'UT', 'MT', 'WY', 'CO', 'NM', 'AK', 'HI']
midwest = ['IL', 'IN', 'IA', 'KS', 'MI', 'MN', 'MO', 'NE', 'ND', 'OH', 'SD',  'WI']
south = ['AL', 'AR', 'DE', 'FL', 'GA', 'KY', 'LA', 'MD', 'MS', 'NC', 'OK', 'SC', 'TN', 'TX', 'VA', 'WV']
northeast = ['CT', 'MA', 'ME', 'NH', 'NJ', 'NY', 'PA', 'RI', 'VT'] # all lengths pass
western = []
midwestern = []
southern = []
northeastern = []
for i,j in state_type_dict.items():
    if i in west:
        western.append(j)
    elif i in midwest:
        midwestern.append(j)
    elif i in south:
        southern.append(j)
    else:
        northeastern.append(j)
west_list = Tools.extract_list_of_lists(western)
midwestern_list = Tools.extract_list_of_lists(midwestern)
southern_list = Tools.extract_list_of_lists(southern)
north_list = Tools.extract_list_of_lists(northeastern)
"""WESTERN REGION"""
graph_west = Tools.count_em_up(west_list)
Tools.show_the_graph(graph_west, x = 'Western Region') # ect. 
