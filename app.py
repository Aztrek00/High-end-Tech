from flask import Flask, render_template, jsonify

app = Flask(__name__)

# GPU data
gpus = [
    {"name": "GeForce 256", "release_date": "1999", "memory": "32MB SDR", "core_clock": "120 MHz", "price": 299},
    {"name": "GeForce3", "release_date": "2001", "memory": "64MB DDR", "core_clock": "200 MHz", "price": 499},
    {"name": "GeForce FX 5800", "release_date": "2003", "memory": "128MB DDR", "core_clock": "500 MHz", "price": 399},
    {"name": "GeForce 6800 Ultra", "release_date": "2004", "memory": "256MB GDDR3", "core_clock": "400 MHz", "price": 499},
    {"name": "GeForce 8800 GTX", "release_date": "2006", "memory": "768MB GDDR3", "core_clock": "575 MHz", "price": 599},
    {"name": "GeForce GTX 280", "release_date": "2008", "memory": "1GB GDDR3", "core_clock": "602 MHz", "price": 649},
    {"name": "GeForce GTX 480", "release_date": "2010", "memory": "1.5GB GDDR5", "core_clock": "700 MHz", "price": 499},
    {"name": "GeForce GTX 680", "release_date": "2012", "memory": "2GB GDDR5", "core_clock": "1006 MHz", "price": 499},
    {"name": "GeForce GTX 980", "release_date": "2014", "memory": "4GB GDDR5", "core_clock": "1126 MHz", "price": 549},
    {"name": "GeForce GTX 1080", "release_date": "2016", "memory": "8GB GDDR5X", "core_clock": "1607 MHz", "price": 699},
    {"name": "GeForce RTX 2080 Ti", "release_date": "2018", "memory": "11GB GDDR6", "core_clock": "1350 MHz", "price": 1199},
    {"name": "GeForce RTX 3090", "release_date": "2020", "memory": "24GB GDDR6X", "core_clock": "1395 MHz", "price": 1499},
    {"name": "GeForce RTX 4090", "release_date": "2022", "memory": "24GB GDDR6X", "core_clock": "2235 MHz", "price": 1599},
]

@app.route('/')
def index():
    return render_template('index.html', gpus=gpus)

@app.route('/api/gpus')
def get_gpus():
    return jsonify(gpus)

if __name__ == '__main__':
    app.run(debug=True)
