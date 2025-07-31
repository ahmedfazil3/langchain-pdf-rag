from rag_chain import generate_retrieval_chain

chain = generate_retrieval_chain("sample.pdf")
query = "What is this document about?"
result = chain.run(query)

print("Answer:", result)
