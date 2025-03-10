from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

if __name__ == "__main__":
    print("hello langchain")

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    information = """
   George Washington Carver (c. 1864[1] – January 5, 1943) was an American agricultural scientist and inventor who promoted alternative crops to cotton and methods to prevent soil depletion.[2] He was one of the most prominent black scientists of the early 20th century.

While a professor at Tuskegee Institute, Carver developed techniques to improve types of soils depleted by repeated plantings of cotton. He wanted poor farmers to grow other crops, such as peanuts and sweet potatoes, as a source of their own food and to improve their quality of life.[3] Under his leadership, the Experiment Station at Tuskegee published over forty practical bulletins for farmers, many written by him, which included recipes; many of the bulletins contained advice for poor farmers, including combating soil depletion with limited financial means, producing bigger crops, and preserving food.

Apart from his work to improve the lives of farmers, Carver was also a leader in promoting environmentalism.[4] He received numerous honors for his work, including the Spingarn Medal of the NAACP. In an era of high racial polarization, his fame reached beyond the black community. He was widely recognized and praised in the white community for his many achievements and talents. In 1941, Time magazine dubbed Carver a "Black Leonardo".[5] 
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    # llm = ChatOllama(model="llama3.1")
    llm = ChatOllama(model="mistral")
    # create a chain
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})
    print(res)
