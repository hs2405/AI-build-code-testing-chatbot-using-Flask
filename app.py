from flask import Flask, render_template, request
import sys
import io

app = Flask(__name__)

def execute_code(user_code):
    try:
        captured_output = io.StringIO()
        sys.stdout = captured_output

        exec(user_code)

        sys.stdout = sys.__stdout__

        return "Code executed successfully! Output:\n" + captured_output.getvalue()

    except Exception as e:
        
      sys.stdout = sys.__stdout__  
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
