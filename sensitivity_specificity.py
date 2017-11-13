
def true_false(cm):
    true_negative = cm[0][0]
    false_positive = cm[0][1]
    false_negative = cm[1][0]
    true_positive = cm[1][1]

    sensitivity = true_positive / (true_positive + false_negative)
    specificity = true_negative / (true_negative + false_positive)

    precision = true_positive / (true_positive + false_positive)
    fMeasure = 2*true_positive / (2*true_positive + false_positive + false_negative)

    print("Sensitivity is", sensitivity)
    print("Specificity is", specificity)
    print("Precision is", precision)
    print("fMeasure is", fMeasure)

