# **Full Text Search (FTS)**

## **Scenario**

You are working at **LinkedIn**, and you need to build a **job search feature** to help users find relevant job postings.

```sql
create table job_postings (
  id bigint primary key,
  title text not null,
  description text,
  created_at timestamp,
  ...
);
```

---

## **Problem Statement**

Given a search query like `"python senior developer"`, how will you find the relevant jobs?

---

### **Query 1 – Exact Match**

```sql
select *
from job_postings
where title = 'python senior developer'
limit 10;
```

#### **Complexity Analysis**

* If the table has **N rows** and each row has **M characters** on average:

  ```
  Time Complexity = O(N * M)
  ```

  → You must scan all rows and compare strings.

✅ **Observation:** This approach is **very slow** for large datasets.

---

### **Improving with Indexes**

```sql
create index idx_job_title on job_postings (title);
create index idx_job_desc on job_postings (description);
```

#### **After Indexing**

* Lookup uses B+Tree index

  ```
  Time Complexity = O((log N) * M)
  ```

✅ **Better performance** for exact matches or prefix matches.

❌ **But not good enough** for partial or semantic search.

---

### **Example Job Posting**

```json
{
  "id": 101,
  "title": "Senior Python Developer needed in Bangalore",
  "description": "We seek a proactive Backend Developer cum Tester with 5-8 years of experience who owns quality and excels in collaboration. Required expertise includes Python, Django, microservices, distributed systems, message buses, multi-threading, CI/CD, automated testing, databases, and cloud platforms.",
  "created_at": "2025-07-03"
}
```

#### **Will the query match this?**

```sql
select *
from job_postings
where title = 'python senior developer'
limit 10;
```

❌ **No.**
Because it only matches **exact strings**, not **partial or rearranged words**.

---

### **Query 2 – Using Wildcards**

```sql
select *
from job_postings
where
  (title ilike '%python%' or description ilike '%python%')
  and
  (title ilike '%senior%developer%' or description ilike '%senior%developer%')
limit 10;
```

#### **Complexity Analysis**

Even with indexes:

```
Time Complexity = O(N * M)
```

✅ Uses `%` wildcards for partial matches.
❌ Still performs a **full table scan** because:

* **B+Tree indexes** support only **exact** or **prefix** matches.
* Cannot efficiently handle **arbitrary substring searches**.

---

## **What Users Actually Expect**

Users expect **semantic search**, not just literal text match.

### **Semantic Search Requirements**

1. 🔍 **Search all relevant fields** (title + description)
2. 🔄 **Word order doesn’t matter**

   * “senior python developer”
   * “python developer, senior”
3. ✨ **Partial word matching**

   * “senior java or python developer”
4. 📝 **Handle spelling mistakes**

   * “pythn” → “python”
5. 💡 **Understand context**

   * “python developer” ≠ “python snake trainer”
6. 🧠 **Include synonyms**

   * “lead python programmer” ≈ “senior python developer”

---

## **Definition**

> **Full Text Search (FTS)** is the technique of searching text **comprehensively and semantically**, not just for exact matches.

### **Goals of FTS**

1. Search the text **fully** – anywhere in the text, not just prefix/postfix.
2. Capture **semantic meaning** – handle synonyms, order, context, etc.

---

## **Common Use Cases**

1. 📜 **Log Search & Analysis**
   (Observability tools, e.g. Splunk, ELK stack)
2. 👥 **User Data Indexing**
   (Posts, comments, reviews, chat messages)
3. 📄 **Document Search**
   (PDFs, resumes, books)
4. 🛒 **Product Search**
   (E-commerce sites like Amazon)
5. 🌐 **Web Search Engines**
   (Google, Bing, etc.)

---

✅ **Summary**

| Query Type               | Technique                                              | Time Complexity | Matches              | Limitations  |
| ------------------------ | ------------------------------------------------------ | --------------- | -------------------- | ------------ |
| Query 1                  | Exact match                                            | O(N * M)        | Only exact text      | Very slow    |
| Query 1 (with index)     | Indexed exact/prefix match                             | O((log N) * M)  | Exact or prefix only | Not semantic |
| Query 2 (with wildcards) | `ilike '%keyword%'`                                    | O(N * M)        | Partial match        | Full scan    |
| Full Text Search         | FTS Engine (e.g. PostgreSQL `tsvector`, Elasticsearch) | O(log N)        | Semantic match       | Needs setup  |

