## HTTP Protocol

- HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the web. It defines how clients (browsers) and servers communicate.

## Key Concepts of HTTP

### 1. Client-Server Model:

- The client (browser) sends a request.
- The server processes the request and sends a response.

### 2. HTTP Request Methods:

- GET → Retrieve data (e.g., load a webpage).
- POST → Submit data (e.g., form submission).
- PUT → Update existing data.
- DELETE → Remove data.
- PATCH → Partially update a resource.

### 3. HTTP Status Codes:

- HTTP status codes are three-digit responses from a web server that indicate the result of a client's request. They are grouped into five categories:

#### 1xx: Informational

- Indicates that the request is received and processing is continuing.

  - 100 Continue – The server received the request headers and expects the client to send the body.
  - 101 Switching Protocols – The server is switching to a different protocol as requested by the client.

#### 2xx: Success

- Indicates that the request was successfully received, understood, and processed.

  - 200 OK – The request was successful.
  - 201 Created – A new resource was successfully created.
  - 202 Accepted – The request is accepted for processing but not yet completed.
  - 204 No Content – The request was successful, but there's no response body.

#### 3xx: Redirection

- Indicates that the client must take additional action to complete the request.

  - 301 Moved Permanently – The resource is permanently moved to a new URL.
  - 302 Found (Moved Temporarily) – The resource is temporarily moved to a new URL.
  - 304 Not Modified – The client’s cached version of the resource is still valid.

#### 4xx: Client Errors

- Indicates that the request was incorrect or cannot be fulfilled by the server.

  - 400 Bad Request – The server cannot understand the request due to malformed syntax.
  - 401 Unauthorized – Authentication is required.
  - 403 Forbidden – The server understands the request but refuses to authorize it.
  - 404 Not Found – The requested resource does not exist.
  - 405 Method Not Allowed – The request method (GET, POST, etc.) is not supported for the resource.
  - 429 Too Many Requests – The client has sent too many requests in a short time.

#### 5xx: Server Errors

- Indicates that the server failed to fulfill a valid request.

  - 500 Internal Server Error – A generic server error occurred.
  - 502 Bad Gateway – The server received an invalid response from an upstream server.
  - 503 Service Unavailable – The server is temporarily unavailable.
  - 504 Gateway Timeout – The server did not receive a response from an upstream server in time.

### 4. Headers in HTTP:

- HTTP headers are key-value pairs sent in requests and responses to provide additional information about the communication between the client (browser) and server. Headers help in authentication, caching, content negotiation, security, and more.

#### **Types of Headers:**

#### 1. Request Headers (Sent by the client to the server)

- These headers provide information about the request, the client, and the content being sent.

- Host

  - Specifies the domain name of the server being requested.
  - Host: example.com

- User-Agent

  - Identifies the client (browser, OS, or bot).
  - User-Agent: Mozilla/5.0

- Accept

  - Specifies the content types the client can handle.
  - Accept: text/html, application/json

- Authorization

  - Provides authentication credentials (Bearer tokens, Basic Auth, etc.).
  - Authorization: Bearer {token}

- Content-Type

  - Specifies the type of data in the request body.
  - Content-Type: application/json

- Referer

  - Indicates the URL of the previous page.
  - Referer: https://google.com

- Cookie

  - Sends stored cookies to the server.
  - Cookie: sessionId=xyz123

#### 2. Response Headers (Sent by the server to the client)

- These headers provide metadata about the response, security policies, and server details.

- Content-Type

  - Defines the MIME type of the response.
  - Content-Type: text/html; charset=UTF-8

- Cache-Control

  - Controls caching behavior.
  - Cache-Control: no-cache, no-store, must-revalidate

- Set-Cookie

  - Sends cookies to store in the client’s browser.
  - Set-Cookie: sessionId=abc123; HttpOnly

- Server

  - Specifies the web server software.
  - Server: Apache/2.4.41

- Content-Length

  - Specifies the size of the response body in bytes.
  - Content-Length: 1024

- Location
  - Redirects the client to a new URL.
  - Location: https://new-url.com

#### 3. Security Headers (Enhance security by preventing attacks)

- These headers help protect web applications from attacks like XSS, clickjacking, and CSRF.

- Strict-Transport-Security (HSTS)
  - Forces HTTPS connections.
  - Strict-Transport-Security: max-age=31536000; includeSubDomains
