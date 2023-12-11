from flask import Flask, redirect, render_template, request

from phone_recommender.pipeline.stage_06_prediction import UserPredictionPipeline

app = Flask(__name__, template_folder='templates', static_folder="staticFiles")


@app.route("/")
def index():
    return redirect("/base")


@app.route("/base")
def base():
    return redirect("/home")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/recommend")
def recommend():
    return render_template("recommend.html")


@app.route("/recommendation", methods=["POST"])
def recommendation():
    results = request.form
    prediction = UserPredictionPipeline()
    recommendation = prediction.main(user_data=results)
    recommendation = list(recommendation.values)
    return render_template("recommend.html", recommendation=recommendation)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
