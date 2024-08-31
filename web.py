import streamlit as st 
import pickle




streams = ['Civil',
 'Computer Science',
 'Electrical',
 'Electronics And Communication',
 'Information Technology',
 'Mechanical']
genders = ['Female', 'Male']



def load_model():
 	with open("model.pkl","rb") as f:
 		model = pickle.load(f)
 	return model 




def set_value(val):
	if val == False:
		val = 0
	else:
		val = 1

	return val




model = load_model()





st.title("Engineering Placement Predictions")



age = st.slider("Age",19,30)
cgpa = st.slider("You CGPA",5,10)
internships = st.checkbox("Have you done any Internships ?")
hostel = st.checkbox("You lived in Hostel ?")
backlogs  = st.checkbox("You have any Backlogs ?")
stream = st.selectbox("What is Your Stream ?",streams)
gender = st.selectbox("What is Your Gender?",genders)



internships = set_value(internships)
backlogs  = set_value(backlogs)
hostel =  set_value(hostel)





values =  [age,internships,cgpa,hostel,backlogs,streams.index(stream),genders.index(gender)]

predict = st.button("Predict")


if predict:
	prediction  = model.predict([values])[0]
	if prediction == 1:
		st.success("The Student Will get Placed ")

	if prediction == 0:
		st.info("Student Will Not Get Placed ")

