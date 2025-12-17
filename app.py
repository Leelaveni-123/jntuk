import streamlit as st

# Set page configuration
st.set_page_config(page_title="Student Grade Calculator", layout="centered")

# Add custom CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stMetric {
        background-color: #f0f7ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📚 Student Grade Calculator")
st.markdown("Calculate your academic grade and percentage")

# Add some spacing
st.markdown("---")

# Step 1: Get number of subjects
st.header("Step 1: Number of Subjects")
num_subjects = st.number_input(
    "How many subjects do you have?",
    min_value=1,
    max_value=12,
    value=1,
    step=1
)

st.markdown("---")

# Step 2: Get marks for each subject
st.header("Step 2: Enter Marks")
st.info("📝 Enter marks for each subject (out of 100)")

marks = {}
subject_names = {}

# Create columns for better layout
col1, col2 = st.columns(2)

for i in range(num_subjects):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"**Subject {i + 1}**")
        subject_names[i] = st.text_input(
            f"Subject {i + 1} name (optional):",
            value=f"Subject {i + 1}",
            key=f"subject_name_{i}",
            label_visibility="collapsed"
        )
        marks[i] = st.number_input(
            f"Marks for Subject {i + 1}:",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
            step=0.5,
            key=f"marks_{i}",
            label_visibility="collapsed"
        )

st.markdown("---")

# Step 3: Calculate and Display Results
st.header("Step 3: Results")

if st.button("📊 Calculate Grade & Percentage", use_container_width=True):
    # Calculate total and percentage
    total_marks = sum(marks.values())
    percentage = (total_marks / num_subjects)
    
    # Determine grade
    if percentage >= 90:
        grade = "A"
        grade_color = "🟢"
    elif percentage >= 80:
        grade = "B"
        grade_color = "🟢"
    elif percentage >= 70:
        grade = "C"
        grade_color = "🟡"
    elif percentage >= 60:
        grade = "D"
        grade_color = "🟠"
    else:
        grade = "F"
        grade_color = "🔴"
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Marks", f"{total_marks:.2f}", "out of " + str(num_subjects * 100))
    
    with col2:
        st.metric("Percentage", f"{percentage:.2f}%")
    
    with col3:
        st.metric("Grade", f"{grade_color} {grade}")
    
    st.markdown("---")
    
    # Display subject-wise breakdown
    st.subheader("📋 Subject-wise Breakdown")
    
    for i in range(num_subjects):
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.write(subject_names[i])
        with col2:
            st.write(f"Marks: {marks[i]:.2f}")
        with col3:
            percentage_subject = (marks[i] / 100) * 100
            st.write(f"{percentage_subject:.1f}%")
    
    st.markdown("---")
    
    # Grade scale information
    st.subheader("📊 Grade Scale")
    grade_info = """
    | Grade | Percentage Range | Status |
    |-------|------------------|--------|
    | A | 90-100% | Excellent |
    | B | 80-89% | Very Good |
    | C | 70-79% | Good |
    | D | 60-69% | Satisfactory |
    | F | Below 60% | Fail |
    """
    st.markdown(grade_info)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</p>",
    unsafe_allow_html=True
)
