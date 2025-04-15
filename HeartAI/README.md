# HeartAI

HeartAI is a machine learning-based heart disease risk predictor with an interactive frontend powered by Streamlit. Users can input clinical health parameters and receive real-time predictions about the likelihood of heart disease, based on a trained classification model.

---

## Features

- Web-based user interface built with Streamlit
- Real-time predictions via a locally-hosted FastAPI backend (or public backend)
- Clean, sectioned layout with input validation and feedback
- Deployable on Streamlit Cloud for instant access

---

## Tech Stack

| Layer       | Technology                |
|-------------|---------------------------|
| Frontend    | Streamlit (Python-based UI) |
| Backend     | FastAPI (REST API)        |
| ML Model    | RandomForestClassifier (scikit-learn) |
| Data        | CSV dataset (Heart Disease - UCI) |
| Deployment  | Streamlit Cloud (frontend), localhost or public API for backend |
| Dependencies| streamlit, requests, scikit-learn, joblib, pandas (optional)

---

## Live App

Visit the deployed app: [https://heartai.streamlit.app](https://heartai.streamlit.app)

---

## Project Structure

```
HeartAI/
├── streamlit_app.py           ← Streamlit app file
├── requirements.txt           ← Streamlit + requests + other dependencies
├── README.md                  ← Project documentation
├── app/                       ← (Optional) FastAPI backend if deployed together
│   ├── main.py
│   ├── core/
│   └── api/
├── train/                     ← Training scripts (optional for backend)
│   └── train_model.py
├── data/
│   └── heart.csv              ← Source dataset
```

---

## Requirements

Install dependencies locally:

```bash
pip install -r requirements.txt
```

Or let Streamlit Cloud install them automatically from the file.

---

## Run Locally

###  Run the Backend (FastAPI)

To serve predictions, you need a local FastAPI server running on `http://localhost:8000`.

#### Steps:

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install backend dependencies if requirements is needed to be installed again
pip install -r requirements.txt

# Train the model
python train/train_model.py

# Start the FastAPI server
uvicorn app.main:app --reload
```

Once running, visit `http://localhost:8000/docs` to explore and test the API using Swagger UI.

---

### Run the Frontend (Streamlit)

In a separate terminal:

```bash
# Activate your virtual environment
source .venv/bin/activate

# Install frontend dependencies
pip install streamlit requests

# Run the app
streamlit run streamlit_app.py
```

Access the app in your browser at:  
[http://localhost:8501](http://localhost:8501)

Make sure the backend is running before clicking “Predict.”

---

## Input Parameters

- Age, sex, resting blood pressure
- Cholesterol, fasting blood sugar
- ECG results, exercise-induced angina
- Max heart rate, ST depression (oldpeak), slope
- Number of major vessels, thalassemia type
- Chest pain type

---

## Backend Integration

The app expects a backend endpoint at:

```
POST http://localhost:8000/api/predict
```

To deploy publicly, the backend must be hosted on a server accessible by Streamlit Cloud (e.g., Fly.io, Render, or Heroku).

---

## Credits

Developed by Zemariam Ephrem  
Powered by Streamlit + FastAPI + scikit-learn