---

# **Why is SQL a Bad Choice for Full Text Search?**

### **1. SQL Queries Cannot Capture Nuanced Semantics**

* SQL is designed for **structured data**, not for **semantic text understanding**.
* It can’t interpret meaning, synonyms, or context.
* Example:
  Searching for `"python developer"` won’t match `"backend engineer with python experience"`.

---

### **2. SQL Indexes Use B+Tree**

#### ✅ **Good For**

* **Exact text matches**
  e.g., `WHERE title = 'Python Developer'`
* **Prefix matches**
  e.g., `WHERE title LIKE 'Python%'`

#### ❌ **Bad For**

* **Arbitrary substring matches**
  e.g., `WHERE title LIKE '%Python%'`
* **Long text fields** (e.g., job descriptions, documents)

> 🧩 **Reason:**
> B+Trees are optimized for *sorted key lookups*, not *text token search*.

---

### **Note**

Modern relational databases like **PostgreSQL** do offer **Full Text Search** (`tsvector`, `tsquery`),
but they’re **not optimized for text search at scale** (e.g., millions of long documents).

---

# **What About NoSQL Databases?**

* Even with **Redis** (key-value store) or **MongoDB** (document store),
  you still need to **scan each key/document** to find matches.
* The issue is **not the type of database**,
  it’s the **type of index** being used.

✅ To solve the Full Text Search problem efficiently,
we need a **specialized data structure** and **algorithm** —
→ **The Inverted Index.**

---

# **Inverted Index (Data Structure)**

---

## **Understanding with a Book Analogy**

### **Table of Contents (TOC)**

* **Mapping:**
  **Page number → Chapter/Title**

| Page | Chapter/Title        |
| ---- | -------------------- |
| 1    | Introduction         |
| 10   | SQL Basics           |
| 25   | Database Replication |

> If you know the **page number**, you can tell what’s there.
> But if you only know a **word**, you can’t find which page it’s on!

🧠 So, the **Table of Contents** is **not helpful** for searching *content*.

---

### **What We Actually Need**

An **Index (at the end of the book)**
that lists **important terms** and the **pages they appear on**.

| Keyword     | Page Numbers |
| ----------- | ------------ |
| Database    | 10, 25       |
| Replication | 25           |
| SQL         | 10           |

📘 **Mapping:**
**Keyword → Page numbers**

> Now, given a word, you can quickly find *where* it occurs.

---

## **Inverted Index Analogy in Databases**

Let’s say we have an array of documents:

```text
["Entry 1", "Entry 2", "Entry 3", ...]
```

### Normal Index:

* Given a **document ID**, find the **content**.
  → `index[i] → document`

### Inverted Index:

* Given a **word**, find the **document IDs** where it appears.
  → `inverted_index[word] → [doc_ids]`

---

## **Formal Definition**

> **Inverted Index** = a mapping from **token (keyword)** → **document ID(s)**

Example:

| Token     | Document IDs  |
| --------- | ------------- |
| python    | 101, 105, 220 |
| developer | 101, 150      |
| backend   | 105           |
| senior    | 101, 150, 199 |

---

# **Steps to Create the Inverted Index**

## **Pre-processing Pipeline**

> Pre-processing is done **independently for each document**.

For example, in **LinkedIn**, each **job posting** is treated as a **document**.
Our goal: efficiently search through all job postings.
So, we must first **pre-process each document** to prepare it for indexing.

---

### **Step 1: Parsing**

**Goal:** Extract only relevant text from raw data (e.g., HTML pages, PDFs, etc.)

#### **Input**

```html
<html>
<body>
<h1>Introduction to Full-Text Search</h1>
<script>console.log('irrelevant')</script>
<p>Full-text search lets you search documents efficiently.</p>
</body>
</html>
```

#### **Output**

```
"Introduction to Full-Text Search Full-text search lets you search documents efficiently."
```

✅ **Removes:** HTML tags, scripts, metadata, and other irrelevant content.

---

### **Step 2: Tokenization**

**Goal:** Split text into individual **words (tokens)** and remove punctuation.

#### **Input**

```
"Introduction to Full-Text Search Full-text search lets you search documents efficiently."
```

#### **Output**

```text
["Introduction", "to", "Full", "Text", "Search", "Full",
"text", "search", "lets", "you", "search", "documents",
"efficiently"]
```

✅ Breaks sentences into meaningful tokens.

