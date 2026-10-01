import streamlit as st

# ===============================
# PAGE CONFIGURATION
# ===============================
st.set_page_config(
    page_title="George Brown MySpace Hub",
    page_icon="🎓",
    layout="wide"
)

# Custom Styling for George Brown MySpace Hub (Navy Blue Theme)
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    [data-testid="stSidebar"] { background-color: #002D62; color: white; }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span { color: #ffffff !important; }
    .gb-header { background: linear-gradient(135deg, #002D62 0%, #004A99 100%); color: white; padding: 20px 25px; border-radius: 8px; margin-bottom: 20px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #002D62; color: #CBD5E1; text-align: center; padding: 8px; font-size: 0.85rem; }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for Global Sharing Across Students Testing the App
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False
    st.session_state.student_name = ""
    st.session_state.student_id = ""
    st.session_state.program = ""

if "shared_messages" not in st.session_state:
    st.session_state.shared_messages = [
        {"sender": "Sarah M. (B428)", "text": "Hey everyone! Welcome to the student hub. Feel free to share notes and connect on LinkedIn!"},
        {"sender": "Alex K. (B428)", "text": "Does anyone have the lecture slides for HRM recruitment strategies?"}
    ]

if "shared_files" not in st.session_state:
    st.session_state.shared_files = [
        {"uploader": "Sarah M.", "filename": "Recruitment_Case_Study_Template.docx", "description": "Template for upcoming HR assignment."},
        {"uploader": "Alex K.", "filename": "Employment_Law_Summary_Notes.pdf", "description": "Key takeaways from week 3 lecture."}
    ]

if "online_students" not in st.session_state:
    st.session_state.online_students = []

if "linkedin_directory" not in st.session_state:
    st.session_state.linkedin_directory = [
        {"name": "Sarah M.", "program": "Post-Graduate Human Resources Management (B428)", "link": "https://www.linkedin.com"},
        {"name": "Alex K.", "program": "Post-Graduate Human Resources Management (B428)", "link": "https://www.linkedin.com"}
    ]


# ===============================
# LOGIN & VERIFICATION SCREEN
# ===============================
if not st.session_state.is_logged_in:
    st.markdown("""
        <div style="text-align: center; padding: 30px;">
            <h1 style="color: #002D62;">🎓 George Brown MySpace Hub</h1>
            <p style="color: #4B5563; font-size: 1.1rem;">Student Collaboration & Professional Network Ecosystem</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 🔐 Student Sign-In")
        input_name = st.text_input("Full Name:", placeholder="e.g., Prabh Maan")
        input_id = st.text_input("George Brown Student ID or Email:", placeholder="e.g., 123456789 or student@georgebrown.ca")
        input_prog = st.selectbox("Select Program:", [
            "Post-Graduate Human Resources Management (B428)",
            "Business Administration - Leadership & Management",
            "Computer Technology & Information Systems",
            "Early Childhood Education",
            "Financial Planning & Services"
        ])

        if st.button("Enter Student Hub 🚀"):
            if input_name and input_id:
                if input_id.endswith("@georgebrown.ca") or input_id.isdigit():
                    st.session_state.is_logged_in = True
                    st.session_state.student_name = input_name
                    st.session_state.student_id = input_id
                    st.session_state.program = input_prog
                    
                    student_tag = f"{input_name} ({input_prog[:10]}...)"
                    if student_tag not in st.session_state.online_students:
                        st.session_state.online_students.append(student_tag)
                        
                    st.rerun()
                else:
                    st.error("Access Denied: Please use a valid @georgebrown.ca email or Student ID.")
            else:
                st.error("Please enter your name and student ID or email.")

    with col2:
        st.info("""
        What Students Can Do Here:
        - 💬 Live Peer Chat: Talk directly with fellow students across courses.
        - 📁 File & Notes Exchange: Upload and download study resources.
        - 💼 LinkedIn Directory: Share your professional profile and network.
        - 📅 Attendance & Grades: Track your academic progress.
        """)

    st.markdown("""
        <div class="footer">
            George Brown MySpace Hub • Student-to-Student Collaboration Space
        </div>
    """, unsafe_allow_html=True)
    st.stop()


# ===============================
# MAIN HUB DASHBOARD INTERFACE
# ===============================

# Sidebar Navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/4/4a/George_Brown_College_logo.svg/1200px-George_Brown_College_logo.svg.png", width=140)
st.sidebar.markdown("---")
st.sidebar.success(f"👤 {st.session_state.student_name}\n`ID: {st.session_state.student_id}\n{st.session_state.program}`")

if st.sidebar.button("🚪 Logout Hub"):
    st.session_state.is_logged_in = False
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("### 📱 Student Menu")
hub_tab = st.sidebar.radio("Navigate:", [
    "🏠 Dashboard & Active Peers",
    "💬 Student Chat Room",
    "📁 Shared Notes & File Vault",
    "💼 Student LinkedIn Directory",
    "📅 Attendance & Time Table",
    "📝 My Grades & Results",
    "📢 College Notices"
])

# Header Banner
st.markdown(f"""
    <div class="gb-header">
        <h2 style="margin:0;">George Brown MySpace Hub</h2>
        <p style="margin:0; font-size:0.95rem;">Welcome, {st.session_state.student_name} | Program: {st.session_state.program}</p>
    </div>
""", unsafe_allow_html=True)


# --- 1. DASHBOARD & ACTIVE PEERS ---
if hub_tab == "🏠 Dashboard & Active Peers":
    st.subheader("📊 Student Overview & Hub Activity")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="Active Hub Peers", value=f"{len(st.session_state.online_students)} Online")
    with c2:
        st.metric(label="Shared Files in Vault", value=f"{len(st.session_state.shared_files)} Documents")
    with c3:
        st.metric(label="LinkedIn Profiles", value=f"{len(st.session_state.linkedin_directory)} Connected")

    st.markdown("---")
    st.markdown("### 👥 Students Registered in This Session")
    if st.session_state.online_students:
        for student in st.session_state.online_students:
            st.markdown(f"- 🟢 {student}")
    else:
        st.write("No other students logged in yet.")


# --- 2. STUDENT CHAT ROOM ---
elif hub_tab == "💬 Student Chat Room":
    st.subheader("💬 Student Discussion & Chat Room")
    st.write("Talk, ask questions, and collaborate with your classmates in real time.")

    chat_container = st.container(height=350)
    with chat_container:
        for msg in st.session_state.shared_messages:
            st.markdown(f"> {msg['sender']}: {msg['text']}")

    st.markdown("---")
    with st.form("chat_form", clear_on_submit=True):
        new_msg = st.text_input("Type your message to the student community...")
        submitted = st.form_submit_button("Send Message 📤")
        if submitted and new_msg:
            st.session_state.shared_messages.append({
                "sender": f"{st.session_state.student_name}",
                "text": new_msg
            })
            st.rerun()


# --- 3. SHARED NOTES & FILE VAULT ---
elif hub_tab == "📁 Shared Notes & File Vault":
    st.subheader("📁 Peer Notes & File Exchange Vault")
    st.write("Upload your study guides, summaries, or assignment templates to share with fellow students.")

    with st.expander("📤 Upload a New File or Note"):
        with st.form("upload_form", clear_on_submit=True):
            file_name_input = st.text_input("File Name / Title:", placeholder="e.g., HRM 9037 Study Guide.pdf")
            file_desc = st.text_input("Short Description:", placeholder="e.g., Contains summary notes for chapter 4.")
            upload_submit = st.form_submit_button("Add to Shared Vault")
            
            if upload_submit and file_name_input:
                st.session_state.shared_files.append({
                    "uploader": st.session_state.student_name,
                    "filename": file_name_input,
                    "description": file_desc
                })
                st.success(f"Successfully added {file_name_input} to the student vault!")
                st.rerun()

    st.markdown("---")
    st.markdown("### 📚 Available Student Files")
    for file in st.session_state.shared_files:
        st.markdown(f"""
        - 📄 {file['filename']} 
          Uploaded by: {file['uploader']}  
          {file['description']}
        """)


# --- 4. STUDENT LINKEDIN DIRECTORY ---
elif hub_tab == "💼 Student LinkedIn Directory":
    st.subheader("💼 Student Professional Network (LinkedIn)")
    st.write("Submit your LinkedIn profile link so your peers and classmates can connect with you professionally.")

    with st.form("linkedin_form", clear_on_submit=True):
        li_link_input = st.text_input("Your LinkedIn Profile URL:", placeholder="https://www.linkedin.com/in/your-profile")
        li_submit = st.form_submit_button("Add My LinkedIn Profile 🔗")
        
        if li_submit and li_link_input:
            st.session_state.linkedin_directory.append({
                "name": st.session_state.student_name,
                "program": st.session_state.program,
                "link": li_link_input
            })
            st.success("Successfully added your profile to the student LinkedIn directory!")
            st.rerun()

    st.markdown("---")
    st.markdown("### 🌐 Classmate Directory")
    for profile in st.session_state.linkedin_directory:
        st.markdown(f"- 👤 {profile['name']} ({profile['program']}) — [Visit LinkedIn Profile]({profile['link']})")


# --- 5. ATTENDANCE & TIME TABLE ---
elif hub_tab == "📅 Attendance & Time Table":
    st.subheader("📅 Attendance Tracker & Weekly Timetable")
    st.progress(0.95, text="Core Program Lectures: 95% Attendance")
    st.markdown(f"---")
    st.markdown(f"### Timetable for {st.session_state.program}")
    st.write("Your weekly class schedule is synchronized with your registered program curriculum.")


# --- 6. MY GRADES & RESULTS ---
elif hub_tab == "📝 My Grades & Results":
    st.subheader("📝 Academic Assessments & Results")
    st.markdown("""
    | Evaluation Item | Weight | Score Obtained | Status |
    | :--- | :--- | :--- | :--- |
    | Assignment 1 | 20% | 19 / 20 | Pass 🟢 |
    | Midterm Evaluation | 30% | 27 / 30 | Pass 🟢 |
    | Project Deliverable | 50% | Pending | In Progress 🟡 |
    """)


# --- 7. COLLEGE NOTICES ---
elif hub_tab == "📢 College Notices":
    st.subheader("📢 Student Hub Circulars & Notices")
    st.info("📌 Announcement: Peer study groups and networking meetups are now organizing through the student chat room and LinkedIn directory.")
    st.markdown("""
    - Library Hours: Extended study rooms open 24/7 during exam periods.
    - Career Hub: Resume review sessions available every Tuesday.
    """)

# Footer
st.markdown("""
    <div class="footer">
        George Brown MySpace Hub • Student-to-Student Collaboration Space
    </div>
""", unsafe_allow_html=True)
 
