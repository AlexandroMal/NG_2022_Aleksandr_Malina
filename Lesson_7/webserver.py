from flask import Flask, render_template, request, send_file, redirect
from download import *
from archiver import *

app = Flask("Downloader photo")


@app.route('/')
def index():
    return render_template ('index.html')


@app.route('/procces')
def procces():
    site_link = request.args.get('link')
    all_links = get_Links_photo(site_link)
    save_image(all_links, site_link)
    manager_zip()
    return redirect('/Download')

@app.route('/Download')
def download_zip():
    path = path_zipfile()
    return send_file(path)


    
app.run(host='0.0.0.0', port='8081')