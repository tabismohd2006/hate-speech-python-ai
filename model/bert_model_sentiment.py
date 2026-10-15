from detoxify import Detoxify

model = Detoxify("original")

def predict_text(text):

    result = model.predict(text)

    toxic = float(result["toxicity"])
    threat = float(result["threat"])
    insult = float(result["insult"])
    identity = float(result["identity_attack"])
    obscene = float(result["obscene"])

    max_score = max(toxic, threat, insult, identity, obscene)

    if threat >= 0.70:
        label = "Threat"

    elif identity >= 0.70:
        label = "Hate Speech"

    elif insult >= 0.60:
        label = "Offensive"

    elif toxic >= 0.60:
        label = "Toxic"

    else:
        label = "Normal"

    return {
        "prediction": label,
        "confidence": max_score,
        "text": text
    }