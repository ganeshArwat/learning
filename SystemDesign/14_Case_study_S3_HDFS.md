## **Large File Storage (LFS)**

Large File Storage refers to systems designed to store and manage **big files** efficiently, often ranging from several MBs to TBs or more. The key considerations for LFS include **scalability, durability, availability, and performance**.

### **Popular Large File Storage Solutions**

#### **1. Managed Cloud Services**

These are fully managed services provided by cloud providers. They are reliable, scalable, and integrate well with other cloud services.

| Service                           | Description                                                                                         |
| --------------------------------- | --------------------------------------------------------------------------------------------------- |
| **AWS S3**                        | Object storage service by Amazon. Highly durable, scalable, and integrates with other AWS services. |
| **Google Cloud Storage**          | Google’s object storage, offering global availability, versioning, and lifecycle management.        |
| **Azure DataLake / Blob Storage** | Azure Blob for general object storage; DataLake is optimized for analytics workloads.               |
| **Oracle Object Storage**         | Cloud storage solution by Oracle, offering secure, scalable object storage.                         |

#### **2. Distributed File Systems**

These are designed to handle **massive amounts of data across multiple machines**. They are often used for analytics or big data workloads.

* **Hadoop Distributed File System (HDFS)**

  * Stores large files across multiple nodes.
  * Provides **fault tolerance** by replicating data.
  * Optimized for **batch processing** rather than low-latency access.

#### **3. Version Control Systems**

Specialized solutions for source code with large assets:

* **Git Large File Storage (Git LFS)**

  * Extends Git to handle large files by storing them outside the repository.
  * Ideal for projects with **large binaries** (images, videos, datasets).

#### **4. Consumer/Personal Storage Services**

These are primarily designed for end-users rather than as backend systems.

* **Google Drive / Dropbox**

  * Can store large files and provide easy sharing.
  * Not optimized as a backend for apps or enterprise-grade storage.
  * Good for **personal or collaborative usage**, but not for high-performance backend systems.

---

**Key Takeaways:**

* **Managed cloud storage** is best for enterprise-grade, scalable, and secure solutions.
* **Distributed file systems** like HDFS are best for big data analytics.
* **Git LFS** is suited for versioning large files in software projects.
* **Consumer cloud services** are convenient but not reliable for backend systems.

---

## **Why Do We Need a New Database for Large Files?**

Most existing databases are **not optimized for storing large files**, due to how they structure and manage data:

### **Limitations of Existing Databases**

| Database Type            | Storage Mechanism      | Limitation for Large Files                                              |
| ------------------------ | ---------------------- | ----------------------------------------------------------------------- |
| **SQL**                  | Fixed-size rows        | Large files make row size huge → inefficient storage and retrieval      |
| **Key-Value / Document** | LSM trees (SSTables)   | Large files bloat SSTables → slower compaction, indexing, and retrieval |
| **Column-Family**        | LSM trees, column-wise | Same issue as above; not optimized for very large blobs                 |

### **Modern Databases: Limited Support**

Some databases provide **partial support** for large files, but with strict limits:

| Database       | Feature   | Limitation                                                                     |
| -------------- | --------- | ------------------------------------------------------------------------------ |
| **PostgreSQL** | `BLOB`    | Can store large binary objects, but performance degrades with very large files |
| **MongoDB**    | `GridFS`  | Max document size = 16MB; needs splitting files into chunks                    |
| **Redis**      | Key-Value | Max value ~500MB, but practical usage: keys ~200 bytes, values ~10KB           |

**Conclusion:**

> None of these databases are designed exclusively for large file storage. Using them for large files can result in poor performance, high latency, and operational complexity.

---

## **Use Cases of Large File Storage**

Large files appear in scenarios where data size grows rapidly or user uploads are heavy:

1. **Aggregated Logs**

   * Observability in large-scale systems.
   * Centralized log files can reach **100TB+**.
   * Example: system metrics, application logs, audit logs.

2. **User-Uploaded Multimedia**

   * Images, audio, video, and attachments (PDF, ZIP, etc.).
   * Popular in social media apps, file-sharing platforms, or e-learning portals.

3. **Frontend Code & Data**

   * Static assets like HTML, CSS, JS, and JSON.
   * Mostly served via **CDNs**, but CDNs need a **backend storage system** as the origin.

**Note:**
Even though files are served through **CDNs**, CDNs are just caches. The **real storage backend** is required to hold the original, persistent data.

---

## **Functional Requirements**

A large file storage system must satisfy the following functional needs:

