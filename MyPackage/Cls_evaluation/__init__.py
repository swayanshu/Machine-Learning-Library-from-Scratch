def confusion_matrix(y_actualdata, y_prediction):
    assert(len(y_actualdata)==len(y_prediction))
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    for y_actualdata, y_prediction in zip(y_actualdata, y_prediction):
        if y_prediction == y_actualdata: 
            if y_prediction == 1: # True Positive
                TP += 1
            else: # tn
                TN += 1
        else: 
            if y_prediction == 1: # False Positive
                FP += 1
            else: # FN
                FN += 1
            
        our_confusion_matrix = [
            [TN, FP],
            [FN, TP]
        ]

    return [TN,FP, FN, TP]

def acc(confusion_matrix):
    [TN, FP, FN, TP] = confusion_matrix
    accuracy_value = 0
    
    accuracy_value = (TP + TN)/(TP+TN+FP+FN)
    return accuracy_value

def precision(confusion_matrix):
    [TN, FP, FN, TP] = confusion_matrix
    precision_value = 0
    
    All_Pred_positives = TP+FP
    precision_value = TP / All_Pred_positives
    
    return precision_value

def recall(confusion_matrix):
    [TN, FP, FN, TP] = confusion_matrix
    recall_value = 0
   
    all_actual_positive = TP+FN
    recall_value = TP/all_actual_positive
    
    return recall_value

def F1(confusion_matrix):
    [TN, FP, FN, TP] = confusion_matrix
    f1_value = 0
    f1_value = 2*(TP )/(2*(TP ) + FP + FN)
    
    return f1_value

def FDR(confusion_matrix):
    [TN, FP, FN, TP] = confusion_matrix
    fdr_value = 0
    fdr_value = FP/(TP+FP)
    return fdr_value
