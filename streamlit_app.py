import folium
import numpy as np
import earthpy as et
from glob import glob
from osgeo import gdal
import rasterio as rio
import geopandas as gpd
import earthpy.plot as ep
import earthpy.spatial as es
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from matplotlib.colors import ListedColormap
from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt

st.write("""
# Simple Satellite Image Analysis App
This app can visualise and download satellite data through sentinalsat API
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

m = folium.Map([50.6, -1.3], zoom_start=3)
boundsdata = r'map (1).geojson'
folium.GeoJson(boundsdata).add_to(m)
m


'''
iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
'''
