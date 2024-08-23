
import streamlit as st
from crewai import Crew, Process
from agents import Blood_Test_Analyzer, HealthArticle_Searcher, HealthAdvisor
from tasks import blood_test_analysis, health_article_search, health_advice
from crewai_tools import SerperDevTool, PDFSearchTool
from dotenv import load_dotenv
load_dotenv()

# Streamlit app title
st.title("Blood Analysis with CrewAI")


# Description
st.write("""
This application analyzes blood test reports, searches for relevant health articles, 
and provides health advice based on the results.
""")

# Upload PDF file
uploaded_file = st.file_uploader("Upload your blood test report (PDF)", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("uploaded_blood_report.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Initialize the PDF parser tool with the uploaded file
    pdf_parser_tool = PDFSearchTool(
        pdf_path="uploaded_blood_report.pdf",  # Use the uploaded file path
        config=dict(
            llm=dict(
                provider="google",
                config=dict(
                    model="gemini-pro",
                    temperature=0.5,
                ),
            ),
            embedder=dict(
                provider="google",
                config=dict(
                    model="models/embedding-001",
                    task_type="retrieval_document",
                ),
            ),
        )
    )

    # Initialize SerperDevTool (for search engine tasks)
    serper_tool = SerperDevTool(
        # api_key=os.getenv("SERPER_API_KEY")  # Ensure the API key is set correctly in your .env file
    )

    # Set up the Crew with the tools
    crew = Crew(
        agents=[Blood_Test_Analyzer, HealthArticle_Searcher, HealthAdvisor],
        tasks=[blood_test_analysis, health_article_search, health_advice],
        process=Process.sequential,
        # memory=True,
        # cache=True,
        # share_crew=True
    )

    # Button to kick off the process
    if st.button('Kickoff Analysis'):
        with st.spinner('Analyzing...'):
            result = crew.kickoff()
            st.success('Analysis complete!')
            # Display the result
            st.write(result)
else:
    st.warning("Please upload a PDF file to proceed.")


