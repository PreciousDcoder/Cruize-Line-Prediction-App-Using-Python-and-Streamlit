import pickle
import streamlit as st

# Loading the trained model
with open('classifier.pkl', 'rb') as pickle_in:
    classifier = pickle.load(pickle_in)

@st.cache
def prediction(Total_cost, Room_costs, Ship_board_expenses, Casino_expenses, Excursion_expenses, Customer_satisfaction_average_of_all_questions, Overall_trip_satisfaction, Room_type):

    # Encode the Room_type into a numerical value
    room_type_mapping = {'Interior': 0, 'Oceanview': 1, 'Balcony': 2, 'Suite': 3}
    Room_type_encoded = room_type_mapping[Room_type]
    
    # Making Predictions
    pred = classifier.predict([[Total_cost, Room_costs, Ship_board_expenses, Casino_expenses, Excursion_expenses, Customer_satisfaction_average_of_all_questions, Overall_trip_satisfaction, Room_type_encoded]])

    if pred == 0:
        return "Will Not Travel Again"
    else:
        return "Will Travel Again"

# This is the main function in which we define our webpage
def main():
    # Front end elements of the web page
    html_temp = '''
    <div style="background-color: #F4D03F; padding:10px">
    <h2 style="color: black; text-align: center;">Cruize Line Prediction App</h2>
    </div>
    '''
    # Display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input fields for user data
    Total_cost = st.number_input("Total cost")
    Room_costs = st.number_input("Room costs")
    Ship_board_expenses = st.number_input("Boarding expenses")
    Casino_expenses = st.number_input("Casino expenses")
    Excursion_expenses = st.number_input("Excursion expenses")
    Customer_satisfaction_average_of_all_questions = st.number_input("Customer satisfaction average")
    Overall_trip_satisfaction = st.number_input("Overall trip satisfaction")

    # Dropdown for Room Type selection
    Room_type = st.selectbox("Select Room Type", ['Interior', 'Oceanview', 'Balcony', 'Suite'])

    result = ""

    # When 'Predict' is clicked, make prediction and store it
    if st.button("Predict"):
        result = prediction(Total_cost, Room_costs, Ship_board_expenses, Casino_expenses, Excursion_expenses, 
                            Customer_satisfaction_average_of_all_questions, Overall_trip_satisfaction, Room_type)
        st.success(f"Prediction: {result}")

if __name__ == '__main__':
    main()
