from flask import Flask
from flask.templating import render_template
from model.loggerCleaner import load_log_from_file as log
from model.loggerCleaner import add_html_tolog as aht

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    log_data = log(filename='temp/scraper.log')
    data = aht(log_data, tag='li',style='list-group-item')
    #breakpoint()

    return render_template('index.html', data=data)


if __name__=="__main__":
    app.run(port=5050, debug=True)

