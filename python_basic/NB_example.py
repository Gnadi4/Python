def NB(a,b):
    X = []
    Y = []

    ##X, Y  구별하기
    for i in range(len(a)):
        temp_X = []
        for j in range(len(a[i])):
            if j != len(a[i])-1:
                temp_X.append(a[i][j])
        X.append(temp_X)
        for j in range(len(a[i])):
            if j == len(a[i])-1:
                Y.append(a[i][j])
    
    
    ## X,Y uinque값 뽑기
    unique_Y = list(set(Y))    
            
    unique_X = []   
    check=0
    for i in a:
        for j in range(len(i)-1):
            compare = 1
            if check==0:
                unique_X.append([i[j]])
            else:
                for k in range(len(unique_X[j])):
                    if compare == 1:
                        if unique_X[j][k] == i[j]:
                            compare = 0
                        else:
                            compare = 1
                if compare == 1:
                    unique_X[j].append(i[j])
            unique_X[j].sort()
        check+=1
        
      
    ## 테이블 만들기
    p_1 = len(X[0])
    max_len = 0
    for i in range(len(unique_X)):
        if len(unique_X[i]) > max_len:
            max_len = len(unique_X[i])
    p_2 = max_len
    n = len(X)

    ## 테이블 0으로 채우기
    I = [[0 for rows in range(p_1*p_2)]for cols in range(len(unique_Y))]

    ##개수 세서 테이블애 채우기
    for i in range(n):
        for j in range(len(I)):
            if Y[i] == unique_Y[j]:
                for k in range(len(X[i])):
                    I[j][unique_X[k].index(X[i][k])+k*len(X[i])] += 1
    
    ## Class별 확률 뽑기             
    pro_Y = []
    for j in range(len(unique_Y)):
            pro_Y.append(0)
    for i in Y:
        for j in range(len(unique_Y)):    
            if i == unique_Y[j]:
                pro_Y[j] +=1
    for i in range(len(unique_Y)):
        pro_Y[i] /= len(Y)
    
    ## input의 X 값들 테이블에 맞춰 index뽑기
    input_index = []
    for i in range(len(b)):
        input_index.append(unique_X[i].index(b[i])+i*len(unique_X[i]))

    ##최종결과 만들기
    result = []
    count = []
   
    #count에 각 열별 총 갯수 세서 넣기
    for j in input_index:
        temp_1 = 0
        for p in range(len(I)):
            temp_1 += I[p][j]
        count.append(temp_1)
    
    #각 클래스별 테이블에 있는 각 x 개수 p(c=1|x1=1)*p(c=1|x2=1)
    for i in range(len(I)):
        temp = 1
        for j in range(len(input_index)):
            temp *= (I[i][input_index[j]]/count[j])
        result.append(temp*pro_Y[i])

    #인덱스 값 뽑아서 최종 결과 예측한 y 클래스 출력하기
    final_result = unique_Y[(result.index(max(result)))]
    return final_result
    
    
    
if __name__ == "__main__":
    a= [[1,2,3],[4,1,1],[1,1,2]]
    b = [1,2]       
    print(NB(a,b))
