import requests

def qrandint_generator(n, l):
    result = []
    
    overpass_url = 'https://qrng.anu.edu.au/API/jsonI.php'
    length = str(n)
    qtype = 'uint8'

    response = requests.get(overpass_url, params={'length': length, 'type': qtype})
    data = response.json()

    for r in data['data']:
        result.append(int((r/255.0) * l))
        
    return result    

def quniform(a, b):
    
    overpass_url = 'https://qrng.anu.edu.au/API/jsonI.php'
    length = '1'
    qtype = 'uint8'

    response = requests.get(overpass_url, params={'length': length, 'type': qtype})
    data = response.json()
    
    interval = abs(b - a)

    return a + interval*(data['data'][0]/255.0)
