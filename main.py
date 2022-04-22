from flask import Flask, render_template, request
from datetime import datetime
from Utils.security import url_encrypt, url_decrypt
import requests
import socket
from Utils.database import Database

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
            if key is None:
                # user_ip = request.remote_addr

                hostname = socket.gethostname()
                user_ip = socket.gethostbyname(hostname)

                url_id = url.split("/")[3].replace("watch?v=", '')

                # inserting into database
                data = {"_id": time_stamp,
                        "url": url_id,
                        "user_ip": user_ip
                        }

                # insertion query
                Database().insertion(data)

                result = requests.get(f"https://api.shrtco.de/v2/shorten?url={url}").json()
                shorten_url = result.get('result').get('full_short_link')

                return f"Your short url is {str(shorten_url)}"
            else:
                str_encoded = url_encrypt(url, key)
                str_decoded = url_decrypt(url, key)
                return f"{str_encoded},  {str_decoded}"

    return render_template("index.html")


@app.route('/video', methods =["GET", "POST"])
def video():
    latest_url, entire_data = Database().search()
    return render_template("video.html", latest_url=latest_url)


@app.route('/track', methods =["GET", "POST"])
def track():
    latest_url, entire_data = Database().search()
    entire_data.reverse()
    return render_template('track.html', data=entire_data)


if __name__ == '__main__':
    app.run(debug=True)