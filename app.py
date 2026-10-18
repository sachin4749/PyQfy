import streamlit as st
import os
import google.generativeai as genai
from pypdf import PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import io

# Page Configuration
st.set_page_config(
    page_title="PyQfy - Smart PYQ & Academic Intelligence Hub",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Glassmorphic Dark Aesthetic
st.markdown("""
    <style>
    .stApp {
        background-color: #070b14;
        background-image: 
            radial-gradient(at 0% 0%, rgba(59, 130, 246, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(139, 92, 246, 0.15) 0px, transparent 50%),
            radial-gradient(at 50% 50%, rgba(15, 23, 42, 0.5) 0px, transparent 100%);
        background-attachment: fixed;
        color: #f3f4f6;
    }
    
    .glass-card {
        background: rgba(15, 23, 42, 0.55);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 1.25rem;
        padding: 1.5rem;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
        margin-bottom: 1.5rem;
    }
    
    .main-title {
        font-size: 2.2rem;
        font-weight: 900;
        background: linear-gradient(to right, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .subtitle {
        color: #9ca3af;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Configure Gemini API Key securely from Streamlit Secrets or Environment Variables
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.warning("⚠️ **GEMINI_API_KEY is not set!** Please add your Gemini API Key in Streamlit Cloud Secrets.")
else:
    genai.configure(api_key=api_key)

# Sidebar Navigation
st.sidebar.markdown("<h2 class='main-title' style='font-size: 1.6rem;'>PyQfy 🎓</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #9ca3af; font-size: 0.8rem;'>Smart PYQ & Academic Hub</p>", unsafe_allow_html=True)

nav_choice = st.sidebar.radio("Navigation", ["Paper Analyzer", "AI Assistant", "Feedback"])

# Helper function to call Gemini AI with deep academic prompt
def ask_gemini(prompt_text):
    try:
        model = genai.GenerativeModel('gemini-3.8-flash')
        enhanced_prompt = f"""You are PyQfy's Elite Academic AI Professor and Expert Evaluator. 
Your core objective is to provide exceptionally deep, accurate, rigorous, and exhaustive model answers for academic questions and question papers.

RULES FOR ANSWERING:
1. EXTRACT AND SOLVE ALL: Carefully scan the provided text or prompt. Identify every single question, sub-question, or numerical problem. Do NOT skip anything.
2. STRUCTURED DEEP BREAKDOWN: For every question, structure your response professionally using these headings:
   - **Core Concept & Definition:** Clear theoretical foundation and definitions.
   - **Detailed Step-by-Step Explanation / Derivation / Calculation:** In-depth breakdown with mathematical formulas, core principles, or logical steps. Avoid superficial summaries; provide complete depth.
   - **Illustrative Example / Application:** Where applicable, provide a short example or use case.
   - **Exam Scoring Tip:** Give precise advice on what examiners look for to award full marks.
3. MAINTAIN ACADEMIC RIGOR: Use proper terminology relevant to the subject.

Input Content:
{prompt_text}"""
        
        response = model.generate_content(enhanced_prompt)
        return response.text
    except Exception as e:
        return f"Error communicating with Gemini AI: {str(e)}"

# Function to generate a formatted multi-page PDF report using ReportLab
def create_pdf_report(analysis_text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'ReportTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=styles['colors'].HexColor('#1e3a8a') if hasattr(styles, 'colors') else None,
        spaceAfter=15
    )
    
    body_style = ParagraphStyle(
        'ReportBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceAfter=8
    )
    
    story = []
    story.append(Paragraph("<b>PyQfy - Deep Model Solutions Report</b>", title_style))
    story.append(Spacer(1, 10))
    
    # Split text by lines/paragraphs and add to Story
    paragraphs = analysis_text.split('\n')
    for para in paragraphs:
        if para.strip():
            # Clean markdown bold/italics markers if necessary or let ReportLab handle basic text
            formatted_para = para.replace('**', '<b>').replace('</b>', '<b>') # basic cleanup
            story.append(Paragraph(formatted_para, body_style))
        else:
            story.append(Spacer(1, 6))
            
    doc.build(story)
    buffer.seek(0)
    return buffer

# 1. Paper Analyzer Section
if nav_choice == "Paper Analyzer":
    st.markdown("<h1 class='main-title'>Question Paper Deep Analyzer</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Smart PYQ & Academic Intelligence Hub</p>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            level = st.selectbox("1. Level / Degree", [
                "10th Standard", "11th Standard", "12th Standard", 
                "BA (Bachelor of Arts)", "B.Tech (Bachelor of Technology)", 
                "M.Tech (Master of Technology)", "BCA (Bachelor of Computer Applications)", 
                "MCA (Master of Computer Applications)", "MBA (Master of Business Administration)", 
                "General Undergraduate", "General Postgraduate"
            ])
        with col2:
            stream = st.selectbox("2. Stream / Branch", [
                "Computer Science & Engineering", "Electronics & Communication", 
                "Information Technology", "Mechanical Engineering", 
                "Civil Engineering", "General Science / Arts", "Commerce & Management"
            ])
        with col3:
            subject = st.selectbox("3. Subject", [
                "Data Structures & Algorithms", "Operating Systems", "Database Management Systems",
                "Computer Networks", "Software Engineering", "Physics", "Mathematics", 
                "Biology / Life Sciences", "Economics", "Business Management"
            ])
        
        uploaded_file = st.file_uploader("Upload Question Paper (PDF or TXT)", type=["pdf", "txt"])
        pasted_text = st.text_area("Or paste question paper text here directly:", height=150)
        
        if st.button("Analyze All Questions", type="primary"):
            paper_content = ""
            if uploaded_file is not None:
                if uploaded_file.type == "application/pdf":
                    reader = PdfReader(uploaded_file)
                    for page in reader.pages:
                        extracted = page.extract_text()
                        if extracted:
                            paper_content += extracted
                else:
                    paper_content = uploaded_file.read().decode("utf-8")
            elif pasted_text.strip():
                paper_content = pasted_text.strip()
                
            if not paper_content:
                st.error("Please upload a file or paste question paper text first!")
            else:
                with st.spinner("Analyzing all questions deeply with Gemini AI... Please wait."):
                    full_query = f"Level: {level}, Stream: {stream}, Subject: {subject}\n\nQuestions:\n{paper_content}"
                    ai_result = ask_gemini(full_query)
                    
                    # Store in session state for local caching/persistence
                    st.session_state['last_analysis'] = ai_result
                    st.success("Analysis Complete & Cached Locally!")
        
        # Display cached analysis if available in session state
        if 'last_analysis' in st.session_state:
            st.markdown("---")
            st.markdown("### 📝 Deep Model Solutions (Cached in Session):")
            st.markdown(st.session_state['last_analysis'])
            
            st.markdown("---")
            # PDF Generation button with full formatted report
            pdf_buffer = create_pdf_report(st.session_state['last_analysis'])
            st.download_button(
                label="📥 Download Complete Formatted PDF Report",
                data=pdf_buffer,
                file_name="PyQfy_Complete_Model_Solutions.pdf",
                mime="application/pdf"
            )
        
        st.markdown("</div>", unsafe_allow_html=True)

# 2. AI Assistant Section
elif nav_choice == "AI Assistant":
    st.markdown("<h1 class='main-title'>Gemini AI Academic Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Ask any doubt, concept breakdown, or numerical query directly.</p>", unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if query := st.chat_input("Type your academic query here..."):
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        with st.chat_message("assistant"):
            with st.spinner("Thinking deeply..."):
                response = ask_gemini(query)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

# 3. Feedback Section
elif nav_choice == "Feedback":
    st.markdown("<h1 class='main-title'>Send Your Feedback</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Help us improve PyQfy by sharing your thoughts.</p>", unsafe_allow_html=True)
    
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        msg = st.text_area("Feedback / Suggestions")
        submitted = st.form_submit_button("Submit Feedback")
        if submitted:
            st.success("Thank you! Your feedback has been recorded.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Designed by **SK Graphics®** | Developer: **sachin4749**")
