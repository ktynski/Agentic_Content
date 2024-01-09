import json
import os

import requests
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html



class BrowserTools():

  @tool("scrape_articles")
  def scrape_articles(self,query):
      """Always the first step, extract the research corpus by scraping and compiling the search results."""
      all_results = []
      num_articles = 10
      article_count = 0
      page = 0

      while article_count < num_articles:
          start_index = page * 10  # Google usually shows 10 results per page
          params = {
              "engine": "google",
              "q": query,
              "start": start_index,
              "gl": "us",
              "api_key": SERP_API_KEY
          }

          try:
            search = GoogleSearch(params)
            results = search.get_dict()
            print(results)
            serp_data = results["organic_results"]
          except:
            print("failed to get organic results")

          for result in serp_data:
              if article_count >= num_articles:  # Check if desired number of articles reached
                  break

              try:
                  link = result['link']
                  title = result['title']
                  snippet = result.get('snippet', '')

                  article_text = Article(link)
                  article_text.download()
                  article_text.parse()

                  text = article_text.text
                  authors = article_text.authors
                  publish_date = article_text.publish_date

                  if len(text.split()) >= 500:
                      root_domain = get_root_domain(link)  # Ensure this function is defined
                      all_results.append((root_domain, link, title, authors, publish_date, snippet, text))
                      article_count += 1
              except Exception as e:
                  print(f"Couldn't download article from {link}: {e}")

          page += 1  # Increment the page number for the next iteration

      columns = ['Root Domain', 'Link', 'Title', 'Authors', 'Publish Date', 'Snippet', 'Text']
      article_df = pd.DataFrame(all_results, columns=columns)
      article_df.to_csv("articles_dataframe.csv", index=False)
      print("Filtered Results from SerpAPI")

      return article_df