---

### **Step 3: Normalization**

**Goal:** Standardize text — lowercase conversion, Unicode normalization, etc.

#### **Input**

```text
["Introduction", "to", "Full", "Text", "Search", "Full",
"text", "search", "lets", "you", "search", "documents",
"efficiently"]
```

#### **Output**

```text
["introduction", "to", "full", "text", "search", "full",
"text", "search", "lets", "you", "search", "documents",
"efficiently"]
```

✅ Ensures “Search” and “search” are treated the same.

---

### **Step 4: Stopword Removal**

**Goal:** Remove words that **don’t carry meaning** or are **undesirable**.

#### **Types of Stopwords**

* **Insensitive words:** slangs, abuses, racial slurs
* **Competitor brands:** “openai”, “swiggy”, etc.
* **Useless words:** “the”, “and”, “of”, “is”, etc.

#### **Input**

```text
["introduction", "to", "full", "text", "search", "full",
"text", "search", "lets", "you", "search", "documents",
"efficiently"]
```

#### **Output**

```text
["introduction", "full", "text", "search", "full", "text",
"search", "search", "documents", "efficiently"]
```

✅ Removes low-value or filler words to reduce noise.

---

### **Step 5: Reduction**

**Goal:** Reduce words to a **common root form**
(using **Stemming** or **Lemmatization**)

---

#### **A. Stemming**

* Algorithmic trimming of **suffixes/prefixes**.
* Works fast but can be **inaccurate** (“dumb” approach).

**Common suffixes:** `ion`, `s`, `es`, `ing`, `er`, `ful`, `acy`, `al`, `ism`, `ance`, `dom`, `or`, `ist`, `ly`
**Common prefixes:** `im`, `un`, `non`, `pre`, `over`, `extra`

| Word    | Stemmed |
| ------- | ------- |
| careful | care    |
| caring  | car     |

❌ “caring → car” — incorrect, since meaning is lost.

---

#### **B. Lemmatization**

* Uses **linguistic knowledge**, **dictionaries**, and **NLP rules**.
* Correctly maps **inflected**, **misspelled**, or **synonymous** words.

##### **Example Mapping (mappings.txt)**

| Word      | Lemma                    |
| --------- | ------------------------ |
| magical   | magic                    |
| careful   | care                     |
| caring    | care                     |
| joyful    | happy                    |
| happiness | happy                    |
| hapiness  | happy (spell correction) |
| overjoyed | happy                    |
| gleeful   | happy                    |

#### **Implementation Concept**

```python
tokens.map(token => replacement_map.get(token, default='other'))
```

#### **Input**

```text
["introduction", "full", "text", "search", "full", "text",
"search", "search", "documents", "efficiently"]
```

#### **Output**

```text
["introduce", "full", "text", "search", "full", "text",
"search", "search", "document", "efficient"]
```

✅ Words are now normalized and semantically aligned for indexing.

---

## **Summary of Pre-processing Pipeline**

| Step | Name             | Goal                  | Example Input → Output             |
| ---- | ---------------- | --------------------- | ---------------------------------- |
| 1    | Parsing          | Extract relevant text | `<h1>Intro</h1>` → `Intro`         |
| 2    | Tokenization     | Split into words      | `"Full Text"` → `["Full", "Text"]` |
| 3    | Normalization    | Lowercase & unify     | `"Search"` → `"search"`            |
| 4    | Stopword Removal | Remove noise          | `"the search"` → `"search"`        |
| 5    | Reduction        | Root word form        | `"documents"` → `"document"`       |

---

# **Indexing**

Once the **pre-processing pipeline** is complete, we can use the cleaned tokens to **build an Inverted Index**.

---

## **Building the Inverted Index**

Each **document** (e.g., job posting) is passed through the **pre-processing pipeline**, and then we **map tokens to the documents** in which they appear.

```js
documents
  .map(pre_process_pipeline)
  .forEach((doc_id, tokens) => {
    for (let token of tokens) {
      inverted_index[token].append(doc_id)
    }
  });
```

---

## **Structure of the Inverted Index**

| Token  | Documents (id, count)                                      |
| ------ | ---------------------------------------------------------- |
| apple  | (301, 5), (233, 1), (103, 2), (981, 7), (145, 6), (234, 7) |
| batman | (116, 2), (147, 6), (202, 5), (182, 3), (115, 1)           |
| design | (17, 9), (24, 5), (109, 7), (11, 2), (513, 4), (241, 3)    |
| zebra  | (119, 2), (33, 8), (313, 11), (187, 6)                     |

