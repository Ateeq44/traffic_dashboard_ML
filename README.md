Traffic & Road Safety Dashboard

This repository contains a sample Traffic & Road Safety Dashboard built with
Streamlit
. It uses a CSV file of road segments
and associated risk scores to display an interactive map and simple
analytics for different Pakistani cities. The goal of the project
is to demonstrate how machine‑learning and data visualization can be
used to identify high‑risk roads and inform traffic safety interventions.

Features

City selector – choose between Karachi, Lahore and Sargodha via a
drop‑down menu. The selected city's roads are highlighted on an
interactive map.

Colour‑coded risk map – each road segment is drawn as a circle
marker on the map. Red indicates high risk, orange indicates
medium risk and green indicates low risk.

Top 10 risky roads – a table lists the ten roads with the
highest risk scores for the selected city, along with the risk
percentage and category.

High‑risk trend chart – a simple line chart shows how the number
of high‑risk segments changes over the last seven days. The
provided implementation uses dummy data; you can replace it with
real time‑series accident counts.

Category tabs – separate tabs display high‑, medium‑ and
low‑risk roads for the selected city.

Files
File	Description
traffic_dashboard.py	Streamlit app that powers the dashboard. Run this file to start the local server.
roads_data.csv	Sample dataset containing road names, risk scores and approximate latitude/longitude for Karachi, Lahore and Sargodha. Replace or extend this file with real accident data and model predictions.
traffic_road_safety_dashboard.md	Research report summarizing the methodology used to identify high‑risk roads and the underlying sources. Useful for background and citations.
README.md	You are reading it.
Requirements

The app requires Python 3.7 or higher and a few common data science
libraries. You can install the dependencies with pip:

pip install streamlit pandas numpy matplotlib folium streamlit-folium


If pip is not recognised on your system, use python -m pip or
py -m pip instead. See the installation instructions

for more details.

Running the dashboard

Clone or download this repository and make sure the files
(traffic_dashboard.py and roads_data.csv) are in the same
folder.

Open a terminal or command prompt and navigate to the folder
containing the files:

cd path/to/your/folder


Install the required libraries if you haven't already:

python -m pip install streamlit pandas numpy matplotlib folium streamlit-folium


Run the Streamlit app:

python -m streamlit run traffic_dashboard.py


A local web server will start and display a link similar to
http://localhost:8501. Streamlit will usually open your
default browser automatically. If not, copy the URL into your
browser to view the dashboard.

Customising the data

The provided roads_data.csv file contains a small sample of road
segments with approximate geographic coordinates and dummy risk
scores. To use the dashboard with your own accident data or
machine‑learning predictions:

Replace the entries in roads_data.csv with your own
information. The file must have the following columns:

city – name of the city (e.g. Karachi, Lahore, Sargodha).

road_name – descriptive name of the road or intersection.

risk_score – numeric risk value between 0 and 1 (higher
indicates more dangerous). Scores ≥0.6 are classified as high
risk, scores between 0.3 and 0.6 as medium risk, and scores <0.3
as low risk.

latitude and longitude – coordinates for placing the marker
on the map.

If you use a machine‑learning model to predict risk scores,
generate these scores as part of your data pipeline and write
them to the CSV file before launching the dashboard.

Restart the Streamlit app to load the updated data.

License

This project is provided for educational purposes and may be used or
adapted freely. See the license file or add your own licensing
information if necessary.

Acknowledgements

The methodology for identifying high‑risk roads and the initial
dataset were derived from publicly available accident reports,
academic research and news articles. See
traffic_road_safety_dashboard.md for citations and detailed
explanations.
