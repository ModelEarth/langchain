import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from app.configuration.ConfigParser import ConfigParser
from app.configuration.Constants import Constants
from app.configuration.EnvironmentLoader import EnvironmentLoader
from app.llm_model.LLM import LLMModel
from app.vector_store.InMemoryVectorStore import InMemoryStore


class ModelEarthQA:

    def __init__(self, llm, db):
        self.llm = llm
        self.db = db

    def construct_prompt(self):
        template = """Answer the question based only on the following context:
        {context}

        Question: {question}
        """

        prompt = ChatPromptTemplate.from_template(template)
        print(prompt)
        return prompt

    def answer_query(self, query, metadata_filters = {}):
        filter = metadata_filters
        k = 5

        retriever = self.db.get_retriever(filter, k)

        setup_and_retrieval = RunnableParallel(
            {"context": retriever, "question": RunnablePassthrough()}
        )
        chain = setup_and_retrieval | self.construct_prompt() | self.llm | StrOutputParser()

        return chain.invoke(query)


if __name__ == "__main__":
    EnvironmentLoader.load_variables()
    model_path = os.path.join(Constants.MODEL_DIRECTORY, f'{ConfigParser.get_key_value("model_name")}.json')
    llm = LLMModel('gpt-3.5-turbo-0125').get_model()
    retriever = InMemoryStore(path = model_path).load_and_get_model()
    qa = ModelEarthQA(llm ,retriever)
    print(qa.answer_query('Tell me about model earth'))

