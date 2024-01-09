from crewai import Crew
from textwrap import dedent
from agents import ContentAgents
from tasks import ContentTasks

from google.colab import userdata
openai_api_key = "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"
SERP_API_KEY = "ecc7d445fb803a51d6a2c16f027f0cef45e01457ad348257072521424d0d217d"
YOU_API_KEY = "e80d4720-af51-4145-bd57-18867d220c1e<__>1OWO11ETU8N2v5f4trtX69bl-PL49zmXP0geLfl"


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
