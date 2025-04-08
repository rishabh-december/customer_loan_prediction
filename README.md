
This projects helps prediction for loan approval for a customer based on below financial features:-

| Column Name       | Description                                       |
| ----------------- | ------------------------------------------------- |
| Loan_ID           | Unique loan identifier                            |
| Gender            | Applicant's gender                                |
| Married           | Marital status                                    |
| Dependents        | Number of dependents                              |
| Education         | Education level                                   |
| Self_Employed     | Employment status                                 |
| ApplicantIncome   | Applicant's monthly income                        |
| CoapplicantIncome | Co-applicant's monthly income                     |
| LoanAmount        | Loan amount requested                             |
| Loan_Amount_Term  | Loan repayment term (in months)                   |
| Credit_History    | Credit history meets guidelines (1: yes, 0: no)   |
| Property_Area     | Urban / Semiurban / Rural                         |
| Loan_Status       | Loan approval status (Y = Approved, N = Rejected) |


**Project Workflow**

- Data loaded to a
  pandas dataframe
- Preprocessing involved
  identifying target variable and encoding categorical column
- Model training involved
  splitting the data and training using XGBoost followed by accuracy score
  evaluation

**Steps to execute**

- Build project and
  download dependencies : pip install -r requirements.txt
- Execute
  train_test_model.py
- Validate accuracy

**Pending Items**

- Save the weights and
  biases for the model
- Deploy as an API
  using FastAPI
