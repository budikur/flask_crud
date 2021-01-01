from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app=Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == "POST":
        nama= request.form['nama']
        alamat= request.form['alamat']
        prodi= request.form['prodi']
        db=sqlite3.connect('crud.db')
        cur=db.cursor()
        cur.execute("INSERT INTO mahasiswa(nama,alamat,prodi) VALUES('"+nama+"','"+alamat+"','"+prodi+"') ")
        db.commit()
        return render_template('berhasil.html')
    return render_template('create.html')

@app.route('/read')
def read():
    db= sqlite3.connect('crud.db')
    cur=db.cursor()
    cur.execute("SELECT * FROM mahasiswa")
    hasilnya=cur.fetchall()
    return render_template('read.html',hasilnya=hasilnya)

@app.route('/update', methods=['GET','POST'])
def update():
    if request.method == "POST":
        nom=request.form['nomor']
        db = sqlite3.connect('crud.db')
        cur = db.cursor()
        cur.execute("SELECT * FROM mahasiswa WHERE no='"+nom+"' ")
        isiupdate = cur.fetchone()
        return render_template('update.html',isiupdate=isiupdate)
    return render_template('index.html')

@app.route('/isiupdate', methods=['GET','POST'])
def isiupdate():
    if request.method == "POST":
        nom=request.form['nomor']
        nam=request.form['nama']
        alam=request.form['alamat']
        prod=request.form['prodi']
        db = sqlite3.connect('crud.db')
        cur = db.cursor()
        cur.execute("UPDATE mahasiswa SET nama='"+nam+"',alamat='"+alam+"',prodi='"+prod+"' WHERE no='"+nom+"' ")
        db.commit()
        return render_template('berhasil.html')
    return render_template('index.html')

@app.route('/delete', methods=['GET','POST'])
def delete():
    if request.method == "POST":
        nom=request.form['nomor']
        db = sqlite3.connect('crud.db')
        cur = db.cursor()
        cur.execute("DELETE FROM mahasiswa WHERE no='"+nom+"' ")
        db.commit()
        return redirect('delete')
    db= sqlite3.connect('crud.db')
    cur=db.cursor()
    cur.execute("SELECT * FROM mahasiswa")
    hasilnya=cur.fetchall()
    return render_template('delete.html',hasilnya=hasilnya)

app.secret_key='Keyanda'
if __name__== "__main__":
    app.run(debug=True)
