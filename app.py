import streamlit as st
import os
import google.generativeai as genai
from pypdf import PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import html
import io
import requests

# 1. Page Configuration
st.set_page_config(
    page_title="PyQfy - Smart PYQ & Academic Intelligence Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Advanced Glassmorphic & Ultra-Modern Dark Theme Styling (No Emojis)
st.markdown("""
    <style>
    .stApp {
        background-color: #030712;
        background-image: 
            radial-gradient(at 0% 0%, rgba(37, 99, 235, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(124, 58, 237, 0.15) 0px, transparent 50%),
            radial-gradient(at 50% 50%, rgba(15, 23, 42, 0.8) 0px, transparent 100%);
        background-attachment: fixed;
        color: #f3f4f6;
        font-family: 'Inter', sans-serif;
    }
    
    .glass-card {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 1.5rem;
        padding: 2rem;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6);
        margin-bottom: 1.5rem;
    }
    
    .main-title {
        font-size: 2.6rem;
        font-weight: 900;
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.03em;
        margin-bottom: 0.1rem;
    }
    
    .subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        font-weight: 500;
        margin-bottom: 2rem;
    }

    .stButton>button {
        background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%);
        color: white;
        border: none;
        border-radius: 0.75rem;
        font-weight: 600;
        padding: 0.65rem 1.5rem;
        box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
        transition: all 0.25s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6);
    }
    
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #030712;
    }
    ::-webkit-scrollbar-thumb {
        background: #1e293b;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #334155;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Secure API Key Configuration
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY is missing. Please configure your API key in Streamlit Cloud Secrets settings.")
else:
    genai.configure(api_key=api_key)

# 4. Sidebar Navigation & Branding
with st.sidebar:
    st.markdown("<h2 class='main-title' style='font-size: 1.8rem;'>PyQfy</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; font-size: 0.85rem; margin-top: -10px;'>Smart PYQ & Academic Hub</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    nav_choice = st.radio("Navigation Menu", ["Paper Analyzer", "AI Assistant", "Feedback"], index=0)
    
    st.markdown("<br>" * 8, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; padding: 14px; border-radius: 1rem; background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255,255,255,0.06);'>
            <span style='font-size: 0.7rem; color: #94a3b8; letter-spacing: 0.05em;'>CRAFTED WITH EXCELLENCE</span><br>
            <b style='color: #60a5fa; font-size: 0.95rem;'>SK Graphics</b><br>
            <span style='font-size: 0.8rem; color: #cbd5e1;'>Lead Developer: <b>Sachin K</b></span>
        </div>
    """, unsafe_allow_html=True)

# 5. Comprehensive Cascading Academic Structure
academic_structure = {
    "10th Standard": {
        "General Curriculum": ["Mathematics", "Science", "Social Science", "English", "Hindi"]
    },
    "11th & 12th Standard": {
        "Science (PCM/PCB)": ["Physics", "Chemistry", "Mathematics", "Biology", "Computer Science"],
        "Commerce": ["Accountancy", "Business Studies", "Economics", "Business Mathematics"],
        "Arts / Humanities": ["History", "Political Science", "Geography", "Sociology", "Economics"]
    },
    "Undergraduate (B.Tech / B.E)": {
        "Computer Science & Engineering": ["Data Structures & Algorithms", "Operating Systems", "Database Management Systems", "Computer Networks", "Software Engineering"],
        "Electronics & Communication": ["Digital Logic Design", "Signals and Systems", "Microcontrollers", "Analog Circuits"],
        "Mechanical / Civil Engineering": ["Engineering Mechanics", "Strength of Materials", "Fluid Mechanics", "Structural Analysis"]
    },
    "Postgraduate (M.Tech / MCA / MBA)": {
        "Computer Applications (MCA)": ["Advanced Data Structures", "Web Technologies", "Python Programming", "Cloud Computing", "Artificial Intelligence"],
        "Management (MBA)": ["Financial Management", "Marketing Management", "Human Resource Management", "Strategic Management"],
        "Engineering (M.Tech)": ["Advanced Algorithms", "Machine Learning", "Research Methodology"]
    },
    "General Degrees (BA / B.Sc / B.Com)": {
        "Arts (BA)": ["English Literature", "History", "Political Science", "Economics", "Psychology"],
        "Science (B.Sc)": ["Physics", "Chemistry", "Mathematics", "Botany", "Zoology"],
        "Commerce (B.Com)": ["Financial Accounting", "Corporate Tax", "Business Law", "Auditing"]
    }
}

# 6. Robust Gemini AI Engine Function
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
        if response and response.text:
            return response.text
        else:
            return "Received an empty response from Gemini AI. Please try again."
    except Exception as e:
        return f"Error communicating with Gemini AI service: {str(e)}"

# 7. Enterprise Numbered Canvas Class for Professional PDF Generation
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor('#6b7280'))
        
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 45, 30, page_str)
        self.drawString(45, 30, "PyQfy - Smart PYQ & Academic Intelligence Hub (SK Graphics)")
        
        self.setStrokeColor(colors.HexColor('#d1d5db'))
        self.setLineWidth(0.5)
        self.line(45, letter[1] - 35, letter[0] - 45, letter[1] - 35)
        self.drawString(45, letter[1] - 30, "Confidential Academic Evaluation & Model Solutions Report")
        
        self.restoreState()

