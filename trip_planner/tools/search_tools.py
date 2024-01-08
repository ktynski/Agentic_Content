import json
import os

import requests
from langchain.tools import tool


class SearchTools():

  @tool("research")
  def query_web_llm(query):
      headers = {"X-API-Key": "e80d4720-af51-4145-bd57-18867d220c1e<__>1OWO11ETU8N2v5f4trtX69bl-PL49zmXP0geLfl"}
      params = {"query": query}
      return requests.get(
          f"https://api.ydc-index.io/rag?query={query}",
          params=params,
          headers=headers,
      ).json()
