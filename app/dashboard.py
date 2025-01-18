from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load applied jobs
applied_jobs_file = "data/applied_jobs.csv"

# Load applied jobs
def get_applied_jobs():
    try:
        return pd.read_csv(applied_jobs_file).to_dict(orient="records")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []  # Return an empty list if the file doesn't exist or is empty

@app.route("/")
def home():
    jobs = get_applied_jobs()
    return render_template("dashboard.html", jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True)
