def getFromRAPI(endpoint, queryParams={}):
    url = f"https://imdb8.p.rapidapi.com{endpoint}"
    querystring = {"tconst":"tt0944947"}
    apiKey = os.getenv("RAPIKEY")
    if not apiKey:
        raise ValueError("Please setup the RAPIKEY env variable")
    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        'Authorization' : f"token {apiKey}"
    }
    
    res = requests.get(url, headers=headers, params=querystring)
    print(res.url)
    return res.json()


   
