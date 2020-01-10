from flask import Flask, render_template, json, jsonify, request


app = Flask('app')


@app.route('/')
def index_page():
  return render_template("chats.html")

@app.route('/health')
def health_page():
  return "OK"

@app.route('/chats/lasi')
def ielasit_chatu():
  lines = []
  fh = open('chats.txt', "r", encoding="UTF-8")
  for line in fh:
    lines.append(line)
  fh.close()
  return jsonify({"Chats":lines})

@app.route('/chats/suuti', methods = ['POST'])
def suutiit_zinju():
  dati = request.json
  with open("chats.txt", "a", newline="") as f:
    f.write(dati["chats"] + "\n")
  return ielasit_chatu()


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)