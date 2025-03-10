from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
# from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("hello langchain")

    summary_template = """
        given the Linkedin information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """


    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    # llm = ChatOllama(model="llama3.1")
    # llm = ChatOllama(model="mistral")
    # create a chain
    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/samirsatam/")
    res = chain.invoke(input={"information": linkedin_data})
    print(res)
