import wikipedia
import requests
def fact_check(statement: str):

    try:
       
       response = requests.get(
        "https://en.wikipedia.org/w/api.php/",
        params={
            "action": "query",
            "list": "search",
            "srsearch": statement,
            "format": "json"
        },
       headers={
            "User-Agent": "NetworkingAssistant/1.0"
        }
        )

       data = response.json()
       title = data["query"]["search"][0]["title"]
       print(title)
       summary_response = requests.get(
    f"https://en.wikipedia.org/api/rest_v1/page/summary/{title.replace(' ', '_')}",
    headers={
        "User-Agent": "NetworkingAssistant/1.0"
    }
)
       summary_data = summary_response.json()

       summary = summary_data["extract"]
       return {
            "verification_status": "Information Retrieved",
            "summary": summary
        }

    except Exception as e:
        print("err",e)
        return {
            "verification_status": "Not Found",
            "summary": None,
        }