---

### **Notes**

* Each **token** maps to a **list of documents** where it appears.
* Each document entry stores:

  * **doc_id** → document identifier
  * **count** → number of times the token appears in that document
  * (Optionally) **positions** → exact locations of the word in the document

This data structure allows **fast retrieval** and **relevance scoring**.

---

## **Operations on the Inverted Index**

---

### **1. `insert(document)`**

#### Steps:

1. Pre-process the document using the existing pipeline → get tokens.
2. For each token:

   * Add `(document_id, count)` to the index.

```js
function insert(document) {
  const tokens = pre_process(document);
  for (let token of tokens) {
    inverted_index[token].append({ doc_id: document.id, count: tokenCount });
  }
}
```

✅ **Effect:** Adds new documents and updates their tokens in the index.

---

### **2. `delete(document_id)`**

#### Steps:

1. Find the document.
2. Pre-process it to get tokens.
3. For each token:

   * Remove `(document_id, count)` from the index.

```js
function delete(document_id) {
  const tokens = pre_process(documents[document_id]);
  for (let token of tokens) {
    inverted_index[token].remove(document_id);
  }
}
```

✅ **Effect:** Ensures index stays consistent when documents are deleted.

---

### **3. `update(document)`**

#### Steps:

1. Delete the old version of the document.
2. Insert the updated version.

```js
function update(document) {
  delete(document.id);
  insert(document);
}
```

✅ **Effect:** Keeps index fresh when documents change.

---

### **4. `find(token)`**

#### Steps:

1. Look up the token in the inverted index.
2. Return the list of matching documents.

```js
function find(token) {
  return inverted_index[token]; // returns [(doc_id, count), ...]
}
```

✅ **Effect:** Quickly retrieves all documents where a keyword appears.

---

## **Summary**

| Operation             | Description                    | Complexity (approx.)        |
| --------------------- | ------------------------------ | --------------------------- |
| `insert(document)`    | Adds tokens and doc references | O(M) — M = number of tokens |
| `delete(document_id)` | Removes doc references         | O(M)                        |
| `update(document)`    | Delete + Insert                | O(2M)                       |
| `find(token)`         | Lookup by keyword              | O(1) (hashmap lookup)       |

---

✅ **Result:**
We now have an efficient **Inverted Index**, enabling **fast text search** by token → document mapping.

---
Perfect ✅ — here’s your **complete and formatted** final version of the **Search (algorithm)** section, including everything you listed **plus a clean pseudocode block** at the end that fits seamlessly with the explanation.

---

## Search (algorithm)

1. We must first preprocess the search query using the same pipeline as the documents
   (to ensure the vocabulary matches).

   **Example:**
   **Input query:**
   `"Jobs for Python developer with 5 years experience"`
   **Output query:**
   `["job", "python", "develop", "experience"]`

2. Now, given the list of query tokens, we can find the set of all documents that contain at least one of the words.

---

### Q: Should we use "any word matches" or "all words match" or …?

We need something that **ranks** documents instead of simply **filtering** them.

We want to somehow figure out how **relevant** a document is for the given search query — because **semantics is nuanced!**

1. All relevant data should be searched
   → we should not only search through the title, but also the description.
2. Words can appear in any order
   → `"senior python developer"` ≡ `"python developer, senior"`.
3. Not all words need to match exactly
   → `"java or python developer"`.
4. Spelling errors should be handled
   → someone could misspell `"pythn"`.
5. Words have contextual meaning
   → `"need python developer"` ≠ `"cobra & python trainer"`.
6. Synonyms should be considered
   → `"lead python programmer"` ≈ `"senior python developer"`.

---

### TF-IDF Score (Term-Frequency, Inverse Document Frequency)

#### Intuition

1. If document **d₁** contains the word **w** more times than document **d₂**, then **d₁** should be ranked higher than **d₂** for a search query containing **w**.

   Example:

   ```
   search_query = "cat food"
   d1 = "I love cats, cats are the best. My cats Spooky & Smokey really love this brand of cat food!"
   d2 = "Dogs, cats, rabbits are various types of pets."
   ```

   → **d₁** is more relevant than **d₂**.

