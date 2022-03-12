from fastapi import FastAPI

app = FastAPI(
    title='Um-sc-search',
    description='Semantic search on um6p papers',
    docs_url='/'
)


@app.get('/api')
def get_sample() -> str:
    return 'sample request'


@app.post('/api/post')
def post_sample(sample: str):
    return sample

@app.post("/get_neighbors/")
def get_neighbors(paper_id:str, k:int=6):
    paper_emb =index.fetch([paper_id,])['vectors'][paper_id]['values']

    paper_emb = [float(k) for k in paper_emb]

    # top k neighbors
    resp = index.query(
    queries=[paper_emb],
    top_k=k,
    include_values=False
    )
    # prep resp 
    match_ids = [match['id'] for match in resp['results'][0]['matches']]
    match_ids = match_ids[1:]

    return match_ids