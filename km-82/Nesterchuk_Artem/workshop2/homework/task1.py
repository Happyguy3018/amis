smth= [
    {
        "name": "Bob",
        "age": 20,
        "marks": {
            "Math": 98,
            "Python":100
        }
    },
    {
        "name": "Boba",
        "age": 19,
        "marks": {
            "Physic": 98,
        }
    },
    {
        "name": "Boban",
        "age": 22,
        "marks": {
        }
    }

]

def max(x):# Допоміжна функція яка шукає найбліьший елемент списку
    for i in range(len(x)):
        max=x[0]
        if x[i]>max:
            max=x[i]
            return max
        else:
            max=x[0]
            return max
def max_age(smth,x):
    if len(smth)==0:
        return max(x)
    x.append(smth[0].get("age"))
    return max_age(smth[1:],x)
x=[]
print(max_age(smth,x))
def get_names(smth,x):
    if len(smth)==0:
        return x
    x.append(smth[0].get("name"))
    return get_names(smth[1:],x)
a=[]
print(get_names(smth,a))