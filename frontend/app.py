from flask import Flask, render_template
from backend.lambda_answer.plot_freq import lambda_handler as plot_handler
from backend.lambda_find_docs.search_docs import lambda_handler as find_docs_handler

app = Flask(__name__)

@app.route('/')
def index():
    # Create a simple plotly chart
    input_text = input("Please enter text:")
    if input_text == "a":
        input_text = "aws aws sage aws route html aws"

    # Convert Plotly figure to HTML
    graph_html = plot_handler(input_text).get("html_plot")

    docs = find_docs_handler(input_text).get("docs")
    print(f"these are the {docs=}")

    return render_template('index.html',
                           graph_html=graph_html,
                           docs_found=docs,
                           event=input_text)

if __name__ == '__main__':
    app.run(debug=True)
