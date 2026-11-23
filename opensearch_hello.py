from opensearchpy import OpenSearch

client = OpenSearch(hosts=[{"host": "localhost", "port": 9200}], use_ssl=False)

print("Connected to OpenSearch", client.info()["version"]["number"])

index = "my-notes"
if not client.indices.exists(index=index):
    client.indices.create(index=index)

client.index(
    index=index,
    id=3,
    body={"title": "What is Iceberg", "text": "Iceberg is an open table format for data lakes."},
    refresh=True,
)

results = client.search(
    index=index,
    body={"query": {"match": {"text": "table"}}},
)

for hit in results["hits"]["hits"]:
    print(hit["_score"], hit["_source"]["title"])