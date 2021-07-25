import streamlit as st
import pickle
import numpy as np
st.title("Jupitor Breast Cancer Detector ")

b = st.sidebar.number_input("mean radius")
c = st.sidebar.number_input("mean texture")
d = st.sidebar.number_input("mean perimeter")
e = st.sidebar.number_input("mean area")
f = st.sidebar.number_input("mean smoothness")
g = st.sidebar.number_input("mean compactness")
h = st.sidebar.number_input('mean concavity')
i = st.sidebar.number_input("mean concave points")
j = st.sidebar.number_input("mean symmetry")
k = st.sidebar.number_input("mean fractal dimension")
l = st.sidebar.number_input("radius error")
m = st.sidebar.number_input("texture error")
n = st.sidebar.number_input("perimeter error")
o = st.sidebar.number_input("area error")
p = st.sidebar.number_input("smoothness error")
q = st.sidebar.number_input("compactness error")
r = st.sidebar.number_input("concavity error")
s = st.sidebar.number_input("concave points error")
t = st.sidebar.number_input("symmetry error")
u = st.sidebar.number_input("fractal dimension error")
v = st.sidebar.number_input("wrost redius")
w = st.sidebar.number_input("wrost texture")
x = st.sidebar.number_input("wrost perimeter")
y = st.sidebar.number_input("wrost area")
z = st.sidebar.number_input("wrost smoothness")
ab = st.sidebar.number_input("wrost compactness")
cd = st.sidebar.number_input("worst concavity")
ef = st.sidebar.number_input("wrost concave points")
gh = st.sidebar.number_input("wrost symmetry")
ij = st.sidebar.number_input("wrost fractal dimension")



detect = st.button('Detect')

def predict():
    model = pickle.load(open('breast-cancer.pickle','rb')) 
    val = ([b ,c ,d ,e ,f ,g ,h ,i ,j ,k ,l ,m ,n , o , p , q , r ,s , t , u ,v ,w ,x ,y , z , ab , cd , ef , gh  , ij])
          
          

    val = np.array([val])

    result = model.predict(val)
    
    if (result[0] == 0):
        
        st.success("Malignant Tumor")
     
       
    else:
        st.error("Benign Tumor")
        
if(detect):
    predict()
