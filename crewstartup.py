from crewai import Agent, LLM

llm = LLM(model='gemini/gemini-1.5-flash',
              api_key='AIzaSyCx4YPE2h9KjCbk9bia4dhynDIPDoXV5N0' )
#Next, we will start to set up the agent. In this example, we will have an agent that can assist us in learning a new language. To do that, we will use the following code.

language_tutor_agent = Agent(

    role="Language Tutor",
    goal="To assist users in learning a new language by providing practice exercises.",
    backstory="A former language teacher with experience in helping students achieve fluency in various languages.",
    verbose=True,
    llm=llm

)
    
