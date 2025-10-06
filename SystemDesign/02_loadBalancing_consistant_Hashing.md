# Load Balancing

## Purpose
- with question that Which server should a particular request be sent to? 
To understand this, we first must understand how the data is distributed across the various 
servers. 
Because otherwise, we will end up sending the requests to servers which don't contain the 
appropriate data (Sanjana's request get sent to a server that contains Ashok's data) 

## Data Sharding
### Vertical Partitioning (Normalization)
### Horizontal Partitioning 
### Vertical Partitioning (across servers)
### Horizontal Partitioning (across servers)

## Sharding
### Sharding Key
### Sharding and Rounting
- It should not be the case that sharding follows logic A, but routing follows logic B. Why? 

## Routing Algorithm
### Characteristics of good Routing Algo
    - Fast
    - Equal distribution
    - We Should be able to freely add/remove servers
    - Minimal data Movement
    - Routing Should be derrministic without exchanging information


## Round Robin
### Example
### Initial Distribution
### Adding and Removing Servers
### Pros
### Cons
### When can we use Round Robin

## Bucketting
### Example
### Initial Distribution
### Adding and Removing Servers
### Pros
### Cons
### When can we use Bucketting

## Mapping Table
### Example
### Initial Distribution
### Adding and Removing Servers
### Pros
### Cons
### When can we use Mapping Table

## Consistant Hashing
### Hash Function
#### Good Hash Function
### Hash Ring
### Consistent Hasing Algo
### Example
### Initial Distribution
### Adding and Removing Servers
### Pros
### Cons
### When can we use Consistant Hashing

## Stateless Servers