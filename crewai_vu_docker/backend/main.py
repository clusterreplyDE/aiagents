from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from fastapi import FastAPI
import uvicorn

researcher = Agent(
    role='Researcher',
    goal='Gather information about a given topic',
    backstory='An advanced AI designed to collect information quickly.',
    tools=[SerperDevTool()],
    verbose=True
)

writer = Agent(
    role='Writer',
    goal='Generate an article based on research',
    backstory='Creates clear summaries from facts.',
    verbose=True
)

task1 = Task(
    description='Research topic: {topic}',
    expected_output='Summary of key facts about {topic}.',
    agent=researcher
)

task2 = Task(
    description='Write short article about {topic}',
    expected_output='Article text about {topic}',
    agent=writer
)

crew = Crew(tasks=[task1, task2])

app = FastAPI()

@app.get('/run')
def run(topic: str):
    result = crew.kickoff(inputs={'topic': topic})
    return {'result': result}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
