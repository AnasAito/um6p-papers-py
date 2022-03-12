

import pinecone


# init vector db 
pinecone.init(api_key="d6e01d18-5764-44d7-93ce-1a489066cc9e", environment="us-west1-gcp")
index = pinecone.Index("papersembs")

"""# papers meta data
with open('papers.pickle', 'rb') as handle:
    papers = pickle.load(handle)"""




