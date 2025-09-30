# Resources

## API Gateway, LB
General: DNS -> LB -> API Gateway -> BE Service
> DNS resolves to LB which fetches response from API Gateway Service


- LB = Software at protocol/socket level to balance incoming traffic and distribute to appropriate destinations
- API Gateway = Managed service via hosting companies taking care of access control, response caching,

- Several API Gateway Clusters
> Scenario 1: User -> DNS -> LB -> API Gateway Cluster -> Service Discovery -> Client LB -> Microservices

- Single API Gateway
> Scenario 2: User -> Gateway -> Microservices

## Inverted Index -> ElasticSearch
- DS = Data Structure
- II is a DS used in info retrieval systems for efficient retrieval of documents/web pages for specific term/set of terms
    * Index is organized by terms(words), each term pointing to a list of docs/web pages with said term
    * Widely used in search engines, db systems, other apps requiring efficient text search
    * Useful for large collections of documents

    > Hashmap like ds directing a user from a word to a document/web page
    - Two types:
        * Record-Level: Contains list of references to documents for each word
        * Word-Level: additionally contains word positions in each document (req more processing power, space for creation)

    > Features
    - Efficient Search: quick id of all docs containing given search term/phrase
    - Fast updates: Quick and efficient updates with new content (near real time indexing)
    - Flexibility: Can be customized for various info retrieval system types
    - Compression: allows for lower storage reqs using encoding
    - Multi Language Support




- Example of II:
    * Word-Level Inverted Index: contains `(index of document that word occurs in, word position)`
        ```
        hello                (1, 1)
        everyone             (1, 2)
        this                 (2, 1)
        article              (2, 2)
        is                   (2, 3); (3, 2)
        based                (2, 4)
        on                   (2, 5)
        inverted             (2, 6)
        index                (2, 7)
        which                (3, 1)
        hashmap              (3, 3)
        like                 (3, 4)
        data                 (3, 5)
        structure            (3, 6)
        ```
        * Steps for Building II:
            1. Fetch Document and remove stopping words
            2. Stem root word -> cop part of every word read to get 'root word' (use Porter's Stemmer)
            3. Record Document Id: if word is already present, add document reference to index else create new entry
                * Add more info like word frequency, word location to induce more weights
                ```
                doc1 = " "
                doc2 = " "
                tokens1 = doc1.lower().split()
                tokens2 = ...
                terms = list(set(tokens1+tokens2))
                inverted_index = {}
                for term in terms:
                    documents = []
                    if term in tokens1:
                        documents.append("Document 1")
                    if term in tokens2:
                        documents.append("Document 2")
                    inverted_index[term] = documents
                for term, documents in inverted_index.items():
                    print(term, "->", ", ".join(documents))
                ```

- Advs of II
    * allows for fast full text search at cost of increased processing for additional docs
    * easy developing, most popular structure in doc retrieval systems
- Disadvs of II
    * large storage overhead, high maintenance costs on operations
    * records retrieved in order they occur in inverted lists vs usefulness
