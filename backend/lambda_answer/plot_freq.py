import pandas as pd
import plotly.express as px
import plotly.io as pio
from backend.utils.compute_stats import stats_average, stats_squared_errors
from backend.utils.text_cleaner import plot_word_freqs

def data_stats(text):
    return {
        "average": stats_average(text),
        "errors": stats_squared_errors(text)
    }

def plot_count(text):
    # Create a simple plotly chart
    df = pd.DataFrame.from_records(list((plot_word_freqs(text)).items()), columns=['word','count'])
    fig = px.scatter(df, x='word', y='count')

    # Convert Plotly figure to HTML
    graph_html = pio.to_html(fig, full_html=False)

    return graph_html

def lambda_handler(event, context=None):
    return {
        "status_code": 200,
        "html_plot": plot_count(event)
    }

if __name__ == "__main__":
    example = """This work can be done without a doubt and can 
                always be done better, for sure!"""
    event_example = {"text": example}
    print(lambda_handler(event=event_example))
         