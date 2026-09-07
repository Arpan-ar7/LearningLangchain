from langchain_community.tools import DuckDuckGoSearchRun


search_tool=DuckDuckGoSearchRun()

results=search_tool.invoke('todays news')

print(results)