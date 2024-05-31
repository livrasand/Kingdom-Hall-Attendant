# proxy_wol.py

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/proxy-wol')
def proxy_wol():
    year = request.args.get('year')
    week = request.args.get('week')
    url = f'https://wol.jw.org/es/wol/meetings/r4/lp-s/{year}/{week}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Failed to fetch data from WOL'}), 500

if __name__ == '__main__':
    app.run(debug=True)
