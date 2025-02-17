from crewai import Task

language_tutor_agent = Agent(
    role="Language Tutor",
    goal="To assist users in learning a new language by providing practice exercises.",
    backstory="A former language teacher with experience in helping students achievefluency in various languages.",
    verbose=True,
    llm=llm
)

language_practice_task = Task(
    description="Provide language {language} practice plan exercises based on theuser's proficiency level: {proficiency},including vocabulary, grammar, and conversation practice.",
    expected_output="A set of tailored language exercises with detailed explanations",
    agent=language_tutor_agent
)
