import streamlit as st
import pickle 
import pandas as pd

# load model
model = pickle.load(open('final_xg', 'rb'))

# Streamlit app
def predict_diamond_price(input_data):
    prediction = model.predict(input_data)
    return prediction

def main():
    st.set_page_config(page_title='Diamond Price Prediction App', page_icon='💎')
    st.title('Diamond Price Prediction App 💎')

    # make the page light mode
    st.markdown('<style>body{color: black; background-color: white}</style>', unsafe_allow_html=True)
    
    # Collecting user input for each feature with descriptions
    carat = st.number_input('Carat (Weight of the diamond)', value=1.00, format="%.2f")
    cut = st.selectbox('Cut (Quality of the cut)', ['Ideal', 'Premium', 'Very Good', 'Good', 'Fair'], index=1)
    color = st.selectbox('Color (Color grade of the diamond)', ['D', 'E', 'F', 'G', 'H', 'I', 'J'], index=3)  
    clarity = st.selectbox('Clarity (Measure of how clear the diamond is)', ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'], index=6)  
    depth = st.number_input('Depth (Depth %, total depth relative to diameter)', value=60.9, format="%.2f")
    table = st.number_input('Table (Table %, width of the top of the diamond relative to widest point)', value=50.0, format="%.2f")
    x = st.number_input('X (Length in mm)', value=4.00, format="%.2f")
    y = st.number_input('Y (Width in mm)', value=8.00, format="%.2f")
    z = st.number_input('Z (Depth in mm)', value=7.00, format="%.2f")
    
    if st.button('Predict Price'):
        input_data = pd.DataFrame([[
            carat, cut, color, clarity, depth, table, x, y, z
        ]], columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z'])
        
        # Predict the price
        price = predict_diamond_price(input_data)
        
        st.write(f'Predicted Diamond Price: ${price[0]:.2f}')

if __name__ == '__main__':
    main()