def create_pdf_report(analysis_text):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer, 
        pagesize=letter, 
        rightMargin=45, 
        leftMargin=45, 
        topMargin=55, 
        bottomMargin=50
    )
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'ReportTitle',
        parent=styles['Heading1'],
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=15
    )
    
    body_style = ParagraphStyle(
        'ReportBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=15,
        spaceAfter=8
    )
    
    story = []
    story.append(Paragraph("<b>PyQfy - Deep Model Solutions Report</b>", title_style))
    story.append(Spacer(1, 10))
    
    lines = analysis_text.split('\n')
    for line in lines:
        cleaned_line = line.strip()
        if cleaned_line:
            escaped_line = html.escape(cleaned_line)
            parts = escaped_line.split('**')
            if len(parts) > 1:
                formatted_parts = []
                for i, part in enumerate(parts):
                    if i % 2 == 1:
                        formatted_parts.append(f"<b>{part}</b>")
                    else:
                        formatted_parts.append(part)
                safe_paragraph_text = "".join(formatted_parts)
            else:
                safe_paragraph_text = escaped_line
                
            story.append(Paragraph(safe_paragraph_text, body_style))
        else:
            story.append(Spacer(1, 4))
            
    doc.build(story, canvasmaker=NumberedCanvas)
    buffer.seek(0)
    return buffer

# ==================== MAIN APP VIEWS ====================

# Section 1: Paper Analyzer
if nav_choice == "Paper Analyzer":
    st.markdown("<h1 class='main-title'>Question Paper Deep Analyzer</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Upload exam papers or previous year questions to generate comprehensive, professor-grade model solutions.</p>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            selected_level = st.selectbox("1. Academic Level", list(academic_structure.keys()))
        
        available_streams = list(academic_structure[selected_level].keys())
        with col2:
            selected_stream = st.selectbox("2. Branch / Stream", available_streams)
        
        available_subjects = academic_structure[selected_level][selected_stream]
        with col3:
            selected_subject = st.selectbox("3. Subject", available_subjects)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("Upload Question Paper (PDF or TXT)", type=["pdf", "txt"])
        pasted_text = st.text_area("Or paste question text directly here:", height=140, placeholder="Paste your questions or exam paper content here...")
        
        analyze_btn = st.button("Analyze All Questions Deeply", type="primary", use_container_width=True)
        
        if analyze_btn:
            paper_content = ""
            if uploaded_file is not None:
                if uploaded_file.type == "application/pdf":
                    reader = PdfReader(uploaded_file)
                    for page in reader.pages:
                        extracted = page.extract_text()
                        if extracted:
                            paper_content += extracted + "\n"
                else:
                    paper_content = uploaded_file.read().decode("utf-8")
            elif pasted_text.strip():
                paper_content = pasted_text.strip()
                
            if not paper_content:
                st.warning("Please upload a valid file or paste your question text first.")
            else:
                with st.spinner("PyQfy AI Professor is breaking down every question into deep model answers. Please wait."):
                    full_query = f"Level: {selected_level}, Stream: {selected_stream}, Subject: {selected_subject}\n\nQuestions:\n{paper_content}"
                    ai_result = ask_gemini(full_query)
                    
                    st.session_state['last_analysis'] = ai_result
                    if 'history' not in st.session_state:
                        st.session_state['history'] = []
                    st.session_state['history'].insert(0, {"subject": selected_subject, "content": ai_result})
                    
                    st.success("Comprehensive Analysis Completed Successfully.")
        
        if 'last_analysis' in st.session_state:
            st.markdown("---")
            st.markdown("### Detailed Model Solutions & Breakdown")
            
            with st.expander("View Complete Analysis Result", expanded=True):
                st.markdown(st.session_state['last_analysis'])
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            try:
                pdf_buffer = create_pdf_report(st.session_state['last_analysis'])
                st.download_button(
                    label="Download Complete Numbered PDF Report",
                    data=pdf_buffer,
                    file_name="PyQfy_Complete_Model_Solutions.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
            except Exception as pdf_err:
                st.error(f"Could not build PDF report: {str(pdf_err)}")
        
        st.markdown("</div>", unsafe_allow_html=True)

# Section 2: AI Assistant Chat
elif nav_choice == "AI Assistant":
    st.markdown("<h1 class='main-title'>Gemini AI Academic Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Ask any complex academic doubt, derivation, or concept breakdown directly.</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if query := st.chat_input("Type your academic query or problem here..."):
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        with st.chat_message("assistant"):
            with st.spinner("Formulating deep model explanation..."):
                response = ask_gemini(query)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                
    st.markdown("</div>", unsafe_allow_html=True)

# Section 3: Feedback Form (Integrated with Formspree)
elif nav_choice == "Feedback":
    st.markdown("<h1 class='main-title'>Send Your Feedback</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Help us enhance PyQfy by sharing your valuable feedback and suggestions.</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='glass-card' style='max-width: 650px; margin: 0 auto;'>", unsafe_allow_html=True)
    with st.form("feedback_form"):
        name = st.text_input("Your Full Name", placeholder="Sachin Kumadalikar")
        email = st.text_input("Your Email Address", placeholder="sachin@example.com")
        msg = st.text_area("Feedback / Suggestions", placeholder="Write your thoughts or feature requests here...", height=120)
        submitted = st.form_submit_button("Submit Feedback", use_container_width=True)
        
        if submitted:
            if name and email and msg:
                # Replace with your actual Formspree endpoint URL
                formspree_url = "https://formspree.io/f/mdeajldr"
                
                payload = {
                    "name": name,
                    "email": email,
                    "message": msg
                }
                
                try:
                    res = requests.post(formspree_url, data=payload)
                    if res.status_code == 200:
                        st.success("Thank you! Your feedback has been sent successfully.")
                    else:
                        st.error("Failed to send feedback. Please verify your Formspree URL.")
                except Exception as ex:
                    st.error(f"An error occurred: {str(ex)}")
            else:
                st.warning("Please fill in all the required fields before submitting.")
    st.markdown("</div>", unsafe_allow_html=True)
