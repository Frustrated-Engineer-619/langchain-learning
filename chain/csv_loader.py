from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_network_ads.csv')
data = loader.load()

print(data[0].page_content)