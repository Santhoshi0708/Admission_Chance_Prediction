# Welcome to Admission Chance Prediction by Santhoshi Kothapalli! 👋

## About
Our Streamlit web application predicts the admission chances for prospective students based on their academic and research-related details. Leveraging a Linear Regression model trained on historical admission data, we offer insights to aid your educational journey.

## Setup and Usage
1. **Environment Setup**
   - Ensure Python is installed on your machine.
   - Install necessary packages via pip:
     ```bash
     pip install streamlit pandas scikit-learn
     ```

2. **Running the App**
   - Clone the repository or download `app.py` and `Admission_Chance.csv`.
   - Navigate to the directory in your terminal.
   - Execute the Streamlit app:
     ```bash
     streamlit run app.py
     ```
   - Access the app in your browser at [http://localhost:8501](http://localhost:8501).

3. **Using the App**
   - Input the following details:
     - GRE Score
     - TOEFL Score
     - University Rating
     - SOP Rating
     - LOR Strength
     - Undergraduate CGPA
     - Research Experience (Binary: 0 for No, 1 for Yes)
   - Click "Make Prediction" to generate the admission chance.
   - View the predicted chance displayed on the interface.

## Dependencies
- Streamlit
- Pandas
- scikit-learn

## Included Files
- `app.py`: Streamlit application code.
- `Admission_Chance.csv`: Historical admission data in CSV format.
- `Admission_Chance_Prediction.ipynb`: Jupyter Notebook with code and explanations for the application.

## Acknowledgments
- The dataset used is for demonstration purposes only.
- This app is a simplified example and may need enhancements for production.
  
## Preview
Check out the app [here]().

## Connect
Reach out on [LinkedIn](https://www.linkedin.com/in/kothapalli-santhoshi-368951254/). Your feedback is valuable! Email us at santhu2002.kothapalli@gmail.com.
