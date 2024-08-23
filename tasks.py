from crewai import Task
from tools import pdf_parser_tool, serper_tool
from agents import Blood_Test_Analyzer, HealthArticle_Searcher, HealthAdvisor

## Blood_Test_Analysis

blood_test_analysis = Task(
    name="Blood Test Analysis",
    description="""
    The Blood Test Analysis task involves analyzing the results of a comprehensive blood test to identify potential health issues, nutritional deficiencies, or other medical conditions. 
    The task requires interpreting a detailed report that includes measurements of various blood components such as red blood cells, white blood cells, platelets, hemoglobin, cholesterol, and blood sugar levels. 
    The analysis should identify any abnormalities or patterns that may indicate underlying health problems, providing insights into the individual's overall health status.
    """,
    expected_output="A 3-long para analysis of the blood test results, highlighting any abnormal values, potential health concerns, and recommendations for further evaluation or lifestyle changes.",
    agent=Blood_Test_Analyzer,

    tools=[serper_tool,pdf_parser_tool], 
    allow_delegation=True
)

## Health_Article_Search

health_article_search = Task(
    name="Health Article Search",
    description="""
    The Health Article Search task involves searching the internet for health-related articles that are specifically tailored to the health needs identified by the Blood_Test_Analyzer. 
    The task requires finding credible sources that address the specific health concerns, dietary recommendations, and lifestyle changes relevant to the individual's blood test results as analyzed by the Blood_Test_Analyzer.
    """,
    expected_output="A curated list of articles  with their links to access them, with brief summaries, focusing on those that provide actionable advice or relevant information for the individual's health needs.",
    agent=HealthArticle_Searcher,
    tools=[serper_tool],  # Using the SerperDevTool for internet search
    allow_delegation=True
)

## Health_Advisor




health_advice = Task(
    name="Health Advisor",
    description="""
    The Health Advisor task involves providing personalized health recommendations based on the blood test analysis from the Blood_Test_Analyzer 
    and the relevant health articles gathered by the HealthArticle_Searcher. 
    The recommendations should focus on actionable lifestyle changes, dietary adjustments, and other health-improving actions tailored to the individual's needs.
    """,
    expected_output="A detailed set of personalized health recommendations, including actionable steps, dietary suggestions, and lifestyle modifications.",
    agent=HealthAdvisor,
    tools = [serper_tool],
    allow_delegation=True
)