1. **Store Very Large Files**

   * Support files up to **100TB** or more.
   * Requires **sharding**: splitting the file across multiple storage nodes for scalability.

2. **Durable Storage**

   * Files must remain **intact and available**, even in case of disk or node failures.
   * Requires **replication**: storing multiple copies of each file across different nodes.

3. **Upload & Download Large Files**

   * Support uploading/downloading in **chunks or streams** to handle massive files efficiently.
   * Allows resuming interrupted uploads/downloads.

4. **Analytics on Large Files**

   * Ability to perform **scans or aggregations** on large files.
   * Example: scanning log files to count the number of exceptions or extract metrics.

---

## **Non-Functional Requirements / Considerations**

* **Editing Existing Files**

  * Direct editing is **not supported**.
  * Rationale: modifying any arbitrary bytes in a 100TB file is inefficient and impractical.
  * Supported alternatives:

    * **Appending**: add data at the end of the file.
    * **Uploading a new version**: replace the entire file.

* **Read/Write Performance**

  * Not optimized for speed because:

    * Large file transfers are constrained by **network bandwidth** and storage hardware (HDD/SSD).
    * Large files are rarely accessed frequently.
  * Smaller files (images, videos, etc.):

    * Reads: served via **CDN**.
    * Writes: uploaded once, mostly static.

* **Search Capabilities**

  * Limited to **directory listing** (file names and paths).
  * Searching **within file contents** is not supported.
  * Large file storage is **data format agnostic**: treats files as **opaque binary blobs**.

---

### **Key Takeaways**

* The system is optimized for **storage, durability, and streaming access**.
* **Editing and content search** are intentionally excluded.
* Smaller, frequently accessed files are better served via **CDNs or specialized storage**.

---

## **Consistency vs Availability**

When designing large file storage, understanding **consistency requirements** is critical.

### **Data in Context**

* The data we care about are the **files being uploaded**.

### **Eventual Consistency (Stale Reads)**

* Definition: after writing, a read may temporarily return **older or missing data**.
* Example problems for large file storage:

  1. **New Uploads**: You just uploaded a file, but when trying to view it immediately, it’s not visible.

     * User/system may think the file is **lost**, leading to a poor experience.
     * **Solution**: “Read-your-write” consistency suffices for this scenario.
  2. **Updated Files**: Uploading a newer version of a file might temporarily show the **old version**.

     * User/system may think their changes were lost.
     * **Problem**: “Read-your-write” consistency is **not enough** if the intended readers are different users.

**Conclusion:**

> For large file storage, **immediate consistency is preferred**, especially for uploads and version updates.

---

### **Design Example: Dropbox**

* Dropbox stores large files and syncs them across devices.
* **Consistency Requirements**:

  1. **File uploads**:

     * Immediate consistency is required for the **device that uploaded the file**.
     * The uploader should always see the latest version.
  2. **Cross-device syncing**:

     * Can be **eventually consistent**.
     * Example: Device 2 may temporarily see a stale version of the file.
     * The system can asynchronously sync changes across devices.

| Operation                     | Consistency Requirement                                 |
| ----------------------------- | ------------------------------------------------------- |
| Upload from Device 1          | Immediate consistency for Device 1                      |
| Upload visibility on Device 2 | Eventual consistency allowed (can be temporarily stale) |
| File sync across devices      | Eventual consistency                                    |

---

**Key Takeaways:**

* **Immediate consistency** is crucial for **uploads and version updates** to avoid losing user trust.
* **Eventual consistency** is acceptable for **replication and multi-device syncing**.
* Properly identifying **who needs to see the latest version** determines the required consistency level.

---

## **Design Considerations for Large File Storage**

### **Can a Single Server Store a 100TB File?**

* **No**, even though modern servers have high capacity, storing everything on a single server is **impractical**:

  * Single Point of Failure (SPoF)
  * Bottleneck for read/write requests
  * Cannot read the entire file into RAM for processing
  * File corruption risks: if a single server fails, the **entire 100TB could be lost**

**Solution:**

* **Split the file into multiple smaller chunks**
* **Distribute chunks across multiple servers**
* Maintain **metadata** to track chunk locations and integrity.

---

### **Example File Sizes**

* **Large ML models**: ChatGPT 3.5 (1.7 trillion parameters) ≈ 13.6TB
* **Raw 8K video (60fps)**:

  * 1 second ≈ 6GB
  * 2 hours ≈ 43.2TB

This illustrates why **splitting and distributing large files** is essential.

---

### **Metadata Requirements**

To manage chunks efficiently, we need to store:

