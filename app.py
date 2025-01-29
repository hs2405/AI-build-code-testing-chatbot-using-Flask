from flask import Flask, render_template, request
import sys
import io

app = Flask(__name__)

# Function to execute the user code and capture output or error
def execute_code(user_code):
    try:
        # Redirect stdout to capture print statements from the code
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Execute the user-provided code
        exec(user_code)

        # Restore the original stdout
        sys.stdout = sys.__stdout__

        return "Code executed successfully! Output:\n" + captured_output.getvalue()

    except Exception as e:
        # If an exception occurs, capture the error message
        sys.stdout = sys.__stdout__  # Restore the original stdout
        return f"Error in code:\n{str(e)}"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_code = request.form["code"]
        result = execute_code(user_code)
        return render_template("index.html", result=result)
    return render_template("index.html", result="")

if __name__ == "__main__":
    app.run(debug=True)
