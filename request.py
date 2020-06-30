import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'CreditScore':2.0000,'Geography':9.0000,'Gender':6.0000,'Age':2.00000,'Tenure':9.00000,'Balance':6.00000,'NumOfProducts':6.00000
                            'HasCrCard':9.00000,'IsActiveMember':6.00000,'EstimatedSalary':6.00000})

print(r.json())
