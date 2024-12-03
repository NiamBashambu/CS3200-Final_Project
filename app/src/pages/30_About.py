import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.title('**Co-Connect🧠**')
st.write('Your go-to platform for co-op opportunities!')

st.subheader("About Us")

st.markdown (
    """
    We are *Co-Connect*, a Facebook like app for co-ops. <br>

    Our platform addresses the difficulties and frustrations felt by students 
    and employers in the co-op process. Co-ops offer students valuable 
    opportunities to jumpstart their careers in their chosen fields. However, 
    due to the limited information provided in job descriptions, students often
    find themselves realizing too late—once they're already on the job—that 
    the role doesn't meet their needs or expectations. <br>

    NUWorks, the current platform, lacks features such as workload variability, 
    work environment, realistic responsibilities, and much more. Northeastern 
    students need a platform that offers a realistic insight into the co-op world 
    and the industries they are preparing to enter. *Co-Connect* offers a more 
    intuitive, data-driven platform that is tailored to co-ops offered to Northeastern
    students. <br>

    Check out some of our features below!
    """,
        unsafe_allow_html=True)


st.subheader('Learn more about what *Co-Connect* can do for you!')



with st.expander('Students on the Co-op Search 👨‍🎓'):
    st.markdown(
        '''
        As students, we understand how important it is for you to find the 
        right co-op that aligns with your career goals. We know that there
        is a co-op made just for you, and our goal is to help you find it.
        *Co-Connect* is designed to help bridge that gap between you and 
        potential employers, creating opportunities for direct communication 
        and personalized matches that lead to better, more fulfilling co-op 
        experiences. <br>
        
        With *Co-Connect*, we encourage you to take charge of your search and 
        allow youself the opportunity to find the co-op that will kickstart 
        your career. <br><br>

        As a student on the co-op search:
        - You can access a co-op listing page with co-ops you can apply to. 
        Each listing includes the position title, department, location, 
        detailed job description, and link to the application. Filter by 
        department if necessary!
        - You can access a post feed where you can share your experiences 
        with co-ops or read up on other students' co-ops.
        - You can update your employment status to notify employers whether
        you're on the search or not.
        - You can upload your resume for future employers to access.
    ''',
        unsafe_allow_html=True)

with st.expander('Students Exploring Fields 🤓'):
        st.markdown(
        '''
        Whether you're a first year who is yet to apply, or a student who's 
        looking to learn more about field, *Co-Connect* provides a platform 
        where you can browse co-op listings and gain insights into an 
        industry without the pressure of applying for the job. Explore various 
        roles, understand the skills employers are seeking, and learn about 
        different companies and work environments. This is a great way to get 
        an early sense of the co-op landscape, and start thinking about your 
        future career path (all while keeping your options open!). <br><br>

        As a student exploring fields:
        - You can access a co-op listing page with each listing including 
        the position title, department, location, detailed job description, 
        and link to application. Get a sense of what applications look like, 
        and what will be expected of you when you ultimately begin your search! 
        Filter by department if necessary!
        - You can view students' posts to gauge how students interact with 
        their fields. Take the time to read up on their challenges and  
        accomplishments while working at their co-ops.
        - You can update your employment status for when you ultimately begin
        your search.
        - You can upload your resume and see how many of your skills and 
        experiences can be applied to different job listings.

    ''',
        unsafe_allow_html=True)

with st.expander('Employers 🧑‍💼'):
    st.markdown(
        '''
        As employers, we know it's just as important for you to find students who 
        meet your company's standards as it is for our students to find roles that
        suit their needs. We at *Co-Connect* aim to bridge that unfamiliarity 
        between students and employers with the hopes of initiating conversations 
        that can lead students to better matched co-ops. <br>

        We here at *Co-Connect* offer a holistic approach to the co-op search, 
        ensuring that both employers and students benefit from co-op opportunities. <br><br>
        
        As employers:
        - You are able to view all co-op opportunities offered to students, as well 
        as post co-op listings of your own.
        - You can view students' posts to gauge how students interact with your 
        company and others. With first-hand student accounts, employers are able to 
        field feedback from their past employees and adapt their models to improve
        students' experiences.
        - You can view student profiles and begin searching for future employees. 
        Search for students by major and employment status and contact students 
        by email to further conversations.
        - You can check out student resumes for certain skills your company may be 
        searching for.

    ''',
        unsafe_allow_html=True)

with st.expander('Co-op Advisors 👩‍🏫'):
         st.markdown(
        '''
        As a co-op advisor, we know you have hundreds of students to oversee at 
        one time. We here at *Co-Connect* have designed our platform to be an 
        invaluable tool to assist in tracking your students' progress while they're 
        on their search. By providing easy access to a wide range of co-op opportunities, 
        you can better assist students in finding roles that match their academic goals 
        and career aspirations. <br>
        
        *Co-Connect* enables you to track industry trends, 
        view student interactions, and stay informed about employer needs, ensuring you 
        can offer tailored advice and support to help students make the most of their 
        co-op experience. <br><br>

        As a co-op advisor:
        - You are able to view all co-op opportunities offered to students, each listing 
        including a detailed description of what the role entails. This will allow you 
        make more personalized recommendations to your students.
        - You can view students' posts to gauge how students interact with their co-ops. 
        See how students matched (or didn't match) with their past co-ops. Connect students 
        who may be interested in a company with students who have worked there in the past.
        - You can access all students and their information. Easily track where students are in the 
        co-op search process and identify who might need additional assistance.
        - You can access all student resumes to ensure students are properly updating their 
        resumes. Take note of skills and experiences that may help students excel at specific 
        co-ops.
    ''',
        unsafe_allow_html=True)