| Field    | Description                                       |
| -------- | ------------------------------------------------- |
| Filename | Name of the file                                  |
| Chunk ID | Sequence number of the chunk                      |
| Checksum | Integrity check for the chunk                     |
| Location | Physical server or path where the chunk is stored |

**Example:**

| Filename                   | Chunk ID | Checksum    | Location                   |
| -------------------------- | -------- | ----------- | -------------------------- |
| avatar_1080p_movie_eng.mp4 | 1        | a3b68a963b… | 10.11.0.1/avatar_chunk_1   |
| avatar_1080p_movie_eng.mp4 | 2        | b68a963baa… | 10.11.1.15/avatar_chunk_2  |
| avatar_1080p_movie_eng.mp4 | 3        | 8a96ad233b… | 10.11.8.101/avatar_chunk_3 |

---

### **Choosing Chunk Size**

**Trade-offs:**

1. **Very small chunks (e.g., 1KB)**

   * Number of chunks = 100TB / 1KB = 100 billion
   * Metadata overhead ≈ 20TB (200 bytes per chunk) → 20% overhead
   * Too much metadata → inefficient

2. **Very large chunks (e.g., 100GB)**

   * Fewer chunks → small metadata overhead
   * Problem: cannot load large chunks into RAM for upload/download or processing

3. **Sweet Spot**

   * Chunk size should **not be too small** → avoid metadata bloat
   * Chunk size should **fit in RAM** → easy streaming and processing

**Benchmarking Required:**

* Depends on:

  * Storage hardware (HDD, SSD)
  * Load patterns and type of data
  * Client requests
* Example from HDFS:

  * HDFS 1.0: 64MB chunks
  * HDFS 2.0: 128MB chunks

**Example Calculation for 128MB Chunks:**

* Number of chunks = 100TB / 128MB ≈ **1 million chunks**
* Metadata size = 1 million * 200 bytes ≈ **200MB**
* Metadata overhead ≈ **0.05%** → very reasonable

**Notes:**

* Most large file storage systems allow clients to configure chunk size.
* Configuration is rarely changed in practice unless **performance benchmarking** suggests otherwise.

---

**Key Takeaways**

1. **Never store huge files on a single server**; always use **chunking and distribution**.
2. **Metadata is crucial** for locating and validating chunks.
3. **Chunk size selection** is a balance between:

   * Metadata overhead
   * RAM/storage constraints
   * Performance
4. Systems like **HDFS** already optimize chunk sizes based on extensive production experience.

---

## **Hadoop Distributed File System (HDFS)**

HDFS is designed to store **very large files** across multiple servers while providing **durability, fault tolerance, and scalability**.

---

### **NameNodes**

* **Role:** Special servers that **store metadata** about files and chunks.
* **Responsibilities:**

  1. Track **which chunks belong to which file**
  2. Track **locations of all chunk replicas**
  3. Ensure **replication policies** are followed
  4. Provide **strong consistency** for metadata operations

**Example Metadata Table:**

| Filename                   | Chunk ID | Replica Locations                                                               |
| -------------------------- | -------- | ------------------------------------------------------------------------------- |
| avatar_1080p_movie_eng.mp4 | 1        | 10.11.0.1/avatar_chunk_1, 10.12.1.2/avatar_chunk_1, 10.13.0.15/avatar_chunk_1   |
| avatar_1080p_movie_eng.mp4 | 2        | 10.11.1.15/avatar_chunk_2, 10.10.0.7/avatar_chunk_2, 10.8.12.115/avatar_chunk_2 |
| avatar_1080p_movie_eng.mp4 | 3        | 10.11.8.101/avatar_chunk_3 …                                                    |

---

### **Do We Need to Shard Metadata?**

* **No.**

  * Metadata size is **tiny compared to the actual file size** (~0.05% overhead).
  * Example:

    * 100TB file → ~200MB metadata
    * 500PB of data → ~1TB metadata
  * Easily fits on a **single server HDD**.

---

### **Do We Need to Replicate Metadata?**

* **Yes.** Metadata is **critical**:

  * Losing metadata can make files inaccessible even if chunks are intact.
  * Must support **high availability** and **read scalability**.
* **Solution:**

  * **Replicate NameNodes** in a **master-slave (or quorum) architecture**.
  * Multiple read replicas handle **metadata queries**.
  * Maintain **strong consistency** for metadata updates.

---

### **Key Takeaways**

1. **HDFS Metadata = Heart of the System**

   * Tracks chunks, replicas, and file-to-chunk mapping.
