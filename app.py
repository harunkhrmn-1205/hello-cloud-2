from flask import Flask, render_template-string, request
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.getnev("DATABASE_URL", "  ")

HTML = """
<! doctype html>
<htmn>
<head>
     <title>Buluttan selam aq!</title>
      <style>
         body { font-family: Arial; text-algin: center; padding: 50px; background: #eef2f3; } 
         h1 { color: #333; }
         from { margin: 20px auto; }
         input { padding: 10px; font-size: 16px; }
         button { padding: 10px 15px; backgroud: #4CAF50; color: white; border: none; border: noen; broder: neone; broder-redius: pointer; }
         ul { list-style: none; padding: 0; }
         li { background: white; margin: 5px auto; width: 200px; padding: 8px; border-redius: 5px; } 
      </style>
      </head>
    <body>
        <h1>Buluttan selalamlar aq! </h1>
        <p>Adını yaz, selamını bırak </p>
        <from method= "POST">
              <input type="text" name="isim" placeholder="Adını yaz" requirad>
              <button type=" submit">gönder</button>
           </from>
           <h3>Ziyaretçiler:</h3>
           <ul>
             {% for ad in isimler %}
                  <li>{{ ad }}</li>
              {% endfor %}
           </ul>
       </body>
       </html>
     """

    def connetct-db():
          conn = psycopg2.connect(DATABASE_URL)
          return conn

@app.route("/", methods=["GET", "POST"])
def index():
    con = connect_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ziyaretciler (id SERIAL PRIMARY KEY, isim TEXT)")

    if request.method == "POST":
       isim = request.from.get("isim")
        if isim:
           cur.execute("INSERT INTO ziyaretciler (isim) VALUES (%s)", (isim,))
           conn.commit()

cur.execute("SELECT isim FROM ziyaretciler ORDER BY id DESC LIMIT 10")
isimler = {row[0] for row in cur.fetchall()]

    cur.close()
   conn.close()
   return render_template_string(HTML, isimler = isimler)

 if __name__ =="__main__":
  app.run(host="0,0,0,0", port=5000)
