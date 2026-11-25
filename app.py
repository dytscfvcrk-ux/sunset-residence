
from flask import Flask, render_template, request, jsonify
import csv
import os
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/apartments")
def apartments():
    return render_template("apartments.html")


@app.route("/infrastructure")
def infrastructure():
    return render_template("infrastructure.html")


@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/send-message", methods=["POST"])
def send_message():
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()
    consent = request.form.get("consent")

    if not name or not phone or not consent:
        return jsonify({
            "error": "Заполните обязательные поля и подтвердите согласие."
        }), 400

    file_exists = os.path.exists("leads.csv")

    with open("leads.csv", "a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Дата",
                "Имя",
                "Телефон",
                "Email",
                "Сообщение"
            ])

        writer.writerow([
            datetime.now().strftime("%d.%m.%Y %H:%M"),
            name,
            phone,
            email,
            message
        ])

    return jsonify({"success": True})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
app.run(host="0.0.0.0", port=port, debug=True)
