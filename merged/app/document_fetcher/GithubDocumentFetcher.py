import os
from langchain_community.document_loaders import GithubFileLoader


class GithubDocumentFetcher():

    def __init__(self, repo):
        self.repo = repo


    def fetch_and_process(self):

        github_token = os.getenv("GITHUB_TOKEN")
        loader = GithubFileLoader(
            repo= self.repo, # Mention the repo we need
            branch="main",  # the branch name
            access_token=github_token,
            github_api_url="https://api.github.com",
            file_filter=lambda file_path: file_path.endswith(
                "README.md"
            ),
        )
        documents = loader.load_and_split()

        # adding filter key repo
        for doc in documents:
            doc.metadata['repo'] = self.repo
            print(doc)
            print(doc.metadata)
            print(doc.page_content)

        return documents
