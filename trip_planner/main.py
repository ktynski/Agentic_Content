from crewai import Crew
from textwrap import dedent
from agents import ContentAgents
from tasks import ContentTasks

from google.colab import userdata
openai_api_key = ""
SERP_API_KEY = ""
YOU_API_KEY = ""


from crewai import Crew
from textwrap import dedent

class ContentCrew:

  def __init__(self, research_topic,scope):
    self.research_topic = research_topic
    self.scope = scope



  def run(self):
    agents = ContentAgents()
    tasks = ContentTasks()

    g_research_agent = agents.google_research_agent()  # or you_research_agent, based on your preference
    y_research_agent = agents.you_research_agent()


    get_google_research = tasks.google_research_task(
      g_research_agent,
      self.topic,
      self.scope,

    )
    get_you_research = tasks.you_research_task(
      y_research_agent,
      self.topic,
      self.scope,

    )




    crew = Crew(
      agents=[
        research_agent, you_research_agent
      ],
      tasks=[
        google_research_task,you_research_task
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to the AI Content Crew")
  print('-------------------------------')
  query = "Matt Walsh Bigotry"
  scope = "Large"

  # Example initialization, replace with appropriate inputs
  content_crew = ContentCrew(query,scope) 
  result = content_crew.run()
  print("\n\n########################")
  print("## Here is your Content")
  print("########################\n")
  print(result)
