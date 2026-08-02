from datetime import datetime

import requests

from bs4 import BeautifulSoup



def read_page(
    url
):

    try:

        response = requests.get(

            url,

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


        for tag in soup.find_all(
            [
                "script",
                "style",
                "nav",
                "footer",
                "header"
            ]
        ):

            tag.decompose()



        text = soup.get_text(

            " ",

            strip=True

        )



        # Estetty sivu

        blocked_words = [

            "Just a moment",

            "Enable JavaScript",

            "Checking your browser",

            "Access denied"

        ]


        for word in blocked_words:

            if word in text:

                return {

                    "success":
                        False,

                    "time":
                        datetime.now().isoformat(),

                    "url":
                        url,

                    "error":
                        "Sivu esti automaattisen luvun"

                }



        return {

            "success":
                True,

            "time":
                datetime.now().isoformat(),

            "url":
                url,

            "length":
                len(text),

            "content":
                text[:3000]

        }



    except Exception as e:


        return {

            "success":
                False,

            "time":
                datetime.now().isoformat(),

            "url":
                url,

            "error":
                str(e)

        }



def read_pages(
    urls
):

    results = []


    for url in urls:

        results.append(

            read_page(
                url
            )

        )


    return {

        "success":
            True,

        "time":
            datetime.now().isoformat(),

        "pages":
            results

    }



def reader_status():

    return {

        "module":
            "web_reader",

        "status":
            "ready"

    }