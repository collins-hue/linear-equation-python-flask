from flask import Flask, render_template, request
import sympy

app = Flask(__name__,  template_folder='Templates')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/solve', methods=['POST'])
def solve():
    equation = request.form['equation']
    x = sympy.symbols('x')
    try:
        # Parse and solve the equation
        equation = sympy.sympify(equation)
        solution = sympy.solve(equation, x)
        return render_template('result.html', equation=equation, solution=solution)
    except (sympy.SympifyError, ValueError):
        return render_template('result.html', equation=equation, solution="Invalid equation")

if __name__ == '__main__':
    app.run(debug=True)
