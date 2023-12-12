from collections import defaultdict

# Example documents
documents = {
    1: "Cloud computing is the on-demand availability of computer system resources.",
    2: "One integrated service for metrics uptime cloud monitoring dashboards and alerts reduces time spent navigating between systems.",
    3: "Monitor entire cloud infrastructure, whether in the cloud computing is or in virtualized data centers."
}

# Building the inverted index
inverted_index = defaultdict(set)

for doc_id, text in documents.items():
    words = text.lower().split()
    for word in words:
        inverted_index[word].add(doc_id)

def search(query):
    words = query.lower().split()
    # Find document sets for each word
    doc_sets = [inverted_index[word] for word in words if word in inverted_index]
    # Intersect the sets
    result = set.intersection(*doc_sets) if doc_sets else set()
    return list(result)

# Example searches
print(search("cloud"))  # Output: [1, 2, 3]
print(search("cloud monitoring"))  # Output: [2]
print(search("Cloud computing is"))  # Output: [1, 3]
