"""
Traffic & Road Safety Dashboard
================================

This Streamlit application provides an interactive dashboard to visualize
accident risk on roads in selected Pakistani cities.  It uses a simple
dataset of road names with associated risk scores and geographic
coordinates to highlight the most dangerous segments and categorize
roads into high, medium and low‑risk categories.  The dashboard shows:

* A drop‑down to select a city.
* A map that highlights each road segment using three colours for risk
  categories (red for high, orange for medium, green for low).
* A table listing the top ten risky roads for the selected city and
  their risk percentages.
* A simple time‑series chart showing the trend of high‑risk segments
  over the last seven days (dummy data for demonstration).
* Tabs that display the roads belonging to each risk category.

To run this app you need to install the required libraries:

```
pip install streamlit pandas numpy matplotlib folium streamlit‑folium
```

Then start the dashboard with:

```
streamlit run traffic_dashboard.py
```

Ensure that the accompanying ``roads_data.csv`` file is located in
the same directory.  Replace or extend the CSV with real accident
statistics, risk scores and geographic coordinates for your own
project.  The current coordinates are approximate and for
demonstration only.
"""

import pandas as pd
import numpy as np
import streamlit as st
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt


def load_data(path: str) -> pd.DataFrame:
    """Load road risk data from a CSV file and compute risk categories.

    Parameters
    ----------
    path : str
        Path to the CSV file containing columns: city, road_name,
        risk_score, latitude, longitude.

    Returns
    -------
    pd.DataFrame
        DataFrame with an added risk_category column.
    """
    df = pd.read_csv(path)
    # Convert risk_score to numeric if loaded as string
    df['risk_score'] = pd.to_numeric(df['risk_score'], errors='coerce')
    # Classify risk categories
    def categorize_risk(score: float) -> str:
        if score >= 0.6:
            return 'High'
        elif score >= 0.3:
            return 'Medium'
        else:
            return 'Low'
    df['risk_category'] = df['risk_score'].apply(categorize_risk)
    return df


def main() -> None:
    """Run the Streamlit dashboard."""
    st.set_page_config(page_title="Traffic & Road Safety Dashboard", layout="wide")
    st.title("Traffic & Road Safety Dashboard")

    # Load data
    data = load_data('roads_data.csv')

    # City selection
    cities = sorted(data['city'].unique())
    selected_city = st.selectbox('Select City', cities)

    # Filter data for selected city
    city_data = data[data['city'] == selected_city]

    # Map display
    if not city_data.empty:
        # Compute map centre
        center_lat = city_data['latitude'].astype(float).mean()
        center_lon = city_data['longitude'].astype(float).mean()
        m = folium.Map(location=[center_lat, center_lon], zoom_start=12)
        # Colour mapping
        colour_map = {'High': 'red', 'Medium': 'orange', 'Low': 'green'}
        # Add circle markers for each road segment
        for _, row in city_data.iterrows():
            folium.CircleMarker(
                location=[float(row['latitude']), float(row['longitude'])],
                radius=6,
                popup=f"{row['road_name']} – Risk Score: {row['risk_score']:.2f}",
                color=colour_map.get(row['risk_category'], 'blue'),
                fill=True,
                fill_color=colour_map.get(row['risk_category'], 'blue'),
                fill_opacity=0.7
            ).add_to(m)
        st.subheader(f"Accident Risk Map of {selected_city}")
        st_folium(m, width=800, height=450)
    else:
        st.info("No data available for this city.")

    # Top 10 risky roads table
    st.subheader("Top Risky Roads")
    top = city_data.sort_values('risk_score', ascending=False).head(10).copy()
    # Calculate percentage for display (risk score × 100)
    top['risk_percentage'] = top['risk_score'] * 100
    top_display = top[['road_name', 'risk_percentage', 'risk_category']]
    top_display.rename(columns={'road_name': 'Road', 'risk_percentage': 'Risk (%)', 'risk_category': 'Category'}, inplace=True)
    # Format percentage
    top_display['Risk (%)'] = top_display['Risk (%)'].map(lambda x: f"{x:.1f}%")
    st.table(top_display)

    # Dummy high‑risk trend chart (last 7 days)
    st.subheader("High‑Risk Trend (Last 7 Days)")
    if not city_data.empty:
        # Use the mean risk score as a base for generating counts
        base = max(int(round(city_data['risk_score'].mean() * 10)), 1)
        np.random.seed(0)
        dates = pd.date_range(end=pd.Timestamp.today(), periods=7)
        counts = np.random.poisson(base, size=len(dates))
        fig, ax = plt.subplots()
        ax.plot(dates, counts, marker='o')
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of High‑Risk Segments')
        ax.set_title(f'High‑Risk Trend in {selected_city}')
        ax.grid(True)
        # Format x-axis labels
        fig.autofmt_xdate()
        st.pyplot(fig)
    else:
        st.write("Insufficient data to display risk trend.")

    # Tabs for risk categories
    st.subheader("Roads by Risk Category")
    high_tab, medium_tab, low_tab = st.tabs(["High Risk", "Medium Risk", "Low Risk"])
    with high_tab:
        st.write("High‑risk roads:")
        high_data = city_data[city_data['risk_category'] == 'High'][['road_name', 'risk_score']]
        high_data.rename(columns={'road_name': 'Road', 'risk_score': 'Score'}, inplace=True)
        st.table(high_data)
    with medium_tab:
        st.write("Medium‑risk roads:")
        med_data = city_data[city_data['risk_category'] == 'Medium'][['road_name', 'risk_score']]
        med_data.rename(columns={'road_name': 'Road', 'risk_score': 'Score'}, inplace=True)
        st.table(med_data)
    with low_tab:
        st.write("Low‑risk roads:")
        low_data = city_data[city_data['risk_category'] == 'Low'][['road_name', 'risk_score']]
        low_data.rename(columns={'road_name': 'Road', 'risk_score': 'Score'}, inplace=True)
        st.table(low_data)


if __name__ == '__main__':
    main()