2. A rare word that appears in fewer documents overall is more meaningful than a common one.
   Example:

   * “pneumonoultramicroscopicsilicovolcanoconiosis” is more meaningful than “however”.
   * The word “the” appears in ~8% of all English text and carries almost no meaning.

---

#### Formula

```
score(doc, query) = Σ ( tf(word, doc) × idf(word) ), for each word in query
```


Where:

* **[tf] = term-frequency(word, doc) ** captures **relevance** – number of times the word appears in the document
* **[idf] document-frequency(word)** captures **popularity** – number of documents containing the word

Hence,
**TF-IDF = Term Frequency × Inverse Document Frequency**

**Example:**

```
search_query = "cat food"
d1 = "I love cats, cats are the best. My cats Spooky & Smokey really love this brand of cat food!"
d2 = "Dogs, cats, rabbits are various types of pets."

score(d1, “cat food”) = tf(cat, d1) * 1/df(cat) + tf(food, d1) * 1/df(food)
                     = 4 * 1/2 + 1 * 1/1
                     = 3
score(d2, “cat food”) = tf(cat, d2) * 1/df(cat) + tf(food, d2) * 1/df(food)
                     = 1 * 1/2 + 0 * 1/1
                     = 0.5
→ d₁ is more relevant than d₂
```

---

#### Final Search Algorithm

1. Preprocess the search query using the same pipeline as the documents
   (to ensure consistent vocabulary).
   **Example:**
   Input: `"jobs for python developer with 5 years experience"`
   Output: `["job", "python", "develop", "experience"]`

2. Find the set of all documents that contain **at least one** of the query tokens.

3. For each matching document, calculate the **TF-IDF score**.

4. Sort and return the **top K** documents based on the score.

---

### Pseudocode

```python
function search(query, inverted_index, total_docs, k):
    # Step 1: Preprocess the query
    tokens = pre_process_pipeline(query)

    # Step 2: Get candidate documents
    candidate_docs = set()
    for token in tokens:
        if token in inverted_index:
            for (doc_id, _) in inverted_index[token]:
                candidate_docs.add(doc_id)

    # Step 3: Calculate TF-IDF score for each candidate document
    scores = {}  # doc_id → score
    for doc_id in candidate_docs:
        total_score = 0
        for token in tokens:
            if token in inverted_index:
                postings = inverted_index[token]
                tf = get_count(doc_id, postings)        # term frequency in this doc
                df = len(postings)                      # number of docs containing token
                idf = 1 / log(df + 1)                   # inverse document frequency
                total_score += tf * idf
        scores[doc_id] = total_score

    # Step 4: Sort by relevance
    ranked_docs = sort_by_value_desc(scores)

    # Step 5: Return top K documents
    return ranked_docs[:k]


function get_count(doc_id, postings):
    for (id, count) in postings:
        if id == doc_id:
            return count
    return 0
```

---

✅ **Summary:**

* Preprocess query → get tokens
* Use inverted index → find candidate docs
* Compute TF-IDF score → rank docs
* Return top K most relevant documents

---

# Apache Lucene

