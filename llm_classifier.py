import requests
import json

def classify_email(subject, body, model='llama2'):
    prompt = f"""
You are an email spam classifier. Analyze the following email and respond with a JSON object containing 'label' (either 'spam' or 'not spam') and 'confidence' (a float between 0 and 1).

Subject: {subject}

Body:
{body}

Respond only with the JSON object.
"""
    response = requests.post(
        f'http://localhost:11434/api/generate',
        json={
            'model': model,
            'prompt': prompt,
            'stream': False
        },
        timeout=60
    )
    response.raise_for_status()
    # Extract JSON from LLM response
    try:
        data = response.json()
        output = data.get('response', '').strip()
        # Find JSON in output
        start = output.find('{')
        end = output.rfind('}') + 1
        if start != -1 and end != -1:
            result = json.loads(output[start:end])
            return result['label'], float(result['confidence'])
    except Exception as e:
        print(f"Error parsing LLM response: {e}")
    return 'unknown', 0.0 