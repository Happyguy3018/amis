input_file = 'patient-characteristics-survey-pcs-2015.csv' 
import re



def get_program_category(line, dataset=dict()):
    result = re.split(r',', line, maxsplit=0)
    key=result[1]
    if key not in dataset.keys():
        dataset[key]={}
    return key, result[2:], dataset


def get_sex_lol(line, program_category, dataset):
    sex = ''.join(re.findall('[M|m]ALE|[F|f]EMALE|[M|m]an|[W|w]oman|[U|u]\w+', line[2]))
    if sex not in dataset[program_category].keys():
        dataset[program_category][sex]=[]
    return sex, line[3:], dataset


def get_edacation(line, program_category, sex, dataset):
    work_line = line[12]
    work_line = ''.join(re.sub(r'\s+', ' ', work_line))
    if work_line[0]==' ':
        work_line= work_line[1:]
    education= ''.join(re.findall('[O|o]\w{3}[r|R]|[U|u]\w{4}[W|w][n|N]|[C|c]\w+\s[O|o]\w\s\w+\s\w+|[S|s][O|o]\w+\s\w+|[M|m][I|i]\w+\s\w+\s\w+\s\w+\s\w+|[P|p][R|r]\w[\w|\-|\s][\w|\s][\w|\s]\w+\s\w+\s\w+|[N|n]\w\s\w+\s\w+|[Y|y][E|e][s|S]|[N|n][O|o]\w+\s\w+', work_line))
    if education == '':
        education=work_line
    dataset[program_category][sex].append(education)
    return education, line[13:], dataset
    


def add_to_dataset(program_category, sex, education, dataset=dict()):
    if program_category in dataset.keys():
        if sex in dataset[program_category].keys():
            dataset[program_category][sex].append(education)
        else:
            dataset[program_category][sex]=[education]
    else:
        dataset[program_category]={sex: [education]}
    return dataset
        
def count_of_education(dataset):
    empty_dict=dict()
    empty_list=[]
    for _,data in dataset.items():
        for sexs, do_i_need_this in data.items():
            do_i_need_this=','.join(do_i_need_this)
            if (re.findall('[N|n][O|o]\w+\s\w+|[U|u]\w{4}[W|w][n|N]', do_i_need_this)):
                do_i_need_this = re.sub('[N|n][O|o]\w+\s\w+|[U|u]\w{4}[W|w][n|N]', '' , do_i_need_this)
            if (re.findall('[N|n][O|o]', do_i_need_this)):
                do_i_need_this = re.sub('[N|n][O|o]', '' , do_i_need_this)
            do_i_need_this = re.sub('\,+', ',' , do_i_need_this)
            sum_of_education=sum([do_i_need_this.count(item) for item in set(do_i_need_this)])
            if sexs not in empty_dict.keys():
                empty_dict[sexs]=sum_of_education
            else:
                empty_dict[sexs]+=sum_of_education
    return empty_dict



def male_study(dataset):
    empty_dict=dict()
    for a, values in dataset.items():
        for key,i_nedd_this in values.items():
            if key == "MALE":
                for study in i_nedd_this:
                    if study not in empty_dict:
                        empty_dict[study]=1
                    else:
                        empty_dict[study]+=1
    return empty_dict


def female_study(dataset):
    empty_dict=dict()
    for a, values in dataset.items():
        for key,i_nedd_this in values.items():
            if key == "FEMALE":
                for study in i_nedd_this:
                    if study not in empty_dict:
                        empty_dict[study]=1
                    else:
                        empty_dict[study]+=1
    return empty_dict




from functools import reduce



with open(input_file, encoding='utf-8') as data:
    data.readline()
    line_counter = 1
    for line in data:
        line = line.strip()
        line_counter += 1
        if not line:
            continue
        program_category, line, dataset = get_program_category(line)
        sex, line, dataset = get_sex_lol(line, program_category, dataset)
        third_element , line, dataset = get_edacation(line, program_category, sex, dataset)
#1 grad
men_vs_women_vs_unknown = count_of_education(dataset)
import plotly.offline as pl
import plotly.graph_objs as go
from plotly import tools
xs, ys=list(men_vs_women_vs_unknown.keys()), list(men_vs_women_vs_unknown.values())
first_graf=go.Bar(x=xs, y=ys, name='man_vs_wome')
# MvsF graf
male, female = male_study(dataset), female_study(dataset)
xm, ym = list(male.keys()), list(male.values())
xf, yf = list(female.keys()), list(female.values())
male_graf = go.Pie(labels=xm, values=ym, name='male', domain={'x': [0.35, 0.65], 'y': [0, 1]})
female_graf = go.Pie(labels=xf, values=yf, name='female', domain={'x': [0.7, 1], 'y': [0, 1]})
#combine
layout = go.Layout(
	xaxis=dict(domain=[0, 0.33]))
fig = go.Figure(data=[first_graf, female_graf, male_graf], layout=layout)
pl.plot(fig, filename='my_graf.html')