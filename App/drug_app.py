import gradio as gr  
import skops.io as sio

untrusted_types = sio.get_untrusted_types(file="Model/drug_pipeline.skops")
pipe = sio.load("Model/drug_pipeline.skops", trusted=untrusted_types)

def predict_drug (age, sex, blood_pressure, cholesterol, na_to_k_ratio):
    """prediction des m€dicaments en fonction des parametres du patient
    
    Args:
        age (int): Âge du patient
        sex (str): Sexe du patient
        blood_pressure (float): Pression artérielle du patient
        cholesterol (float): Cholesterol du patient
        na_to_k_ratio (float): Ratio sodium/potassium du patient

    Returns:
        str: Le médicament prédit pour le patient
    """
    
    features = [age, sex, blood_pressure, cholesterol, na_to_k_ratio]
    predicted_drug = pipe.predict([features])[0]
    
    label = f"Le médicament prédit pour le patient est : {predicted_drug}"
    return label


inputs = [
    gr.Slider(15, 74, step=1, label="Âge du patient"),
    gr.Radio(["M", "F"], label="Sexe du patient"),
    gr.Radio(["LOW", "NORMAL", "HIGH"], label="Pression artérielle du patient"),
    gr.Radio(["NORMAL", "HIGH"], label="Cholesterol du patient"),
    gr.Slider(0.0, 100.0, step=0.1, label="Ratio sodium/potassium du patient")
]

outputs = [gr.Label(num_top_classes=1, label="Prédiction du médicament" )]

examples = [
    [25, "M", "NORMAL", "NORMAL", 15.0],
    [45, "F", "HIGH", "HIGH", 30.0],
    [60, "M", "LOW", "NORMAL", 10.0], ]

title = "Prédiction du médicament pour le patient"
description = "Entrez les paramètres du patient pour prédire le médicament approprié."
article = "Ce modèle prédit le médicament approprié pour un patient en fonction de son âge, sexe, pression artérielle, cholestérol et ratio sodium/potassium."  

gr.Interface(
    fn = predict_drug,
    inputs = inputs,
    outputs = outputs,
    examples = examples,
    title = title,
    description = description,
    article = article  ,
    theme = gr.themes.Soft(),
).launch()
    
    
    