# -*- coding: utf-8 -*-
"""Visualization .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19HoW8lXIKWOVopCV05PjoUakS4p-D5zt

Visualization of Data:

Using Matplotlib or Seaborn to create visual representations of the model's performance, making the results easier to understand.
"""

# visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
import predictive_maintenance_ as pm

def visualize_confusion_matrix(y_test, predictions):
    cm = confusion_matrix(y_test, predictions)

    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('Truth')
    plt.title('Confusion Matrix')
    plt.show()

    return cm

def print_classification_report(y_test, predictions):
    report = classification_report(y_test, predictions, output_dict=True)
    print(classification_report(y_test, predictions))

    return report

def generate_conclusion(cm, report):
    total = cm.sum()
    accuracy = (cm[0, 0] + cm[1, 1]) / total
    precision = report['1']['precision']
    recall = report['1']['recall']
    f1_score = report['1']['f1-score']

    print("\nConclusion:")
    print(f"Total samples: {total}")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1_score:.2f}")

    if accuracy > 0.8:
        print("The model performs well in predicting maintenance needs with high accuracy.")
    else:
        print("The model needs improvement to better predict maintenance needs.")

    if recall > 0.8:
        print("The model effectively identifies most cases where maintenance is needed.")
    else:
        print("The model may miss some cases where maintenance is needed, indicating a potential risk.")

    if precision > 0.8:
        print("The model has a low rate of false positives in predicting maintenance needs.")
    else:
        print("The model has a higher rate of false positives, suggesting over-prediction of maintenance needs.")

if __name__ == '__main__':
    X_train, X_test, y_train, y_test = pm.load_and_preprocess_data()
    model, predictions = pm.train_and_evaluate_model(X_train, X_test, y_train, y_test)

    cm = visualize_confusion_matrix(y_test, predictions)
    report = print_classification_report(y_test, predictions)
    generate_conclusion(cm, report)