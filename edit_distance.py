'''
edit_dist - This function returns get edit distance between two strings

get_edit_distnce - This function returns dictionary where keys are elements of list and values as edit distance from all list elements below than provided threshould values

'''

def edit_dist(input1, input2):
    
    if len(input1) > len(input2):
        diff = len(input1) - len(input2)      
    elif len(input2) > len(input1):
        diff = len(input2) - len(input1)     
    else:
        diff = 0
    for i in range(len(input1)):
        try:
            if input1[i] != input2[i]:
                diff += 1
        except:
            pass
        
    return diff

def get_edit_distnce(input_list,THRESHOLD):
    out_dict={}
    for i in range(len(input_list)):
        input1 =input_list[i]
        k=0   
        while(k !=len(input_list)):
            input2=input_list[k]

            distance=edit_dist(input1,input2)
            #print(input1 +"    "+ input2+"====>"+str(distance))
            if distance < THRESHOLD:    
                if input1!=input2:
                    out_dict.setdefault(input1,[]).append(input2)
            k+=1  
    
    return out_dict

if __name__ == "__main__":

    in_list = ['man','pan','mat','pass']
    THRESHOLD = 2
    for k, v in get_edit_distnce(in_list,THRESHOLD).items():
        print(k,v)