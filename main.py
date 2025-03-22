import os

os.system("python src/data_ingestion.py")
print("--------------Data Ingestion Completed--------------")

os.system("python src/data_preprocessing.py")
print("--------------Data Preprocessing Completed--------------")

os.system("python src/feature_engineering.py")
print("--------------Feature Engineering Completed--------------")

os.system("python src/model_building.py")
print("--------------Model Building Completed--------------")

os.system("python src/model_evaluation.py")
print("--------------Model Evaluation Completed--------------")