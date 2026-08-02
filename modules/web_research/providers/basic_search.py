from datetime import datetime
import requests
from bs4 import BeautifulSoup



def search_web(query):

    try:

        url = "https://html.duckduckgo.com/html/"

        response = requests.post(

            url,

            data={

                "q":
                    query

            },

            headers={

                "User-Agent":
                    "Mozilla/5.0"

            },

            timeout=10

        )


        soup = BeautifulSoup(

            response.text,

            "html.parser"

        )


        results = []


        for item in soup.select(
            ".result"
        )[:5]:

            title = item.select_one(
                ".result__title"
            )

            link = item.select_one(
                ".result__a"
            )

            snippet = item.select_one(
                ".result__snippet"
            )


            results.append(

                {

                    "title":
                        title.get_text(
                            " ",
                            strip=True
                        )
                        if title
                        else "Ei otsikkoa",


                    "link":
                        link.get("href")
                        if link
                        else None,


                    "summary":
                        snippet.get_text(
                            " ",
                            strip=True
                        )
                        if snippet
                        else ""

                }

            )



        return {

            "success":
                True,

            "time":
                datetime.now().isoformat(),

            "query":
                query,

            "provider":
                "duckduckgo",

            "results":
                results

        }



    except Exception as e:


        return {

            "success":
                False,

            "error":
                str(e),

            "query":
                query

        }



def provider_status():

    return {

        "provider":
            "duckduckgo",

        "status":
            "ready"

    }