2. **Sharding Metadata is unnecessary**

   * Even for **exabyte-scale** storage, a single NameNode can hold metadata.
3. **Replication of Metadata is critical**

   * Ensures **durability**, **availability**, and **query scalability**.
4. **Strong consistency required** for metadata

   * Unlike file chunks, metadata updates cannot tolerate stale reads.

---

## **DataNodes**

* **Role:** Store the actual chunks of data.
* **Characteristics:**

  * “Dumb” machines — only store data; no complex logic.
  * Chunks are **immutable** — once created, they cannot be edited.

---

## **Replication**

* Every chunk is **replicated across multiple DataNodes**.
* **Distribution** is managed by the **NameNodes**.

### **Two Types of Data in HDFS**

1. **Chunks (actual data)**

   * **Immutable:** never modified once written.
   * Operations:

     * **New version of file:** creates new chunks; metadata updated; old chunks garbage collected.
     * **Appending:** new chunks are created for the appended data.
     * **Editing:** not allowed.
   * **Consistency:** automatic, no need for special consistency mechanisms since chunks cannot be changed.

2. **Metadata**

   * **Mutable:** tracks chunk locations and file structure.
   * **Consistency:** requires **immediate consistency**.
   * **Handling network partitions:**

     * During large partitions, if a majority of NameNodes is unreachable, **writes are blocked** until the quorum is restored.
     * **Reads** can still continue for available metadata.

---

## **Rack-Aware Algorithms**

### **Problem**

* Data centers are organized into **racks**.
* Servers within a rack share:

  * Router
  * Power supply
* If the rack’s router/power supply fails → **all servers in the rack go down**.
* If all replicas of a chunk are in the same rack → **chunk becomes unavailable**.

### **Solution**

1. Each server stores:

   * **Data center ID**
   * **Rack ID**
2. NameNodes enforce **rack-aware placement**:

   * At least **1 replica of a chunk in a different rack**.
   * At least **1 replica in a different availability zone** for high availability.

### **Benefits**

* Protects against **rack-level failures**.
* Ensures **high durability and availability** for all chunks.

---

### **Key Takeaways**

* **Chunks**: immutable → automatically consistent.
* **Metadata**: mutable → strong consistency required.
* **Rack-aware replication**: prevents data loss due to **rack or availability zone failures**.

---

## **File Upload Process**

### **1. Upload from User to Backend Server**

* **Chunked upload (UX purpose only):**

  * Show **upload progress** to the user.
  * Allow **resume** if upload gets interrupted.
  * This **chunking is independent** of HDFS/S3 chunking.
* The uploaded file is first stored on the **backend server’s local HDD**.

---

### **2. Backend Server → HDFS/S3**

* Backend server uploads a **continuous data stream** to HDFS/S3.
* **Internal chunking** happens at HDFS/S3:

  * HDFS divides the stream into **fixed-size chunks** (e.g., 128MB).
  * Metadata is updated via **NameNodes** to track chunk locations.

#### **Upload Algorithm (Python-like Pseudocode)**

```python
CHUNK_SIZE = 128 * (1 << 20)  # 128 MB

def handle_upload():
    buffer = bytearray(CHUNK_SIZE)
    index = 0
    while byte := get_data_from_network_stream():
        buffer[index] = byte
        index += 1
        if index == CHUNK_SIZE:
            dump_buffer(buffer)  # upload in separate thread
            index = 0
    if index > 0:
        dump_buffer(buffer)  # last chunk may be smaller

def dump_buffer(buffer):
    # 1. Ask NameNodes for chunk storage location
    # 2. Upload the chunk to the designated DataNodes
```

**Key Points:**

* From the **user or backend perspective**, the file appears as a single continuous stream.
* **Chunking is handled internally**; the user is unaware of it.
* Each time a buffer is full, the backend asks the **NameNodes** where to store the next chunk.

---

### **Failure Scenarios**

1. **Network or HDFS App Server Failure**

   * File upload fails.
   * NameNode **rolls back metadata**.
   * Backend retries upload from the beginning.

2. **DataNode Upload Failure for a Chunk**

   * Retry upload multiple times.
   * If persistent failure:

     * NameNode may assign a **different DataNode** for the replica.
     * Or return an error to the backend, which can **rollback and retry** the upload.

3. **File Size Not Divisible by Chunk Size**

   * Example: Chunk = 128MB, File = 200MB → 2 chunks:

     * 128MB chunk
     * 72MB chunk
   * The **last chunk can be smaller** than the standard chunk size.

---

### **Key Takeaways**

