# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "pandas",
#   "seaborn",
#   "matplotlib",
#   "numpy",
#   "scipy",
#   "openai",
#   "scikit-learn",
#   "requests",
#   "ipykernel",
#   "python-dotenv"
# ]
# ///

import os
from dotenv import load_dotenv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json
from datetime import datetime
from tabulate import tabulate
from scipy import stats

# Load the .env file from the specified directory
def load_env(file_name):
    dotenv_path = os.path.join("C:/Users/91735/OneDrive/Desktop/Analysis", file_name)
    load_dotenv(dotenv_path)
    return os.environ.get("AIPROXY_TOKEN")

# Initialize OpenAI API
def init_openai_api():
    api_token = load_env("myfile.env")
    if not api_token:
        raise ValueError("Error: AIPROXY_TOKEN not found in .env file.")
    return {
        "base_url": "https://aiproxy.sanand.workers.dev/openai/v1",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_token}"
        }
    }

# Read CSV with fallback encoding
def read_csv(filename):
    try:
        return pd.read_csv(filename, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(filename, encoding="latin1")
    except Exception as e:
        raise ValueError(f"Error loading {filename}: {e}")

# Perform basic analysis on the dataset
def analyze_data(df):
    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum().to_dict(),
        "summary_statistics": df.describe(include="all").to_dict()
    }

# Generate visualizations and save as images
def generate_visualizations(df, output_prefix):
    charts = []

    numeric_columns = df.select_dtypes(include=["number"]).columns
    if numeric_columns.empty:
        return charts

    # Correlation Heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[numeric_columns].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    heatmap_file = f"{output_prefix}_heatmap.png"
    plt.title("Correlation Heatmap")
    plt.savefig(heatmap_file, dpi=100, bbox_inches='tight')
    charts.append(heatmap_file)
    plt.close()

    # Histograms
    for col in numeric_columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[col], kde=True, bins=30)
        plt.title(f"Distribution of {col}")
        hist_file = f"{output_prefix}_{col}_hist.png"
        plt.savefig(hist_file, dpi=100, bbox_inches='tight')
        charts.append(hist_file)
        plt.close()

    return charts

# Construct a dynamic prompt for the LLM
def construct_prompt(analysis, charts, filename):
    chart_descriptions = "\n".join([f"- {chart}" for chart in charts])
    return f"""
    I analyzed a dataset from {filename}. Here are the details:
    - Shape: {analysis['shape']}
    - Columns: {analysis['columns']}
    - Missing Values: {analysis['missing_values']}
    - Summary Statistics: {analysis['summary_statistics']}
    
    The following charts were generated:
    {chart_descriptions}
    
    Write a detailed report summarizing the dataset, the analyses conducted, key insights derived, and actionable recommendations based on these insights.
    """

# Generate a detailed story from the LLM
def narrate_story(api, analysis, charts, filename):
    prompt = construct_prompt(analysis, charts, filename)
    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(
            f"{api['base_url']}/chat/completions", 
            headers=api['headers'], 
            json=data
        )
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Story generation failed: {e}"

# Save story and visualizations to a markdown file
def save_readme(story, charts, output_file):
    with open(output_file, "w") as f:
        f.write("# Analysis Report\n\n")
        f.write(story + "\n\n")
        for chart in charts:
            f.write(f"![Chart](./{chart})\n")

# Generate unique filename
def generate_unique_filename(filename):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename, extension = os.path.splitext(filename)
    return f"{filename}_{timestamp}{extension}"

# Main script execution
def main():
    folder_path = "C:/Users/91735/OneDrive/Desktop/Analysis"

    try:
        os.chdir(folder_path)
    except Exception as e:
        raise ValueError(f"Error accessing folder {folder_path}: {e}")

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    if not csv_files:
        print("No CSV files found in the directory.")
        return

    api = init_openai_api()

    for filename in csv_files:
        filepath = os.path.join(folder_path, filename)
        df = read_csv(filepath)
        analysis = analyze_data(df)
        output_prefix = os.path.splitext(filename)[0]
        charts = generate_visualizations(df, output_prefix)
        story = narrate_story(api, analysis, charts, filename)
        readme_file = generate_unique_filename(f"README_{output_prefix}.md")
        save_readme(story, charts, readme_file)
        print(f"Analysis completed for {filename}. Check {readme_file} and charts.")

if __name__ == "__main__":
    main()
