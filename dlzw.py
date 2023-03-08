
def dic_query(dic, index):
    if index<=256:
        return chr(index)
    else:
        return dic[index-256-1]

def dlzw(seq):
    result = ""
    dic = []
    index = 0
    while index<len(seq)-1:
        token = seq[index]
        next_token = seq[index+1]
        first = dic_query(dic,token)
        dic.append(first)
        result+=first
        last = dic_query(dic, next_token)[0]
        dic[-1] = first+last
        print(f"{result:>60}{(index+257):>5}\t{('|'+dic[-1]+'|'):>7}\t{token}")
        index+=1
    print(f"{(result+dic_query(dic,seq[-1])):>60}{'':>5}\t{'':>5}\t{seq[-1]}")

if __name__ == '__main__':
    dlzw([65,66,257,259,66])