* **User upload chunking** = UX/resumable uploads.
* **HDFS/S3 chunking** = internal for storage, replication, and durability.
* **Last chunk size** doesn’t need to match standard chunk size.
* **Failure handling** relies on retrying, NameNode coordination, and metadata rollback.

---

## **File Download Process**

### **1. Request Handling**

* The download request is sent to the **app server** inside HDFS.
* The server queries the **NameNodes** to get metadata:

  * Number of chunks
  * Chunk IDs
  * Replica locations for each chunk

---

### **2. Chunk-by-Chunk Download**

* **Parallel streaming**:

  1. Start downloading the **first chunk** from any available replica.
  2. If a replica is down, fetch from another replica.
  3. Store chunk in an **in-memory buffer**.
  4. Start streaming the buffered data to the client.
  5. In parallel, begin downloading the **next chunk**.

---

### **Download Algorithm (Pseudocode)**

```python
CHUNK_SIZE = 128 * (1 << 20)  # 128 MB

def download(filename):
    chunk_metadata = get_metadata_from_namenodes(filename)
    for chunk in chunk_metadata:
        buffer = download_chunk(chunk)
        stream_buffer(buffer)  # stream to client

def download_chunk(chunk):
    while True:
        try:
            read the chunk from a random replica
            return buffer  # success
        except:
            continue  # try next replica
```

---

### **Key Points**

* **Chunked streaming**: the entire file is **not loaded into app server memory**.
* **Replica-aware reading**: ensures reliability and distributes load.
* **Parallel processing**: while one chunk is being streamed to the client, the next chunk is already being downloaded.

---

## **Large File Storage & Distributed Systems Resources**

### **1. AWS S3**

* **Official Documentation:** Comprehensive guide to Amazon S3, covering storage classes, data management, security, and more.
* **Link:** [AWS S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

---

### **2. HBase Internals**

* **Video:** Deep dive into HBase architecture, internals, and operations from SREcon19 Asia/Pacific.

  * Focuses on design, storage, and large-scale data management.
  * **Link:** [HBase Internals and Operations (YouTube)](https://www.youtube.com/watch?v=N0h8DISLawI)

* **Slides:** Detailed slides covering HBase internals and best practices.

  * **Link:** [HBase SREcon19 Slides (PDF)](https://www.usenix.org/sites/default/files/conference/protected-files/srecon19apac_slides_nair.pdf)

---

## **BitTorrent Overview**

**BitTorrent** is a **peer-to-peer (P2P) file sharing protocol** designed for efficient distribution of large files across many users without overloading a single server.

---

### **Key Concepts**

1. **Peers**

   * Users participating in the file sharing network.
   * Can be:

     * **Seeders**: peers who have the complete file and upload it to others.
     * **Leechers**: peers who are still downloading the file; they also upload chunks they have to other peers.

2. **Chunks / Pieces**

   * Files are **split into small fixed-size chunks**.
   * Chunks are downloaded **in any order** from multiple peers simultaneously.
   * Each chunk has a **hash** to verify integrity.

3. **Tracker**

   * A server that **coordinates peers** by keeping track of who has which chunks.
   * Does **not store the file itself**.
   * Modern implementations may use **trackerless protocols** (DHT – Distributed Hash Table).

4. **Swarming**

   * Peers download chunks from multiple sources **in parallel**, maximizing network bandwidth and reducing download time.
   * Once a peer completes a chunk, it can immediately **upload it to others**.

---

### **Advantages**

* **Highly scalable**: As more users download, more bandwidth becomes available.
* **Efficient distribution**: No single server is overwhelmed.
* **Fault tolerant**: If one peer goes offline, chunks can be retrieved from others.

---

### **BitTorrent vs Traditional Large File Storage**

| Feature             | BitTorrent                     | HDFS / S3 / Cloud Storage                   |
| ------------------- | ------------------------------ | ------------------------------------------- |
| Storage             | Distributed across peers       | Centralized servers / clusters              |
| Availability        | Dependent on active peers      | Guaranteed via replication                  |
| Chunking            | Built-in, variable-size chunks | Fixed-size, managed by system               |
| Performance Scaling | Better with more peers         | Scaling requires more servers               |
| Use case            | File sharing, P2P distribution | Backend storage, analytics, enterprise apps |

---

**Key Takeaways**

* BitTorrent is **designed for P2P file distribution**, not as a persistent backend storage solution.
* Uses **chunking, hashing, and swarming** to efficiently distribute very large files.
* Many principles (chunking, replication, streaming) **overlap with distributed storage systems** like HDFS or S3.

---
