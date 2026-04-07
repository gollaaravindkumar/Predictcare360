# risk_checker/views.py
from django.shortcuts import render
import joblib
import numpy as np
import os
from django.conf import settings

def breast_cancer_form(request):
    """Render the breast cancer input form."""
    return render(request, 'breast_cancer_predict.html')

def predict_cancer(request):
    """Handle prediction when user submits form."""
    if request.method == "POST":
        try:
            # Extract input fields
            features = [
                float(request.POST.get("concave_points_mean")),
                float(request.POST.get("area_mean")),
                float(request.POST.get("radius_mean")),
                float(request.POST.get("perimeter_mean")),
                float(request.POST.get("concavity_mean")),
            ]

            # Load model
            model_path = os.path.join(settings.BASE_DIR, "risk_checker", "models", "cancer_model.pkl")
            model = joblib.load(model_path)

            # Predict
            result = model.predict(np.array(features).reshape(1, -1))[0]

            # Determine risk
            if int(result) == 1:
                prediction = "⚠️ High Risk: Please consult an oncologist immediately."
                color = "danger"
                high_risk = True
            else:
                prediction = "✅ Low Risk: No major signs of breast cancer detected."
                color = "success"
                high_risk = False

            return render(
                request,
                "breast_cancer_predict.html",
                {
                    "prediction_text": prediction,
                    "color": color,
                    "high_risk": high_risk
                },
            )
        except Exception as e:
            return render(
                request,
                "breast_cancer_predict.html",
                {"prediction_text": f"Error: {str(e)}", "color": "warning"},
            )
    return render(request, "breast_cancer_predict.html")

def diabetes_form(request):
    """Render the diabetes input form."""
    return render(request, 'diabetes_predict.html')


def predict_diabetes(request):
    """Handle prediction when user submits diabetes form."""
    if request.method == "POST":
        try:
            # Extract form inputs — adjust based on your dataset features
            features = [
                float(request.POST.get("pregnancies")),
                float(request.POST.get("glucose")),
                float(request.POST.get("blood_pressure")),
                float(request.POST.get("bmi")),
                float(request.POST.get("diabetes_pedigree_function")),
                float(request.POST.get("age")),
            ]

            # Load model
            model_path = os.path.join(settings.BASE_DIR, "risk_checker", "models", "diabetes_model.pkl")
            model = joblib.load(model_path)

            # Predict
            result = model.predict(np.array(features).reshape(1, -1))[0]

            # Risk message
            if int(result) == 1:
                prediction = "⚠️ High Risk: Please consult a diabetologist immediately."
                color = "danger"
                high_risk = True
            else:
                prediction = "✅ Low Risk: Your diabetes indicators appear within a healthy range."
                color = "success"
                high_risk = False

            return render(
                request,
                "diabetes_predict.html",
                {
                    "prediction_text": prediction,
                    "color": color,
                    "high_risk": high_risk,
                },
            )

        except Exception as e:
            return render(
                request,
                "diabetes_predict.html",
                {"prediction_text": f"Error: {str(e)}", "color": "warning"},
            )

    return render(request, "diabetes_predict.html")


def heart_form(request):
    """Render the heart disease input form."""
    return render(request, 'heart_predict.html')


def predict_heart(request):
    """Handle prediction when user submits heart disease form."""
    if request.method == "POST":
        try:
            # Extract 6 important input features (adjust to your trained model)
            features = [
                float(request.POST.get("cp")),
                float(request.POST.get("trestbps")),
                float(request.POST.get("chol")),
                float(request.POST.get("fbs")),
                float(request.POST.get("restecg")),
                float(request.POST.get("thalach")),
                float(request.POST.get("exang")),
            ]

            # Load model
            model_path = os.path.join(settings.BASE_DIR, "risk_checker", "models", "heart_model.pkl")
            model = joblib.load(model_path)

            # Predict
            result = model.predict(np.array(features).reshape(1, -1))[0]

            # Risk message
            if int(result) == 1:
                prediction = "⚠️ High Risk: Possible signs of heart disease detected. Please consult a cardiologist immediately."
                color = "danger"
                high_risk = True
            else:
                prediction = "✅ Low Risk: Your heart indicators appear within a healthy range."
                color = "success"
                high_risk = False

            return render(
                request,
                "heart_predict.html",
                {
                    "prediction_text": prediction,
                    "color": color,
                    "high_risk": high_risk,
                },
            )

        except Exception as e:
            return render(
                request,
                "heart_predict.html",
                {"prediction_text": f"⚠️ Error: {str(e)}", "color": "warning"},
            )

    return render(request, "heart_predict.html")



