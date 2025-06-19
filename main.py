from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials
app = Flask(__name__)
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', SCOPES)
gc = gspread.authorize(creds)
SPREADSHEET_NAME = 'Popular_Items'
sheet = gc.open(SPREADSHEET_NAME).sheet1
@app.route('/')
def index():
    records = sheet.get_all_records()
    return render_template('home.html', records=records)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sale')
def sale():
    return render_template('sale.html')

@app.route('/dogCatalog')
def dogCatalog():
    return render_template('dogCatalog.html')

@app.route('/riderCatalog')
def riderCatalog():
    return render_template('riderCatalog.html')

@app.route('/horseCatalog')
def horseCatalog():
    return render_template('horseCatalog.html')

@app.route('/stableCatalog')
def stableCatalog():
    return render_template('stableCatalog.html')

if __name__ == '__main__':
    app.run(debug=True)