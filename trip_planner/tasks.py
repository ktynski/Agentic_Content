from crewai import Task
from textwrap import dedent
from datetime import date

class ContentTasks():

  def google_research_task(self, agent, topic, scope):
    return Task(description=dedent(f"""
        Conduct in-depth research on the following topic: {topic}.
        The scope of the research should cover {scope}.
        Your final output should be a comprehensive report summarizing
        key findings and relevant data. Ensure that the information is 
        accurate, up-to-date, and well-sourced.
      """),
                agent=agent)

  def you_research_task(self, agent, topic, scope):
    return Task(description=dedent(f"""
        Conduct in-depth research on the following topic: {topic}.
        The scope of the research should cover {scope}.
        Your final output should be a comprehensive report summarizing
        key findings and relevant data. Ensure that the information is 
        accurate, up-to-date, and well-sourced. Use this function when you want to use You.com's data.
      """),
                agent=agent)

                  # You can keep the __tip_section if it's still relevant to your context
  def __tip_section(self):
    return "If you do your BEST WORK, I'll tip you $100!"
'''
  def editing_task(self, agent, document):
    return Task(description=dedent(f"""
        Review and edit the following document: {document}.
        Focus on improving clarity, grammar, and style.
        Ensure that the final document is error-free and polished.
      """),
                agent=agent)

  def document_handling_task(self, agent, documents):
    return Task(description=dedent(f"""
        Organize and manage the following set of documents: {documents}.
        Your task includes categorizing, labeling, and storing the 
        documents efficiently. Ensure easy retrieval and maintenance.
      """),
                agent=agent)

  def outline_generating_task(self, agent, content_type, main_points):
    return Task(description=dedent(f"""
        Create an outline for a {content_type}.
        The outline should cover the following main points: {main_points}.
        Ensure that the structure is logical, clear, and facilitates 
        an effective narrative or argument flow.
      """),
                agent=agent)

  def information_synthesizing_task(self, agent, data_sources):
    return Task(description=dedent(f"""
        Synthesize information from the following sources: {data_sources}.
        Your task is to integrate this information into a cohesive and
        comprehensive narrative or report. Focus on drawing connections 
        and presenting the information in an easily digestible format.
      """),
                agent=agent)'''


