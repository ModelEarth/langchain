import os

from flask import Flask, request, jsonify
from queue import Queue
import threading

from app.configuration.ConfigParser import ConfigParser
from app.configuration.Constants import Constants
from app.configuration.EnvironmentLoader import EnvironmentLoader
from app.document_fetcher.GithubDocumentFetcher import GithubDocumentFetcher
from app.langchain_chaining.prompt_chaining import ModelEarthQA
from app.llm_model.LLM import LLMModel
from app.vector_store.InMemoryVectorStore import InMemoryStore




app = Flask(__name__)

# Create a thread-safe Queue
data_queue = Queue()


"""
Loading environment variables for developer mode

Defining LLM and the vector store to be used (move thise somewhere else?)
"""
model_path = os.path.join(Constants.MODEL_DIRECTORY, f'{ConfigParser.get_key_value("model_name")}.json')
EnvironmentLoader.load_variables()
llm = LLMModel('gpt-3.5-turbo-0125').get_model()
vector_store = InMemoryStore(path = model_path)


# Function for background processing thread
def process_jobs():
    while True:
        data = data_queue.get()
        if data:

            try:
                documents = GithubDocumentFetcher(data).fetch_and_process()


                # InMemoryStore(path = model_path).load_and_get_model().update_model(documents)

                """
                  updating the same in memory model as we have just one processor. Have to move out this logic once we scale it up
                """
                vector_store.update_model(documents)

            except Exception as e:
                print(f" Could not fetch/process data {e} ")
        data_queue.task_done()

@app.route('/update-vectordb', methods=['POST'])
def post_data():

    target_repo = request.args.get('repo_name')

    if not target_repo:
        return jsonify({"error": "No repo provided"}), 400
    data_queue.put(target_repo)
    return jsonify({"message": "Repo added for processing", "queue_size": data_queue.qsize()}), 200

@app.route('/get-result', methods=['GET'])
def get_queue():

    target_repo = request.args.get('repo_name')
    filter = {'repo': target_repo}
    query = request.args.get('query')

    if not query:
        return jsonify({"error": "No query parameters provided"}), 400

    try:
        qa = ModelEarthQA(llm, vector_store)
        answer = qa.answer_query(query, filter)
        return jsonify({"answer": answer}), 200
    except Exception as e:
        print(f"Could not retrieve results due to error {e}")

    return jsonify({"error": "The service is down"}), 500


if __name__ == '__main__':
    # Start the background thread before running Flask

    processing_thread = threading.Thread(target=process_jobs, daemon=True)
    processing_thread.start()

    # Run the Flask app
    app.run(threaded=True, debug=True)

