import PyPDF2
from crewai_tools import SerperDevTool, PDFSearchTool
from dotenv import load_dotenv
load_dotenv()




pdf_parser_tool = PDFSearchTool(
    pdf_path=r"C:\Users\chopr\OneDrive\Desktop\Wingify\blood_report.pdf", 
    config=dict(
        llm=dict(
            provider="google",  
            config=dict(
                model="gemini-pro",  # Use the "gemini-pro" model
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



serper_tool = SerperDevTool(
    # api_key=os.getenv("SERPER_API_KEY")  # Replace with your actual API key
)