def kidney_form(request):
    """Render the kidney disease input form."""
    return render(request, "kidney_predict.html")


def predict_kidney(request):
    """Handle kidney disease prediction when user submits the form."""
    if request.method == "POST":
        try:
            # Extract input features from the form
            features = [
                float(request.POST.get("bp")),   # Blood Pressure
                float(request.POST.get("sg")),   # Specific Gravity
                float(request.POST.get("al")),   # Albumin
                float(request.POST.get("su")),   # Blood Sugar
                float(request.POST.get("rbc")),  # Red Blood Cells
                float(request.POST.get("pc")),   # Pus Cell
                float(request.POST.get("pcc")),  # Pus Cell Clumps
            ]

            # Load trained kidney disease model
            model_path = os.path.join(settings.BASE_DIR, "risk_checker", "models", "kidney_model.pkl")
            model = joblib.load(model_path)

            # Make prediction
            result = model.predict(np.array(features).reshape(1, -1))[0]

            # Prepare risk message
            if int(result) == 1:
                prediction = "⚠️ High Risk: Signs of kidney disease detected. Consult a doctor immediately."
                color = "danger"
                high_risk = True
            else:
                prediction = "✅ Low Risk: Your kidney indicators appear normal."
                color = "success"
                high_risk = False

            return render(
                request,
                "kidney_predict.html",
                {
                    "prediction_text": prediction,
                    "color": color,
                    "high_risk": high_risk,
                },
            )

        except Exception as e:
            return render(
                request,
                "kidney_predict.html",
                {"prediction_text": f"⚠️ Error: {str(e)}", "color": "warning"},
            )

    return render(request, "kidney_predict.html")



def liver_form(request):
    """Render the liver disease input form."""
    return render(request, "liver_predict.html")


def predict_liver(request):
    """Handle liver disease prediction when user submits the form."""
    if request.method == "POST":
        try:
            # Extract exactly 7 features from the form
            features = [
                float(request.POST.get("Total Bilirubin")),
                float(request.POST.get("Direct_Bilirubin")),
                float(request.POST.get("Alkaline_Phosphotase")),
                float(request.POST.get("Alamine_Aminotransferase")),
                float(request.POST.get("Total_Protiens")),
                float(request.POST.get("Albumin")),
                float(request.POST.get("Albumin_and_Globulin_Ratio")),
            ]

            # Load trained liver disease model
            model_path = os.path.join(settings.BASE_DIR, "risk_checker", "models", "liver_model.pkl")
            model = joblib.load(model_path)

            # Make prediction
            result = model.predict(np.array(features).reshape(1, -1))[0]

            # Prepare risk message
            if int(result) == 1:
                prediction = "⚠️ High Risk: Signs of liver disease detected. Consult a hepatologist immediately."
                color = "danger"
                high_risk = True
            else:
                prediction = "✅ Low Risk: Your liver indicators appear normal."
                color = "success"
                high_risk = False

            return render(
                request,
                "liver_predict.html",
                {
                    "prediction_text": prediction,
                    "color": color,
                    "high_risk": high_risk,
                },
            )

        except Exception as e:
            return render(
                request,
                "liver_predict.html",
                {"prediction_text": f"⚠️ Error: {str(e)}", "color": "warning"},
            )

    return render(request, "liver_predict.html")


def disease_overview(request):
    return render(request, 'disease_overview.html')
