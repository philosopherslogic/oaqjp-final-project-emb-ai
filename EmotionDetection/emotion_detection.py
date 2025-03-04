import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json=input_json)
    if response.status_code==400:
        output = {'anger':None, 'disgust':None, 'fear':None, 'joy':None, 'sadness':None, 'dominant_emotion':None}
        return output
    else:
        output = format_response(response)
        return output
    


def format_response(response):
    data = response.json()
    anger_score = data['emotionPredictions'][0]['emotion']['anger']
    disgust_score = data['emotionPredictions'][0]['emotion']['disgust']
    fear_score = data['emotionPredictions'][0]['emotion']['fear']
    joy_score = data['emotionPredictions'][0]['emotion']['joy']
    sadness_score = data['emotionPredictions'][0]['emotion']['sadness']
    output = {'anger':anger_score, 'disgust':disgust_score, 'fear':fear_score, 'joy':joy_score, 'sadness':sadness_score}
    dominant_emotion_name = dominant_emotion(output)

    output['dominant_emotion'] = dominant_emotion_name

    return output

    

def dominant_emotion(dic):
    dominant = None
    for key in dic: 
        if not dominant is None:
            if dic[key] > dic[dominant]:
                dominant = key
        else:
            dominant = key
    return dominant