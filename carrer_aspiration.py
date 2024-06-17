import streamlit as st

# Import necessary libraries
import streamlit_authenticator as stauth
import yaml
from streamlit_authenticator import Authenticate
from yaml.loader import SafeLoader

# Load configuration from a YAML file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Initialize the authenticator
authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Rename the login page to "Career Analysis and Aspiration Project"
name, authentication_status, username = authenticator.login('Career Analysis and Aspiration Project', 'main')

# Check authentication status
if authentication_status:
    authenticator.logout('Logout', 'main')
    # Change the welcome message
    st.title(f'Welcome to the Career Analysis and Aspiration Project, {name}!')


    import streamlit as st
    import seaborn as sns

    st.set_option('deprecation.showPyplotGlobalUse', False)
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    import csv
    import mysql.connector

    dataset1 = pd.read_csv("carrer.csv")

    # mysql connection settings
    database = mysql.connector.connect(host="localhost", user="root", password="", database="career")
    cur = database.cursor()

    st.sidebar.title("Select an option:")
    action1 = "Survey"
    action2 = "Analysis"

    action_choice = st.sidebar.selectbox("Select an option", (action1, action2))

    if action_choice == action1:
        st.title("SURVEY FORM")
        with st.form("Survey form"):
            # district selection
            # q1 district
            st.info("Please fill the form to analyse the dataset for career aspirations")
            district1 = "Bangalore"
            district2 = "Gulbarga"
            district3 = "Raichur"
            district4 = "Other"
            district_choice_other = ""
            selected_district = ""

            district_choice = st.selectbox("Enter Your District", (district1, district2, district3, district4))
            if district_choice == district4:
                district_choice_other = st.text_input("Enter other district from where you are:")

            # higher education preference
            # q2
            question_2 = "Would you pursue higher education/post graduate outside the India, if you have to self sponsor it."
            q2o1 = "Yes, i will earn and do that"
            q2o2 = "No, but if someone would bare the cost ,I will do it"
            q2_answer = st.radio(question_2, [q2o1, q2o2])

            q3 = "PIN code"
            q3ans = st.number_input(q3,step=1)

            q4 = "Gender"
            male = "Male"
            female = "Female"
            q4ans = st.radio(q4, [male, female])

            q5 = "Which of the following factors influence the most about your career aspirations"
            q5o1 = "People who have changed the world for better"
            q5o2 = "Social Media like LinkedIn"
            q5o3 = "My Parents"

            q5_ans = st.radio(q5, [q5o1, q5o2])

            q15 = "How likely is that you will work for one employer for 3 years or more ?"
            q151 = "This will be hard to do, but if it is the right company I would try"
            q152 = "Will work for 3 years or more"
            q15ans = st.radio(q15, (q151, q152))

            q6 = "Would you work for a company whose mission is not clearly defined and publicly posted."
            q6o1 = "Yes"
            q6o2 = "No"

            q6_ans = st.radio(q6, [q6o1, q6o2])

            q7 = "How likely would you work for a company whose mission is misaligned with their public actions or even their product ?"
            q71 = "Will work for them"
            q72 = "Will not work for them"
            q7_ans = st.selectbox(q7, (q71, q72))

            q8 = "How likely would you work for a company whose mission is not bringing social impact ?"

            q8a = st.selectbox(q8, ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'))

            q9 = "What is the most preferred working environment for you."
            q91 = "Remote"
            q92 = "Office"
            q93 = "Hybrid (Office + Home)"

            q9a = st.radio(q9, [q91, q92, q93])

            q10 = "Which of the below Employers would you work with."
            q101 = "Employer who pushes your limits by enabling an learning environment, and rewards you at the end"
            q102 = "Employer who appreciates learning and enables that environment"
            q10a = st.selectbox(q10, (q101, q102))

            q11 = "Which type of learning environment that you are most likely to work in ?"
            q111 = "Instructor or Expert Learning Programs, Trial and error by doing side projects within the company"
            q112 = "Self Paced Learning Portals, Instructor or Expert Learning Programs"

            q11a = st.radio(q11, (q111, q112))

            q12 = "Which of the below careers looks close to your Aspirational job ?"
            q121 = "Business Operation"
            q122 = "Design and Developement"
            q123 = "Teaching"
            q124 = "Design and Creative strategy"

            q12a = st.radio(q12, (q121, q122, q123, q124))

            q13 = "What type of Manager would you work without looking into your watch ?"
            q131 = "Manager who explains what is expected, sets a goal and helps achieve it"
            q132 = "Manager who sets goal and helps me achieve it"

            q13a = st.radio(q13, (q131, q132))

            q14 = "Which of the following setup you would like to work ?"
            q141 = "Work alone"
            q142 = "Work alone, Work with 2 to 3 people in my team"
            q143 = "Work with 5 to 6 people in my team"
            q144 = "Work with 7 to 10 or more people in my team"
            q145 = "Work with more than 10 people in my team"

            q14a = st.radio(q14, (q141, q142, q143, q144, q145))
            submit_button = st.form_submit_button("Submit")

            if submit_button:
                st.subheader("Response:")
                if district_choice:
                    selected_district = district_choice

                if district_choice_other:
                    selected_district = district_choice_other

                # values selected
                st.write(f"District:")
                st.success(selected_district)
                st.write(question_2)
                st.success(q2_answer)
                st.write(q3)
                st.success(q3ans)
                st.write(q4)
                st.success(q4ans)
                st.write(q5)
                st.success(q5_ans)
                st.write(q15)
                st.success(q15ans)
                st.write(q6)
                st.success(q6_ans)
                st.write(q7)
                st.success(q7_ans)
                st.write(q8)
                st.success(q8a)
                st.write(q9)
                st.success(q9a)
                st.write(q10)
                st.success(q10a)
                st.write(q11)
                st.success(q11a)
                st.write(q12)
                st.success(q12a)
                st.write(q13)
                st.success(q13a)
                st.write(q14)
                st.success(q14a)

                # databse insertion
                try:
                    # CREATE TABLE SurveyResponses ( ID INT PRIMARY KEY AUTO_INCREMENT, District VARCHAR(255),
                    # HigherEducationPreference VARCHAR(255), PINCode INT, Gender VARCHAR(10),
                    # CareerAspirationsFactor VARCHAR(255), WorkDurationPreference VARCHAR(255),
                    # MissionClarityPreference VARCHAR(3), MissionAlignmentPreference VARCHAR(3),
                    # SocialImpactPreference INT, WorkingEnvironmentPreference VARCHAR(255), EmployerPreference VARCHAR(255),
                    # LearningEnvironmentPreference VARCHAR(255), CareerPreference VARCHAR(255),
                    # ManagerTypePreference VARCHAR(255), TeamSizePreference VARCHAR(255) );
                    sql = "insert into surveyresponses(District,HigherEducationPreference,PINCode,Gender,CareerAspirationsFactor,WorkDurationPreference,MissionClarityPreference,MissionAlignmentPreference,SocialImpactPreference,WorkingEnvironmentPreference,EmployerPreference,LearningEnvironmentPreference,CareerPreference,ManagerTypePreference,TeamSizePreference)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (selected_district, q2_answer, q3ans, q4ans, q5_ans, q15ans, q6_ans, q7_ans, q8a, q9a, q10a, q11a,
                    q12a, q13a, q14a)
                    cur.execute(sql, val)
                    database.commit()
                    st.success("Registration Successful")
                    st.write(cur.rowcount, "Record inserted")

                except Exception as e:
                    print(e)

    if action_choice == action2:
        ao1 = "Higher Education"
        ao2 = "Job"
        ao3 = "Work Type"
        ao4 = "Working Period on same Company"
        ao5="All data present in Database"

        visual_choice = st.sidebar.selectbox("Select the aspiration parameter", (ao1, ao2, ao3, ao4,ao5))
        # highrer education
        if visual_choice == ao1:

            st.title("Higher Education Analysis")
            st.header("District stats")

            district_counts = dataset1['Enter your District'].value_counts()
            raichur_count = district_counts['Raichur']
            gulbarga_count = district_counts['Gulbarga']
            bangalore_count = district_counts['Bangalore']
            delhi_count = district_counts['Delhi']
            plt.pie(district_counts, labels=['Raichur', 'Gulbarga', 'Bangalore', 'Delhi'], autopct='%.2f%%',radius=0.5)
            st.pyplot()

            st.write("RAICHUR")
            st.success(raichur_count)
            st.write("GULBARGA")
            st.success(gulbarga_count)
            st.write("BANGALORE")
            st.success(bangalore_count)
            st.write("DELHI")
            st.success(delhi_count)
            raichur_percentage = (raichur_count / (
                        raichur_count + gulbarga_count + bangalore_count + delhi_count)) * 100
            gulbarga_percentage = (gulbarga_count / (
                        raichur_count + gulbarga_count + bangalore_count + delhi_count)) * 100
            bangalore_percentage = (bangalore_count / (
                    raichur_count + gulbarga_count + bangalore_count + delhi_count)) * 100
            delhi_percentage = (delhi_count / (raichur_count + gulbarga_count + bangalore_count + delhi_count)) * 100
            st.write("RAICHUR PERCENTAGE:")
            st.success(raichur_percentage)
            st.write("GULBARGA PERCENTAGE:")
            st.success(gulbarga_percentage)
            st.write("BANGALORE PERCENTAGE:")
            st.success(bangalore_percentage)
            st.write("DELHI PERCENTAGE:")
            st.success(delhi_percentage)

            #################################################
            st.header(
                "Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.")
            results = "Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it."

            # Create the countplot using the specified column
            sns.countplot(x=results, data=dataset1)

            # Calculate counts
            higher_education_counts = dataset1[results].value_counts()

            # Add count labels on top of the bars

            # Get counts for 'Yes' and 'No'
            yes_count = higher_education_counts.get('Yes', 0)
            no_count = higher_education_counts.get('No', 0)

            plt.xlabel('Response')

            # Show the plot using Streamlit
            st.pyplot()

            st.write("YES")
            st.success(yes_count)
            st.write("NO")
            st.success(no_count)
            yes_percentage = (yes_count / (yes_count + no_count)) * 100
            no_percentage = (no_count / (yes_count + no_count)) * 100
            st.write("YES PERCENTAGE:")
            st.success(yes_percentage)
            st.write("NO PERCENTAGE:")
            st.success(no_percentage)
            ##################################################
            st.header('Gender')

            plt.figure(figsize=(8, 6))
            # implement the logic for plotting higher education graphs
            sns.countplot(x='Gender', data=dataset1)
            gender_counts = dataset1['Gender'].value_counts()
            for i, count in enumerate(gender_counts):
                plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)  # Adjust fontsize as needed

            male_count = gender_counts['Male']
            female_count = gender_counts['Female']
            st.pyplot()

            st.write("MALE COUNT")
            st.success(male_count)
            st.write("FEMALE COUNT")
            st.success(female_count)
            male_percentage = (male_count / (male_count + female_count)) * 100
            female_percentage = (female_count / (male_count + female_count)) * 100
            st.write("MALE PERCENTAGE:")
            st.success(male_percentage)
            st.write("FEMALE PERCENTAGE:")
            st.success(female_percentage)

            st.header('Which of the following factors influence the most about your career aspirations')
            factor_column = 'Which of the following factors influence the most about your career aspirations'
            factor1 = 'People who have changed the world for better'
            factor2 = 'Social Media like LinkedIn'

            # Set the figure size
            plt.figure(figsize=(10, 6))  # Adjust the width and height as needed

            # Create the countplot using the specified column
            sns.countplot(x=factor_column, data=dataset1)

            # Calculate factor counts
            factor_count = dataset1[factor_column].value_counts()

            for i, count in enumerate(factor_count):
                plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)  # Adjust fontsize as needed

            # You can access specific factor counts like this
            fr1_count = factor_count[factor1]
            fr2_count = factor_count[factor2]

            # Show the plot using Streamlit
            st.pyplot()

            st.write("People who have changed the world for better")
            st.success(fr1_count)
            st.write("Social Media like LinkedIn")
            st.success(fr2_count)
            fr1_percentage = (fr1_count / (fr1_count + fr2_count)) * 100
            fr2_percentage = (fr2_count / (fr1_count + fr2_count)) * 100
            st.write("People who have changed the world for better. PERCENTAGE:")
            st.success(fr1_percentage)
            st.write("Social Media like LinkedIn. PERCENTAGE:")
            st.success(fr2_percentage)

            # completed no change required

        elif visual_choice == ao2:
            st.title("Job interest analysis")

            work_mission_question = "Would you work for a company whose mission is not clearly defined and publicly posted."
            wmo1 = "Yes"
            wmo2 = "No"
            st.header(work_mission_question)

            sns.countplot(x=work_mission_question, data=dataset1)
            work_mission_count = dataset1[work_mission_question].value_counts()
            for i, count in enumerate(work_mission_count):
                plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)
            wo1_count = work_mission_count[wmo1]
            wo2_count = work_mission_count[wmo2]
            plt.xlabel("Responses")

            # Show the plot using Streamlit
            st.pyplot()

            st.write("NO")
            st.success(wo2_count)
            st.write("YES")
            st.success(wo1_count)
            wo1_percentage = (wo1_count / (wo1_count + wo2_count)) * 100
            wo2_percentage = (wo2_count / (wo1_count + wo2_count)) * 100
            st.write("NO PERCENTAGE:")
            st.success(wo2_percentage)
            st.write("YES PERCENTAGE:")
            st.success(wo1_percentage)

            ################################################################
            work_question = "How likely would you work for a company whose mission is misaligned with their public actions or even their product ?"
            wqo1 = "Will work for them"
            wqo2 = "Will NOT work for them"
            st.header(work_question)
            work_question_count = dataset1[work_question].value_counts()
            for i, count in enumerate(work_question_count):
                plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)
            wqo1_count = work_question_count[wqo1]
            wqo2_count = work_question_count[wqo2]
            sns.countplot(x=work_question, data=dataset1)
            plt.xlabel("work preference for mission misaligned")
            st.pyplot()

            st.write("Will NOT work for them")
            st.success(wqo2_count)
            st.write("Will work for them")
            st.success(wqo1_count)
            wqo1_percentage = (wqo1_count / (wqo1_count + wqo2_count)) * 100
            wqo2_percentage = (wqo2_count / (wqo1_count + wqo2_count)) * 100
            st.write(" Will NOT work for them PERCENTAGE:")
            st.success(wqo2_percentage)
            st.write("Will work for them PERCENTAGE:")
            st.success(wqo1_percentage)

            #########################################################################

            work_question2 = "How likely would you work for a company whose mission is not bringing social impact ?"
            st.header(work_question2)
            work_question2_count = dataset1[work_question2].value_counts()

            wq2o1 = 1
            wq2o2 = 2
            wq2o3 = 3
            wq2o4 = 4
            wq2o5 = 5
            wq2o6 = 6
            wq2o7 = 7
            wq2o8 = 8
            wq2o9 = 9
            wq2o10 = 10

            wq2o1_count = work_question2_count[wq2o1]
            wq2o2_count = work_question2_count[wq2o2]
            wq2o3_count = work_question2_count[wq2o3]
            wq2o4_count = work_question2_count[wq2o4]
            wq2o5_count = work_question2_count[wq2o5]
            wq2o6_count = work_question2_count[wq2o6]
            wq2o7_count = work_question2_count[wq2o7]
            wq2o8_count = work_question2_count[wq2o8]
            wq2o9_count = work_question2_count[wq2o9]
            wq2o10_count = work_question2_count[wq2o10]
            sns.countplot(x=work_question2, data=dataset1)
            plt.xlabel("Numbers from 1-10")
            st.pyplot()

            st.write(1)
            st.success(wq2o1_count)
            st.write(2)
            st.success(wq2o2_count)
            st.write(3)
            st.success(wq2o3_count)
            st.write(4)
            st.success(wq2o4_count)
            st.write(5)
            st.success(wq2o5_count)
            st.write(6)
            st.success(wq2o6_count)
            st.write(7)
            st.success(wq2o7_count)
            st.write(8)
            st.success(wq2o8_count)
            st.write(9)
            st.success(wq2o9_count)
            st.write(10)
            st.success(wq2o10_count)
            wq2o1_percentage = (wq2o1_count / (
                        wq2o1_count + wq2o2_count + wq2o3_count + wq2o4_count + wq2o5_count + wq2o6_count + wq2o7_count + wq2o8_count + wq2o9_count + wq2o10_count)) * 100
            wq2o2_percentage = (wq2o2_count / (
                        wq2o1_count + wq2o2_count + wq2o3_count + wq2o4_count + wq2o5_count + wq2o6_count + wq2o7_count + wq2o8_count + wq2o9_count + wq2o10_count)) * 100
            wq2o3_percentage = (wq2o3_count / (
                        wq2o1_count + wq2o2_count + wq2o3_count + wq2o4_count + wq2o5_count + wq2o6_count + wq2o7_count + wq2o8_count + wq2o9_count + wq2o10_count)) * 100
            wq2o4_percentage = (wq2o4_count / (
                        wq2o1_count + wq2o2_count + wq2o3_count + wq2o4_count + wq2o5_count + wq2o6_count + wq2o7_count + wq2o8_count + wq2o9_count + wq2o10_count)) * 100
            wq2o5_percentage = (wq2o5_count / (
                        wq2o1_count + wq2o2_count + wq2o3_count + wq2o4_count + wq2o5_count + wq2o6_count + wq2o7_count + wq2o8_count + wq2o9_count + wq2o10_count)) * 100
            wq2o6_percentage = (wq2o6_count / (
                        wq2o1_count + wq2o2_count + wq2o3_count + wq2o4_count + wq2o5_count + wq2o6_count + wq2o7_count + wq2o8_count + wq2o9_count + wq2o10_count)) * 100
            wq2o7_percentage = (wq2o7_count / (
                        wq2o1_count + wq2o2_count + wq2o3_count + wq2o4_count + wq2o5_count + wq2o6_count + wq2o7_count + wq2o8_count + wq2o9_count + wq2o10_count)) * 100
            wq2o8_percentage = (wq2o8_count / (
                        wq2o1_count + wq2o2_count + wq2o3_count + wq2o4_count + wq2o5_count + wq2o6_count + wq2o7_count + wq2o8_count + wq2o9_count + wq2o10_count)) * 100
            wq2o9_percentage = (wq2o9_count / (
                        wq2o1_count + wq2o2_count + wq2o3_count + wq2o4_count + wq2o5_count + wq2o6_count + wq2o7_count + wq2o8_count + wq2o9_count + wq2o10_count)) * 100
            wq2o10_percentage = (wq2o10_count / (
                        wq2o1_count + wq2o2_count + wq2o3_count + wq2o4_count + wq2o5_count + wq2o6_count + wq2o7_count + wq2o8_count + wq2o9_count + wq2o10_count)) * 100

            st.write(" 1 PERCENTAGE:")
            st.success(wq2o1_percentage)
            st.write(" 2 PERCENTAGE:")
            st.success(wq2o2_percentage)
            st.write(" 3 PERCENTAGE:")
            st.success(wq2o3_percentage)
            st.write(" 4 PERCENTAGE:")
            st.success(wq2o4_percentage)
            st.write(" 5 PERCENTAGE:")
            st.success(wq2o5_percentage)
            st.write(" 6 PERCENTAGE:")
            st.success(wq2o6_percentage)
            st.write(" 7 PERCENTAGE:")
            st.success(wq2o7_percentage)
            st.write(" 8 PERCENTAGE:")
            st.success(wq2o8_percentage)
            st.write(" 9 PERCENTAGE:")
            st.success(wq2o9_percentage)
            st.write(" 10 PERCENTAGE:")
            st.success(wq2o10_percentage)

            ###############################################

        if visual_choice == ao3:
            st.title("Working preference analysis")

            work_preference_question = "What is the most preferred working environment for you."
            st.header(work_preference_question)
            work_preference_question1 = "Remote"
            work_preference_question2 = "Office"
            work_preference_question3 = "Hybrid (Office + Home)"

            work_preference_question_count = dataset1[work_preference_question].value_counts()
            wpoo1_count = work_preference_question_count[work_preference_question1]
            wpoo2_count = work_preference_question_count[work_preference_question2]
            wpoo3_count = work_preference_question_count[work_preference_question3]
            sns.countplot(x=work_preference_question, data=dataset1)
            plt.xlabel("Working preferences")
            st.pyplot()

            st.write("Remote")
            st.success(wpoo1_count)
            st.write("Office")
            st.success(wpoo2_count)
            st.write("Hybrid (Office + Home)")
            st.success(wpoo3_count)

            wpoo1_percentage = (wpoo1_count / (wpoo1_count + wpoo2_count + wpoo3_count)) * 100
            wpoo2_percentage = (wpoo2_count / (wpoo1_count + wpoo2_count + wpoo3_count)) * 100
            wpoo3_percentage = (wpoo3_count / (wpoo1_count + wpoo2_count + wpoo3_count)) * 100
            st.write("Remote PERCENTAGE:")
            st.success(wpoo1_percentage)
            st.write("Office PERCENTAGE:")
            st.success(wpoo2_percentage)
            st.write("Hybrid (Office + Home) PERCENTAGE:")
            st.success(wpoo3_percentage)

            ##############################################################################
            work_employer_question = "Which of the below Employers would you work with."
            st.header(work_employer_question)
            weqo1 = "Employer who pushes your limits by enabling an learning environment, and rewards you at the end"
            weqo2 = "Employer who appreciates learning and enables that environment"

            work_employer_question_count = dataset1[work_employer_question].value_counts()
            weqo1_count = work_employer_question_count[weqo1]
            weqo2_count = work_employer_question_count[weqo2]
            plt.figure(figsize=(17, 8))
            for i, count in enumerate(work_employer_question_count):
                plt.text(i, count, str(count), ha='center', va='bottom', fontsize=18)

            sns.countplot(x=work_employer_question, data=dataset1)
            plt.xlabel("Employer Preference", fontsize=20)
            st.pyplot()

            st.write("Employer who pushes your limits by enabling an learning environment, and rewards you at the end")
            st.success(weqo1_count)
            st.write("Employer who appreciates learning and enables that environment")
            st.success(weqo2_count)

            weqo1_percentage = (weqo1_count / (weqo1_count + weqo2_count)) * 100
            weqo2_percentage = (weqo2_count / (weqo1_count + weqo2_count)) * 100

            st.write(
                " Employer who pushes your limits by enabling an learning environment, and rewards you at the end PERCENTAGE:")
            st.success(weqo1_percentage)
            st.write("Employer who appreciates learning and enables that environment PERCENTAGE:")
            st.success(weqo2_percentage)

            ########################################################
            work_environment_question = "Which type of learning environment that you are most likely to work in ?"
            st.header(work_environment_question)
            wenqo1 = "Instructor or Expert Learning Programs, Trial and error by doing side projects within the company"
            wenqo2 = "Self Paced Learning Portals, Instructor or Expert Learning Programs"

            work_environment_question_count = dataset1[work_environment_question].value_counts()
            wenqo1_count = work_environment_question_count[wenqo1]
            wenqo2_count = work_environment_question_count[wenqo2]
            plt.figure(figsize=(16, 9))

            sns.countplot(x=work_environment_question, data=dataset1)
            plt.xlabel("Work Environment", fontsize=20)
            st.pyplot()

            st.write(
                "Instructor or Expert Learning Programs, Trial and error by doing side projects within the company")
            st.success(wenqo1_count)
            st.write("Self Paced Learning Portals, Instructor or Expert Learning Programs")
            st.success(wenqo2_count)

            wenqo1_percentage = (wenqo1_count / (wenqo1_count + wenqo2_count)) * 100
            wenqo2_percentage = (wenqo2_count / (wenqo1_count + wenqo2_count)) * 100

            st.write(
                "Instructor or Expert Learning Programs, Trial and error by doing side projects within the company PERCENTAGE:")
            st.success(wenqo1_percentage)
            st.write("Self Paced Learning Portals, Instructor or Expert Learning Programs PERCENTAGE:")
            st.success(wenqo2_percentage)

            ###############################################################################
            # Define the question and career options
            st.header("Which of the below careers looks close to your Aspirational job")
            work_asp_question = "Which of the below careers looks close to your Aspirational job"
            work_asp_1 = "Business Operation"
            work_asp_2 = "Design and Developement"
            work_asp_3 = "Teaching"
            work_asp_4 = "Design and Creative strategy"

            work_asp_question_count = dataset1[work_asp_question].value_counts()
            work_asp_1_count = work_asp_question_count[work_asp_1]
            work_asp_2_count = work_asp_question_count[work_asp_2]
            work_asp_3_count = work_asp_question_count[work_asp_3]
            work_asp_4_count = work_asp_question_count[work_asp_4]
            plt.figure(figsize=(16, 9))
            sns.countplot(x=work_asp_question, data=dataset1)
            plt.xlabel("Aspirational job", fontsize=20)
            st.pyplot()

            st.write("Business Operation")
            st.success(work_asp_1_count)
            st.write("Design and Developement")
            st.success(work_asp_2_count)
            st.write("Teaching")
            st.success(work_asp_3_count)
            st.write("Design and Creative strategy")
            st.success(work_asp_4_count)

            work_asp_1_percentage = (work_asp_1_count / (
                        work_asp_1_count + work_asp_2_count + work_asp_3_count + work_asp_4_count)) * 100
            work_asp_2_percentage = (work_asp_2_count / (
                        work_asp_1_count + work_asp_2_count + work_asp_3_count + work_asp_4_count)) * 100
            work_asp_3_percentage = (work_asp_3_count / (
                        work_asp_1_count + work_asp_2_count + work_asp_3_count + work_asp_4_count)) * 100
            work_asp_4_percentage = (work_asp_4_count / (
                        work_asp_1_count + work_asp_2_count + work_asp_3_count + work_asp_4_count)) * 100

            st.write("Business Operation PERCENTAGE:")
            st.success(work_asp_1_percentage)
            st.write("Design and Developement PERCENTAGE:")
            st.success(work_asp_2_percentage)
            st.write("Teaching PERCENTAGE:")
            st.success(work_asp_3_percentage)
            st.write("Design and Creative strategy PERCENTAGE:")
            st.success(work_asp_4_percentage)

        if visual_choice == ao4:
            st.title("working period on same Company Analysis")
            #########################################################
            watch_question = "What type of Manager would you work without looking into your watch ?"
            watch_o1 = "Manager who explains what is expected, sets a goal and helps achieve it"
            watch_o2 = "Manager who sets goal and helps me achieve it"
            st.header(watch_question)
            watch_question_count = dataset1[watch_question].value_counts()
            watch_o1_count = watch_question_count[watch_o1]
            watch_o2_count = watch_question_count[watch_o2]
            for i, count in enumerate(watch_question_count):
                plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)
            plt.figure(figsize=(14, 10))

            sns.countplot(x=watch_question, data=dataset1)
            plt.xlabel("Response")
            st.pyplot()

            st.write("Manager who explains what is expected, sets a goal and helps achieve it")
            st.success(watch_o1_count)
            st.write("Manager who sets goal and helps me achieve it")
            st.success(watch_o2_count)

            watch_o1_count_percentage = (watch_o1_count / (watch_o1_count + watch_o2_count)) * 100
            watch_o2_count_percentage = (watch_o2_count / (watch_o1_count + watch_o2_count)) * 100

            st.write("Manager who explains what is expected, sets a goal and helps achieve it:(%)")
            st.success(watch_o1_count_percentage)
            st.write("Manager who sets goal and helps me achieve it:(%)")
            st.success(watch_o2_count_percentage)

            #################################################################
            st.header("How likely is that you will work for one employer for 3 years or more ?")
            work_column = "How likely is that you will work for one employer for 3 years or more ?"
            wo1 = "This will be hard to do, but if it is the right company I would try"
            wo2 = "Will work for 3 years or more"

            # plt.figure(figsize=(16,8))
            sns.countplot(x=work_column, data=dataset1)
            work_column_count = dataset1[work_column].value_counts()
            for i, count in enumerate(work_column_count):
                plt.text(i, count, str(count), ha='center', va='bottom', fontsize=12)
            wo1_count = work_column_count[wo1]
            wo2_count = work_column_count[wo2]
            plt.xlabel("Responses")

            # Show the plot using Streamlit
            st.pyplot()

            st.write("How likely is that you will work for one employer for 3 years or more ?")
            st.success(wo1_count)
            st.write("Will work for 3 years or more")
            st.success(wo2_count)

            wo1_count_percentage = (wo1_count / (wo1_count + wo2_count)) * 100
            wo2_count_percentage = (wo2_count / (wo1_count + wo2_count)) * 100

            st.write("How likely is that you will work for one employer for 3 years or more ?(%)")
            st.success(wo1_count_percentage)
            st.write("Will work for 3 years or more(%)")
            st.success(wo2_count_percentage)
        if visual_choice==ao5:
            try:
                data=cur.execute("select * from surveyresponses")
                res=cur.fetchall()
                import pandas as pd
                dataf=pd.DataFrame(res)
                st.data_editor(dataf,width=1200)


            except Exception as e:
                print(e)



elif authentication_status == False:
    # Change the error message for incorrect credentials
    st.error('Incorrect username or password. Please try again.')

elif authentication_status == None:
    # Change the warning message for empty fields
    st.warning('Please enter your username and password.')