- X-Frame-Options
  - Prevents clickjacking attacks.
  - X-Frame-Options: DENY
- X-Content-Type-Options
  - Prevents MIME type sniffing.
  - X-Content-Type-Options: nosniff
- Content-Security-Policy (CSP)
  - Prevents XSS attacks.
  - Content-Security-Policy: default-src 'self'

#### 4. Caching Headers (Improve performance by controlling how resources are cached)

- ETag
  - Unique identifier for cached resources.
  - ETag: "abc123"
- Last-Modified
  - Timestamp of last modification.
  - Last-Modified: Tue, 20 Mar 2023 12:00:00 GMT
- Cache-Control
  - Defines caching rules.
  - Cache-Control: max-age=3600, must-revalidate
- Expires
  - Specifies when the resource expires.
  - Expires: Wed, 21 Oct 2025 07:28:00 GMT

#### 5. CORS Headers (Cross-Origin Resource Sharing)

- Used to control access between different origins (domains).

- Access-Control-Allow-Origin
  - Specifies which origins can access resources.
  - Access-Control-Allow-Origin: \*
- Access-Control-Allow-Methods
  - Defines allowed HTTP methods.
  - Access-Control-Allow-Methods: GET, POST
- Access-Control-Allow-Headers
  - Specifies allowed request headers.
  - Access-Control-Allow-Headers: Content-Type, Authorization

### 5. Stateless Nature:

#### The Stateless Nature of HTTP

- HTTP (HyperText Transfer Protocol) is inherently stateless, meaning that each request from a client (browser) to a server is independent and does not retain any memory of previous interactions. This design allows for scalability and simplicity, but it also introduces challenges when maintaining user sessions.

#### Why is HTTP Stateless?

1. Request-Response Independence – Each HTTP request is processed in isolation, meaning the server does not track past interactions.
2. No Built-in Session Management – Unlike stateful protocols (e.g., FTP), HTTP does not store client information between requests.
3. Scalability – Statelessness enables high concurrency since the server does not have to allocate resources for tracking user states.

#### Implications of Statelessness

- Efficiency: Servers can handle numerous requests simultaneously without maintaining user-specific states.
- Redundancy & Load Balancing: Requests can be distributed across multiple servers because no single server is responsible for maintaining session data.
- Security Considerations: Since HTTP does not inherently remember users, session hijacking risks arise if authentication mechanisms are weak.

#### How Do We Handle Statelessness?

- To overcome the limitations of statelessness, developers use mechanisms such as:

1. Cookies – Small pieces of data stored on the client’s browser to track sessions.
2. Session Tokens (JWT, OAuth) – Securely signed tokens that allow authentication without maintaining server-side session states.
3. Database Session Storage – Storing user sessions in databases or distributed caches (e.g., Redis, Memcached) for efficient retrieval.
4. URL Parameters & Hidden Fields – Passing session-related data in query strings or hidden form inputs.

### 6. HTTP vs. HTTPS:

- HTTP is unencrypted, whereas HTTPS uses SSL/TLS for security.

### Http 1 and Http 2

## Rendering Patterns

---

## Network Optimization

- To speed up website loading and improve performance, we can optimize network usage.

### 1. Reduce HTTP Requests

- Minimize external resources (CSS, JS, images).
- Use CSS sprites to combine multiple images.
- Combine and minify CSS and JavaScript files.

### 2. Use Caching

- Browser caching stores static files (CSS, JS, images) to reduce requests.
- Server-side caching (Redis, Memcached) speeds up responses.

### 3. Enable Compression

- Gzip/Brotli Compression reduces response size.
- Minify CSS, JavaScript, and HTML files.

### 4. Use a CDN (Content Delivery Network)

- Distributes content across multiple servers globally.
- Reduces latency and speeds up load time.

### 5. Optimize Images

- Use modern formats like WebP.
- Implement lazy loading to load images only when needed.

### 6. Reduce DNS Lookups

- Minimize the number of unique domains in your web requests.

### 7. Keep-Alive & HTTP/2

- Keep-Alive: Reuses the same TCP connection for multiple requests.
- HTTP/2: Multiplexes requests, reducing latency.

### 8. Optimize Database Queries

- Use indexing to speed up searches.
- Implement query caching to reduce database load.
