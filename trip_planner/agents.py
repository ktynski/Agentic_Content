from crewai import Agent
from langchain.llms import OpenAI

from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
#from tools.document_tools import DocumentTools
#from tools.editing_tools import EditingTools
#from tools.outline_tools import OutlineTools
#from tools.research_tools import ResearchTools
#from tools.synthesis_tools import SynthesisTools


class ContentAgents():

  def google_research_agent(self):
    return Agent(
        role='Research Expert',
        goal='Conduct thorough research on specified topics',
        backstory=
        'An expert in gathering and analyzing information from various sources',
        tools=[
            BrowserTools.scrape_articles,
        ],
        verbose=True)

  def you_research_agent(self):
    return Agent(
        role='Research Expert',
        goal='Conduct thorough research on specified topics',
        backstory=
        'An expert in gathering and analyzing information from various sources',
        tools=[
            SearchTools.query_web_llm,
        ],
        verbose=True)




  '''  
  def writing_agent(self):
    return Agent(
        role='Skilled Writer',
        goal='Compose well-structured and engaging content',
        backstory="""An experienced writer with a knack for clear and 
        compelling writing""",
        tools=[
            OpenAI.write_text,
        ],
        verbose=True)

  def editor_agent(self):
    return Agent(
        role='Expert Editor',
        goal='Refine and perfect written content',
        backstory="""A detail-oriented editor focused on clarity, grammar, 
        and style""",
        tools=[
            EditingTools.edit_text,
        ],
        verbose=True)

  def document_handling_agent(self):
    return Agent(
        role='Document Specialist',
        goal='Efficiently manage and organize documents',
        backstory="""A professional in handling, categorizing, and 
        maintaining various documents""",
        tools=[
            DocumentTools.organize_documents,
        ],
        verbose=True)

  def outline_generating_agent(self):
    return Agent(
        role='Outline Creator',
        goal='Develop clear and effective outlines for content',
        backstory="""A strategic thinker skilled in structuring content 
        for optimal flow and comprehension""",
        tools=[
            OutlineTools.create_outline,
        ],
        verbose=True)

  def information_synthesizing_agent(self):
    return Agent(
        role='Synthesis Expert',
        goal='Integrate and summarize information cohesively',
        backstory="""An analytical mind adept at weaving together disparate 
        pieces of information into a cohesive whole""",
        tools=[
            SynthesisTools.synthesize_information,
        ],
        verbose=True)'''
