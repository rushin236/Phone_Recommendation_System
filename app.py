from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)

from src.phone_recommender.pipeline.stage_06_prediction import UserPredictionPipeline

app = Flask(__name__)
app.secret_key = "123"


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


@app.route("/")
def index():
    return redirect("/base")


@app.route("/base")
def base():
    return redirect("/home")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/recommend", methods=["POST", "GET"])
def recommend():
    if request.method == "POST":
        results = request.form
        if int(results['lower_price']) > int(results['upper_price']):
            flash(
                f"Lower Limit Price {int(results['lower_price'])} Cannot be grater than Upper Limit Price {int(results['upper_price'])}!",
                category='error',
            )
            return redirect(url_for("recommend"))
        else:
            prediction = UserPredictionPipeline()
            recommendation = prediction.main(user_data=results)
            if len(recommendation) != 0:
                recommendation = list(recommendation.values)
                return render_template("recommend.html", recommendation=recommendation)
            else:
                flash(
                    f"No recommendations found for {' '.join([value for key, value in results.items() if key not in ['lower_price', 'upper_price']])} given specifications! change the inputs and try again!",
                    category='error',
                )
                return redirect(url_for("recommend"))
    elif request.method == "GET":
        return render_template("recommend.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