[Official Website](https://lucene.apache.org/)

**Overview:**

* Open-source **Java library** for **indexing and search**.
* Provides advanced features like:

  * Spellchecking
  * Hit highlighting
  * Tokenization & analysis
* Runs on a **single server**.

**Key Functionality:**

* Takes a set of documents (e.g., JSON)
* Performs pre-processing (except parsing)
* Builds an **inverted index** for fast search

---

### ⚠️ Limitations of a Single Lucene Server

* Single point of failure
* Cannot store billions of documents
* Cannot handle **very high search load**

---

This naturally leads to **distributed search systems** like **Elasticsearch** or **Solr**, which use Lucene under the hood but scale horizontally across multiple servers.

---

# Sharding

Imagine each document is ~1KB in size, and each server has 1 TB of storage.

* Each server can store roughly **1 billion documents**.
* Suppose LinkedIn has **100 billion posts** to search through.

### Inverted Index Size Estimation

* Let’s assume there are **1 million unique words** across all documents (the dictionary).
* On average, each word appears in **1 million documents**.
* Each entry in the inverted index stores **2 integers** (8 bytes each).

```
Size = 2 integers × 8 bytes × 1 million entries per word × 1 million words
     = 16 million million bytes
     = 16 TB
```

✅ **Conclusion:** We need **sharding** to distribute the data across multiple servers.

---

## What's the Data?

1. **Documents**

```json
{
  "id": 101,
  "title": "Senior Python Developer needed in Bangalore",
  "description": "We seek a proactive Backend Developer cum Tester with 5-8 years of experience who owns quality and excels in collaboration. Required expertise includes Python, Django, microservices architecture, distributed systems, message buses, multi-threading, CI/CD (GitLab/Jenkins), automated testing, databases (PostgreSQL/MySQL), and cloud platforms (AWS/Azure/GCP).",
  "created_at": "7/3/2025"
}
```

2. **Inverted Index Example**

| Token  | Documents (id, count)                     |
| ------ | ----------------------------------------- |
| apple  | 301,5  233,1  103,2  981,7  145,6  234,7  |
| batman | 116,2  147,6  202,5  182,3  115,1         |
| design | 17,9   24,5   109,7  11,2   513,4   241,3 |
| ...    | ...                                       |
| zebra  | 119,2  33,8   313,11  187,6               |

---

## Ideal Sharding Key

1. **Documents**

* Each document is independent.
* **Ideal sharding key:** `document_id`.

2. **Inverted Index**

* Inverted Index acts like a hashmap: key → token, value → list of documents.
* **Ideal sharding key (naïve choice):** `token`.

---

### Sharding Inverted Index by Token (**Not a Good Idea**)

* Each token goes to a different shard.
* Problem: a single document contains **thousands of tokens**.

---

#### Insert / Update / Delete

Given a document (job posting):

1. Preprocess the document → get list of tokens: `["job", "python", "developer"]`
2. For each token, go to the **appropriate shard** and insert/update/delete.

**Problems:**

* Operations are **fan-out** → may hit hundreds of servers.
* Need **atomic updates** per document to avoid partial indexing.
* Atomic updates across hundreds of servers → **practically impossible** (some server will fail).

---

#### Search

1. Preprocess the query:

```
Input query: "jobs for python developer with 5 years experience"
Output query: ["job", "python", "develop", "experience"]
```

2. For each token, go to the appropriate shard.

**Issues:**

* Can shards calculate TF-IDF? ❌

  * No. Shards contain only tokens, not the complete set of documents.
* What can shards return?

  * Each shard returns the **list of documents** containing the token it holds.

3. Collect all returned data in the app server:

* Each shard may return **tens of thousands of documents**.
* Combined → millions of documents (GBs of data).
* **Feasibility:** ❌ Not practical to fetch and process this much data per query.

4. Calculate TF-IDF scores and sort → **too much network overhead**.

---

✅ **Conclusion:**
Sharding the inverted index by **token** does **not work**.

* Insert/update/delete become extremely complex.
* Search is inefficient and unfeasible due to massive fan-out and network load.

---

### Sharding Inverted Index by `document_id`

* Each document is assigned to a shard based on its `document_id`.
* Each shard builds an **independent inverted index** for its subset of documents.
* Effectively, **each shard is an Apache Lucene server** handling millions of documents.

**Notes:**

* With billions of documents, each shard receives millions.
* Each shard has a large variety of documents.
* Most tokens appear in multiple shards → **each shard’s inverted index contains almost all tokens**.

---

#### Insert / Update / Delete

1. Use `document_id` to select the **appropriate shard**.
2. Preprocess the document and update the index **within that shard**.

* ✅ No fan-out required (hit exactly **1 server**).

---

#### Search

1. Preprocess the query:

```
Input query: "jobs for python developer with 5 years experience"
Output query: ["job", "python", "develop", "experience"]
```

2. Query all shards:

* Every shard may have potential matches → **all shards must be checked**.
* Shards can calculate **TF-IDF scores locally** for documents they hold.
* Each shard returns its **top K matches** with scores.

3. App server merges the results:

* Merge all shard responses into **a single top K list**.
* Data per shard is small (top 10 → few KBs).
* ✅ Feasible to process and return results quickly.

---

**Key Points:**

* Search queries involve **fan-out**, but only for **reads**.
* Each shard handles **inserts/updates locally**.
* Highly efficient, low network overhead, scalable to billions of documents.

---

### Fan-out: When is it Bad and When is it Okay?

#### Why fan-out is generally considered bad:

1. **Increased Load**

   * Each query multiplies the load by the number of servers.
   * Example: 1000 servers → 1000× load.

2. **High Latency**

   * Must wait for all servers to respond.
   * Query completion is limited by the **slowest server**.

3. **Atomic Updates are Hard or Impossible**

   * Atomic update requires success on **all servers**.
   * With 1000 servers, at least one is likely to fail → rollback is required, practically impossible.

---

#### Why fan-out is okay for Search:

1. **Parallel Search is Needed**

   * Each query searches billions of documents.
   * Using the entire cluster in parallel (like Map-Reduce) is necessary.

2. **Subset of Shards is Enough**

   * Don’t need to query all shards every time.
   * Random subset search:

     * First search may miss some documents.
     * Subsequent searches can query different shards → more relevant results.

3. **Partial Results Are Acceptable**

   * Users care about **highly relevant results**, not exact ranking.
   * Some top results may be missed, but overall relevance remains high.

4. **Writes Are Local, Only Reads Fan-out**

   * Updates happen in a **single shard** → no atomicity issues.
   * Only read operations fan-out to multiple shards.

5. **Latency Can Be Controlled**

   * App server can set **timeouts** (e.g., 80ms for 100ms target).
   * Only shards responding within the timeout contribute to final results.

✅ **Key Takeaway:**

* Fan-out search is powerful for **low-latency, large-scale text search**.
* Returning **partial, highly relevant results** is acceptable and efficient.

---

# Elasticsearch

Elasticsearch is a **document database optimized for full-text search**.

* Uses **Apache Lucene** internally
* Combines multiple Lucene servers in a **cluster**
* Supports **Sharding & Replication**

---

## Terminology

1. **Document**

* Any JSON object you want to index.

```json
{
  "_id": 101,
  "_index": "job-postings",
  "title": "Senior Python ... Bangalore",
  "description": "We seek ... (AWS/Azure/GCP).",
  "created_at": "7/3/2025"
}
```

2. **Index**

* Logical namespace grouping documents.
* Each document belongs to **exactly one index**.
* Index has a **schema** defining which fields to index and how.
* Note: this is **not the inverted index**—just a logical grouping like `job-postings`, `people-search`, etc.

3. **Node**

* A single server in the Elasticsearch cluster.

---

## Sharding

* Number of shards must be specified at index creation (default: 5).
* Cannot be changed after creation.
* Documents are distributed using **bucket-based routing**:

```
shard_id = hash(doc_id) % number_of_shards
```

---

## Replication

* Each shard is replicated (master + replica).
* Default replication factor = 2 (1 master + 1 replica).
* Masters and replicas are distributed **across different nodes**.

---

## Query Flow

1. Any query can be sent to **any shard**.
2. The shard acts as a **coordinator**:

   * Forwards the query to other shards
   * Each shard calculates **top K results**
   * Coordinator collects and merges results → returns **final top K**

---

## Consistency vs Availability

* **Stale read:** recently updated documents might not appear immediately or may appear slightly lower in ranking.

* **Tradeoff:** Elasticsearch prioritizes **availability over strict consistency** for large-scale search.

  * Users want **relevant results**, not exact ordering.

* **Exception:** Systems like Slack need **immediate consistency**:

  * Messages must be searchable immediately.
  * Can handle small data per shard (per organization), so all updates fit in a single shard.

---

# Elasticsearch Resources

### Mandatory (SDE-2 or higher)

1. **Elasticsearch Tutorial | Getting Started Guide for Beginners** – Sematext
   [YouTube Link](https://www.youtube.com/watch?v=n9mE5MXGkaA&ab_channel=Sematext)

2. **Elasticsearch text analysis and full text search - a quick introduction** – George Bridgeman
   [YouTube Link](https://www.youtube.com/watch?v=ajNfOPeWiAY&ab_channel=GeorgeBridgeman)

3. **Elastic Search Playground** – Interactive search environment
   [Playground Link](https://xivapi.com/search/playground)

---

### Optional

1. **Tutorials**

   * *What is Elasticsearch: Tutorial for Beginners* – Logz.io
     [Link](https://logz.io/blog/elasticsearch-tutorial/)
   * *Mini Beginner's Crash Course to Elasticsearch and Kibana* – YouTube Playlist
     [Playlist Link](https://www.youtube.com/playlist?list=PL_mJOmq4zsHbcdoeAwNWuhEWwDARMMBta)

2. **Demystifying Elasticsearch shard allocation** – AWS Open Distro Blog
   [Link](https://aws.amazon.com/blogs/opensource/open-distro-elasticsearch-shard-allocation/)

---
