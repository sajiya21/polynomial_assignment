from flask import Flask, render_template, request
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

                return f"Your short url is {str(url)}"
            else:
                str_encoded = (url, key)
                str_decoded = (url, key)
                return f"{str_encoded},  {str_decoded}"

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)