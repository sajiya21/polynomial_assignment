from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def shortner():
    if request.method == "POST":

        time_stamp = datetime.now()

        # getting input with name = fname in HTML form
        url = request.form.get("url_input")

        key = request.form.get("key_input")
        if url == "":
            return "error"

        else:
            if key == None:
                user_ip = request.remote_addr
                url_id = url.split("/")[3].replace("watch?v=", '')

                # inserting into database
                data = {"_id": time_stamp,
                        "url": url_id,
                        "user_ip": user_ip
                        }

                # database insertion query

                result = requests.get(f"https://api.shrtco.de/v2/shorten?url={url}").json()
                shorten_url = result.get('result').get('full_short_link')

                print(shorten_url)

                return f"Your short url is {str(shorten_url)}"
            else:
                # encoding and decoding query
                str_encoded = (url, key)
                str_decoded = (url, key)
                return f"Your short url is {str_encoded},  {str_decoded}"

    return render_template("index.html")

