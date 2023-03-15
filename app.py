from flask import Flask ,render_template
import requests


app = Flask(__name__)

CHANNELS = {
  'qazi': 'UCqrILQNl5Ed9Dz6CGMyvMTQ',
  'mrbeast': 'UCX6OQ3DkcsbYNE6H8uQQuVA',
  'mkbhd': 'UCBJycsmduvYEL83R_U4JriQ',
  'pm': 'UC3DkFux8Iv-aYnTRWzwaiBA',
}


@app.route('/')
def index():
  url = "https://youtube138.p.rapidapi.com/channel/videos/"

  querystring = {"id":CHANNELS["pm"],"hl":"en","gl":"US"}

  headers = {
	"X-RapidAPI-Key": "a8d1dbdc0emsha554d3086e33539p1e4b31jsnd98555b7510e",
	"X-RapidAPI-Host": "youtube138.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  data =response.json()
  contends =data["contents"]

  filtereddata = [videos["video"] for videos in contends if videos["video"]["publishedTimeText"] ]
  

  return render_template("index.html",filtereddata=filtereddata)
  
app.run(host='0.0.0.0', port=81)