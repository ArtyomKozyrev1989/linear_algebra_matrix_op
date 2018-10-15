def _pr_matrix(determinant):   
    '''The function is used to print determinant if you want to do it'''
    for i in range(len(determinant)):
        line=""
        for j in range(len(determinant[i])):
            line+=f"{matrix[i][j]:>6d}"
        print(line)

def _get_minor(determinant,row):
    '''The function is used to find minor of the first line element (defined by row)
    multiplied by the element and signum +-'''
    result=[]
    for i in range(len(determinant)):
        minorline=[]
        for j in range(len(determinant[i])):
            if i!=0 and j!=row:
                minorline.append(determinant[i][j])
        if minorline!=[]:
            result.append(minorline)
    if row%2==0:
        for i in range(len(result[0])):
            result[0][i]=determinant[0][row]*result[0][i]
    else:
        for i in range(len(result[0])):
            result[0][i]=(-1)*determinant[0][row]*result[0][i]
    
    return result

def _get_all_minors(determinant):
    ''' The method is used to get all minors of the first line elements
    multiplied by the element and signum +-'''
    result=[]
    for i in range(len(determinant)):
        result.append(_get_minor(determinant,i))
    return result

def _get_smallest_matrix_sum(smallestminors):
    ''' The method is used to calculate sum of determinant element multiplied by minor'''
    result=0
    for i in range(len(smallestminors)):
        for j in range(len(smallestminors[i])):
            for k in range(len(smallestminors[i][j])):
                result+=smallestminors[i][j][z]
    return result

def get_determinant_value(determinant):
    ''' The method is used to calculate determinant of matrix'''
    result=0
    smallestminors=[]
    smallestminors.append(determinant)
    while(True):
        temporaryresult=[]
        for i in smallestminors:
            a=get_all_minors(i)
            for j in a:
                temporaryresult.append(j)
        smallestminors=temporaryresult
        if len(smallestminors[0])==1:
            break
    result=_get_smallest_matrix_sum(smallestminors)
    return result

#Test
#a=[[1,2,3,100,10],[5,6,7,8,10],[9,100,11,12,10],[13,14,15,16,10],[1,2,3,4,5]]
#answer=get_determinant_value(a)
