import math

def accuracy(actual, predicted):
    error_sum = 0
    for i in range(len(actual)):
        error = actual[i] - predicted[i]
        error_sum = error ** 2

    mse = error_sum/len(actual)
    rmse = math.sqrt(mse)
    
    accuracy = max(0,100 -rmse)
    return accuracy

if __name__ =="__main__":
    actual =[90,80,70]
    predicted = [89,78,69]
    print("accuracy:",accuracy(actual,predicted))
    

