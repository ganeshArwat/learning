----------------------------------------------------------------------------------------------------------------------------------------
14 Patterns to Ace Any Coding Interview Question
    https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed
Coding interviews: Everything you need to prepare
    https://www.techinterviewhandbook.org/coding-interview-prep/
## Introduction to DSA ##

	1. Introduction to Problem Solving
        #What is factor
            if a number is a factor of n, then n % a == 0
        #Count factors of a NO. 
        #Problems related to factor
        for (int i = 2; i * i <= A; ++i) {}
        N = a*b  a<=b
        b= N/a
        #For most numbers, factors come in pairs. For example, for 12:
                Factors: 1, 2, 3, 4, 6, 12.
                Factor pairs: (1, 12), (2, 6), (3, 4). The number of factors is 6, which is even.
            However, if a number is a perfect square, one of its factors will not have a pair. For example, for 36:
                Factors: 1, 2, 3, 4, 6, 9, 12, 18, 36.
                Here, 6 is a factor that pairs with itself, so there are 9 factors in total, which is odd.
        #RANGE
            [L R] = R-L+1
            (L R) = R-L-1
        #sum of natural no
            N*(N+1)/2
        #geometric series
            a(r^n -1)/(r-1)

        Execution Time is not the right parameter To check Performance of algorithms
        Use (NO. of iterations) to Compare Algorithms
        
	2. Time Complexity
        #Logarithms
            LOG b a = C || => b^c = a 
        #how to find intterations
        #comare two algorithms for large inputs
        #Asymptotic Analysis (big O)
        #step to calculate big O
            1. Find NO of iterations
            2. Ignore Lower Order Terms
            3. Ignore Constant Coefficient
        #Time Complexity
            [log(N)] < [Root(N)] < [N] < [N * log(N)] < [N^2] < [N^3] < [2^N] < [N!] < [N^N]   
        #TLE AND Constraints  
            In **Data Structures and Algorithms (DSA)**, **constraints** provide critical guidance for determining the most efficient algorithm to solve a problem without exceeding the time limits, which can lead to a **Time Limit Exceeded (TLE)** error.
            ### How Constraints Help:
            1. **Understanding Input Size**: 
            - Constraints give you an idea of the maximum input size, which helps in estimating the required **time complexity**.
            - For example, if a constraint specifies that an array can have up to **10⁶ elements**, a **brute-force** approach with O(n²) complexity will be inefficient because it would require around 10¹² operations, which is far too many for most competitive programming environments (where typically up to 10⁸ operations can be handled in 1 second).

            2. **Choosing the Right Algorithm**:
            - If the constraints allow **small input sizes** (e.g., n ≤ 100), you can often use **brute-force** or **recursive** algorithms with higher time complexity like O(n³) or O(2ⁿ).
            - If the constraints are **large** (e.g., n ≤ 10⁵ or n ≤ 10⁶), you need an algorithm with a more efficient time complexity, such as O(n log n) or O(n).

            3. **Guiding Optimization**:
            - Constraints allow you to optimize your approach accordingly. For example:
                - If the constraint is n ≤ 10⁶, you know you need at most **O(n log n)** complexity (e.g., sorting algorithms or divide and conquer approaches).
                - If n ≤ 10⁴, O(n²) solutions may still be feasible, such as dynamic programming with nested loops.

            ### Example:
            If you're solving a problem with n ≤ 10⁵, and you try a brute-force solution with O(n²) time complexity:
            - The number of operations will be around 10¹⁰, which can lead to a TLE in most online judges, as this exceeds the typical limit of 10⁸ operations per second.
            - A more efficient algorithm with O(n log n) complexity, such as **merge sort** or **binary search**, will handle this input size within the time limit.

            ### General Rule of Thumb:
            - O(n²) works for n ≤ 10³.
            - O(n log n) works for n ≤ 10⁵ to 10⁶.
            - O(n) works for n ≤ 10⁷ to 10⁸.

    3. Memory Management
        # Introduction to Stacks Memory
            LIFO (Last In First Out)
        # Introduction To Functin Call Stack
        Types of Memory
            Stack Memory
            Heap Memory
        Heap Memory
######################
## UNIT 1 ##
###################### 
## Arrays ##
	1. Introduction to Arrays
        # what is Arrays
        # how to Traversal the array
        # how to access the element of array
        # how to calcualte the MIN and MAX of array
        # Reverse the given integer array
            while(i<j){}
            swap the first and last element till middle
                1. swap method 
                2. addition method
        # Reverse the given array in range
            define first and last according to range 
            swap the first and last element till middle
                while(i<j){}
                define i and j as per the range L and R
        # Rotate k times the given array
            Reverse(0, N-1);
            Reverse(0, k-1);
            Reverse(k, N-1);
        # dynamic array
            size not fixed
            size can be changed
        # QUESTIONS
            Q1. Good Pair
            Q2. Reverse in a range
            Q3. Array Rotation
            Q4. Max Min of an Array
            Q1. Linear Search - Multiple Occurences
            Q2. Time to equality
            Q3. Count of elements
            Q4. Second Largest
    2. Arrays - Prefix Sum
        # what is Prefix sum
            A Prefix Sum (also known as Cumulative Sum) is an array where each element at index i represents the sum of all elements from the beginning of the original array up to index i. It is primarily used to perform range sum queries efficiently.
        # how to calculate Prefix sum of array
            P[0] = A[0]
            P[i] = P[i-1] + A[i];
            A[i] = P[i] - P[i-1]
        # how to find sum of range L to R using prefix sum
            if(L == 0) P[R]
            else P[R] - P[L-1]
        # even element Prefix sum
            if(i%2 == 0) P[i] = P[i-1] + A[i]
            else P[i] = P[i-1]
        # odd element prefix sum
            if(i%2 == 1) P[i] = P[i-1] + A[i]
            else P[i] = P[i-1]
        # Special Index
            A = [3 2 7 6 -2]
            even_P = [3 3 10 10 8]
            odd_P = [3 5 5 11 11]

            A = [2 7 6 -2]
            even_P = [2 2 8 8]
            odd_P = [2 9 9 7]

            if i == 0
                even_sum = odd_P[N-1] - odd_P[i]
                odd_sum = even_P[N-1] - even_P[i]
            else 
                even_sum = even_P[i-1] + ( odd_P[N-1] - odd_P[i] )
                odd_sum = odd_P[i-1] + ( even_P[N-1] - even_P[i] )
            if(even_sum == odd_sum) 
                return i

        # QUESTIONS
            Q1. Range Sum Query
            Q2. Special Index
                after removeing the element even_sum == odd_sum
            Q3. In-place Prefix Sum
            Q1. Equilibrium index of an array
                left sum ==  right sum
            Q2. In-place Prefix Sum
    3. Carry Forward & Subarrays
        # Count 'a-g' Pairs 
        # what is carry forward
            calculate and use
            Carry Forward is a general programming concept where a value or state is carried over from one step or iteration to the next. It is not limited to summation but can involve maintaining any form of state or information as you traverse through data structures.
                int cnt =0;
                int ans =0;
                for(int i=(A.size()-1); i>=0; i--){
                    if(A[i] == 'G')  cnt++;
                    if(A[i] == 'A') ans += cnt ;
                }
        # what is Subarrays
            Continuous Part of Sub array
        # representation of Subarrays
            L - R   => start and end
        # total no of Subarrays
            N*(N+1)/2
        # how to print Subarray
        # how to print all Subarrays
        # smallest subarray which contains the min and MAX
            1. calcualte MIN and Max of Array
            2. take two varibles as l_min and l_max
            3. if we found min then
                update the l_min
                calculate length as (i - l_max+1)   # [l_max, i]
                take a min of ans and length
            4. if we found Max then
                update the l_max
                calculate length as (i - l_min+1)  # [l_min, i]
                take a min of ans and length
        ## Sub Array ## 
            ## 1. Basic Subarray Understanding
                - **Definition**: A subarray is a contiguous segment of an array.
                - **Size**: Subarrays can range from a single element to the entire array.
                - **Number of Subarrays**: For an array of length `n`, there are `n(n + 1) / 2` possible subarrays.

            ## 2. Types of Subarray Problems
            - **Sum-related**:
                - Maximum subarray sum (Kadane's Algorithm)
                - Subarray sum equals `k`
            - **Product-related**:
                - Maximum/minimum product subarray
            - **Count subarrays with certain properties**:
                - Subarray with all elements less than a value
                - Subarray with at most `k` distinct elements

            ## 3. Common Subarray Algorithms
            - **Kadane's Algorithm**: 
                - Used to find the maximum sum subarray in `O(n)` time.
                - It works by carrying forward the maximum sum and updating it for each element.

            - **Sliding Window Technique**: 
                - Useful for fixed-length subarray problems or finding subarrays that meet certain criteria (like maximum or minimum length).

            - **Two-pointer Technique**: 
                - Helps in solving problems involving ranges or conditions like "at most `k` distinct elements" or "sum/product of subarray <= threshold".

            - **Prefix Sum/Cumulative Sum**: 
                - For problems where you need to calculate sums over ranges. You can compute cumulative sums in `O(n)` and use them to efficiently find the sum of any subarray.

            - **Divide and Conquer**: 
                - An extension of the maximum subarray sum problem, which splits the array into two halves and recursively solves the problem.

            ## 5. Handling Different Constraints
            - **Positive vs Negative Numbers**: Understand how algorithms like Kadane's deal with negative numbers.
            - **Fixed-Length vs Variable-Length Subarrays**: Focus on finding subarrays of a specific length or any length that meets a condition.
            - **Modulo Operations**: Often, subarray sums or products are required modulo a certain number.

            ## 6. Data Structures
            - **Hash Maps / Hash Sets**: Often used in problems involving counting subarrays with a specific sum or length.
            - **Deque**: Can be used in sliding window problems to maintain a range of values or indices.

            ## 7. Common Subarray Problems
            - **Maximum Sum Subarray**: Kadane's Algorithm
            - **Subarray with Sum `k`**: Sliding window or hash map
            - **Maximum Product Subarray**: Dynamic programming
            - **Find Subarray of Given Length with Max Sum**: Sliding window
            - **Subarray with Equal 0s and 1s**: Prefix sum and hash map
            - **Subarray with Distinct Elements**: Two-pointer/sliding window

        # QUESTIONS
            Q1. Closest MinMax
            Q2. Subarray in given range
            Q3. Generate all subarrays
            Q4. Special Subsequences "AG"
            Q1. Pick from both sides!
                # 1. take sume of first B elements
                # 2. set as a max sum
                # 3. take window of size B add from N-i and remove B-i index elements
            Q2. Leaders in an array
                # Algo 1
                    1. add last element in leader
                    2. take last element as a max and compare with other elements 
                    3. travers from Right to left and comapare and keep updating max
                # Algo 2
                    1. Create a Sufix array of Grater elements
                    2. Traver Left to Right and check current element is greater than with the suffix array if yes than add in Leaders
            Q3. Count Subarrays with unique elements
            Q4. Best Time to Buy and Sell Stocks I
    4. Sliding Window & Contribution Technique
        # Find the Total sum of all posible sub array
            -- BruteForce approach
            -- Prefix Sum
            -- Carray forward
            -- Contribution Technique
                Break down the problem: Instead of solving for every subarray, subsequence, or combination, calculate how each element contributes to the final solution.
                Sum up contributions: Once you know how much each element contributes, you sum them up to get the final result.
        # how to calculate contribution
            long long contribution = A[i] * (i + 1) * (N - i);
            total += contribution;
        # Find the Total sum of all posible sub array of Length K
            N-K+1
        #What is Sliding Window Tech.
        # Print all start and end indices of length K
            for(int L=0; L<=N-k; L++){
                int R = L+k-1;
                cout<< L << " " << R << endl;
            }
        # how to implement Sliding Window
        # whre to use Sliding window 
        # Given an Integer Array Find Max Subarray sum of Length K
        # QUESTIONS
            Q1. Maximum Subarray Easy
                -- N^2 2 Loop Aproach
                    use n^2 loop to find the sum and comapare with B and ans 
                -- Sliding Window Technique
            Q2. Sum of All Subarrays
                -- contributions Technique
                    for (int i = 0; i < N; ++i) {
                        long long contribution = A[i] * (i + 1) * (N - i);
                        totalSum += contribution;
                    }
            Q3. Subarray with given sum and length
            Q1. Good Subarrays Easy
            Q2. Minimum Swaps
            Q3. Subarray with least average
            Q4. Counting Subarrays Easy
    5. 2D Matrices
        # A[N][M]; N->rows; M->columns
        # How to Traverse the 2D Matrix
            -- rowwise
            --columnwise
        # How to print Principal Digonal 
            i=0;j=0;i=j;
        #How to print Anitiagonal 
            i=0,j=M; i++,j--;
            i+j = N-1;
            j = N-1-i;
        # print all elements Digonaly and Anti digonaly
            [0 to M-2] + [1 to N-1] // all Anti Digonal
        #Transpose of 2D Matrix
            traver all upper trangular element and replace them with lower trangular
        # How to Rotate the 2D Matrix
            transpose the matrix
            reverse each row
        # QUESTIONS
            Q1. Column Sum
            Q2. Main Diagonal Sum
            Q3. Anti Diagonals
            Q4. Matrix Transpose
            Q5. Rotate Matrix
            Q1. Matrix Scalar Product
            Q2. Add the matrices
            Q3. Minor Diagonal Sum
            Q4. Row Sum
    6. Arrays 1: One Dimensional
        # Questions
            Q1. Max Sum Contiguous Subarray
            Q2. Continuous Sum Query
            Q3. Rain Water Trapped
            Q1. Add One To Number
            Q2. Flip
    7. Arrays 2: Two Dimensional
        # Questions
            Q1. Spiral Order Matrix II
            Q2. Search in a row wise and column wise sorted matrix
            Q3. Sum of all Submatrices
            Q4. Row with maximum number of ones
            Q1. Minimum Swaps
    8. Arrays 3: Interview Problems
        # Questions
            Q1. Length of longest consecutive ones
            Q2. Majority Element
            Q3. Count Increasing Triplets
            Q1. N/3 Repeat Number
            Q2. Check anagrams
            Q3. Colorful Number
            Q1. First Missing Integer
            Q2. Merge Sorted Overlapping Intervals - 2
            Q3. Merge Intervals - 2
            Q1. Next Permutation
            Q2. Number of Digit One
    9. Array Extra
        # Introduction to array
            # Largest Element in an Array
                f(A){
                    largest = INT_MIN
                    for(i as 0 -> N-1){
                        if(A[i] > largest){
                            largest = A[i]
                        }
                    }
                    return largest
                }
            # Second Largest Element in an array
                F(A){
                    largest = INT_MIN
                    Slargest = INT_MIN

                    for (i as 0 -> N-1){
                        if(A[i] > largerst){
                            Slargest = largest
                            largest = A[i]
                        }

                        if(A[i] > Slargest && A[i] < largest){
                            Slargest = A[i]
                        }
                    }
                    return Slargest
                }
            # Check if the array is sorted
                F(Arr){
                    for(i as 1 -> N-1){
                        if(!(Arr[i] >= Arr[i-1])){
                            return false
                        }
                    }
                    return true
                }
            # Remove duplicates from an array (inplace)
                F(arr){
                    i = 0
                    for(j as 1 -> N-1){
                        if(arr[i] != arr[j]){
                            A[i+1] = arr[j]
                            i++
                        }
                    }
                    return A
                }
        # Rotate Array by K places | Union, Intersection of Sorted Arrays
            # Left Rotate Array by 1 place
                // Solution
                    F(arr){
                        temp = arr[0];
                        for (i as 1 -> N-1){
                            arr[i-1] = arr[i]
                        }
                        arr[N-1] = temp
                        return arr;
                    }
            # Left Rotate Array by D Place
                D = D % N
                if you want to rotate the array to the left by D places, you will get the original array back
                // Solution 1 
                    F(arr){
                        Temp
                        for(i as 0 -> d-1){
                            temp[i] = arr[i]
                        }
                        for(i as d -> N-1){
                            arr[i-d] = arr[i]
                        }
                        j=0
                        for (i as N-d -> N-1){
                            A[i] = temp[j] // temp[i - (n-d)]
                            j++
                        }
                    }
                // Solution 2
                    F(arr){
                        reverse(arr, 0, d-1)
                        reverse(arr, d, N-1)
                        reverse(arr, 0, N-1)
                    }
            # Move all Zeros to the end of the array
                // Solution 1
                    F(arr){
                        temp
                        for(i 0 -> n-1){
                            if(arr[i] != 0){
                                temp.add(arr[i])
                            }
                        }
                        for(i as 0 -> temp.size()-1){
                            arr[i] = temp[i]
                        }                  
                        for (i as temp.size() -> N-1){
                            arr[i] = 0
                        }  
                    }
                // Solution 2
                    F(arr){
                        j = -1
                        for(i as 0 -> N-1){
                            if(arr[i] == 0){
                                j = i
                                break
                            }
                        }

                        for( i as j+1 -> N-1){
                            if(arr[i] != 0){
                                swap(arr[i], arr[j])
                                j++
                            }
                        }
                    }
            # Linear Search
                f(arr targer){
                    for(i 0 -> N-1){
                        if(arr[i] == target){
                            return i
                        }
                    }
                   return -1
                }
            # Union of Two sorted Array
                // Solution 1
                    1. put all element of both array in ordered set
                    2. create array of size set.size()
                    3. put all element of set in array
                // Solution 2
                    F(a, b){
                        n1= a.size()
                        n2= b.size()

                        i= 0
                        j= 0
                        union;
                        while(i<n1 && j<n2){
                            if(a[i] <= b[j]){
                                if(union.size() == 0 || union.back() != a[i]){
                                    union.add(a[i])
                                }
                                i++
                            }else{
                                if(union.size() == 0 || union.back() != b[j]){
                                    union.add(b[j])
                                }
                                j++
                            }
                        }
                        while(i < n1){
                            if(union.size() == 0 || union.back() != a[i]){
                                union.add(a[i])
                            }
                            i++
                        }
                        while(j < n2){
                            if(union.size() == 0 || union.back() != b[j]){
                                union.add(b[j])
                            }
                            j++
                        }
                    }
            # Intersection of Two sorted Array
                // Solution 
                    F(a, b){
                        i=0
                        j=0
                        ans
                        while(i<n && j<m){
                            if(a[i] < b[j]){
                                i++
                            }else if(b[j] < a[i]){
                                j++
                            }else{
                                ans.add(a[i])
                                i++
                                j++
                            }
                        }
                    }
        # Find element that appears once | Find missing number | Max Consecutive number of 1's
            # Missing NO
                # BruteForce
                    Traverse from 1 to N
                    search each no in array 
                    if no is not present array return no
                # Better 
                    use hasmap of N+1
                    mark each if found
                    traverse the hashmap from 1 to n check which is not found 
                    return it
                # Optimal
                    - Using Sum
                        calculate the sum of N no -> Sum_N
                        calculate the array sum -> Sum_A
                        return Sum_N - Sum_A
                    - Using Xor 
                        Calculate the Xor  of N no -> Xor_N
                        calculate the Xor of array -> Xor_A
                        return Xor_N ^ Xor_A
            # Maximum Consucutive one's
                1. Traverse the array 
                2. if  (A[i] == 1)
                    then cnt++; max=max(max,cnt);
                3. else 
                    cnt = 0
        # Longest Subarray with sum K | Brute - Better - Optimal | Generate Subarrays
            # Longest Subarray with sum K
                # Brute Force
                    use N^3 approach
                    i 0->n
                    j i+1->n
                    k i->n // actual subbarray
                    for(i 0->n){
                        for(j i->n){
                            sum = 0
                            for(k i->j){
                                sum += A[k]
                            }
                            if(sum==k){
                                maxlen = max(maxlen, j-i+1)
                            }
                        }
                    }
                # Carry Forward
                    for(i 0->n){
                        sum = 0
                        for(j i->n){
                            sum+=A[j]
                            if(sum == K) maxlen = max(maxlen, j-i+1)
                        }
                    }
                # Better (using Hashing and Prefix sum)
                    1. initilize the hashmap hm <int int> (sum, last_index)
                    2. start the traversing for the Prefix Sum 
                    3. Every time not the (sum, i) in map
                    4. if current prefix sum (PSum) is grater than the k
                        check the (PSum-k) is present in map or not
                        if present then calculate the length and take max
                # Optimal (two Pointers)
                    1. initialize the two pointer L and R as 0
                    2. move forward r and add element in sum
                    3. if sum is greater than K move L and subtract element from sum
                    4. calculate the length and take max
        # 2 Sum Problem
            # Brute Force
                - Using N^2 Approach
                1. for(i as 0 -> N-1){
                    for(j as i+1 -> N-1){
                        if(i!=j && A[i]+A[j]==K){
                            return i,j
                        }
                    }
                }
            # Better (Hashing)
                - Using Hashing
                1. create a hashmap
                2. for(i as 0 -> N-1){
                    if(hashmap.find(K-A[i]) != hashmap.end()){
                        return i, hashmap[K-A[i]]
                    }
                }    
            # Optimal (Two Pointers)
                1. initialize two pointers as L=0 and R = N-1
                2. do until L<R
                3. if(A[l] + A[r] == K) return l,r
                4. if(A[l] + A[r] < K) L++
                5. if(A[l] + A[r] > K) R--
        # Sort an array of 0's 1's & 2's 
            # BruteForce (NlogN)
                Using Sorting Algo
            # Better (2N)
                1. Traverse the Array
                2. find the cout of 0,1,2
                3. overwrite the array according the counts 0,1,2 rescpectively
            # Optimal (Dutch National Flag Algo)
                - 3 pointers 
                    low, mid, high
                - Divide the array into 3 parts
                    1. [0 -> low-1] = 0
                    2. [low -> mid-1] = 1
                    3. [high+1 -> N-1] = 2
                    [mid -> high] = unsorted data
                - Value of mid can be 0,1,2
                1. 3 Pointers
                    low=0,mid=0,High=N-1;
                2. if(A[mid] = 0) swap(low, mid); low++; mid++;
                3. if(A[mid] = 1) mid++;
                4. if(A[mid] = 2) swap(mid, high); high--;
        # Majority Element I
            # Brute Force
                Use N^2 approach
                1. count the A[i] in whole array 
                2. if count > N/2 return i
            # Better (Hashing)
                Store the count of each element in a Hashmap
                iterate the hasmap if count is more than N/2 return element
            # Optimal (Moore's Voting Algo)
                Traverse the array:
                1. If count == 0, set the current element as the candidate.
                2. If the current element matches the candidate, increment the count.
                3. Otherwise, decrement the count.
        # Kadane's Algorithm | Maximum Subarray Sum | Finding and Printing
            # BruteForce
                N^3 Approach Genrating all subarray
                1. Use three nested loops:
                    - Outer loop to set the start of the subarray.
                    - Middle loop to set the end of the subarray.
                    - Inner loop to calculate the sum of the subarray.
                2. Compare each sum with the maximum sum.
            # Better 
                N^2 Carry forward teq.
                1. Use two nested loops:
                    - Outer loop to set the start of the subarray.
                    - Inner loop to calculate the sum of the subarray iteratively.
                2. Compare each sum with the maximum sum.
            # kadane's Algo
                1. Initialize current_sum to 0 and max_sum to negative infinity.
                2. Iterate through the array :
                    - Add the current element to current_sum.
                    - Update max_sum if current_sum is greater.
                    - If current_sum becomes negative, reset it to 0 (start a new subarray).
                3. Return max_sum.
        # Rearrange Array Elements by Sign | 2 Varieties of same Problem
            # Type 1 (Positive and Negative) are eqaual (N/2)
                # Bruteforce (N^2)
                    Create Two array Positive and Negative
                    arrange one by one
                # Optimal
                    initialize a exmpty array as ans
                    initilize a tow pointers posivtive=0 and negations=1
                    traverse the given array 
                    if(A[i]>0){
                        ans[positive] = A[i]
                        posivtive += 2
                    }else{
                        ans[negative] = A[i]
                        negative += 2
                    }
            # Type 2 (Positive and Negative) are not equal
        # Best Time to Buy and Sell Stock
            # Brute Force (O(N²))
                Compare every possible pair of days, calculate the profit, and track the maximum.
            # Optimal Approach (O(N))
                Using a single pass, keep track of the minimum price seen so far and calculate the maximum profit possible at each step.
        # Next Permutation
            # Bruteforce
                1. Genrate all permutations
                2. find the current permutation position
                3. give the current+1 permutation
            # Better using (CPP STL)
                next_permutation(A.begin(), A.end());
            # Optimal 
                1. findout the Break point (ind)
                    A[i] < A[i+1]
                    for(i as N-2 ->0)
                    if  not found  i.e. it is the last permutation
                    then return the first permutation by Reversing the current array
                2. find the A[i] > A[ind] first from last
                    Treverse 
                    for(i as N-1 -> ind+1)
                        find A[i] > A[ind]
                        Swap(A[i], A[ind])
                3. Reverse the subarray from ind+1 to N-1
        # Leaders in an Array
            - Everything in the right should be smaller
            BruteForce 
                use N^2 loop
                for(i as 0->N-1)
                    for(j as i+1 -> N-1)
            better
                1. create the prefix sum array that will store the Gratest element of right til current
                2. traver Left to right if prefixsum[i] <= A[i] then result.add(A[i])
            Optimal 
                use carry forward approach
                traverse form right to left 
                    keep track of greatest till i in a variable 
                    according to that add the leader in result
        # Longest Consecutive Sequence
            # Brute-force Approach: 
                1. To begin, we will utilize a loop to iterate through each element one by one.
                2. Next, for every element x, we will try to find the consecutive elements like x+1, x+2, x+3, and so on using the linear search algorithm in the given array.
                    - Within a loop, our objective is to locate the next consecutive element x+1. 
                        + If this element is found, we increment x by 1 and continue the search for x+2. 
                        + Furthermore, we increment the length of the current sequence (cnt) by 1. 
            # Better
                - We will consider 3 variables, 
                    + 'lastSmaller' →(to store the last included element of the current sequence), 
                    + 'cnt' → (to store the length of the current sequence), 
                    + 'longest' → (to store the maximum length).
                - Initialize 'lastSmaller' with 'INT_MIN', 'cnt' with 0, and 'longest' with 1(as the minimum length of the sequence is 1).
            # Optimal
                - First, we will put all the array elements into the set data structure.
                - If a number, num, is a starting number, ideally, num-1 should not exist. So, for every element, x, in the set, we will check if x-1 exists inside the set. :
                    + If x-1 exists: This means x cannot be a starting number and we will move on to the next element in the set.
                    + If x-1 does not exist: This means x is a starting number of a sequence. So, for number, x, we will start finding the consecutive elements.
        # Set Matrix Zeroes
            # BruteForce
                1. traverse the matrix 
                2. find 0  mark -1 to their row and cols element except 0
                3. traverse the matrix 
                4. find -1 mark 0
                5. return matrix
            # Better
                1. initialize the row array as size N and col array as size M
                2. traverse the matrix if 0 found mark row[i] = 1 and col[j] = 1
                3. Traverse the matrix again and check if row[i] or col[j] is 1 mark matrix[i][j] = 0
                4. return matrix
            # Optimal
                1. First, we will traverse the matrix and mark the proper cells of 1st row and 1st column with 0 accordingly. The marking will be like this: if cell(i, j) contains 0, we will mark the i-th row i.e. matrix[i][0] with 0 and we will mark j-th column i.e. matrix[0][j] with 0.
                    If i is 0, we will mark matrix[0][0] with 0 but if j is 0, we will mark the col0 variable with 0 instead of marking matrix[0][0] again.
                2. After step 1 is completed, we will modify the cells from (1,1) to (n-1, m-1) using the values from the 1st row, 1st column, and col0 variable.
                    We will not modify the 1st row and 1st column of the matrix here as the modification of the rest of the matrix(i.e. From (1,1) to (n-1, m-1)) is dependent on that row and column.
                3. Finally, we will change the 1st row and column using the values from matrix[0][0] and col0 variable. Here also we will change the row first and then the column.
                    If matrix[0][0] = 0, we will change all the elements from the cell (0,1) to (0, m-1), to 0.
                    If col0 = 0, we will change all the elements from the cell (0,0) to (n-1, 0), to 0.
        # Rotate Matrix
        # Spiral Traversal of Matrix
        # Count Subarray sum Equals K
        # Pascal Triangle | Finding nCr in minimal time
        # Majority Element II
        # 3 Sum
        # 4 Sum
        # Number of Subarrays with Xor K
        # Merge Overlapping Intervals
        # Merge Sorted arrays without extra space
        # Find the Missing and Repeating Number
        # Count Inversion in an Array
        # Reverse Pairs
        # Maximum Product Subarray
## Two Pointer ## 
    1. Two Pointers
        # Pair With Given Sum (Given an integer sorted array A and an integer K. Find any pair[ i , j ]  such that A[ i ] + A[ j ] = K, i != j)
        # Pair With Given Sum - 2 (Find count of all the pairs in a sorted array whose sum is K.  ( i != j ))

        # Pair With Given Difference ( Given an integer sorted array A and an integer K. Find any pair[ i , j ]) such that A[ i ] - A[ j ] = K, i != j)
        # Subarray With Given Sum (Given an arr[ N ] of positive integers and an integer K. Check if there exists a subarray with sum = K.)
        # Container With Most Water
        # Questions
            Q1. Container With Most Water
            Q2. Subarray with given sum
            Q3. Pairs with given sum II
            Q4. Pairs with Given Difference
            Q1. 3 Sum
            Q2. Array 3 Pointers
            Q3. Max Continuous Series of 1s
            Q4. Another Count Rectangles
            Q5. Closest pair from sorted arrays
    2. Two Pointers & Sliding Window Extra
        # Introduction to Sliding Window and Two Pointer / Template / Patterns
            1. Constant Window
            2. Longest Subarray / substring Where < Condition
                Q. Longest Subarray With Sum <= K
                    + Expand (R++)
                    + Shrink (L++)
                    findlength(){
                        l=0;
                        r=0;
                        sum =0
                        maxlength = 0;
                        while(r<N){
                            sum = sum+arr[r]
                            while(sum>K){
                                sum = sum - arr[l]
                                l++
                            }
                            if(sum<=k){
                                maxlength = max(maxlength, r-l+1)
                                r++
                            }

                        }
                        return maxlength
                    }
            3. No. of Subarray Where <Condition>
                - Using Pattern 2
                Q. No. of Subarray With Sum <= K
            4. Shortest/Minimum window where <Condition>
        # Maximum Points You Can Obtain from Cards
            1. lsum: This is the sum of the first k elements.
            2. rsum: This is the sum of the last k elements, which we will incrementally adjust as we move through the array.
            3. maxSum: This keeps track of the maximum sum found

            f(nums k){
                lsum =0, rsum=o, maxSum = 0
                for(i 0 -> k-1){
                    lsum += nums[i]
                }
                maxSum = lsum
                ri = n-1
                for(i as k-1 -> 0){
                    lsum -= nums[i]
                    rsum += nums[ri]
                    ri--
                    maxSum = max(maxSum, (lsum+rsum))
                }

                return maxSum
            }
        # Longest Substring Without Repeating Characters
            + Sliding Window: We use two pointers, l (left) and r (right), that represent the window in the string. We expand the window by moving r and contract the window by moving l when a duplicate character is found.
            + Hash Array: A hash array of size 256 (for all ASCII characters) is used to store the index of the most recent occurrence of each character. If a character is found within the window (i.e., between l and r), we update the left pointer l to exclude the previous occurrence of that character.
            f(s){
                hash(256, -1)
                l=0,r=0,maxlen=0

                while(r<n){
                    if(hash[s[r]] != -1){
                        if(hash[s[r]] >= l){
                            l = hash[s[r]]+1
                        }

                    }

                    len = r-l+1
                    maxlen = max(maxlen, len)
                    hash[s[r]] = r
                    r++;
                }

                return maxlen
            }  
        # Max Consecutive Ones III (at max k zeros allowed) 
            # Solution 1
                1. Expand the window by moving r.
                2. Count the zeros. If the count of zeros exceeds k, shrink the window by moving l.
                3. Update the result (maxlen) when the number of zeros in the window is valid (i.e., zeros <= k).

            f(nums,k){
                maxlen=0,l=0,r=0,zeros=0
                while(r<n){
                    if(nums[r] == 0){
                        zeros++
                    }
                    while(zeros > k){
                        if(nums[l] == 0){
                            zeros--
                        }
                        l++
                    }
                    len = r-l+1
                    maxlen = max(maxlen,len)
                    r++
                }
                return maxlen
            }
            # Solution 1
                1. Expand the window by moving r.
                2. Count the zeros and immediately shrink the window if the number of zeros exceeds k.
                3. Update the result (maxlen) after checking that the window is valid (i.e., zeros <= k).

            f(nums,k){
                maxlen=0,l=0,r=0,zeros=0
                while(r<n){
                    if(nums[r] == 0){
                        zeros++
                    }
                    if(zeros > k){
                        if(nums[l] == 0){
                            zeros--
                        }
                        l++
                    }
                    if(zeros <= k){
                        len = r-l+1
                        maxlen = max(maxlen,len)
                    }
                    r++
                }
                return maxlen
            }
        # Fruit Into Baskets
            # Solution 1
                1. Expand the window by moving r and updating the map.
                2. Shrink the window if the map.size() exceeds K by incrementing l in a nested while loop.
                3. Update the maximum length whenever the map.size() is valid (i.e., <= K).
            F(arr, K){
                l =0,r=0,maxlen=0
                map
                while(r<n){
                    map[arr[r]]++
                    while(map.size() > K){
                        map[arr[l]]--;
                        if(map[arr[l]] == 0){
                            map.erase(arr[l])
                        }
                        l++
                    }
                    if(map.size() <= K){
                        len = r-l+1
                        maxlen = max(maxlen,len)
                    }
                    r++
                }
                return maxlen
            }
            # Solution 2
                1. Expand the window by moving r and updating the map.
                2. Shrink the window if map.size() exceeds K by incrementing l.
                3. Update the maximum length whenever the map.size() is valid (i.e., <= K).
             F(arr, K){
                l =0,r=0,maxlen=0
                map
                while(r<n){
                    map[arr[r]]++
                    if(map.size() > K){
                        map[arr[l]]--;
                        if(map[arr[l]] == 0){
                            map.erase(arr[l])
                        }
                        l++
                    }
                    if(map.size() <= K){
                        len = r-l+1
                        maxlen = max(maxlen,len)
                    }
                    r++
                }
                return maxlen
            }
        # Longest Substring With At Most K Distinct Characters
            # Solution 1
                1. Expand the window by moving r and updating the map.
                2. Shrink the window if map.size() exceeds K by incrementing l.
                3. Update the maximum length whenever the map.size() is valid (i.e., <= K).

            F(s, K){
                l=0,r=0,maxlen=0,map<char, int>

                while(r<n){
                    map[s[r]]++
                    while(map.size() > K){
                        map[s[l]]--;
                        if(map[s[l]] == 0){
                            map.erase(s[l])
                        }
                        l++
                    }
                    if(map.size() <= K){
                        maxlen = max(maxlen, r-l+1)
                    }
                    r++
                }
                return maxlen
            }
            # Solution 2
                1. Expand the window by moving r and updating the map.
                2. Shrink the window if map.size() exceeds K by incrementing l in a nested while loop.
                3. Update the maximum length whenever the map.size() is valid (i.e., <= K).

            F(s, K){
                l=0,r=0,maxlen=0,map<char, int>

                while(r<n){
                    map[s[r]]++
                    if(map.size() > K){
                        map[s[l]]--;
                        if(map[s[l]] == 0){
                            map.erase(s[l])
                        }
                        l++
                    }
                    if(map.size() <= K){
                        maxlen = max(maxlen, r-l+1)
                    }
                    r++
                }
                return maxlen
            }
        # Number of Substrings Containing All Three Characters
            F(s){
                Lastseen(3, -1)
                cnt = 0
                for(i as 0 -> n-1){
                    Lastseen[s[i]-'a'] = i
                    if(Lastseen[0] != -1 && Lastseen[1] != -1 && Lastseen[2] != -1){
                        cnt += 1 + max(Lastseen[0], Lastseen[1], Lastseen[2])
                    }
                }
                return cnt
            }
        # Longest Repeating Character Replacement
            # solution 1
            F(S, K){
                l=0,r=0,maxlen=0,malf=0
                hash(26, 0)
                while(r<N){
                    hash[S[r]-'a']++
                    maxf = max(maxf, hash[S[r]-'a'])
                    while((r-l+1-maxf) > K){
                        hash[S[l]-'a']--
                        maxf = 0
                        for(i as 0 ->26) maxf = max(maxf, hash[i])
                        l++
                    }
                    if((r-l+1-maxf) <= K){
                        maxlen = max(maxlen, r-l+1)
                    }
                    r++
                }
                return maxlen
            }
            # Solution 2
            F(S, K){
                l=0,r=0,maxlen=0,malf=0
                hash(26, 0)
                while(r<N){
                    hash[S[r]-'a']++
                    maxf = max(maxf, hash[S[r]-'a'])
                    if((r-l+1-maxf) > K){
                        hash[S[l]-'a']--
                        maxf = 0
                        l++
                    }
                    if((r-l+1-maxf) <= K){
                        maxlen = max(maxlen, r-l+1)
                    }
                    r++
                }
                return maxlen
            }
        # Binary Subarrays With Sum | count subarray sum = k
            F_less_equal_K(arr, k) - F_less_equal_K(arr, k-1)
            F_less_equal_K(arr, k){
                if(k<0) return 0
                l=0,r=0,sum=0
                count = 0
                while(r<n){
                    sum += arr[r]
                    while(sum > k){
                        sum -= arr[l]
                        l++
                    }
                    count += (r-l+1)
                    r++
                }
                return count
            }
        # Count No. of Nice Subarray | No. of Subarray with no. of odd no is K
            1. Treat odd no as 1 and even no as 0
            2. find the no of subbarrays has sum = K
                2.1 find no of subarray has sum <= K
                2.2 find no of subarray has sum <= k-1
            3. return F_less_equal_K(arr, k) - F_less_equal_K(arr, k-1)
        # Subarray with k different integers
            F(arr, k) - F(arr, k-1)
            F(arr, k){
                l=0, r=0, cnt=0, map
                while(r<n){
                    map[arr[r]]++
                    while(map.size() > k){
                        map[arr[l]]--
                        if(map[arr[l]] == 0){
                            map.erase(arr[l])
                        }
                        l++
                    }
                    if(map.size()<= k){
                        cnt += (r-l+1)
                    }
                    r++
                }
                return cnt
            }
        # Minimum Window Substring
## Bit Manipulation ##
    1. Bit Manipulations Basics
        # Decimal Number System
        # Binary Number System
        # Binary to Decimal Conversion
        # Decimal to Binary Conversion
        # Addition of two binary numbers
        # Bitwise operators
        # AND (&)
        # OR (|)
        # NOT (!)
        # XOR (^)
        # How Negative NO are Stored
        # Questions
            Q1. Add Binary Strings
    2. Bit Manipulation 1
        # Questions
            Q1. Set Bit
            Q2. Unset i-th bit
            Q3. Check bit
            Q4. Number of 1 Bits
            Q5. Help From Sam
            Q6. Toggle i-th bit
            Q1. Unset x bits from right
            Q2. Finding Good Days
            Q3. Find nth Magic Number
    3. Bit Manipulation 2
        # Questions
            Q1. Single Number
            Q2. Single Number II
            Q3. Single Number III
            Q4. Find Two Missing Numbers
            Q5. Maximum AND Pair
            Q6. SUBARRAY OR
            Q1. Strange Equality
            Q2. Min XOR value
            Q3. Sum of Xor of all Pairs
    4. Bit Manipulation Extra
        # Introduction To Bit Manipulation
            - Binary Conversion
            - Decimal to Binary
            - Binary to Decimal
            - 1''s Complement
            - 2''s Complement
            - Operator 
                And
                OR
                NOT
                XOR
                    even no of 1''s - False
                    odd no of 1''s - True
                Left Shift
                    n*2^K
                Right Shift
                    n/2^K
            - How Negative No are Stored
        # Must Know Tricks in Bit Manipulation | Swap two numbers without third variable
            - Swap 2 NO
                5^5 = 0

                A = A^B; 
                B = A^B;  => (A^B) ^ B = A
                A = A^B;  => (A^B) ^ B=>(A) = B

            - Check ith bit set or Not
                <<
                if((N & (1<<i)) != 0) True
                else False

                >>
                if((N>>i & 1) == 1) True
                else False

            - Set ith bit
                N = N | (1<<i)
            
            - Unset ith bit
                N = N & ~(1<<i)

            - Toggle the ith bit 
                N = N ^ (1<<i)
            
            - Remove the Last Set Bit (Rightmost)
                N = N & (N-1)
            
            - Check if a number is power of 2
                if((N & (N-1)) == 0) True
                else False

            - Count the number of set bits
                int CountSetBit(int N){
                    cnt = 0
                    while(N > 1){
                        if(N%2 == 1) cnt++;
                        N = N/2;
                    }
                    if(N==1) cnt++

                    return cnt
                }

                int CountSetBit(int N){
                    cnt = 0
                    while(N > 1){
                       cnt += N & 1
                       N = N>>1
                    }
                    if(N==1) cnt++
                    return cnt
                }

                int CountSetBit(int N){
                    cnt = 0
                    while(N != 0){
                       N = N & (N-1)
                       cnt++
                    }
                    return cnt
                }
        # Power Set
            1. Number of Subsets:
                - For a set of size n, there are 2^n subsets (including the empty set).
                - 1 << n computes 2^n using bitwise left shift.
            2. Masking with Bits:
                - Each integer mask from 0 to 2^n - 1 represents a potential subset.
                - The bits in mask determine whether an element is included (1) or excluded (0) from the subset.
        # Single Number-I
            - a ^ a = 0
            - a ^ 0 = a
            1. Initialize result to 0: This acts as the XOR accumulator.
            2. Iterate through the array:
                For each element, apply the XOR operation with result.
            3. Final result: The number left in result after all XOR operations is the single number.
        # Single Number - II
            // Sollution 1
            int singleNumber(vector<int>& nums) {
                ans = 0;
                for( bi as 0 -> 31){
                    cnt = 0
                    for (i as 0 -> n-1){
                        if(isset(nums[i], bi)){
                            cnt++
                        }
                    }
                    if(cnt % 3 == 1){
                        ans set ith bit
                    }
                }
                return ans;
            }
            
            // solution 2
            int singleNumber(vector<int>& nums) {
                sort(nums)
                for(i 1 -> n i+=3){
                    if(nums[i] != nums[i-1]){
                        return nums[i-1]
                    }
                }
                return nums[n-1]
            }

            // Sollution 3
            int singleNumber(vector<int>& nums) {
                ones = 0
                twos = 0

                for(0 -> N-1){
                    ones = (ones ^ nums[i]) & ~(twos)
                    twos = (twos ^ nums[i]) & ~(ones)
                }

                return ones
            }
        # Single Number III
            1. XOR all numbers to get xorResult, which is the XOR of the two unique numbers since all other elements cancel out.
            2. Find a bit that is set (1) in xorResult (let's call it the rightmostSetBit). This bit differs between the two unique numbers.
            3. Partition the numbers into two groups based on this bit and XOR separately to find the two unique numbers.
        # XOR of Numbers in a Given Range
            XOR 1 to N
                N % 4 = 1 => 1
                N % 4 = 2 => N+1
                N % 4 = 3 => 0
                N % 4 = 4 => N

            XOR L TO R
                L to R = XOR(1 to L-1) ^ XOR(1 to R)
        # Divide Two Integers without using Multiplication and Division Operators
######################
## UNIT 2 ##
###################### 
## Strings ##
    1. Strings
        # ASCII Value
            A-Z = 65-90
            a-z = 97-122
            0-9 = 48-57
        # Toggle Case
            if('a'<= ch && ch <= 'z'){
                A[i]=(char)(ch-32);
            }else{
                A[i] = (char)(ch+32);
            }
        # substring
        # check for a substring if it's a palindrom or not
        # given a string fing longest palindrom substring
        # immutability of strings
        # Questions 
        Q1. Toggle Case
        Q2. Simple Reverse
        Q3. Reverse the String
        Q4. Longest Palindromic Substring
        Q1. Longest Common Prefix
        Q2. Count Occurrences
        Q3. Amazing Subarrays
        Q4. Isalnum()
    2. String Extra
        # String Rotation
## Maths ##
    1. Maths: Modular Arithmetic & GCD
        # Modulo (%)
            0 <= A%B <= B-1
        # Modulo Properties
            1. (a+b) % m = ((a%m) + (b%m)) % m
            2. (a*b) % m = ((a%m) * (b%m)) % m
            3. (a-b) % m = ((a%m) - (b%m) + m) % m
            4. (a)^b % m = ((a%m)^b) % m

            if(A<B)
                A%B = A
        # Given an Interger Array, Find Count of Pairs
            S.T. (A[i] + A[j]) % m = 0 & i<J
        # GCD 
            gcd(x,y) = d => X%d = 0 & Y%d = 0
            gdc(0,X) = x
            gcd(0,0) = 0 | Infinity
            gcd(15,20) = 5
        # GCD Properties
            1. gcd(x,0) = X
            2. gcd(x,y) = gcd(y,x)
            3. gcd(x,y,z) = gcd(gcd(x,y),z) = gcd(x, gcd(y,z)) = gcd(y, gcd(x,z))
            4. gcd(x,y) = gcd(x-y, y)
                (x>y)
            5. gcd(x,y) = gcd(x-y, y)
                        = gcd(x-y-y, y)
                        = gcd(x-y..., y)
                        = gcd(x%y, y)
                gcd(100,15) = gcd(100%15, 15) = gcd(10, 15)
        # Find Gcd(x, y)
        # Given an array find max gcd of the array after deleting an element
        # cpp method of GCD
            gcd(a, b)
        # Questions
            Q1. Pair Sum divisible by M
            Q2. Greatest Common Divisor
            Q3. Delete one
            Q4. Mod Sum
            Q1. A, B and Modulo
            Q2. Largest Coprime Divisor
            Q3. Divisor game
    2. Maths: Combinatorics Basics
        # Multiplication Rule
            Given 10 girls and 7 Boys. How many different pairs of 1:1 can be formed
            pair => 1 girl and 1 Boy
                use Manipulation Principal when "AND" is there
        # Addition Rule
            Q. Find Number of Ways to travel for Pune to Delhi or Mumbai
                use Addition Principal whene "OR" is there
        # Permutations
            arrangement of Objects
            -  in how many ways n distince character can be arranged
                ways(N) = N!
            - in how many ways can we arrange  R out N Distinct character 
                nPr = n! / (n-r)!   
        # Combinations
            Selection of Objects        
                nCr = n!/(r!(n-r)!)
        # Properties
            nC0 = 1
            nCn = 1
            nCn-r = N!/ R! * (N-R)!
        # Pascal Triangle
        # Nth Column Title
        # Questions
            Q1. Pascal Triangle
            Q2. Excel Column Title
            Q3. Compute nCr % m
            Q1. Excel Column Number
            Q2. Number of Digit One
            Q3. Consecutive Numbers Sum  
    3. Maths: Prime Numbers
        # What is Prime Number
        # Check if a Number is Prime
        # Sieve of Eratosthenes
        # Find the count of divisors for every integer from 1 to N. 
        # Sorted Permutation Rank
        # Questions
            Q1. Sorted Permutation Rank
            Q2. Count of divisors
            Q3. Find All Primes
            Q1. Prime Sum
            Q2. Lucky Numbers
## Hashing ##
    1. Hashing 1: Introduction
        # what is Hashing
        # Hash Set
        # Hash Map
        # Operations
            insert(key value)
            size()
            delete(key)
            get(key)
            contains_key(key)
        # Given N integers, find first non-repeating value. 
        # Find the count of Distinct elements in an array
        # Given an interger array, check subarray with 0 sum
        # Questions
            Q1. Frequency of element query
            Q2. Count distinct elements
            Q3. First Repeating element
            Q4. Sub-array with 0 sum
            Q5. Common Elements
            Q6. Count unique elements
            Q7. Count Subarray Zero Sum
    2. Hashing 2: Problems
        # Given an Integer array, check if there exists a pair (i, j) such that A[i] + A[j] = K & i!=j
        # Given an Integer array, Count a pair (i, j) such that A[i] + A[j] = K & i!=j
        # Check if there exits a subarray with sum k
        # Count subarray with sum k
        # Given an array, find count of Distinct element in every window of size K
        # Questions
            Q1. Check Pair Sum
            Q2. Count Pair Difference
            Q3. Subarray Sum Equals K
            Q4. Distinct Numbers in Window
            Q5. Longest Subarray Zero Sum
            Q6. Count Pair Sum
            Q7. Subarray with given sum
    3. Hashing 3: Internal Implementation & Problems
        # Questions
            Q1. Longest Increasing Subsequence
            Q2. Longest Subarray Zero Sum
            Q1. Colorful Number
            Q2. Count Subarrays
            Q3. Sort Array in given Order
## OOPS ##
    1. OOPS 1: Introduction
        Prgramming paradigms
    2. OOPS 2: Constructor, Inheritance & Polymorphism
    3. OOPS EXTRA
        # What is OOPS
            object
                entity
                    State/ Properties
                    Behavior/ Methods
             Object-Oriented Programming (OOP)
                Encapsulation: Bundling data and methods together.
                Inheritance: Deriving new classes from existing ones.
                Polymorphism: Using a single interface to represent different data types.
                Abstraction: Hiding complex implementation details and showing only essential features.
        # Class
        # How to Access Properties
            use (.) operator
        # Acess Modifiers
            1. public: Accessible from outside the class.
            2. private (default) : Accessible only within the class.
            3. Protected : Accessible in the class and derived classes.
        # Getter and Setter
            - Getters and Setters are special methods in Object-Oriented Programming (OOP) used to access and modify private attributes of a class. They provide controlled access to the attributes, ensuring encapsulation and data integrity.
            - Getter    
                get_data(){
                    return data
                }
                set_data(value){
                    data = value
                }
        # Behind the Scene
        # Padding 
        # Greedy Allignment
        # Static and Dynamic allocation
            Static Allocation: 
                Objects are created at compile-time and have a fixed lifetime (stack memory).
                When an object is statically allocated:
                    The memory is automatically managed.
                    The object is destroyed when it goes out of scope.
            Dynamic Allocation:
                Objects are created at runtime and are stored in the heap memory. They require explicit deallocation.
                When an object is dynamically allocated:
                    Memory is allocated during runtime on the heap.
                    We use the new keyword to allocate memory.
                    Explicitly delete the object using the delete keyword to avoid memory leaks.
        # constructor
            default Constructor
                A default constructor is a constructor that takes no arguments and is automatically called when an object is created. It is used to provide default values to object attributes.
            Parameterized Constructor
                A parameterized constructor is used to initialize an object with specific values when it is created.
            Copy Constructor
                A copy constructor is used to create a new object as a copy of an existing object. It is useful when we want to duplicate an object while ensuring its values remain the same.
        # Destructor
            A destructor is a special method called when an object is destroyed (goes out of scope). It is used to clean up resources (e.g., free memory). It is defined using a tilde (~) before the class name.
        # Deep And Shallow Copy
            // Shallow Copy
                A shallow copy copies the memory address (pointer) of dynamically allocated resources. Both the original and copied objects share the same memory location. This can lead to issues when one object is destroyed, leaving the other with a dangling pointer.
            // Deep Copy
                A deep copy creates a new copy of the dynamically allocated memory. This ensures that each object has its own independent memory space, avoiding issues like dangling pointers.
        # Copy Assignment Operator
            The copy assignment operator is used when an already initialized object is assigned the value of another object of the same type. It is different from the copy constructor, which is invoked during initialization or object creation. The copy assignment operator is invoked when an existing object is assigned the value of another existing object.
        # Static Variable
            A static variable retains its value between function calls. Unlike local variables, which are created and destroyed each time the function is called, static variables persist throughout the lifetime of the program. They are initialized only once, and their value is preserved across multiple calls.
                - Scope: Local static variables have local scope, but their lifetime extends for the duration of the program.
                - Usage: Static variables can be used to maintain state between function calls.
        # Static Member Variables (in Classes)
            A static member variable is shared by all instances of a class. It is not tied to a particular object of the class but belongs to the class itself. Static member variables can be accessed without creating an object, but they must be defined outside the class if they are to be used.
                - Shared by all objects: All instances of the class share the same static member.
                - Accessed using class name: Static members can be accessed directly by the class name or through objects.
        # Static Member Functions (in Classes)
            A static member function is a function that operates on static member variables or performs operations that are not specific to an instance of the class. Static member functions can be called without creating an object of the class.
                - Cannot access non-static members: Static member functions can only access static member variables or other static member functions.
                - Can be called using the class name: Static member functions can be called directly using the class name, without needing an object.
        # Static Function (Global Scope)
            A static function defined at the global scope can only be called within the file where it is defined. It is not visible to other translation units or source files. This is often used to limit the visibility of functions to a specific file in large projects.
        # Piller of OOPS
            1. Encapsulation
            2. Abstraction
            3. Inheritance
            4. Polymorphism
        # Encapsulation
            - Encapsulation is the concept of bundling the data (attributes) and the methods (functions) that operate on the data into a single unit known as a class. In simpler terms, it means hiding the internal state of an object and only exposing necessary parts of it through well-defined interfaces (i.e., getters and setters).
            - Private and Public Access Modifiers:
                Private members of a class can only be accessed by methods of that class, and not from outside the class.
                Public members can be accessed from outside the class.
            By hiding the internal details and exposing only what is necessary, we can control how the data is accessed or modified, thus ensuring security and integrity.
        # fully encapsulated
            A class is said to be fully encapsulated when:
                - Its data members (variables) are private, meaning they are not directly accessible from outside the class.
                - It provides public methods (getters and setters) to allow controlled access to those private data members.
                - It ensures that no data is directly exposed to external code, maintaining strict control over how the data is accessed or modified.
        # Abstraction
            - Abstraction is one of the fundamental principles of Object-Oriented Programming (OOP) that involves hiding the implementation details and exposing only the essential features or functionalities of an object. The goal is to reduce complexity and allow the programmer to focus on high-level operations rather than implementation details.
            - Abstraction can be achieved in two primary ways:
                Abstract Classes
                Interfaces
        # Inheritance
            Inheritance is one of the fundamental concepts of Object-Oriented Programming (OOP), and it allows a class (known as the derived class) to inherit properties and behaviors (methods) from another class (the base class). The derived class can reuse the code in the base class and can also add new features or modify existing ones.
            Types of Inheritance
                Single Inheritance
                Multilevel Inheritance
                Multiple Inheritance
                Hierarchical Inheritance
                Hybrid Inheritance
        # mode of Inheritance
            Public:Public -> Public
            Public:Proctected -> Protected  
            Public:Private -> Private 

            Proctected:Public -> Protected
            Protected:Proctected -> Protected
            Protected:Private -> Private

            Private:Public -> Not Accessible
            Private:Protected -> Not Accessible
            Private:Private -> Not Accessible

            private data memver connot be inherited
        # Inheritance Ambiguity
        # Polymorphism
            compile time 
                Function Overloading
                Operator Overloading
            runtime
                Method overrriding
        # Diff between Abstraction and Encapsulation
######################
## UNIT 3 ##
###################### 
## Sorting ##
    1. Sorting Basics
        # What is Sorting
        # Find the Minimum Cost to remove all elements from the array
            1.sort the array in descending order
            2. cost += A[i]*(i+1)
        # Nobel Integer
            1. sort the array in ascending order
            if (A[i] == i) cnt ++
        # Selection Sort
            works by repeatedly finding the minimum (or maximum, depending on sorting order) element from the unsorted part of the list and swapping it with the first element of the unsorted part. Over time, the sorted portion of the list grows, and the unsorted portion shrinks.
            it select the minimum element and swap it with the first element
            1. find the minimum element
            2. swap it with the first element
            3. shrink the array by 1 and repeat the process
            // 4 types of selection sort
                Ascending
                    max -> last 
                    min -> first
                Descending
                    Min -> last
                    Max -> first
        # Bubble Sort
            it looks like the bigger elements bubble up to the top thats why it is called as bubble sort
            1. compare the adjacent elements
            2. swap if the elements are not in the right order
            3. repeat the process until the array is sorted
        # Insertion Sort
            Insert an Element form unsorted array to its correct position in the sorted array
            1. Start from the second element: Assume that the first element is already sorted.
            2. Pick the next element: Compare it with elements in the sorted portion.
            3. Shift elements if needed: If the current element is smaller than any element in the sorted portion, shift those elements one position to the right to make space for the current element.
            4. Insert the current element: Insert it into its correct position in the sorted portion.
            5. Repeat: Continue with the next element until the entire array is sorted.
        # Questions
            Q1. Elements Removal
                1.sort the array in descending order
                2. cost += A[i]*(i+1)
            Q2. Noble Integer
                1. sort the array in ascending order
                2. if (A[i] == i) cnt ++
            Q3. Kth Smallest Element
                1. sort the array
                2. return A[k-1]
            Q1. Arithmetic Progression?
                1. sort the array
                2. take Difference of first two elements
                3. check if the difference is equal to the difference of next two elements till Last element
                4. if same return true else return false
    2. Sorting 1: Count Sort & Merge Sort
        # Q. Find the Smallest NO that can be formed by rearranging the digits in the given array 
            -- Count sort
                1. Find min and Max of array and create an array of size max-min+1 (frequncy array)
                2. Traverse the array and increment the frequncy array
                3. crate the array from the frequncy array
        # Q. Merge two sorted arrays into a single sorted Array
            1. Initialize Pointers: Set pointers for both arrays (e.g., i for array1 and j for array2) and create an empty array for the merged result.
            2. Compare and Merge:
                While both pointers are within the length of their respective arrays:
                    Compare the elements at array1[i] and array2[j].
                    Append the smaller element to the merged array and move the corresponding pointer forward.
            3. Copy Remaining Elements:
                If there are any elements left in array1, append them to the merged array.
                If there are any elements left in array2, append them to the merged array.

        # Merge Sort
            1. Divide the array into halves
            2. Recursively sort the halves
            3. Merge the sorted halves
        # Find the No of Pairs S.T. i<j & A[i] < A[j] (Inversion Count)
            Cnt += NO of Remaining Elements in Left Half When Selcting the element from Right Half
        # Questions
            Q1. Merge Two Sorted Arrays
                1. Initialize Pointers: Set pointers for both arrays (e.g., i for array1 and j for array2) and create an empty array for the merged result.
                2. Compare and Merge:
                    While both pointers are within the length of their respective arrays:
                        Compare the elements at array1[i] and array2[j].
                        Append the smaller element to the merged array and move the corresponding pointer forward.
                3. Copy Remaining Elements:
                    If there are any elements left in array1, append them to the merged array.
                    If there are any elements left in array2, append them to the merged array.
            Q2. Inversion count in an array
                same as merge sort but while checking 
                Cnt += NO of Remaining Elements in Left Half When Selcting the element from Right Half
            Q3. Count Sort
            Q4. Reverse pairs
            Q5. Minimum Absolute Difference
                1. sort the array
                2. take a traversal loop and find the difference between the adjacent elements
                3. return the min difference
            Q6. Max Chunks To Make Sorted
                1. maxValue = max(maxValue, A[i]); // Update the maximum value encountered so far
                2. if (maxValue == i) // Check if current maxValue equals the current index
                3. ++chunks; // We can create a valid chunk up to index i
    3. Sorting 2: Quick Sort & Comparator Problems
        # Q. Given an Integer array, Consider First Element as Pivot, Rearrange the Element Such that 
            All i 
                A[i]<p -> Move left
                A[i]>p -> Move right
        # Quick Sort
        # Random Pivot
        # Comparator
            1. A comparator is essentially a function or an object that takes two arguments of the same type and returns a boolean value. The return value indicates the order of the elements:
            2. True: The first element is considered less than the second (meaning it should come before it in sorted order).
            3. False: The first element is considered greater than or equal to the second.
        # Factor Sort
        # arrange the number as make largest strings
        # Questions
            Q1. Factor Sort
            Q2. Largest Number
            Q3. B Closest Points to Origin
            Q4. Sort by Color
            Q1. Wave Array
            Q2. Tens Digit Sorting
    4. Sorting Extra
## SEARCHING ##
    1. Searching 1: Binary Search on Array
        # Types of Searching Algo
            # Linear Search
                - Description: This is the simplest search algorithm. It checks each element in the array sequentially until it finds the target value or reaches the end of the array.
                - Time Complexity: O(N), where N is the number of elements in the array.
                - Use Case: Works well for small or unsorted data sets.
            # Binary Search
                - Description: This algorithm works on sorted arrays. It divides the search interval in half repeatedly, checking whether the target is in the left or right half until the target is found or the interval is empty.
                - Time Complexity: O(log N).
                - Use Case: Efficient for large sorted data sets.
            # Interpolation Search
                - Description: This algorithm improves upon binary search for uniformly distributed data. It calculates the position to check based on the value of the target relative to the range of values in the array.
                - Time Complexity: O(log log N) on average, but can degrade to O(N) in the worst case.
                - Use Case: Efficient for uniformly distributed sorted arrays.            
        # Whats is Binary Search
            Binary search is a fundamental algorithm that efficiently finds a target value in a sorted array
            Time Complexity: O(log N)
            Space Complexity: O(1) 
        # 3 steps to implement Binary Search
            1. Define a Search Speace 
            2. Check if a Mid is the target
            3. Decide the Left/Right
        # How its Work 
            1. Initialization: Start with two pointers, left and right, which represent the current search interval.
            2. Calculate Midpoint: Find the midpoint mid of the current interval :
                MID = L+((R-L)/2)  Using this formula helps avoid overflow issues
            3. Comparison : 
                - If arr[mid] is equal to the target, the search is successful, and you return the index mid.
                - If arr[mid] is less than the target, the target must be in the right half of the array, so update left to mid + 1.
                - If arr[mid] is greater than the target, the target must be in the left half, so update right to mid - 1.
            4. Repeat: Continue the process until the target is found or the search interval is empty (left exceeds right).
        
        # MID = L+((R-L)/2)
            The expression "L + (R - L) / 2" is used instead of "L + R / 2" to find the midpoint in binary search or similar algorithms to avoid potential overflow issues.
        # 1. while (l <= r)
                - Condition:
                    The loop continues as long as l is less than or equal to r. This means the loop will also execute when l == r, i.e., when there is exactly one element left to check.
                - Use Case:
                    This condition is typically used when you're looking for an exact match or when you need to ensure that every element in the search range is considered, including the last element.
                    For example, in standard binary search where you want to find the exact position of a target value, you would use while (l <= r).

        # Q. Find the First Occurance of a Number.
                1. L =0; R=N-1
                2. calculate mid
                3. check mid is the target
                    if yes check if privious element is target or not
                        if yes go left
                        else return mid
                    else chcke mid < target
                        go Right
                    else go left
        # Q. Find the Last Occurance of a Number.
                1. L =0; R=N-1
                2. calculate mid
                3. check mid is the target
                    if yes check if next element is target or not
                        if yes go right
                        else return mid
                    else chcke mid < target
                        go Right
                    else go left
        # Q. Given an integer array where every element occurs twice except for 1 element find that unique element. Duplicate elements are adjacent to each other (data is unsorted)
                - privious and next are not equal to mid means the element is unique
                - check index of mid is even or odd using that we can find out where to go left or a right
                
                1. L =0; R=N-1
                2. calcualte mid
                3. if privious and next is not eqaul to mid return mid
                4. if privious is equal to mid  
                        if mid is even go right
                        else go left
                5. else  
                        if mid is even go left
                        else go right
                index will chenge as even odd index after that single element
        # Q. Given an increasing decreasing array with distinct elements find max element
                -  Find Peak Element
                -  10 15 12   both side of 15 element are lower than 15
        # Q. Given an array with distinct elements. Find any one Local Minima.
                - both side element is lower than mid
                if (arr[mid] < arr[mid - 1] && arr[mid] < arr[mid + 1]) { }

        # Questions
        # Q1. Sorted Insert Position
            binary search and return left
        # Q2. Search for a Range
            Fist Occurance for Left and Last Occurance for Right
            2 binary search one for left and one for right
        # Q3. Find a peak element
            both side element are lower than peak
        # Q4. Single Element in Sorted Array
            index will chenge as even odd index after that single element
        # Q5. Matrix Search.
            The idea is to treat the 2D matrix like a 1D sorted array, where the element at index mid is found using the formula A[mid / M][mid % M].
            int left = 0, right = N * M - 1;
            int midValue = A[mid / M][mid % M];

            1. mid / M: This gives the row index.
                Explanation: In a flattened 1D array, each row of the matrix contains M elements. So, dividing mid by M tells us which row the element is in.

                Example: For mid = 5 and M = 3, 5 / 3 = 1. This means the element is in row 1 (second row, since indices are 0-based).

            2. mid % M: This gives the column index.
                Explanation: The remainder when dividing mid by M tells us the position within the row (i.e., the column index).

                Example: For mid = 5 and M = 3, 5 % 3 = 2. This means the element is in column 2 (third column, since indices are 0-based).
            
        # Q1. Minimum Difference
            do not creat array
                rather than
                check min difference of current element and closest element in next row and take min difference
                return the min of all differences

            1. Iterate each element of every row except last
            2. check for lowebound and upperbound of current element
            3. take min difference
            
            1. Sort Each Row: Sorting each row allows us to use binary search, which is faster for finding closest elements compared to linear search.
            2. Binary Search for Closest Elements:
                - For each element in the current row, use binary search on the next row to find:
                    + The smallest element that is greater than or equal to the current element.
                    + The largest element that is less than the current element.
                - These two elements help determine the minimum possible difference for adjacent elements in the 1-D array.
            3. Calculate Minimum Difference:
                - For each element, calculate the absolute difference with both the closest greater and closest smaller elements in the next row. Track the smallest difference to minimize the cost of the new array.

        # Q2. Maximum height of staircase
            1. max height will liest between 1 and N
            2. take mid as height and calculate no of required block to build staircase of mid as height
            3. if < sum is grater : go left
            4. if > sum is less : stor in ans and go right
            5. if == sum is equal : return ans
    2. Searching 2: Binary Search Problems
        #Q. Given a [rotated sorted array]. find index of element K If not present return 1 (unique elements)
            Check X is in Part 1 and Part 2
                "if X > A[0]" then -> x is in part 1  
                    if M > A[0] then -> M is in part 1
                        normal search
                    else go left
                else -> x is in part 2
                    if M < A[0] then -> M is in part 2
                        normal search
                    else 
                        go right
        # Q. Find sqrt(N) only integer part
            1 <= roon(N) <= N
            Sqrt of N Lies in [1, N] i.e. L= 1, R = N

            0. L=1 R=N
            1. calculate mid
            2. if mid*mid == N then return "ans" == mid
            3. if mid*mid < N  then store mid in "ans" and go right
            4. if mid*mid > N  then go left
            5. return "ans"


        # Q. Nth Magical Number (x,y, K)
            1. gcd(x, y)
            2. lcm(x, y) = x*y / gcd(x, y)
            3. count of Numbers <= K, divisible by x  = K/x
            4. count of Numbers <= K, divisible by x or y or both  = K/X + K/Y - K/lcm(x, y)

        # Q. Find Nth Number which is divisible by X or Y or both
            1. Define Search Space
                [L = MIN(x, y), R = K*MAX(x, y)]
            2. find count of numbers <= mid divisible by x or y or both
            3. if mid == K and mid is divisible by X or Y  then return mid
            4. if count < K then go right
            5. else go left
        # Q. Find Median of given array
            1. median will lies in Min and Max
                Define L = min and R = max
            2.  calculate mid.
            3. calculate the count of less element than mid
            4. if count is less than and equal to mid then store mid and go right
            5. if count is greater than mid then go left
            6. return L;
        # Q. Find the Median of Two sorted array
            - we have to find the median of two sorted array without mergeing them
            - we can use binary search to find the partition
            - The left half of the combined array contains half of the total elements (or slightly more if odd).
            - The right half contains the rest.
            - The largest element on the left side if the total number of elements is odd.
            - The average of the largest element on the left and the smallest element on the right if the total number of elements is even.

        # Questions
        # Q1. Rotated Sorted Array Search
            Check X is in Part 1 and Part 2
                "if X > A[0]" then -> x is in part 1  
                    if M > A[0] then -> M is in part 1
                        normal search
                    else go left
                else -> x is in part 2
                    if M < A[0] then -> M is in part 2
                        normal search
                    else 
                        go right
        # Q2. Median of Array
            1. median will lies in Min and Max
                Define L = min and R = max
            2.  calculate mid.
            3. calculate the count of less element than mid
            4. if count is less than and equal to mid then store mid and go right
            5. if count is greater than mid then go left
            6. return L;
        # Q3. Ath Magical Number
            1. Define Search Space
                [L = MIN(x, y), R = K*MAX(x, y)]
            2. find count of numbers <= mid divisible by x or y or both
            3. if mid == K and mid is divisible by X or Y  then return mid
            4. if count < K then go right
            5. else go left
        # Q4. Square Root of Integer
            1 <= roon(N) <= N
            Sqrt of N Lies in [1, N] i.e. L= 1, R = N

            0. L=1 R=N
            1. calculate mid
            2. if mid*mid == N then return "ans" == mid
            3. if mid*mid < N  then store mid in "ans" and go right
            4. if mid*mid > N  then go left
            5. return "ans"
        # Q1. ADD OR NOT
        # Q2. Find Smallest Again
        # Q3. Matrix Median
    3. Searching 3: Binary Search on Answer
        # Painter's Partition Problem
        # Find the min # Painters required to paint all the boards in T unit of time if not possible return -1.
            1. start with 1 painter and its Time t = T;
            2. Check all Boards one by one will able to paint or no
            3. if any boards size is grater than T then return not possible (-1)
            4. if painter has time (t) to paint current board then allocate them and reduce t
            5. if not then increment painter and reduce T - time required to paint current board
            6. return painter

        # Find the Min time required to paint all boards if K painters are available.
            1. Define Serach Space 
                L = max(all board sizes); R = sum(all board sizes)
            2. calculate mid as Time to required to paint all boards
            3. Check time is fissible or not
            4. if yes then store time and go left to check any min time is there or not
            5. if no then go right tno check fissible time

        # Distribute the emails to K handlers
            + Situation:
                - Imagine you are tasked with developing a system for "evenly distributing the workload among a team" Of email response handlers in a customer service department. 
                - Each email is assigned a "complexity score" which represents the esti mated time and effort required to address it. 
                - The complexity scores are represented as an "array, where each element corresponds to a single email".
            + Task
                - The goal is to divide the array into "K contiguous blocks (where K is the number of email handlers)", 
                - such that the "maximum sum of the complexity scores in any block is minimized". 
                - This approach aims to ensure that no single email handler is overwhelmed with high-complexity emails while others have a lighter load.
            + Minimize the Maxima

        # Common Observation of Binary Search
            - maximize the minima
            - minimize the maxima

        # Aggressive Cows
            - Cows are aggressive towards each other. So, farmer wants to "maximise the minimum distance" between any pair of cows.
            - Maximize the Minima

            1. Define Serach Space 
                L = 1;  R = max(A) - min(A)  // (A[n-1] - A[0])
            2. calculate mid as posible distance
            3. Check distance is possile or not
            4. if yes then store distance and go left to check any min distance is there or not
            5. if no then go right tno check fissible distance

        # Question
        # Q1. Aggressive cows
            - Cows are aggressive towards each other. So, farmer wants to "maximise the minimum distance" between any pair of cows.
            - Maximize the Minima

            1. Define Serach Space 
                L = 1;  R = max(A) - min(A)  // (A[n-1] - A[0])
            2. calculate mid as posible distance
            3. Check distance is possile or not
            4. if yes then store distance and go left to check any min distance is there or not
            5. if no then go right tno check fissible distance
        # Q2. Painter's Partition Problem
            1. Define Serach Space 
                L = max(all board sizes); R = sum(all board sizes)
            2. calculate mid as Time to required to paint all boards
            3. Check time is fissible or not
            4. if yes then store time and go left to check any min time is there or not
            5. if no then go right tno check fissible time
        # Q3. Special Integer
        # Q1. Allocate Books
    4. Searching Extra
        # Recursive Binary Search Algorithm
            1. Define the Base Case:
                - If the search range (defined by left and right indices) is invalid (e.g., left > right), the target is not present, so return -1.
                - If the middle element matches the target, return the middle index.
            2. Recursive Case:
                - If the middle element is greater than the target, search in the left half (left to mid - 1).
                - If the middle element is less than the target, search in the right half (mid + 1 to right).
        # Lower Bound And Upper Bound
            Lower Bound = Smallest index such that Arr[mid] >= target

                1. The loop continues until left == right.
                2. If arr[mid] >= target, 
                    then we go LEFT to find the smallest is there or not
                    right = mid -1.
                3. Otherwise, left becomes mid + 1.
                4. When the loop exits, left will be at the first occurrence of target or the first element greater than target.

                in STL 
                    int LB = (std::lower_bound(arr.begin(), arr.end(), value)) -  arr.begin();

            Upper Bound = Smallest index such that Arr[mid] > target

                1. The loop continues until left == right.
                2. If arr[mid] >= target, 
                    then we go LEFT to find the smallest is there or not
                    right = mid -1.
                3. Otherwise, left becomes mid + 1.
                4. When the loop exits, left will be at the first occurrence of target or the first element greater than target.

                in STL 
                    int LB = (std::upper_bound(arr.begin(), arr.end(), value)) -  arr.begin();
        # Floor and Ceil of X in an array
            Floor of X
                Largest no in Array <= X
                We will declare the 2 pointers and an 'ans' variable initialized to -1 (If we don''t find any index, we will return -1).

                1. Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index and high will point to the last index.
                2. Calculate the 'mid': Now, we will calculate the value of mid using the following formula:
                    - mid = (low+high) // 2 ( '//' refers to integer division)
                3. Compare arr[mid] with x: With comparing arr[mid] to x, we can observe 2 different cases:
                    - Case 1 - If arr[mid] <= x: The index arr[mid] is a possible answer. So, we will store it and will try to find a larger number that satisfies the same condition. That is why we will remove the left half and try to find the number in the right half.
                    - Case 2 - If arr[mid] > x: arr[mid] is definitely not the answer and we need a smaller number. So, we will reduce the search space to the left half by removing the right half.
                4. The above process will continue until the pointer low crosses high.
            Ceil of X (same as Lower Bound)
                Smallest no in Array >= X
                We will declare the 2 pointers and an 'ans' variable initialized to -1(If we don''t find any index, we will return -1).
                1. Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index and high will point to the last index.
                2. Calculate the 'mid': Now, we will calculate the value of mid using the following formula:
                    mid = (low+high) // 2 ( '//' refers to integer division)
                3. Compare arr[mid] with x: With comparing arr[mid] to x, we can observe 2 different cases:
                    Case 1 - If arr[mid] >= x: This condition means that the index arr[mid] may be an answer. So, we will update the 'ans' variable with arr[mid] and search in the left half if there is any smaller number that satisfies the same condition. Here, we are eliminating the right half.
                    Case 2 - If arr[mid] < x: In this case, arr[mid] cannot be our answer and we need to find some bigger element. So, we will eliminate the left half and search in the right half for the answer.
                4. The above process will continue until the pointer low crosses high.
        # Search in Rotated Sorted Array with Duplicate
            - Indentify The Sorted Half

            1. Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index, and high will point to the last index.
            2. Calculate the 'mid': Now, inside a loop, we will calculate the value of 'mid' using the following formula:
                - mid = (low+high) // 2 ( '//' refers to integer division)
            3. Check if arr[mid] = target: If it is, return True.
            4. Check if "arr[low] = arr[mid] = arr[high]": If this condition is satisfied, we will just increment the low pointer and decrement the high pointer by one step. We will not perform the later steps until this condition is no longer satisfied. So, we will continue to the next iteration from this step.
            5. Identify the sorted half, check where the target is located, and then eliminate one half accordingly:
                - "If arr[low] <= arr[mid]": This condition ensures that the left part is sorted.
                    + If arr[low] <= target && target <= arr[mid]: It signifies that the target is in this sorted half. So, we will eliminate the right half (high = mid-1).
                    + Otherwise, the target does not exist in the sorted half. So, we will eliminate this left half by doing low = mid+1.
                - Otherwise, if the right half is sorted:
                    + If arr[mid] <= target && target <= arr[high]: It signifies that the target is in this sorted right half. So, we will eliminate the left half (low = mid+1).
                    + Otherwise, the target does not exist in this sorted half. So, we will eliminate this right half by doing high = mid-1.
            6. Once, the 'mid' points to the target, we will return True.
            7. This process will be inside a loop and the loop will continue until low crosses high. If no element is found, we will return False
        # Minimum in Rotated Sorted Array
            - Indentify The Sorted Half
            - Sorted Half May or May not  have the answer
            - pick the min from the sorted half and eleminate the sorted half

            1. Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index, and high will point to the last index.
            2. Calculate the 'mid': Now, inside a loop, we will calculate the value of 'mid' using the following formula:
                - mid = (low+high) // 2 ( '//' refers to integer division)
            3. If arr[low] <= arr[high]: In this case, the array from index low to high is completely sorted. Therefore, we can select the minimum element, arr[low], and update the 'ans' variable with the minimum value i.e. min(ans, arr[low]). Once this is done, there is no need to continue with the binary search algorithm. So, we will break from this step.
            4. Identify the sorted half, and after picking the leftmost element, eliminate that half.
                - If arr[low] <= arr[mid]: This condition ensures that the left part is sorted. So, we will pick the leftmost element i.e. arr[low]. Now, we will compare it with 'ans' and update 'ans' with the smaller value (i.e., min(ans, arr[low])). Now, we will eliminate this left half(i.e. low = mid+1).
                - Otherwise, if the right half is sorted:  This condition ensures that the right half is sorted. So, we will pick the leftmost element i.e. arr[mid]. Now, we will compare it with 'ans' and update 'ans' with the smaller value (i.e., min(ans, arr[mid])). Now, we will eliminate this right half(i.e. high = mid-1).
            5. This process will be inside a loop and the loop will continue until low crosses high. Finally, we will return the 'ans' variable that stores the minimum element.
        # Find How many time Array has been Rotated
            Same as the Find Minimum in Roated Sorted array 
            Just return the index of Roated Sorted array
        # Find the Nth root of an Integer
            L= 1, R = N
            check mid is Nth root or not
            if is_ans(min, N) > M then R = mid - 1
            else L = mid + 1;
        # Koko Eating Bananas
            Problem Statement: 
                A monkey is given 'n' piles of bananas, whereas the 'ith' pile has 'a[i]' bananas. An integer 'h' is also given, which denotes the time (in hours) for all the bananas to be eaten.
                Each hour, the monkey chooses a non-empty pile of bananas and eats 'k' bananas. If the pile contains less than 'k' bananas, then the monkey consumes all the bananas and won''t eat any more bananas in that hour.
                Find the minimum number of bananas 'k' to eat per hour so that the monkey can eat all the bananas within 'h' hours.

            - Take 1 and N as a Ragne and Check the mid is fisible if yes then go left for more optimise ans or not to go right for fisible ans

            1. First, we will find the maximum element in the given array i.e. max(a[]).
            2. Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 1 and the high will point to max(a[]).
            3. Calculate the 'mid': Now, inside the loop, we will calculate the value of 'mid' using the following formula:
                - mid = (low+high) // 2 ( '//' refers to integer division)
            4. Eliminate the halves based on the time required if Koko eats 'mid' bananas/hr:
                - We will first calculate the total time(required to consume all the bananas in the array) i.e. totalH using the function calculateTotalHours(a[], mid):
                    + If totalH <= h: On satisfying this condition, we can conclude that the number 'mid' is one of our possible answers. But we want the minimum number. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
                    + Otherwise, the value mid is smaller than the number we want(as the totalH > h). This means the numbers greater than 'mid' should be considered and the right half of 'mid' consists of such numbers. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).
            5. Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.
        # Minimum days to make M bouquets
            L = min R = max
            Check mid is possible ans if yes then go left to further efficient ans
            else go right to find possible ans
        # Find the Smallest Divisor Given a Threshold
            L = 1 R = max
            Check mid is possible ans if yes then go left to further efficient ans
            else go right to find possible ans
        # Capacity to Ship Packages within D Days
            L = Max R= Sum(Array)
            Check mid is possible ans if yes then go left to further efficient ans
            else go right to find possible ans
        # Kth Missing Positive Number
            1. Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to index 0 and the high will point to index n-1 i.e. the last index.
            2. Calculate the 'mid': Now, inside the loop, we will calculate the value of 'mid' using the following formula:
                - mid = (low+high) // 2 ( '//' refers to integer division)
            3. Eliminate the halves based on the number of missing numbers up to index 'mid':
                - We will calculate the number of missing numbers using the above-said formula like this: missing_numbers = vec[mid] - (mid+1).
                    + If missing_numbers < k: On satisfying this condition, we can conclude that we are currently at a smaller index. But we want a larger index. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).
                    + Otherwise, we have to consider smaller indices. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
            4. Finally, when we are outside the loop, we will return the value of (k+high+1) i.e. the kth missing number.
        # Split array - Largest Sum
            1. Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to max(arr[]) and the high will point to sum(arr[]).
            2. Calculate the 'mid': Now, inside the loop, we will calculate the value of 'mid' using the following formula:
                - mid = (low+high) // 2 ( '//' refers to integer division)
            3. Eliminate the halves based on the number of subarrays returned by countPartitions():
                - We will pass the potential value of 'maxSum', represented by the variable 'mid', to the 'countPartitions()' function. This function will return the number of partitions we can make.
                    + If partitions > k: On satisfying this condition, we can conclude that the number 'mid' is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).
                    + Otherwise, the value mid is one of the possible answers. But we want the minimum value. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
            4. Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.
        # Minimize Max Distance to Gas Station
            1. First, we will find the maximum distance between two consecutive gas stations i.e. max(dist).
            2. Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 0 and the high will point to max(dist).
            3. Now, we will use the 'while' loop like this: while(high - low > 10^(-6)).
            4. Calculate the 'mid': Now, inside the loop, we will calculate the value of 'mid' using the following formula:
                - mid = (low+high) / 2.0
            5. Eliminate the halves based on the number of stations returned by numberOfGasStationsRequired():
                - We will pass the potential value of 'dist', represented by the variable 'mid', to the 'numberOfGasStationsRequired()' function. This function will return the number of gas stations we can place.
                    + If result > k: On satisfying this condition, we can conclude that the number 'mid' is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid).
                    + Otherwise, the value mid is one of the possible answers. But we want the minimum value. So, we will eliminate the right half and consider the left half(i.e. high = mid).
            6. Finally, outside the loop, we can return either low or high as their difference is beyond 10^(-6). They both can be the possible answer. Here, we have returned the 'high'.
        # Median of 2 sorted arrays
            - Make the Correct Left Half H = N+M+1/2
            - Taking the Binary Sarch on Smaller array (A) to dicide how many element will go to left half from smaller array rest will be in right half 
            - if we got the correct no element in Left half from LA then from B is LB = H - LA
            - Then remaining element will go to right half RA and RB
            - To Identify Correct LA using Binary Search 
                      LAmax < RBmin
                      LBmax < RAmin
            - L = max(LAmax,LBmax)
            - R = min(RAmin,RBmin)
            - Median = L+R/2
        # Kth element of 2 sorted arrays
            Just like the Median of 2 Sorted Arrays 
            Just make the Partition AS
                K | N-K
            return the max of Left partioin 
        # Find the row with maximum number of 1's
            - Find the MID as first occurrence of 1 in every row
            - Calculate the number of 1''s in every row using the formula using the MID
            - Take Max of each row and min Index of Max Row
            - return the min Index of Max Row
        # Search in a 2 D matrix
            - The idea is to treat the 2D matrix like a 1D sorted array, where the element at index mid is found using the formula A[mid / M][mid % M].
            - int left = 0, right = N * M - 1;
            - int midValue = A[mid / M][mid % M];

            1. mid / M: This gives the row index.
                Explanation: In a flattened 1D array, each row of the matrix contains M elements. So, dividing mid by M tells us which row the element is in.

                Example: For mid = 5 and M = 3, 5 / 3 = 1. This means the element is in row 1 (second row, since indices are 0-based).

            2. mid % M: This gives the column index.
                Explanation: The remainder when dividing mid by M tells us the position within the row (i.e., the column index).

                Example: For mid = 5 and M = 3, 5 % 3 = 2. This means the element is in column 2 (third column, since indices are 0-based).          
        # Search in a row and column wise sorted matrix
            1. As we are starting from the cell (0, m-1), the two variables i.e. 'row' and 'col' will point to 0 and m-1 respectively.
            2. We will do the following steps until row < n and col >= 0(i.e. while(row < n && col >= 0)):
                - If matrix[row][col] == target: We have found the target and so we will return true.
                - If matrix[row][col] > target: We need the smaller elements to reach the target. But the column is in increasing order and so it contains only greater elements. So, we will eliminate the column by decreasing the current column value by 1(i.e. col--) and thus we will move row-wise.
                - If matrix[row][col] < target: In this case, We need the bigger elements to reach the target. But the row is in decreasing order and so it contains only smaller elements. So, we will eliminate the row by increasing the current row value by 1(i.e. row++) and thus we will move column-wise.
            3. If we are outside the loop without getting any matching element, we will return false.
        # Find Peak Element (2D Matrix)
            1. Choose the middle column: Perform a binary search on the columns. At each step, take the middle column.
            2. Find the global maximum in this column: Identify the row index that contains the maximum element in this column.
            3. Check the neighbors of this element:
                - If this maximum element is greater than or equal to its left and right neighbors (if they exist), then it is a peak, and we return this element.
                - Otherwise, if the left neighbor is greater, the peak must lie in the left half of the matrix, so move your search to the left side.
                - If the right neighbor is greater, the peak must lie in the right half of the matrix, so move your search to the right side.
            4. Repeat until you find a peak.
        # Matrix Median
            1. Determine the Range:
                - The median must lie between the smallest element in the matrix (left) and the largest element (right).
                - Since each row is sorted, we can find the smallest element as the first element of the first row and the largest as the last element of the last row.
            2. Binary Search on Value:
                - Use binary search within the range [left,right].
                - For each middle value mid, count how many elements in the matrix are less than or equal to mid.
                - If the count is less than or equal to half the total elements, then increase mid (move right). Otherwise, decrease  mid (move left).
                - The goal is to converge to the median value.
            3. Counting Elements:
                - Use binary search on each row to count how many elements in that row are less than or equal to mid.
## LINKED LIST ##
    1. Linked List: Introduction & Basic Problems
        #Why Linked List
            issue with array :-  continuous memory allocation
            some time we dont have continuous memory to Allocate
        #linked list
            Non - continuous memory allocation,  linear data Structure
        #Structure
            class node {
                int val;
                Node next;
                public Node(int v){
                    this.val = v;
                    this.next = NULL;
                }
            }     
        # Q. how to access the element at kth index in a linked list
            take a for loop till k 
            do temp = temp.next
            return temp.val
        #  Search in Linked List
        # insertion in linked list in Kth index
            cases
                K = 0
                K = length
                k = random other than 0 and length
        # Deletion in Linked List
            Delete first Occurance of element
            Delete all Occurance of element
        # Reverse the linked list
        # Check the linked list is palindrome or not
        # Questions
            Q1. Print Linked List
            Q2. Insert in Linked List
            Q3. Delete in Linked List
            Q4. Reverse Linked List
            Q5. Palindrome List
            Q1. Remove Nth Node from List End
            Q2. Remove Duplicates from Sorted List
            Q3. Reverse Link List II
            Q4. K reverse linked list
            Q5. Longest Palindromic List
    2. Linked List: Sorting and Detecting Loop
        # Middle of Linked list
        # Merge two Sorted LinkedLists
        # Merge Sort Linked List
        # Check If There is a Loop
        # Find the Start Point of the loop
        # Questions
            Q1. Sort List
            Q2. Merge Two Sorted Lists
            Q3. Remove Loop from Linked List
            Q4. Middle element of linked list
            Q1. Swap List Nodes in pairs
            Q2. Reorder List
            Q3. Add Two Numbers as Lists
    3. Linked List: Problems & Doubly Linked List
        # Doubly Linked List
        # Insertion in Doubly Linked List
        # Deletion in Doubly Linked List
        # L.R.U. (Least Recently Used) Cache
        # Check if the Given Linked list is Palindrome
        # Questions
            Q1. Intersection of Linked Lists
            Q2. LRU Cache
            Q3. Palindrome List
            Q1. Partition List
            Q2. Longest Palindromic List
            Q3. Flatten a linked list
    4. Linked List Extra
## STACKS & QUEUE
    1. Stacks 1: Implementation & Basic Problems
        # What is Stack
            - Last In First Out (LIFO)
            - Stack of plate
            - Stack of books
            - Stack of Functions
            - Undo/Redo
        # Operations in Stack
            - Push(X) // s.push(10);
            - Pop() // s.pop();
            - Top()/ Peak() // s.top();
            - isEmpty() // s.empty();
            - Size // s.size();
            - O(1)
        # Stack Implementation Using Array
            1. use Vector as a stack
            2. Push(value) - add element at the end
            3. isEmpty() - return true if array is empty
            4. pop() - if array is not empty then remove last element
            5. top() - return last element
            6. size() - return size of array
        # Stack Implementation Using Linked List
            1. Initally Use Null Node as Stack - (Name : top)
            2. Push(value) - insert at end of linked list
            3. isEmpty() - return true if Top is Null
            4. pop() - if Top is not Null then remove last node
            5. top() - return last node
            6. size() - return size of linked list
        # Balanced Paranthesis
            1. traverse the string 
            2. if open bracket then push in stack
            3. if close bracket then pop from stack
                if close bracket type is not equal to open bracket type then return false
            4. if stack is not empty then return false
            5. if string is empty and stack is empty then return true
        # Double Character Trouble
            1. traverse the string
            2. if stack is empty or top of stack is not equal to current character then push current character
            3. else pop from stack
            4. after traversing is over
            5. pop each character from stack until stack is empty
            6. reverse the ans and return the ans
        # Evaluate Posfix Expression
            1. traverse the string
            2. if character is digit then push it
            3. if character is operator then pop two elements from stack
                perform operation and push the result
        # Questions
        # Q1. Passing game
            1. Push the Id in Stack
            2. Pop the Id from Stack if current is 0
            3. Return the Id of the player who currently possesses the ball (top of stack)
        # Q2. Balanced Paranthesis
            1. traverse the string 
            2. if open bracket then push in stack
            3. if close bracket then pop from stack
                if close bracket type is not equal to open bracket type then return false
            4. if stack is not empty then return false
            5. if string is empty and stack is empty then return true
        # Q3. Double Character Trouble
            1. traverse the string
            2. if stack is empty or top of stack is not equal to current character then push current character
            3. else pop from stack
            4. after traversing is over
            5. pop each character from stack until stack is empty
            6. reverse the ans and return the ans
        # Q4. Evaluate Expression
            1. traverse the string
            2. if character is digit then push it
            3. if character is operator then pop two elements from stack
                perform operation and push the result
        # Q5. Infix to Postfix
            1. create a operator precedance map
            2. create stack S
            3. traverse the string
            4. if character is digit then push it
            5. if character is operator then pop lower precedance operator from stack and Push current in stack
            6. if character is '(' then push it
            7. if character is ')' then pop until '(' is found
            8. after traversing is over 
            9. pop each operator from stack until stack is empty
        # Q1. Min Stack
            1. Declare the Stack S; and int min_element = INT_MAX;
            2. Push(X) -
                if stack is empty then push the element directly and update min_element as X
                else 
                    if X < min_element then push 2*X - min_element and update min_element as X
                    else push X
            3. pop() - 
                if stack is empty then do nothing
                if (top < min_element) then min_element = 2*min_element - top and then pop
                else pop
            4. top()
                if empty return -1
                if top < min_element then return min_element
                else return top

            5. getmin()
                if empty return -1
                else return min_element
        # Q2. Redundant Braces
        # Q3. Check two bracket expressions
    2. Stacks 2: Nearest Smaller/Greater Element
        # Nearest Smaller Element ON Left
            1. Traverse ON Array Left to Right
            2. Create Stack
            3. if Current element is >= Top of Stack then Pop
            4. if Stack is not empty then ans[i] = -1; else ans[i] = Top
            5. Push Current Element
        # Nearest Smaller or Equal Element ON Left
            1. Traverse ON Array Left to Right
            2. Create Stack
            3. if Current element is > Top of Stack then Pop
            4. if Stack is not empty then ans[i] = -1; else ans[i] = Top
            5. Push Current Element
        # Nearest Greatest Element ON Left
            1. Traverse ON Array Left to Right
            2. Create Stack
            3. if Current element is <= Top of Stack then Pop
            4. if Stack is not empty then ans[i] = -1; else ans[i] = Top
            5. Push Current Element
        # Nearest Greatest or Equal Element ON Left
            1. Traverse ON Array Left to Right
            2. Create Stack
            3. if Current element is < Top of Stack then Pop
            4. if Stack is not empty then ans[i] = -1; else ans[i] = Top
            5. Push Current Element
        # Nearest Smaller Element ON Right
            1. Traverse ON Array Right to Left
            2. Create Stack
            3. if Current element is >= Top of Stack then Pop
            4. if Stack is not empty then ans[i] = -1; else ans[i] = Top
            5. Push Current Element
        # Nearest Smaller or Equal Element ON Right
            1. Traverse ON Array Right to Left
            2. Create Stack
            3. if Current element is > Top of Stack then Pop
            4. if Stack is not empty then ans[i] = -1; else ans[i] = Top
            5. Push Current Element
        # Nearest Greatest Element ON Right
            1. Traverse ON Array Right to Left
            2. Create Stack
            3. if Current element is <= Top of Stack then Pop
            4. if Stack is not empty then ans[i] = -1; else ans[i] = Top
            5. Push Current Element
        # Nearest Greatest or Equal Element ON Right
            1. Traverse ON Array Right to Left
            2. Create Stack
            3. if Current element is < Top of Stack then Pop
            4. if Stack is not empty then ans[i] = -1; else ans[i] = Top
            5. Push Current Element
        # Find Restaurant
            A person uses Google Maps to find the nearest restaurants and picks one  based on it''s proximity. Unfortunately, after visiting, they realised that the restaurant didn''t meet their expectations.
            # Task
            Let''s break it down with a simple example. You have a list of restaurants and their ratings. "For each restaurant, we''re going to find the next restaurant to the right on the list that''s not just close but also has a higher rating than the current one." If  there''s no better option on the list, we''ll say there''s none available
            # Problem
            Given a sequence of restaurants listed on Google Maps with their ratings, create a tool that helps users discover the rating of the next higher-rated restaurant to the right for each listed establishment.

            # Solution
                Nearest Greater on Right
        # Largest Rectangle in Histogram
            - For all Height we can find the max width by using smallest on left and smallest on right
            1. Calculate the smallest on left
            2. Calculate the smallest on right
            3. traverse all the heights
            4. calculate width by R-L-1
            5. calculate the max area by width*height take max and return the max
        # Sum of Min and Max of all Subarray
            - Ans =  Sum( 
                A[i] * [ (i - Nearest_Greater_Left(i)) * (Nearest_Greater_Right(i) -1) ] - [ (i - Nearest_Smallest_Left(i)) * (Nearest_Smallest_Right(i) - i) ] 
            )

            1. Calculate the Nearest_Greater_Left
            2. Calculate the Nearest_Greater_Right
            3. Calculate the Nearest_Smallest_Left
            4. Calculate the Nearest_Smallest_Right
            5. Trverse the array and calculate the diff using above formula and add in Ans
            6. return ans
        # Count Subarray that Ith Element is maximum
            1. Calculate the Nearest_Greater_or_Equal_Left
            2. Calculate the Nearest_Greater_Right
            3. Traver array calculate the contribution for each I using follwing formula
                [ (i - Nearest_Greater_Left(i)) * (Nearest_Greater_Right(i) -1) ] 
        # Solve for Duplicate Values
            1. Calculate the Nearest_Greater_or_Equal_Left
            2. Calculate the Nearest_Greater_Right
            3. Calculate the Nearest_Smallest_or_Equal_Left
            4. Calculate the Nearest_Smallest_Right
            5. Trverse the array and calculate the diff using above formula and add in Ans
            6. return ans
        # Questions
        # Q1. Nearest Smaller Element
        # Q2. Largest Rectangle in Histogram
        # Q3. MAX and MIN
        # Q4. Next Greater
        # Q1. Max Rectangle in Binary Matrix
        # Q2. Sort stack using another stack
    3. Queues: Implementation & Problems
        # What is Queue
            First in First Out
        # Operations in Queue
            Enqueue(x)
            Dequeue()
            front()/rare()
            isEmpty()
            Size()
        # Implementation of Queue Using Array
        # Implementation of Queue Using Linked List
        # Implementation of Queue Using 2 Stacks
        # Perfect Numbers
            Find Nth NO formed using digit 1 & 2

            1. push digit 1 & 2 in queue
            2. Iterate till N
            3. pop fornt of queue ans save in current and push current+1 current+2 in queue
            4. return current
        # Double Ended Queue
            A Double-Ended Queue, or Deque, is a linear data structure that allows insertion and deletion from both ends, unlike a regular queue which operates in a First In, First Out (FIFO) manner with insertion at the back and deletion at the front.
            Operations in Deque
                + Insert at Front: Adds an element at the front.
                + Insert at Back: Adds an element at the back.
                + Delete from Front: Removes an element from the front.
                + Delete from Back: Removes an element from the back.
                + Peek Front/Back: Checks elements at the front/back.
        # Sliding Window Maximum
            1. Initialize an empty deque.
            2. Iterate through the array:
                + Remove out-of-bound indices (indices outside the current window).
                + Remove smaller elements from the deque's back to keep only potentially maximum elements.
                + Add current index to the deque.
                + Record maximum if the window has reached size k (element at deque's front).
            3. Output the recorded maximums.
        # Questions
        # Q1. Queue Using Stacks
        # Q2. Perfect Numbers
        # Q3. Parking Ice Cream Truck
        # Q4. N integers containing only 1, 2 & 3
        # Q1. Reversing Elements Of Queue
        # Q2. Sum of min and max
        # Q3. Unique Letter
    4. Stack & Queue Extra
        # Implement Stack using Array 
            1. Declare an array of particular size.
            2. Define a variable “Top” and initialize it as -1.
            3. push(x): insert element is the array by increasing top by one.
            4. pop(): check whether top is not equal to -1 if it is so, return top and decrease its value by one.
            5. size(): return top+1.  
        # Implement Queue Using Array
            0. The basic approach is to maintain two variables to point to the START and END of the filled elements in the array. START pointer is used to point to the starting index of the elements and the same case for the END pointer(ending index). Initially, both have value -1(indicating empty queue). 
            1. First, let''s see the implementation of the push function. Push basically inserts a new element at the end. So only the END variable is going to be incremented.
                - Corner case 1: What if we have no empty places in the array? So, first check that, if we don''t have we exit, in the other case we increment the START variable and put the new element.
                - Corner case 2: What if END reaches the last index? We are doing mod with addition. So, END goes back to index 0([0-(n-1)] will always be the range for END).
            2. Second, let us see the pop function. In Queue pop removes and returns the front element. So, START needs to be modified. The general approach is to copy the current element pointed by START and increase the START variable to the next index.
                - Corner case 3: What if the Queue is empty? That''s why we are checking the START variable. If it is -1, then the queue is empty, we just exit.
                - Corner case 4: What if START goes out of bound? As done for END, mod addition comes to the rescue.
                - Corner case 5: What happens after popping the last element? We check this state with the currSize variable. Queue returns to the initial state, both START and END are set to -1.
            3. Third, let''s see the top function. It behaves more like a pop function. We need to return the element pointed by the START variable. Since we are not actually removing any element, it''s fine to ignore corner cases 4 and 5.
        # Implement stack using linked list
            We can insert it at the beginning of the linked list using the following steps:
                - Create a node for our new element.
                - Point to the next pointer of our element node to point to the head of the linked list.
                - Make the element node our top node.
                - Increment the size variable.
        # Implement Queue using linked list
            Enqueue: 
                Create a node with a value that is to be Enqueued.
                Make the Rare Pointers next, point to the newly created Node.
                As the newly created Node is inserted at the rear end, this is the last value in Queue.
            Dequeue :
                First create a ListNode pointer temp, and make it point to the Front value of Queue.
                We should delete the Front Value in Queue. So move the Front pointer to the next node after Front Node. That means Front = Front→next 
                Temp is pointing to the previous Front value, temp→next is pointing to the newFront value, as we are interested to delete the temp, Make the temp→next point null.
                We dont require temp anymore, So delete the temp.
            Peek: 
                If Queue is not empty return Front value of Queue.
            Empty: 
                If Front is Null then Queue is empty else not.
            Size: 
                Maintain a variable size, initially set to zero. Upon Enqueue increment size and on Dequeue decrement size.
        # Implement Stack using single Queue
            - Take a single queue.
            - push(x): Push the element in the queue.
            - Use a for loop of size()-1, remove element from queue and again push back to the queue, hence the most recent element becomes the most former element and vice versa.
            - pop(): remove the element from the queue.
            - top(): show the element at the top of the queue.
            - size(): size of the current queue.
            - Repeat step3 at every insertion of the element.
        # Implement Queue using Stack
            Solution 1: Using two Stacks where push operation is O(N)
            Solution 2: Using two Stacks where push operation is O(1)
        # Implement Min Stack
            1. push(int value):
                - Key point: If value < mini, push 2 * value - mini onto the stack to store the transformed value.
                - If the stack is empty, set mini = value.
                - If value >= mini, simply push the value onto the stack.
            2. pop():
                - Key point: If the popped element is less than mini (i.e., a transformed value), adjust mini by the formula:
                - mini = 2 * mini - popped value.
                - Otherwise, just pop the element without modifying mini.
            3. top():
                - Key point: If the top element is a transformed value (less than mini), return the current mini instead.
                - Otherwise, return the top value itself.
            4. getMin():
                - Returns the current minimum value (mini).
        # Infix to Postfix
            1. Check if it is a Operand (A-Z,a-z,0-9)
                directly add in Result
            2. Check if it is a "("
                push in to the stack
            3. Check it its is ")"
                pop and add into the ans untill "(" is not found or stack is not empty
                pop "("
            4. Else (Check if it is Operator)
                pop all greatter precedance operator from stack and add into the ans
                push current in stack
            5.  Pop all the remaining elements from the stack
        # Infix to Prefix
            1. Reverse the given Infix Exp and after that replace the ")" -> "(" and "(" -> ")"
            2. Convert Infix to Psotfix -> ans
            3. Reverse the Ans and return the Ans
        # Postfix to Infix
            1. if Operand directly Push
            2. if Operator get Last Two Operand 
                Push ( "(" + T2 + Operator + T1 + ")")
        # Postfix to Prefix
            0. Treverse the R -> L
            1. if Operand directly Push
            2. if Operator get Last Two Operand
                Push ( Operator + T1 + T2)
        # Prefix to Infix
            1. Traverse Given Prefix Exp R->L
            2. if Operand Directly Push
            3. if Operator get Last Two Operand
                Push( "(" + T1 + Operator + T2 + ")")
        # Prefix to Postfix
            0. Treverse the R -> L
            1. if Operand directly Push
            2. if Operator get Last Two Operand
                Push( T1 + T2 + Operator)
        # Next Greater Element
            -  Intution from A[i] Height of Light Poles
            1. Travers from R -> L
            2. if top > A[i]
                    ans[i] =  top
                    push(A[i])
            else 
                    pop untill top <= A[i]
                    ans[i] = top
                    push(A[i])
        # Next Greater Element 2
            See Circularly 
            Use circular Traversal til that element
            update the Ans only if (i < N)
            1. Traverse L->R from 2N-1 -> 0
            2. if top > A[i]
                    if (i < N)
                        ans[i] =  top
                    push(A[i])
            else 
                    pop untill top <= A[i]
                    if (i < N)
                        ans[i] = top
                    push(A[i])
        # Next Smaller Element
            1. Travers from L -> R
            2. if top < A[i]
                    ans[i] =  top
                    push(A[i])
            else 
                    pop untill top >= A[i]
                    ans[i] = top
                    push(A[i])
        # Trapping Rainwater
            Find Left_max and Right max 
            traverse to array L->R
                for each element 
                    Total += min(Left_max, Right_max) - A[i]
            
            // approach 1
                Lmax and Rmax can be found using Prefix sum teq.
                Lmax will be the Prefix sum is max of element from left to right
                Rmax will be the Prefix sum is max of element from Right to Left
            // Approach 2
                We can use the Two pointers apporach
                1. Initialize Variables:
                    - left pointer starting at index 0.
                    - right pointer starting at index n - 1 (end of array).
                    - maxLeft and maxRight to track the maximum height on the left and right, initialized to 0.
                    - res to store the result (total trapped water), initialized to 0.
                2. While left <= right:
                    - if height[left] <= height[right]:
                        + If height[left] is greater than or equal to maxLeft, update maxLeft to height[left].
                        + Else, add maxLeft - height[left] to res (water trapped at this position).
                        + Increment left.
                    - Else (if height[left] > height[right]):
                        + If height[right] is greater than or equal to maxRight, update maxRight to height[right].
                        + Else, add maxRight - height[right] to res (water trapped at this position).
                        + Decrement right.
                3. Return res.
                    The total water trapped.
        # Sum of subarray minimum
            # Sollution 1
                - generate all subarray and take sum of min using carray forward teq.
            # Sollution 2
                - get next smaller element
                - get previous smaller and equal element 
                - using that calculate the contribution of each element and add in total
        # Sum of subarray ranges (Sum of diff of min and max of for all subarray)
            1. min_sum = find sum of minimum for eahc subarray
                - get next smaller element
                - get previous smaller and equal element 
                - using that calculate the contribution of each element and add in total
            2. max_sum = find sum of maximum for each subarray
                - get next grater element
                - get previous grater and equal element 
                - using that calculate the contribution of each element and add in total
            3. return max_sum - min_sum
        # Asteroid Collision
            use Stack to check Collision
            1. Traverse the Array L->R
            2. Process collision
                Take distroid flag as false
                unitll stack is not empty and top is posivtive and current asteroid is negative
                Stacks top asteroid is smaller, top gets destroyed
                Stacks top asteroid is same, both gets destroyed
                    distriod = true
                    break
    
            3. if distroid flag is false
                push current asteroid
            4. after Traverse Array
                pop all stack element untill stack is empty and store in ans array
            5. reverse ans array and return ans array
        # Largest rectangle in a histogram
            - Traverse the L->R
            - we can calcualte the widht for each height (A[i])
                height = A[i]
                widht =  next_small_element - privious_small_element - 1
            - Calculate the area = height * width
            - Find max area
            - Return the max area

            1. We traverse through each bar in the histogram and use a stack to keep track of bar indices in ascending order of their heights.
            2. If we encounter a bar that is shorter than the bar represented by the index at the top of the stack, we pop elements from the stack until the current bar is taller.
            3. For every popped element, we calculate the possible rectangle area with the popped bar's height as the smallest (or limiting) height.
            4. The width of the rectangle is determined by the difference between the indices of the current bar and the bar at the new top of the stack, minus one.
        # Maximal Rectangles
            -  we can Determine the Height of each column for each row so can Treat the Every row as a histogram and find the largest Rectangle in Histogram
            1. Traverse the Matrix the top to bottom (Columnwise)
            2. initialize col_height=0 for each columnwise iteration 
                if value is 1
                    increament the col_height 
                    mark current height = current_height
                else 
                    col_height = 0;
                    current height = 0
            3. traverse the each row and find the largest Rectangle in Histogram
            4. return Max of each row 
        # Remove k Digits
            -  Keep Smaller Digits at Start
            1. Traverse the Array L->R
            2. Pop untill top > A[i]
            3. push current element in stack
            4. after traversal pop all stack element untill stack is empty
            5. reverse the ans and return in ans
            6. Edge Case:
                + if K == N return 0
                    because we have to remove all digits
                + N = "00123" then remove tralling zeros
                    N = "123"
                + K not removed in trversal 
                    if N == "123" and K = 2
                    then remove the K digit for last 
                    ans = "1" removed = "23"
        # Stock span problem
            Maximum "Consecutive" days for which the Stock price was less than or equal to current days.
            we can use the privious Grater element to check last day the stock price was less than or equal to current day

            1. Traverse the Array L->R
            2. pop untill top < A[i]
            3. span[i] = i - top
            4. push(i)
            5. reutrn the span array
        # Sliding Window maximum
            1. We maintain a deque that stores indices of array elements, ensuring the elements are in decreasing order.
            2. The deque''s front will always have the index of the maximum element for the current window.
            3. As we slide the window, we:
                - Remove elements from the back that are smaller than the current element (since they will never be needed again).
                - Remove elements from the front that are no longer within the current window.
        # The Celebrity Problem
            // Solution 1 (N*M)
                1. use the two N size Array    
                    know_me
                    i_know
                2. Traverse the each element in matrix and update the Arrays as per
                    M[r][c] == 1
                        i_know[r]++
                        know_me[c]++
                3. traverse the 0 -> N-1
                    if (know_me[i] == N-1 && i_know[i]==0){
                        return i
                    }
            // Solution 2 (N) (1)
                we are using the two pointer top = 0 and bottom = n-1
                1. if is top knwos the Bottom
                    if yes top ++
                2. if is Bottom knows the top   
                    if yes bottom --
                3. do it untill the top < bottom
                4. last is Celebrity or not
        # LRU cache (IMPORTANT)
            - we are using the doubly Linked List and Map
            1. Lru(size){
                Capacity = size
                map.clear()
                head->next = null
                talt->next = null
            }
            2. get(key){
                if(! map.containsKey(key)){
                    return -1
                }
                node temp = map[key]
                delete(temp)
                insertAtHead(temp)
                return temp->value
            }
            3. put(key, value){
                if(map.containsKey(key)){
                    node temp = map[key]
                    temp->value = value
                    delete(temp)
                    insertAtHead(temp)
                }else{
                    if(map.size == Capacity){
                        node temp = tail->prev
                        map.erase(temp->key)
                        delete(temp)
                    }

                    node temp = new node(key, value)
                    insertAtHead(temp)
                    map[key] = temp
                }
            }
            4. insertAtHead(temp){
                temp->next = head->next
                head->next->prev = temp
                head->next = temp
                temp->prev = head
            }
            5. delete(temp){
                temp->prev->next = temp->next
                temp->next->prev = temp->prev
                temp->next = null
                temp->prev = null
            }
        # LFU cache
            get(key){
                if present{
                    increment the frequency
                    update the frequency list
                    return value
                }else{
                    return -1
                } 
            }
            put(key, value){
                if (present){
                    update the value
                    increment the frequency
                    update the frequency list
                }else{
                    if (cache is full){
                        Delete_LFU()
                    }
                    create new node
                    insert the node
                    increment the frequency
                    update the frequency list
                }
            }
            delete_LFU(){
                delete the least frequency node
                if multiple then delete the least recently used
            }
            class LFUCache {
                public:
                    int Capacity, minFreq;
                    unordered_map<int, Node*> map;  // Store key to Node mapping
                    unordered_map<int, DoublyLinkedList> freqList;  // Store nodes by frequency
                    LFUCache(int size) {
                        Capacity = size;
                        minFreq = 0;
                        map.clear();
                        freqList.clear();
                    }
                    int get(int key) {
                        if (! map.containsKey(key)) {
                            return -1;  // Key not found
                        }
                        Node* temp = map[key];
                        updateFrequency(temp);
                        return temp->value;
                    }

                    void put(int key, int value) {
                        if (Capacity == 0) return;
                        
                        if(map.containsKey(key)){
                            Node* temp = map[key];
                            temp->value = value;
                            updateFrequency(temp);
                        } else {
                            if (map.size == Capacity) {
                                Delete_LFU();
                            }
                            Node* temp = new Node(key, value);
                            map[key] = temp;
                            updateFrequency(temp);
                        }
                    }

                private:
                    void updateFrequency(Node* node) {
                        int freq = node->frequency;
                        freqList[freq].remove(node);

                        if (freqList[freq].isEmpty()) {
                            if (minFreq == freq) {
                                minFreq++;
                            }
                        }

                        node->frequency++;
                        freqList[node->frequency].insert(node);

                        if (minFreq > node->frequency) {
                            minFreq = node->frequency;
                        }
                    }

                    void Delete_LFU() {
                        Node* LFU_ele = freqList[minFreq].removeLast();
                        map.erase(LFU_ele->key);
                    }
            };
## Trees ## 
    1. Trees 1: Structure & Traversal
        # What is Tree
            Hirarchical Data Structure
            Root
            Leaves
            Node
            edge
            parrent-Child
            Siblings
        # Height of Node
            Count of edges (distance) to travel form current  node to farthest leaf
        # Depth or Level of Node
            Count of Edges  (distance) form Root to current Node
        # Subtree of a Node X
            All the Node we can Travel from Node X to farthest leaf
        # Binary Tree
            Max child will be 2
            left subtree (left child)
            Right Subtree (right child)
        # Structure of Binary Tree
            class TreeNode{
                int val;
                TreeNode left, right;
            }
        # Types of Traversals        
            Preorder Traversal
                N L R
                Recursive 
                    PRINT(N)
                    F(N->L)
                    F(N->R)
                Iterative
                    push root
                    while stack is not empty
                        pop N
                        print N
                        push(N->R)
                        push(N->L)
            Inorder Traversal
                L N R
                Recursive
                    F(N->L)
                    print(N)
                    F(N->R)
                Iterative
                    while(curr!=null && stack not empty){
                        # push all left node of Currnet
                        while(curr!=null){
                            push(Curr->L)
                            curr = curr->L
                        }

                        # print leftmost node
                        print L
                        curr = curr->R
                    }
            Postorder Traversal
                L R N
                Recursive
                    F(N->L)
                    F(N->R)
                    print(N)
                Iterative
                    st1 st2
                    st1.push(root)
                    while(st1 != empty()){
                        N = st1.pop()
                        st2.push(N)
                        st1.push(N->left)
                        st1.push(N->right)
                    }
        # Build a binary tree From Preorder and Inorder
            1. Pick element from preorder and create a node
            2. increament preorder index
            3. Search element position in inorder
                for searching position we can create the {A[i] -> i} Map
            4. call to build left subtree from inorder 0 to position -1
            5. call to build Right subtree from inorder position +1 to N -1
            6. Return the root
        # Build a binary tree From Postorder and Inorder
            1. Pick the current root from the last element of the postorder traversal.
            2. Decrement the postorder index.
            3. Search for the root in the inorder traversal. This splits the inorder traversal into left and right subtrees:
                Left subtree: elements before the root''s position in inorder.
                Right subtree: elements after the root''s position in inorder.
            4. Recursively build the right subtree first (because the next root in postorder is for the right subtree).
            5. Recursively build the left subtree.
            6. Return the root node.
        # Q1. Preorder Traversal
        # Q2. Inorder Traversal
        # Q3. Binary Tree From Inorder And Postorder
        # Q1. Postorder Traversal
        # Q2. Binary Tree From Inorder And Preorder
    2. Trees 2: Views & Types
        # Level Order Traversal
            Level wise Traversal
                Left to Right Level order traversal
                Right to Left Level order traversal
                top to bottom -> left to right
            1. Initialize a queue and enqueue the root node.
            2. While the queue is not empty:
                - Dequeue the front node, process it (e.g., add its value to the result).
                - Enqueue its left child (if it exists).
                - Enqueue its right child (if it exists).
            3. Repeat until all nodes are processed.
        # Right View of Binary tree
            Last Node of each level
        # Left View of Binary tree
            First Node of each level
        # Vertical Order traversal of binary tree
            how to caluculate the distance hashmap using laverl order traversal
                use 1 to N vector to store parrent node distance
            use this distance hashmap to print the vertical order traversal
            analyze the space complexity of this approach

            1. Caluclate the distance map of each node from root
                - use level order traversal
                - using Queue of pair of <node, distance>
                push {root,0}
                do Level order Traversal
                    pop {node,dist}
                    map[dist] = push_back(node)
                    queue.push({node->left, dist-1})
                    queue.push({node->right, dist+1})
            2. use this distance map to print the vertical order traversal
                iterate the Map and print the Verical level nodes
        # Top View of Binary tree
            first element of each distance hashmap
        # Bottom view of binary tree
            do not store in the distance hashmap instead just maintain one node for all update with latest node       
        # Types of Binary tree
            -- Proper / Full Binary Tree
                Every Node has Either 0  or 2 children
            -- Complete Binary Tree
                All levels are completely filled Except Possibly last level and the last level is filled from left to right
            -- Perfect Binary Tree
                All levels are completely filled
        # Height of Perfect Binary Tree of N nodes will be 
            LOG(N)
        # Balance Binary Tree
            (The Absolute difference of height of left and right subtree is) <= 1   
            need to check for every node     
        # Height of Binary Tree
            F(N){
                if(N==NULL){
                    return -1;
                }
                L= F(N->L)
                R = F(N->R)
                return 1 + max(L, R)
            }
        # Questions
            Q1. Level Order
            Q2. Right View of Binary tree
            Q3. Vertical Order traversal
            Q4. Balanced Binary Tree
            Q1. ZigZag Level Order Traversal BT
            Q2. Serialize Binary Tree
            Q3. Deserialize Binary Tree
            Q4. Top View of Binary tree
    3. Trees 3: BST
        #What is BST
            A Binary Search Tree (BST) is a binary tree that follows these properties:
            1. Node Structure: Each node has a key (or value) and pointers to left and right children.
            2. Ordering Property:
                For any node, all values in its left subtree are smaller, and all values in its right subtree are larger
            3. Operations: 
                Insert: Add a node, maintaining the ordering property.
                Search: Find a node with a specific value, generally taking O(logn) time.
                Delete: Remove a node while restructuring to preserve BST properties.
            4. Traversal:
                Inorder Traversal provides values in ascending order.
        # Search in BST
            N = Root
            while(N!=NUll){
                if N == Target then return N
                if N > Target then N = N.left
                else N = N.right  # N < Target
            }
            return NULL  # NOT Found 
        # Insertion in BST
            1. Check if K is Smaller than root
                Go to Leaf of Left Subtree
            2. Check if K is greater than root
                Go to Leaf of Right Subtree
            3. Insert K as Leaf
        # find minimum and maximum value in BST
            Find Min 
                1. Start from root
                2. Go Left until Current.left != Null
                3. Return Current
            Find Max
                1. Start from root
                2. Go Right until Current.right != Null
                3. Return Current
        # Deletion in BST
            Leaf Node
                Direct Delete
                1. Traverse till Parrent of K
                2. Parrent.child = NULL
            Single Child Node
                Conect Child to Grand Parent or Node's Parent
                1. Travel Till Parrent of K
                2. parrent.child = K.child
            Two Child Node
                1. Relace the Node with Gratest element in Left Subtree
                    Inorder Predessor
                                OR
                2. Relace the Node with Smallest element in Right Subtree
                    Inorder Successor

                + some time Greatest/Smallest has a child

                1. Travel till Node K
                2. max_ele = Find the Largest in Left Subtree
                3. Delete max_ele
                4. Replace K with max_ele
        # Red Black Tree
        # AVL tree
        # Construct BST from Sorted Array
            - Sorted array is Always the INORDER TRAVERSAL OF A BST
            LNR
            1. mid = Find the middle element of the array
            2. Create a root node as N = node(A[mid])
            3. for left subtree is all element before mid in Array
                N->L = Construct(A, start, mid-1)
            4. for right subtree is all element after mid in Array
                N->R = Construct(A, mid+1, end)
            5. retufn N
        # Counstruct Bst from Unsorted Array
            - Add all element ONE-BY-ONE
            + To construct a Binary Search Tree (BST) from an unsorted array, you can insert each element of the array into the BST one by one. The BST property ensures that for any given node:
                1. All values in the left subtree are smaller than the node's value.
                2. All values in the right subtree are greater than the node's value.
        # Check if a Binary Tree is BST or not
            // Solution 1
                1. Do INORDER TRAVERSAL of Tree
                    it suppose to give the sorted array
                2. Traverse the given Inorder Traversal Array
                    check if it is a sorted or not
                        if yes then it is a BST
                        else it is not a BST
            // Solution 2
                1. The left subtree of a node must contain only nodes with values less than the node's value.
                2. The right subtree of a node must contain only nodes with values greater than the node's value.
                3. Both the left and right subtrees must also be binary search trees.
        # Questions
            Q1. Search in BST
            Q2. Delete a node in BST
            Q3. Sorted Array To Balanced BST
            Q4. Valid Binary Search Tree
            Q1. Check for BST with One Child
            Q2. BST nodes in a range
            Q3. Two Sum BST
    4. Trees 4: LCA + Morris Inorder Traversal
        # Find K th Smallest Element in BST 
            Using Inorder Traversal till K element
        # Morris Inorder Traversal
            - Threaded Binary Tree
            # Node does not have the left subtree
            1. current->left == Null
                Print(current)
                current= current->right
            # Node has a Left subtree
                # Create a Thread to [Rightmost Node of Left Subtree] -> Right  = Node  
            2. else
                Find the [Rightmost Node of Left Subtree] as T
                    if T has is Null then Create  a Thread
                    else (Thread is allready present) 
                        set to Go right
                        delete Thread
                if(T.right == Null)
                    Make connection (thread) 
                        RightMost.right = current
                        current = current->left
                else // RightMost.right == current
                    print(current)
                    RightMost.right = Null  // reset the connection (thread)
                    current = current->right               
        # Morris Preordrer Traversal
            - Same as the Morris Inorder Traversal
            while creating the Thread 
                print the current node 
                create the thread 
            rest all process is same
             1. current->left == Null
                Print(current)
                current= current->right
            2. else
                find the rightmost node of current left subtree (RightMost)
                    i.e. RightMOst = find the rightmost node in current->left
                 
                if(RightMost.right == Null)
                    print(current)
                    Make connection (thread) 
                        RightMost.right = current
                        current = current->left
                else // RightMost.right == current
                    RightMost.right = Null  // reset the connection (thread)
                    current = current->right
        # Path From Root To Node
            1. Recursive Traversal: Traverse the tree from the root.
            2. Check for Target Node:
                - If the current node is the target, add it to the path and return true.
                - Recursively check the left and right subtrees.
            3. Backtracking:
                - If the target node is found in either subtree, add the current node to the path and return true.
                - If neither subtree contains the target, remove the current node from the path (backtrack) and return false.
        # Lowest Common Ancestor
            // Solution 1 
                1. Take the Path from root to Node for Both Nodes
                2. Compare the path of Both Nodes
                3. Return the Last common Node
            // Solution 2
                1. Using the Recursive Traversals
                2. First travese in Left and then Right
                3. if the any Node found Return Node 
                4. else return null
                5. if both Node not found return null
                6. else if Both node found then return current node
        # LCA in BST
            1. if both node present at left subtree
                Go to Current->left
            2. if both node present at right subtree
                Go to Current->right
            3. if one node is present at left subtree and other at right subtree
                return current
            4. else return null
        # Questions
            Q1. Least Common Ancestor
            Q2. Kth Smallest Element In BST
            Q3. LCA in BST
            Q4. Morris Inorder Traversal
            Q1. Recover Binary Search Tree
            Q2. Common Nodes in Two BST
            Q3. Distance between Nodes of BST
    5. Trees 5: Problems on Trees
        # Invert The Binary Tree
        # Equal Tree Partition
        # Next Pointer to Binary Tree
        # Check if Root to Leaf path sum is equal to K
        # Diameter in Binary Tree
        # Questions
            Q1. Next Pointer Binary Tree
            Q2. Diameter of binary tree
            Q3. Path Sum
            Q4. Invert the Binary Tree
            Q1. Identical Binary Trees
            Q2. Invert the Binary Tree
    6. Trees Extra
        # Maximum Depth of Binary Tree
            1 + Max(height(current->left), height(current->right))
        # check for Balanced Binary Tree
            // solution 1
            What is Balanced Binary Tree
                if (abs(height(current->left) - height(current->right)) <= 1)
                    return true
                else
                    return false

            // solution 2
            if(depth(current->left) == -1 || depth(current->right) == -1)
                return -1
            if (abs(depth(current->left) - depth(current->right)) > 1)
                return -1
            else
                return 1 + max(depth(current->left), depth(current->right))
        # Diameter of Binary Tree
            - The diameter of a binary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root
            1. diameter of current through current node is [LH + RH]
            2. caluculate the diameter for every node and take max
            3. return the Max as diameter
        # Maximum Path Sum
            - Find the Maximum Possible path in Binary tree
            - Path for Current node is
                Left_Path + Right_Path + Current Node
            - Take Max of all paths
        # Check if Two Binary Trees are Identical Or Not
            Use Single Traversal on Both Trees and check both node are identical or not 
        # Zig - Zag or Spiral Traversal 
            // solution 1
                Just like Level order Traversal just change is pushing into the queue is depend on flag whether it is right to left OR Left to Right
            1. Initialize a queue and enqueue the root node.
            2. Use a flag (boolean variable) to keep track of the current traversal direction:
                If true, traverse from left to right.
                If false, traverse from right to left.
            3. For each level:
                Determine the number of nodes at that level.
                Use a temporary container (like a vector) to store nodes'' values.
                Based on the flag, either append values to the end (left-to-right) or the beginning (right-to-left).
            4. Toggle the flag after processing each level to switch the direction.
            5. Repeat until all nodes are processed.
        # Boundry Traversal of Binary Tree
            1. Print Left Boundry Excluding Leaf (Left Boundry)
            2. Print All Leaf Nodes (Bottom Boundry)
            3. Print Right Boundry Excluding Leaf in Reverse Order (Right Boundry)

            1. Add the root node to the result.
            2. Traverse the left boundary:
                Start from the root''s left child.
                Move downwards, adding each node''s value to the result until reaching a leaf node.
                Do not add the leaf nodes in this step.

            3. Traverse all leaf nodes:
                    Collect all leaf nodes in left-to-right order.
                    This includes leaf nodes from both left and right subtrees.
            4. Traverse the right boundary in reverse:
                Start from the root's right child.
                Move downwards, collecting each node's value in a temporary container until reaching a leaf node.
                Do not add the leaf nodes in this step.
                Finally, add the collected nodes in reverse order to the result
        # Check For Symmetrical Binary Tree
            Use Modified Preorder Traversal
                (left subtree) N L R  == N R L (Right Subtree)
            1. Define a recursive function that compares two nodes:
                - If both nodes are nullptr, they are symmetric.
                - If one of the nodes is nullptr and the other is not, they are not symmetric.
                - If the values of the two nodes are the same, recursively check:
                    - The left subtree of the left node with the right subtree of the right node.
                    - The right subtree of the left node with the left subtree of the right node.
            2. Start the comparison from the root's left and right children.
        # Maximum Widht of Binary Tree
            - The maximum width of a binary tree is defined as the maximum number of nodes present at any level of the tree. We can calculate this efficiently by using a "level-order traversal" (BFS) approach, where we keep track of the positions of nodes within each level. The width of each level is then the difference between the maximum and minimum positions of the nodes on that level, plus one.
            Left index  = 2*i + 1
            Right index  = 2*i + 2

            1. Use a queue to perform a level-order traversal, where each entry in the queue is a pair containing a node and its position within the level.
            2. For each level, record the first and last positions of nodes in the queue.
            3. The width of the level is calculated as last_position - first_position + 1.
            4. Track the maximum width across all levels.
        # Check Children Sum Property
            - The Children Sum Property in a binary tree requires that the value of each node should be equal to the sum of the values of its children. This property applies only to non-leaf nodes (i.e., nodes that have at least one child). If a node does not have children, it automatically satisfies this property.
            1. For each node:
                - Check if it is a leaf node; if so, return true.
                - Compute the sum of the values of its left and right children.
                - Check if the current node's value matches this sum.
            2. Recursively check the left and right subtrees.
            3. If all nodes satisfy the property, return true; otherwise, return false.
        # Make Children Sum Propert Binary Tree
            1. Base Check: If the node is NULL, return.
            2. Calculate Children Sum: Add the values of the left and right children.
            3. Adjust Current Node:
                - If children sum is greater than or equal to the current node's value, update the current node to this sum.
                - If the current node's value is higher, set its value to one of the children (left or right).
            4. Recurse: Apply these steps recursively to left and right children.
            5. Post-recursion Update: After recursive calls, set the current node's value to the new sum of its children (if it has any).
        # Print all Node at Distance K from a Node in all Direction 
            1. To Track the Parrent for upward search Use Level Order Traversal Crate a "Node and Parrent Map"
            2. find the Node 
            3. Then Using Queue and Visited node Set do the tree traversal till distance K in all three direction
                - Left
                - Right
                - Parrent
        # Minimum Time Taken to Burn the Binary Tree
            1. DFS Function: The dfs function builds a mapping of each node to its parent.
            2. BFS Function: The minTimeToBurnTree function performs BFS to simulate the fire spreading:
                - It starts from the target node and spreads to its left and right children and to its parent.
                - We keep track of visited nodes to avoid cycles and count the time taken to burn all nodes.
            3. Return Time: Finally, the function returns the total time taken to burn the entire tree.
        # Count total Node in Complete Binary Tree 
            // Solution 1 (O(N))
                Use Inorder traversal to count the number of nodes
            //  Solution 2 (O(log(N)))
                1. Height Functions: The functions findHeightLeft and findHeightRight calculate the heights of the leftmost and rightmost paths, respectively. This is important because, in a complete binary tree:
                    - If both heights are equal, the tree is full, and the number of nodes can be calculated using the formula 
                        + [ 2^height - 1 ]
                2. Recursive Counting: If the tree is not full, the function recursively counts the nodes in the left and right subtrees.
        # Serialize and Deserialize Binary Tree
            To serialize and deserialize a binary tree using level-order traversal (also known as breadth-first traversal), we can follow these steps:
            Serialization
                - Level-Order Traversal: Traverse the tree level by level, starting from the root. Use a queue to facilitate this process.
                - Storing Values: For each node, store its value in a list. If a node is null, store a placeholder (like "null") to indicate its absence.
                - Join Values: Finally, convert the list into a string by joining the values with a delimiter (e.g., comma).
            Deserialization
                - Split the String: Split the serialized string using the same delimiter to get the list of values.
                - Reconstruct the Tree: Use a queue to create nodes in level order, replacing placeholders with null as appropriate.
        # Flatten a Binary Tree to Linked List 
            # Solution 1 [Recursive] T(N) S(N) 
                1. Use a helper function to perform the post-order traversal.
                2. Maintain a pointer to the previous node that will be modified during the traversal.
                3. On visiting each node:
                    - Set the right child to the previous node.
                    - Set the left child to nullptr.
                    - Update the previous node to the current node
            # Solution 2 [Iterative] T(N) S(N)
            1. Use a stack to simulate the depth-first traversal of the tree.
            2. Start from the root node and push it onto the stack.
            3. While the stack is not empty, pop the top node from the stack:
                - Push the right child of the current node onto the stack (if it exists).
                - Push the left child of the current node onto the stack (if it exists).
                - Set the right child of the current node to the top of the stack (which represents the next node to be processed).
                - Set the left child to nullptr

            # Solution 3 [Morris Traversal] T(N) S(1)
                1. Start at the root and iterate through the tree.
                2. If the current node has a left child:
                    Find the rightmost node of the left subtree.
                    Make its right pointer point to the current node.
                    Move the current node to its left child.
                3. If there''s no left child, we:
                    Record the current node as the right child of the previous node.
                    Move to the right child.
                4. Continue until all nodes are processed.
        # Ceil and Floor in BST
            Ceil:
                Start from the root.
                If the root''s value is equal to the key, the ceil is the key itself.
                If the root''s value is greater than the key, the ceil could either be the root or in the left subtree. We''ll explore the left subtree to find a smaller valid value.
                If the root''s value is less than the key, then the ceil must be in the right subtree.
            Floor:
                Start from the root.
                If the root''s value is equal to the key, the floor is the key itself.
                If the root''s value is less than the key, the floor could either be the root or in the right subtree. We''ll explore the right subtree to find a larger valid value.
                If the root''s value is greater than the key, the floor must be in the left subtree.
        # Check if a Tree is a BST or BT
            1. In-Order Traversal Approach:
                1.1 Perform an in-order traversal (left, root, right) of the tree.
                1.2 Check that the sequence of node values is strictly increasing.
            2. Recursive Range Approach:
                2.1 Use the property that each node's value must fall within a specific range for the tree to be a BST.
                2.2 For each node, recursively check that its value lies between a specified min and max.
                2.3 For the left subtree, update the max to the current node's value, and for the right subtree, update the min to the current node's value.
        # Construct a BST from a preorder traversa
            1. The first element in the preorder traversal array is the root of the BST.
            2. Recursively, we can split the rest of the array into left and right subtrees by using an upper bound:
                - All elements less than the root form the left subtree.
                - All elements greater than the root form the right subtree.
            3. Use this upper bound property to keep track of where each node should be placed, avoiding additional splits in the array.
        # Inorder Successor/Predecessor in BST
            Inorder Successor
                1. If the node has a right child:
                    - The inorder successor is the leftmost node in the right subtree of the given node.
                    - Traverse to the right child, then keep moving left until you reach a node that has no left child.
                2. If the node does not have a right child:
                    - Start from the root and traverse the tree. Keep track of the last node you encountered that is greater than the given node. This node will be the inorder successor.
            Inorder Predecessor
                1. If the node has a left child:
                    - The inorder predecessor is the rightmost node in the left subtree of the given node.
                    - Traverse to the left child, then keep moving right until you reach a node that has no right child.
                2. If the node does not have a left child:
                    - Start from the root and traverse the tree. Keep track of the last node you encountered that is less than the given node. This node will be the inorder predecessor.
        # Binary Search Tree Iterator
            - A Binary Search Tree (BST) Iterator allows us to traverse a BST in sorted order with efficient next() and hasNext() operations. Here's a typical way to implement a BST Iterator in C++ using an inorder traversal (left -> node -> right), which naturally provides elements in ascending order for a BST.
            To implement a BST Iterator, we can use a stack to simulate the inorder traversal:
                1. Use the stack to keep track of nodes as you traverse down the left subtree.
                2. For each call to next(), pop the top of the stack (the current smallest element), process it, and then push all left nodes from its right subtree to the stack.
                3. hasNext() simply checks if there are any elements left in the stack.
        # Two Sum In BST
            Approach 1: Inorder Traversal + Two-Pointer Technique
                1. Perform an inorder traversal on the BST to get a sorted list of values. In a BST, inorder traversal gives elements in ascending order.
                2. Use the two-pointer technique on the sorted list:
                    - Initialize one pointer at the beginning (left) and another at the end (right).
                    - If the sum of elements at left and right equals the target, return true.
                    - If the sum is less than the target, increment left to increase the sum.
                    - If the sum is greater than the target, decrement right to decrease the sum.
                3. If no such pair is found by the time the pointers cross, return false.
            Approach 2: Using a Hash Set
                Alternatively, we can use a hash set to store values we have seen so far and check if target - node->val exists in the set as we traverse the BST.
        # Recover BST | Correct BST with two nodes swapped
            1. Perform an inorder traversal and find the two nodes where the order is incorrect.
                The first incorrect node (first) is where we find the first drop in order.
                The second incorrect node (second) is found at the next drop in order.
            2. After identifying these nodes, swap their values to restore the BST.
        # Largest BST in Binary Tree
            1. Define a helper structure for each node to store:
                The size of the largest BST subtree rooted at that node.
                The minimum and maximum values in the subtree.
                Whether the subtree rooted at that node is a BST.
            2. Recursive Function:
                For each node, recursively compute the information for its left and right children.
                Check if the current node, along with its left and right children, forms a BST:
                    The left subtree must be a BST, and all values in it must be less than the current node's value.
                    The right subtree must be a BST, and all values in it must be greater than the current node's value.
                If the subtree rooted at the current node is a valid BST, update the size of the largest BST subtree found so far.
                If not, return the maximum size of the largest BST subtree in either the left or right subtree.
######################
## UNIT 4 ##
######################     
## Heaps ##
    1. Heaps 1: Introduction
        # Why Heaps
            1. Efficient for Priority Queues
            2. Optimal for Heap Sort
            3. Dynamic Min/Max Lookup
            4. Efficient for Merging
                + In algorithms like merge k sorted lists or merge k sorted arrays
            5. Memory Efficient
                + A heap is implemented as an array, which makes it memory efficient compared to other tree-based structures like binary search trees.
            6. Applications in Real-World Problems
                + Dijkstra''s Algorithm: Heaps efficiently find the shortest path in graphs by managing the set of unvisited nodes.
                + Median Finder: Heaps are used in finding the median of a data stream.
                + Minimum Spanning Tree (Prim''s Algorithm): Manages the priority of edges while growing the spanning tree.
            7. Connecting Roap Problem
                need to find the Smallest after each iteration
        # What is a Heap?
            1. Complete binary Tree
            2. Follow Heap Order Property
        # Types of Heap (Insertion & Extaction O(logn))
            Max-Heap
            Min-Heap
        # Visualise Array as Binary Tree
            For All Node I
                Left Child = i * 2 + 1
                Right Child = i * 2 + 2
                Parrent = (i-1) / 2
        # Operations on a Heap:
            Insert - O(logN) - push(N)
            Delete/Extract - O(logN) - pop()
            Heapify - O(log N)
            top() - O(1)
        # Heap Representation:
            The left child is at index :- (2i + 1)
            The right  child is at index :- (2i + 2)
            The parent is at index :- ((i - 1) / 2)
        # Heapify
            1. Bottom Up Heapify
                - Also called Sift-Up or Percolate-Up.
                - Used when a new element is inserted into the heap, initially placed at the bottom (last position in the array representation).
                - Fixes the heap property by comparing the inserted element with its parent and moving it upwards if it violates the heap property.
                - Steps : 
                    1.1. Start at the position of the newly added element.(N-1)
                    1.2. Compare it with its parent:
                        + In a max-heap, if the current node is greater than its parent, swap them.
                        + In a min-heap, if the current node is smaller than its parent, swap them.
                    1.3 Repeat the process until:
                        + The current node is at the root, or
                        + The heap property is satisfied.
            2. Top Down Heapify
                - Also called Sift-Down or Percolate-Down.
                - Used when the root of the heap is replaced (e.g., during deletion of the max/min element in a priority queue).
                - Fixes the heap property by comparing the root with its children and moving it downward if it violates the heap property.
                - Steps : 
                    2.1. Start at the root of the heap.
                    2.2. Compare the root with its children:
                            + In a max-heap, swap it with the larger child if it''s smaller than the child.
                            + In a min-heap, swap it with the smaller child if it''s larger than the child.
                    2.3. Repeat the process down the tree until:
                            + The current node has no children, or
                            + The heap property is satisfied.
        # Insertion in Heap (min heap)
            1. Add a element to the end (N-1) Position
            2. Apply Bottom to Up Heapify
                2.1. Stats form current position(N-1)
                2.2. Compare it with its parent and swap them if needed
                        2.2.1 Find out the parrent of current position
                        2.2.2 check current is lesser than its parrent
                            if yes 
                                then swap parrent and current
                            else
                                break
                2.3. Repeat the process until:
                    + The current node is at the root, or
                    + The heap property is satisfied
        # Deletion in Heap
            1. Replace the Root
                - Replace the root of the heap with the last element in the heap.
                - This step temporarily disrupts the heap property.
            2. Remove the Last Element
                - Reduce the size of the heap by removing the last element (as it''s now at the root).
            3. Heapify (Top-Down)
                - Perform Top-Down Heapify (Sift-Down) on the root to restore the heap property:
                    + Edge Cases :
                        - Current is Leaf Node
                        - Current has only left child
                        - current has both left and right child
                    + Compare the root with its children.
                    + Swap the root with the largest child (max-heap) or smallest child (min-heap) if the heap property is violated.
                    + Repeat the process down the tree until the node is in the correct position or no children violate the heap property.
        # Heap Implementation
            vector<int> heap;
            heapify_down(index);
            heapify_up(index);
            insert(value)
            top()
            extract()

        # Build Heap 
            # Approaches 1
            1. Naive Method:
                - Start with an empty heap.
                - Insert each element of the array into the heap one by one using the Insert Operation.
                - Time Complexity:
                    O(NLog(N))
            # Approaches 2 
            2. Optimal Method:
                - Use the Heapify Operation to directly transform the array into a heap.
                - Start from the last non-leaf node and move upwards to the root, applying Bottom-Up Heapify.
                - Time Complexity: 
                    O(n), 
                    as heapifying smaller subtrees takes progressively less time.
        # Build Heap in O(NLog(N))
            1. Start with an Empty Heap:
                - Represent the heap as an array (or vector in C++).
            2. Iteratively Insert Each Element:
                - Add an element to the end of the heap (array).
                - Perform the Bottom-Up Heapify (sift-up) operation to ensure the heap property is maintained.
            3. Repeat for All Elements:
                - Process all elements in the input array one by one.
        # Build Heap on Array in O(N)
            - To build a heap in O(N) time, the bottom-up heapify approach should be used.
            - The bottom-up heapify method works by treating the array as a complete binary tree and starting the heapify process from the last non-leaf node (which is at index floor(n/2) - 1 for a zero-based array) up to the root. This ensures that every subtree is already a valid heap before moving upward.
            1. Start from the Last Non-Leaf Node:
                - For an array of size n, the last non-leaf node is at index (⌊n/2⌋ - 1).
                - Nodes after this are leaf nodes and already satisfy the heap property.
            2. Perform Bottom-Up Heapify:
                - Traverse from the last non-leaf node up to the root (index 0).
                - Call the Heapify function at each node to maintain the heap property.
        # Questions
            "Q1. Connect ropes"
            "Q2. Build a Heap"
            "Q3. Heap Queries"
            "Q1. Maximum array sum after B negations"
                - Greedy Approach:
                    Always flip the smallest element first to maximize the total sum.
            "Q2. Misha and Candies"
                - choose a box having the minimum number of candies
                - not like a box if it has the number of candies greater than B
                -  eat half of the candies and put the remaining candies in the other box that has the minimum number of candies.

                1. put all the box in min heap
                2. choose the top of min heap who is <= B
                3. add remaining candies to other box
                    - calulate the current Eatten and Remaining Candies
                    - add remaining canding to top and add in the heap 
                4. return the total candies eaten
                    min heap of <value, original_value>
            "Q3. Minimum largest element"
                1. Priority Queue (Min-Heap):
                    - The min-heap is used to efficiently access the smallest current element and update it during each operation.
                    - A custom comparator ensures the heap is sorted based on the value after adding the original value.
                2. Each element in the heap is a pair (current_value, original_value).
                    - current_value is the value of the element after some operations.
                    - original_value is the fixed value added during every operation.
                3. Algorithm Steps:
                    - Initialization: Push all elements of the array into the heap as (current_value, original_value) pairs.
                    - Operations: For B times, extract the smallest element from the heap, update its value by adding original_value, and push it back.
                    - Result Calculation: After all operations, the largest value among the elements in the heap is the result.
    2. Heaps 2: Problems
        # Heap Sort
            // Solution 1 T=O(NLog(N)) S=O(N)
                1. Build a max heap from the input array.
                2. Extract the root of the max heap and add it to the sorted array.
                3. Repeat the process until all elements are sorted.

            // Solution 2 [In-Place Heap Sort] T=O(NLog(N)) S=O(1)
                1. Build a max heap from the input array.
                2. Swap the root of the max heap with the last element of the heap.
                3. Reduce the size of the heap and call the heapify function to maintain the max heap property.
                4. Repeat until all elements are sorted.
        # K-th Largest Element
            1. Use a Min Heap:
                - Use a min heap to keep track of the K largest elements seen so far.
                - If the size of the heap exceeds K, remove the smallest element (the root of the min heap).
            2. Final Result:
                - After processing all elements, the root of the min heap will be the K-th largest element.
        # K-th Largest Element for all Windows
            1. Initialize a Min-Heap of size k.
            2. Iterate through the array:
                For the first k elements, add them to the min-heap.
                For each subsequent element, replace the root of the heap with the new element (if it's larger than the root).
            3. Return the root of the min-heap after processing each window.
        # Median of Stream of Integers
            1. Insert New Element:
                - If the new element is smaller than or equal to the root of the max-heap, insert it into the max-heap.
                - Otherwise, insert it into the min-heap.
            2. Balance Heaps:
                - Ensure that the size difference between the heaps is at most 1:
                    + If max-heap has more than one extra element, move its root to the min-heap.
                    + If min-heap has more elements, move its root to the max-heap.
            3. Compute Median:
                - If the max-heap has more elements, the median is its root.
                - If both heaps are of equal size, the median is the average of the roots of the two heaps.
        # Questions
            Q1. Ath largest element
            Q2. Running Median
            Q1. Ways to form Max Heap
                T(1) = 1
                T(2) = 1
                T(3) = 2
                T(N) = n-1 C k * T(k) * T(n-k-1)
                N = No of Keys
                K = No of Nodes in left subtree
                N-K-1 = No of Nodes in right subtree
                # Approach #
                1. Distribute Elements Between Subtrees:
                    - For a heap of size N, the root takes the largest element.
                    - The rest N-1 elements are split between:
                        + Left subtree of size L.
                        + Right subtree of size R.
                    - L is calculated using the properties of complete binary trees:
                        + H: Height of the tree ( H = ⌊log2(N)⌋).
                        + 2^H : Total nodes in the last level.
                        + L = Nodes in left subtree = (2^(H-1) - 1) + min(remaining nodes, 2^(H-1)).
                2. Recursive Function:
                    - Base Case:
                        if( N = 1 or N = 2){ return 1} 
                    - Recursive Step:
                        Calculate ways to form heaps for the left (L) and right (R) subtrees:
                        ways = T(L) * T(R)
                    - Total combinations for choosing L elements from N-1:
                        (N-1)C(L) = (N-1)! / (L!(N-1-L)!)
                    - Multiplying  Ways(L) * Ways(R) * (N-1)C(L)
                3. Precomputations:
                    To compute (N-1)C(L) efficiently, precompute factorials and modular inverses modulo 1e9+7.
                
                # Full Code Walkthrough
                1. expo  (Modular Exponentiation): Efficiently computes a^b mod c used to calculate modular inverses
                2. calcfact (Precomputing Factorial) : Precomputes factorials and modular inverses up to A
                3. Ways : (Recursive Function): Recursively calculates the number of heaps for size N, Spliting N-1 elements between left and right subtrees
                4. solve: Calls calcfact to initialize factorials and computes the result using ways(A).
            Q2. Product of 3
                # Approach
                    1. Initialization:
                        - Use a [priority_queue<int> (max-heap)] to keep track of the largest numbers encountered so far.
                    2. Iterate Through the Array:    
                        - For each A[i], add it to the heap.
                        - If i≥2 (meaning at least 3 elements have been encountered):
                            + Extract the top 3 elements from the heap.
                            + Compute their product.
                            + Push these elements back into the heap to maintain state for subsequent iterations.
                    3. Edge Case:
                        - If the array size N<3, the result for all indices is -1.
            Q3. Kth Smallest Element in a Sorted Matrix
                # Approach
                    1. Binary Search on Value Range:
                        - The smallest element in the matrix: A[0][0].
                        - The largest element in the matrix: A[N−1][M−1].
                        - Perform binary search on this range to find the B-th smallest element.
                    2. Counting Function: 
                        - Count the number of elements in the matrix A that are ≤ [mid] using a helper function [countLessEqual].
                    3. Binary Search Logic:
                        1. Compute [mid] as the average of [low] and [high].
                        2. Use countLessEqual to find how many elements are ≤ mid.
                            If the count is less than B, move the search to the right (low = mid + 1).
                            Otherwise, move the search to the left (high = mid).
                        3. Stopping Condition:
                            When low == high, the B-th smallest element is found.
    3. Interview Problems
        # Meeting Rooms 
            + Considering the overlapping Case
            + N overlapping need N Rooms

            1. Create the Hash array for time from 0 to max_time
            2. trverse the metting array
                1. mark the start time as 1++
                2. mark the end time as 1--
            3. traverse the hash array
                make prefix sum for checking the max overlapping
            4. return the max overlapping
        # Sort the nearly sorted array 
            1. Create the min heap of size K
            2. Traverse the array till K
                insert the element in the min heap
            3. traver the array from i as k+1 to N-1 initialize a J pointer as 0
                A[j] = min heap.top()
                min heap.pop()
                min heap.push(A[i])
            4. pop all remainingelement untill j < n
            5. return the array
        # Merge K sorted arrays 
            1. Understand the Structure:
                Each array is already sorted.
                Use a Min-Heap to efficiently retrieve the smallest element among all arrays.
            2. Use a Min-Heap:
                The heap will store elements along with their metadata (e.g., value, array index, and position in the array).
            3. Algorithm:
                Step 1: Initialize a Min-Heap.
                Step 2: Insert the first element of each array into the heap along with the array index and the element''s index within the array.
                Step 3: While the heap is not empty:
                    Extract the smallest element from the heap.
                    Add it to the result array.
                    If the extracted element''s array has more elements, insert the next element from that array into the heap.
                Step 4: Return the result array.
        # Minimum Distance Equal Pair
            1. use Map of <value, latest_index>
            2. traverse the array
                if(value is present){
                    min_distance = min(min_distance, i-map[vlaue])
                }
                map[value] = i
            3. return min_distance
        # Minimum Window Substring
            1. Two Pointers (Sliding Window):
                Use two pointers (left and right) to represent the bounds of the current window in S.
            2. Character Count:
                Maintain a count of characters in T using a hash map.
                Track the frequency of characters in the current window using another hash map.
            3. Expand and Contract the Window:
                Expand the window by moving the right pointer and adding characters to the current window.
                Contract the window by moving the left pointer when the current window contains all characters in T.
            4. Update the Minimum Window:
                Whenever the current window is valid (contains all characters in T), update the minimum window size if the current window is smaller.
            5. Return the Result:
                If a valid window is found, return the substring corresponding to the minimum window. Otherwise, return an empty string.
        # Questions
            Q1. Shaggy and distances
                1. use Map of <value, latest_index>
                2. traverse the array
                    if(value is present){
                        min_distance = min(min_distance, i-map[vlaue])
                    }
                    map[value] = i
                3. return min_distance
            Q2. K Places Apart
                1. Create the min heap of size K
                2. Traverse the array till K
                    insert the element in the min heap
                3. traver the array from i as k+1 to N-1 initialize a J pointer as 0
                    A[j] = min heap.top()
                    min heap.pop()
                    min heap.push(A[i])
                4. pop all remainingelement untill j < n
                5. return the array
            Q3. Merge K Sorted Lists
            Q4. Meeting Rooms II
                + Considering the overlapping Case
                + N overlapping need N Rooms

                1. Create the Hash array for time from 0 to max_time
                2. trverse the metting array
                    1. mark the start time as 1++
                    2. mark the end time as 1--
                3. traverse the hash array
                    make prefix sum for checking the max overlapping
                4. return the max overlapping
    4. Heaps Extra
## Greedy ##
    1. Greedy
        # Flipkart's Challenge  in Effective Inventory Management
            - given Expiration dates and Profit margin
            - Sell items such that the sum of the profit by items is maximised
            1. Sort the array in ascending order of Expiration
            2. Traverse the array
            3. if current time is lesser than the Expiration time 
                add in profit and add in min heap
               else if value is lesser than the min heap.top() 
                    then pop the min heap and subtract the top from profit
                    add the current value in profit
                    add the value in min heap
            4. return the profit
        # Job Scheduling Problem
            will pick those jobs whose end first
            1. sort the jobs w.r.t end time
            2. initilize the end = E[0]
            3. traver the jobs array
            4. if s[i] >= end
                ans ++
                end = e[i]
            5. return ans
        # Distribute Candy
            - Think Like a Graph some are equal, some are in increasing order, some are in decreasing order
            function F(ratings[]) {
                # Initialize the total sum to 1 as every rating gets at least 1 point.
                sum = 1; 
                # Start iterating from the second element.
                i = 1; 

                # Loop through the ratings array until the second last element.
                while (i < n - 1) {
                    # If two consecutive ratings are equal, increment the sum by 1.
                    if (ratings[i] == ratings[i + 1]) {
                        sum += 1; # Each gets 1 point.
                        i++;      # Move to the next element.
                        continue; # Skip the rest of the loop for this iteration.
                    }

                    # `peak` keeps track of increasing subsequences (peaks).
                    peak = 1; # Start with the initial value as 1.
                    # Count increasing ratings until they stop.
                    while (i < n - 1 && ratings[i] > ratings[i - 1]) {
                        peak++;          # Increment the peak size.
                        sum += peak;     # Add the peak value to the sum.
                        i++;             # Move to the next element.
                    }

                    # `down` keeps track of decreasing subsequences (downslopes).
                    down = 1; # Start with the initial value as 1.
                    # Count decreasing ratings until they stop.
                    while (i < n - 1 && ratings[i] < ratings[i - 1]) {
                        sum += down;     # Add the downslope value to the sum.
                        down++;          # Increment the downslope size.
                        i++;             # Move to the next element.
                    }

                    # If the downslope is longer than the peak, adjust the sum.
                    # This ensures all elements in the downslope are accounted for.
                    if (down > peak) {
                        sum += down - peak; # Add the extra downslope elements to the sum.
                    }
                }

                # Return the total computed sum.
                return sum;
            }
        # Questions
            "Q1. Flipkarts Challenge in Effective Inventory Management"
                # Approach
                - given Expiration dates and Profit margin
                - Sell items such that the sum of the profit by items is maximised
                1. Sort the array in ascending order of Expiration
                2. Traverse the array
                3. if current time is lesser than the Expiration time 
                    add in profit and add in min heap
                else if value is lesser than the min heap.top() 
                        then pop the min heap and subtract the top from profit
                        add the current value in profit
                        add the value in min heap
                4. return the profit          
            "Q2. Finish Maximum Jobs"
                # Approach
                will pick those jobs whose end first
                1. sort the jobs w.r.t end time
                2. initilize the end = E[0]
                3. traver the jobs array
                4. if s[i] >= end
                    ans ++
                    end = e[i]
                5. return ans
            "Q3. Distribute Candy"
                - Think Like a Graph some are equal, some are in increasing order, some are in decreasing order
                # Approach
                    1. Initialize the total sum to 1 as every rating gets at least 1 point.
                    2. Start iterating from the second element.
                    3. Loop through the ratings array until the second last element.
                    4. If two consecutive ratings are equal, increment the sum by 1.
                    5. Each gets 1 point.
            "Q1. Another Coin Problem"
                # Approach
                1. Coin Values: The coins are in the form 5^k where K>=0
                    his means the coin values are 1,5,25,125,…, and so on.
                2. Steps:
                    Start with the largest coin 5^k where 5^k <= A
                    Use as many of this coin as possible to reduce A.
                    Move to the next smaller coin value and repeat until A=0.
                3. Implementation:
                    Generate all possible coin values less than or equal to  A.
                    Iterate from the largest coin to the smallest, reducing A at each step while keeping track of the count of coins.
            "Q2. Seats"
                # Approach
                1. Minimizing Distance Using Median:
                    - To minimize the total movement, the occupied seats should be centered around the median of their current positions.
                    - he median ensures that the sum of absolute differences (|x1 - M| + |x2 - M| + ...) is minimized.
                2. Sequential Arrangement:
                    Once the median is selected, the seats are rearranged contiguously, starting from a hypothetical position where the group is aligned.
                # Steps in Code
                    1. Store Occupied Seat Indices:
                        - Traverse the string A and collect all indices where the seat is occupied ('x').
                        - Example: For A = "....x..xx...x..", ocupied_seats = [4, 7, 8, 12].
                    2. Find Median:
                        Calculate the median index of ocupied_seats.
                        For ocupied_seats = [4, 7, 8, 12], the median index is mid = 2, and median = 8.
                    3. Determine Starting Seat Number:
                        The group is to be shifted to start from Seat_no, such that they are contiguous and centered around the median.
                        For median = 8 and mid = 2, Seat_no = 8 - 2 = 6.
                    4. Calculate Total Jumps:
                        - Traverse the ocupied_seats array and calculate the total jumps required to move each person to their target position.
                        - Seat_no is incremented after each move to ensure contiguous seating.
            "Q3. Assign Mice to Holes"
                1. Sort the both array
                2. Traverse the any one array
                3. time = abs(A[i] - B[i])
                4. min_time = min(min_time, time)
                5. return min_time
    2. Greedy Extra
        # Assign Cookies
            - We Can Assign Small Cookies to Least Greed Factor Child 
            - Smallest first

            1. Sort the size array
            2. Sort the grid array
            3. use two pointer 
                L = size
                R = grid
            4. Assign until L<N and R<M
            5. if greed[r] <= size[l]
                    r++
               else 
                    l++
            6. return the R  // R child is statisfied
        # Lemonade Change
            - You are running a lemonade stand where each cup of lemonade costs $5. Customers come to you in a queue to buy lemonade, and they pay with either $5, $10, or $20 bills. You do not have any change initially.
            - always bill = 5 remaining is to return as a Change
            - Smallest First 
            - we can Keep track of 5,10,20 denominations count
            - 5 -> ++(5)
            - 10 -> ++(10), -(5) // return 5 chagnge
            - 20 _> ++(20), [(--(10,5)) OR (--(5,5,5))] // return 15 in changes 

            1. initialize 
                five = 0, ten=0, twenty=0
            2. Traverse the array L->R
            3. if [i] = 5
                    five++
            4. else if[i] == 10
                    if(five > 0)
                        five--
                        ten++
                    else
                        return false
            5. else
                    if(ten > 0 && five > 0)
                        ten--
                        five--
                    else if(five > 3)
                        five -= 3
                    else 
                        return false
            6. return true
        # Program for Shortest Job First (or SJF) CPU Scheduling
            - Think like as a Non overlapping Intervals from shortest to longest

            1. sort the array
            2. initialize
                time = 0
                waiting = 0
            3. traverse the Array L->R
            4. time += A[i] , waiting += time
            5. after travesing is over return waiting/N
        # Jump Game
            Q. You are given an array of non-negative integers nums, where each element represents the maximum number of steps you can jump forward from that position. Your task is to determine if you can reach the last index starting from the first index.

            if you able to cross 0''s then you can definitely cross all the element
            just check can the privious element help to reach till me if yes go further else return false
            we can use the Max index

            1. initialize MaxInd = 0
            2. traverse the array
                if (i > MaxInd)
                    return false
                MaxInd = max(MaxInd, i + A[i])
            3. return true
        # Jump Game 2
            - Q. Given an array nums, where each element represents the maximum number of steps you can jump forward from that position, find the minimum number of jumps required to reach the last index. Assume you can always reach the last index.
            - we can check the ranges
            - Focus on Farthest from current Range
                1. initialize 
                    jumps = 0; L=R=0;
                2. while(R<N-1){
                    farthest = 0
                    for (ind L->R){
                        farthest = max(ind + arr[ind] , farthest)
                    }

                    L=R+1
                    R = farthest
                    jumps++
                }
                3. return jumps
        # Job sequencing Problem
            - we have to focus on Max profit with least Deadline
            + Delay at edn day 
            + Get Max Profit

            1. sort the array according to profit
            2. totalProfit = 0, cnt=0, max_deadline = -1;
            3. max_deadline = find max deadline
            4. create the array Hash of size max_deadline+1
            5. traverse the array
                for i 0->N-1{
                    for j job[i].deadline -> 0 (reverse traversal in Hash){
                        if (Hash[j] == -1){
                            cnt++
                            hash[j] = job[i].id
                            totalProfit += job[i].profit
                            break
                        }
                    }
                }
            6. return totalProfit
        # N meetings in one room
            + I am focusing on Faster Meetings First (which is end first)
            + sorting the array according to end 

            given start and end array of N size

            1. create structure that store the start and end and position
            2. Traverse the i 0 -> N-1
                store all info in Data one by one
                arr[i].start = start[i]
                arr[i].end = end[i]
                arr[i].pos = i+1
            3. sort the arr according to end
                initialize cnt =1, freetime=arr[0].end, ds = {arr[0].pos}

            4. traverse the array i 0 -> N-1
                if(arr[i].start > arr[i].end){
                    cnt++
                    freetime = arr[i].end
                    ds.push_back(arr[i].pos)
                }
            5. return ds
        # Non-overlapping Intervals
            + I will focus on Early ending intervals first  
                I will remove the Longest overlapping Intervals
            
            1. Sort the array according to arr[i][1]
            2. initialize
                cnt = 1
                lastEndTime = arr[0][1]
            3. traverse the array 1 -> N-1
                if(arr[i][0] >= lastEndTime){
                    cnt++
                    lastEndTime = arr[i][1]
                }
            4. return N-cnt
        # Insert Interval
            + given non overlapping intervals in sorted order
            + insert the new interval
            + if overalps then merge the overlapping intervals

            1. Initialize 
                res = []
                i = 0
            2. while(i<N && (arr[i][1] < newInterval[0])){ // left non overlapping intervals
                    res.add(arr[i])
                    i++
               }
            3. while(i<N && (arr[i][0] <= newInterval[1])){ // overlapping intervals
                    newInterval[0] = min(newInterval[0], arr[i][0])
                    newInterval[1] = max(newInterval[1], arr[i][1])
                    i++
               }
               res.add(newInterval) // add merged interval
            4. while(i<N){ // right non overlapping intervals   
                    res.add(arr[i])
                    i++
               }
            5. return res        
        # Minimum number of platforms required for a railway
            + Considering the overlapping Case
            + N overlapping need N platforms

            1. sort the arrival, sort the departure
            2. initialize
                i = 0; j=0;cnt=0;max_cnt=0;
            3. while(i<N){
                if(arrival[i] <= departure[j]){
                    cnt++
                    max_cnt = max(max_cnt, cnt)
                    i++
                }else{
                    cnt--
                    j++
                }
            }

            4. return max_cnt
        # Valid Paranthesis Checker
            # solution 1 Recursive (3^N)
                f(s, ind, cnt){
                    if(cnt<0) return false
                    if(ind == N) return cnt == 0

                    if(s[ind] == "("){
                        return f(s, ind++, cnt++)
                    }else if(s[ind] == ")"){
                        return f(s, ind++, cnt--)
                    }else{
                        return (f(s, ind++, cnt++) OR f(s, ind++, cnt--) OR f(s, ind++, cnt))
                    }
                }
            # solution 2 (N)
                f(S){
                    min = 0, ,max =0
                    for i as 0 -> N-1{
                        if(S[i] == '('){
                            min++
                            max++
                        }else if(S[i] == ')'){
                            min--
                            max--
                        }else{
                           min-- 
                           max++
                        }
                        if(min < 0) min = 0
                        if(max < 0) return false
                    
                    }
                    return min == 0
                }
        # Candy
            # solution 1
                f(ratings[]){
                    left[n], right[n]
                    left[0]=1; right[n-1]=1

                    // left iteration
                    for(i as 1->n-1){
                        if(ratings[i] > ratings[i-1]){
                            left[i] = left[i-1] + 1
                        }else{
                            left[i] = 1
                        }
                    }

                    // right iteration
                    for(i n-1 -> 0){
                        if(ratings[i] > ratings[i+1]){
                            right[i] = right[i+1] + 1
                        }else{
                            right[i] = 1
                        }
                    }

                    // sum 
                    int sum = 0
                    for (i 0 -> n-1){
                        sum += max(left[i], right[i])
                    }
                    return sum
                }
            # solution 2
                function F(ratings[]){
                    sum = 1 i =1
                    while(i < n-1){
                        if(ratings[i] == ratings[i+1]){
                            sum += 1
                            i++
                            continue
                        }
                        
                        peak = 1
                        while(i < n-1 && ratings[i] > ratings[i-1]){
                            peak++
                            sum += peak
                            i++
                        }
                        down = 1
                        while(i < n-1 && ratings[i] < ratings[i-1]){
                            sum += down
                            down++
                            i++
                        }

                        if(down > peak){
                            sum += down-peak
                        }
                    } 
                    return sum 
                }
        # Fractional Knapsack Problem
            - Max perWeight Value first
            - Sort items by value-to-weight ratio
            
            Function fractionalKnapsack(W, items)
                Sort items by value-to-weight ratio in descending order

                maxValue = 0.0  // Initialize maximum value achievable

                For each item in items
                    If W == 0
                        Break  // Knapsack is full, stop the loop

                    If item.weight <= W
                        // If the entire item can fit in the knapsack
                        W = W - item.weight  // Decrease knapsack capacity
                        maxValue = maxValue + item.value  // Add full value of the item
                    Else
                        // Take the fraction of the item that fits
                        maxValue = maxValue + (item.value * (W / item.weight))
                        W = 0  // Knapsack is now full

                Return maxValue  // Return the maximum value
        # Greedy algorithm to find minimum number of coins
        # Program for Least Recently Used (LRU) Page Replacement Algorithm
## Recursion and Backtracking ##
    1. Recursion 1
        # What is Recursion
            Funtion calling itself
        # How to implement Recursion
        # Three Rules to implement Recursion
            1. Define Exactly what the Function do.
            2. Identify how to use subproblems to get the answers
            3. Write a Base Case
        # Find the sum of first N natural no.
            sum(n) = sum(n-1) + n
        # Funtion call Tracing
            void recursiveFunction(int n) {
                cout << "Entering: recursiveFunction(" << n << ")" << endl; // Log entry
                if (n <= 0) {
                    cout << "Base Case Reached for n = " << n << endl;
                    return;
                }
                recursiveFunction(n - 1);
                cout << "Exiting: recursiveFunction(" << n << ")" << endl; // Log exit
            }
        # Find Factrorial fo N using Recursion
            if (n==0){
                return 1
            }
            Fact(n) = n*Fact(n-1)
        # Print Number 1 to N in increasing order using recursion
            if (n==1){
                print(1)
                return
            }
            F(n-1)
            print(n)
        # Print Number N to 1 in decreasing order using recursion
             if (n==1){
                print(1)
                return
            }
            print(n)
            F(n-1)
        # Given an Intege N, Print Number N to 1 followed by 1 to N using recursion
            if (n==1){
                print(1)
                return
            }
            print(n)
            F(n-1)
            print(n)
        # Fibonacci Series usign recursion
            if(n<=1){
                return n
            }
            F(n) = F(n-1) + F(n-2)
        # Space Complexity

        # Questions
        Q1. Find Fibonacci 
        Q2. Find Factrorial (N*(N-1)*(N-2)*....1)
        Q3. Print 1 to N
        Q4. Sum of digits
        Q5. Print N to 1
        Q6. decreasing increasing in one Function
    2. Recursion 2
        # Find a^b using recursion
            2^4 = 2^2 * 2^2;
            2^5 = 2^2 * 2^2 * 2;
        
            if(b == 0){
                return 1
            }
            if(b % 2 == 0){
                return square(a, b/2) * square(a, b/2)
            }else{
                return square(a, b/2) * square(a, b/2) * a
            }
        # Print array element using recursion
            if(i = a.length){
                return
            }
            print(A[i])
            print_Array(A, i+1)
        # Find Max element of array using recursion
            if(i = a.length){ return INT_MIN }
            return max(a[i], max_array(a, i+1))
        # Check if the given String is palindrom
            l = 0, r=N-1
            if(l>=r){
                return true
            }
            if(s[l]!=s[r]){
                return false
            }
            return is_palindrome(s, l++, r--)
        # Tower Of Hanoi
            TOH(N A B C)
                if N==1{
                    R{N  A  C}
                }

                TOH(N-1 A C B)
                R {N  A  B}
                TOH(N-1 B A C)  
        # Questions
        Q1. Implement Power Funtion
            2^4 = 2^2 * 2^2;
            2^5 = 2^2 * 2^2 * 2;
            if (half < 0) {
                half = (half + C) % C;
            }
        Q2. Print Array Using Recursion
            if(i = a.length){
                return
            }
            print(A[i])
            print_Array(A, i+1)
        Q3. Max of A array using recursion
            if(i = a.length){ return INT_MIN }
            return max(a[i], max_array(a, i+1))
        Q4. IsPalindrome
            l = 0, r=N-1
            if(l>=r){
                return true
            }
            if(s[l]!=s[r]){
                return false
            }
            return is_palindrome(s, l++, r--)
        Q5. All indices of array
        Q6. Tower of Hanoi
             TOH(N A B C)
                if N==1
                R{N  A  C}
                TOH(N-1 A C B)
                R {N  A  B}
                TOH(N-1 B A C)  
        "Q7. Kth Symbol - Easy"
            # Intution
            Look this as a Binary Tree
            1. for knowing the N level K th node 
                we have to know whether its parrent is [1 or 0]
            2. then we have to know whether the node is the left child or right child of its parrent
                for this we can check the [K is Odd or Even]
                    if it is a even then it is 
                        Left child
                    if it is a odd then it is
                        Right child
            3. if parrent == 0
                left child = 0
                right child =  1
            4. if parrent == 1
                left child = 1
                right chid = 0

            kth_symbol(N, K){
                if(N == 1){
                    return 0;
                }
                parrent  =  kth_symbol(n-1, floor(K/2))
                isKOdd = (k%2 == 1)
                if(parrent == 1){
                    if(isKOdd){
                        return 0
                    }else{
                        return 1
                    }
                }else{
                    if(isKOdd){
                        return 1
                    }else{
                        return 0
                    }
                }
            }
        "Q8. Is Magic No."
        Q9. First Index using recursion
        Q10. Last Index using recursion
        Q11. Kth Symbol - Hard
    3. Backtracking 1
        # Backtracking
            Trying all possibilities using recursion
        # Decimal to Binary Conversion
            Conver(n){
                if(n == 0){
                    return 0
                }
                return convert(n/2) * 10 + N%2 
            }
        # Given an Interger A Pairs of Parentheses. Write a Funtion to Generate all combinations of well-formed parentheses of length 2*A
            2 Options 
                1. "("
                2. ")"
            genrate(str, open, close){
                if(open = 0 && close == 0){
                    print(str)
                    return
                }
                if(open > 0){
                    genrate(str+"(", open-1, close)
                }
                if(close > open) {
                    genrate(str+")", open, close-1)
                }
            }
        # Defination of Subset And Subsequences
            Subsequences
                may or may not continuous but follows order
            Subsets
                may or may not continuous but not follows order
        # Given an Array of Distinct Elements, Print all Subsets
            we are going left to right 
            we are getting ans for two posiblities that selecting and rejecting current index in result
            forwarding this ans till last index then add it in result
        # Permutations
        # Given a character array, print all possible permutations
            f(arr, ind, ans){
                if(ind == arr.size()){
                    ans.add(arr)
                    return
                }

                for(i as ind -> n-1){
                    swap(arr[ind], arr[i])
                    f(arr, ind+1, ans)
                    swap(arr[ind], arr[i])
                }
            }
        # Questions
            Q1. Permutations
            Q2. Generate all Parentheses II
            Q3. Generate Subsets
            "Q1. Letter Phone"
                # Steps in the Code
                    1. Digit to Letter Mapping:
                        - Create a map (digitMap) that associates each digit with the corresponding string of characters as per the telephone keypad.
                        - Digits 0 and 1 map to themselves as per the problem
                    2. Backtracking Function:
                        - Base Case:
                            + If the current index matches the length of the digit string, the combination is complete. Add it to the result.
                        - Recursive Case:
                            For each letter corresponding to the current digit, add it to the current combination, recurse for the next digit, and then backtrack (remove the letter).
                    3. Main Function (letterCombinations):
                        - Handles edge cases like empty input.
                        - Initializes the backtracking process with an empty current string and the starting index of 0.
                    4. Lexicographical Order:
                        Since the digit-to-letter mapping in digitMap is in natural order, the combinations are generated in lexicographical order.
            "Q2. Kth Symbol - Easy"
                # Key Observations
                1. - Row Generation Pattern:
                    Row 1: 0
                    Row 2: 01
                    Row 3: 0110
                    Row 4: 01101001

                    - Each row is generated by replacing:
                            0 → 01
                            1 → 10
                    - Hence:
                        The length of row 2^(A-1)   // (A-1 because 1 based indexing)
                2. Halving the Problem:
                    - The first half of a row is identical to the previous row.
                    - The second half is the complement of the previous row
                3. the length of the privious row is the midpoint of current row beacuse
                    - The first half of a row is identical to the previous row.
                    - The second half is the complement of the previous row.
                    - The length of Currnet row = 2^(A-1) 
                    - The length of Privious Row = 2^(A-2)
                    - Mid = 2^(A-2)
                4. if B is lesser then mid 
                        B is present in first half
                        return kth_symbol(A-1, B)
                5. if B is greater then mid
                        B is present in second half
                        second half is the complement of the previous row
                        return !kth_symbol(A-1, B-mid) 
    4. Backtracking 2
        # Print paths to Climp Stairs
            Approach:
                1. Recursive Backtracking:
                    - Start from the first step and try both 1-step and 2-step moves.
                    - If the current step count reaches or exceeds the total steps n, backtrack.
                    - Keep track of the path by storing each choice (1-step or 2-step) along the way.
                2. Base Case:
                    - If the total steps taken equals n, print the path.
                3. Recursive Case:
                    - Try both possible steps (1-step or 2-step) and recursively explore further.
                
                print_path(n, current_step, current_path, paths){
                    
                    if(current_step == n){
                        paths.add(current_path)
                        return
                    }

                    if(current_step+1 <= n){
                        current_path.insert(1)
                        print_path(n, current_step+1, current_path, paths)
                        current_path.pop_back()

                    }

                    if(current_step + 2 <= n){
                        current_path.insert(2)
                        print_path(n, current_step+2, current_path, paths)
                        current_path.pop_back()
                    }
                }
        # Print all paths from source to destination
            find_all_path(r, c, n, m, current_path, paths){
                if(r >= n || c >= m){
                    return
                }
                if(r == n-1 && c == m-1){
                    paths.add(current_path)
                    return
                }

                find_all_path(r+1, c, n, m, current_path+"D", paths)
                find_all_path(r, c+1, n, m, current_path+"R", paths)
            }
        # Shortest path in a matrix with huddles 
            min_dist = INT_MAX
            find_min_path(A, r, c, n, m, dist, visited, delta_move){
                if(r == n-1 && c == m-1){
                    min_dist = min(min_dist, dist)
                    return
                }

                for(int i=0; i<4; i++){
                    int new_r = r + delta_move[i][0]
                    int new_c = c + delta_move[i][1]

                    if(new_r>=0 && new_r<n && new_c>=0 && new_c<m && !visited[new_r][new_c] && A[new_r][new_c] != 0){
                        visited[new_r][new_c] = true
                        dist += 1
                        find_min_path(A, new_r, new_c, n, m, dist, visited, delta_move)
                        dist -= 1
                        visited[new_r][new_c] = false
                    }
                }
            }
        # Questions
            "Q1. Subset Sum equal to K"
                subsetSumK(A, i, k ){
                    if(k == 0){
                        return true
                    }

                    if(i>=A.size()){
                        return false
                    }

                    if(subsetSumK(A, i+1, k-A[i])) return true  // select
                    if(subsetSumK(A, i+1, k)) return true // reject

                    return false
                }
            Q2. Print paths in Staircase
            Q3. Print All Maze Paths
            Q1. Kth Symbol - Hard
            Q2. Shortest path in a Binary Maze with Hurdles
    5. Rcursion & Backtracking Extra
        # Introduction to Recursion 
            - when a function call itself until a specified condition is met
            - Stack overflow
            - Base Case
            - Recursion Tree (dry run)
        # Problems on Recursion
            - Backtracking
                + Execution Starts from Back first
                + last Guy Has been Executed First
            Q. Print Name N times Using Recursion
                f(i, n){
                    if(i>n){
                        return
                    }
                    print("name")
                    f(i+1, n)
                }
            Q. Print Linearly 1 -> n using recursion
                f(i, n){
                    if(i>n){
                        return
                    }
                    print(i)
                    f(i+1, n)
                }
            Q. Print N to 1 using recursion
                f(i, n){
                    if(i<1){
                        return
                    }
                    print(i)
                    f(i-1, n)
                }
            Q. Print 1 to N using backtrack
                f(i, n){
                    if(i<1){
                        return
                    }
                    f(i-1, n)
                    print(i)
                }
            Q. Print N to 1 using backtrack
                f(i, n){
                    if(i>n){
                        return
                    }
                    f(i+1, n)
                    print(i)
                }
        # Parameterized and Functional Recursion
            - Parameterized Recursion
                - Sum of N
                    f(i, sum){
                        if(i<1){
                            print(sum)
                        }
                        f(i-1, sum+i)
                    }
                - Factorial of N
                    f(i, sum){
                        if(i<1){
                            print(sum)
                        }
                        f(i-1, sum*i)
                    }
            - Functional Recursion
                - Sum of N
                    f(n){
                        if(n == 0){
                            return 0;
                        }

                        return n + f(n-1);
                    }
                - Factorial of N
                    f(n){
                        if(n == 1){
                            return 1;
                        }
                        return n * f(n-1);
                    }
        # Problems on Functional Recursion
            // Reverse the Array
                f(l,r, A){
                    if(l>=r){
                        return
                    }
                    swap(A[l], A[r])
                    f(l+1, r-1, A)
                }
            // Check if String is Palindrome
                f(i, s){
                    if(i >= s.size()/2){
                        return true;
                    }

                    if(s[i] != s[s.size()-i-1]){
                        return false;
                    }

                    return f(i+1, s);
                }
        # Multiple Recursion Calls
            - N th Fibonacci Number
                f(n){
                    if(n<=1){
                        1
                    }

                    return f(n-1) + f(n-1)
                }
            - Recursion tree
                                  fibonacci(5)
                                /             \
                            fibonacci(4)       fibonacci(3)
                            /        \           /       \
                    fibonacci(3) fibonacci(2) fibonacci(2) fibonacci(1)
                        /    \        /   \        /   \
                    fibonacci(2) fibonacci(1) fibonacci(1) fibonacci(0) fibonacci(1) fibonacci(0)
                    /    \
                    fibonacci(1) fibonacci(0)
        # Recursion on Subsequences
            we are going left to right 
            we are getting ans for two posiblities that selecting and rejecting current index in result
            forwarding this ans till last index then add it in result

            F(i, current, A){
                if (i>= A.size()){
                    print(current) // got a subsequence
                    return
                }

                // imp
                current.add(A[i])
                F(i+1, current, A) // call with selected
                current.remove(A[i])
                F(i+1, current, A) // call with rejecting
            } 
        # All Kind of Patterns in Recursion
            - Print Parameter wise
            - print one ans -> return true/false  AND  Avoid further Recursion Calls if you get true
            - count -> return 1/0 AND Add all f() calls in result
            - 
            -  
            1. All Subsequences whose sum is K
                F(i, current, currentSum, A, K){
                    if (i>= A.size()){
                        if(currentSum == K){
                            print(current) // got a subsequence
                        }
                        return
                    }

                    // imp
                    current.add(A[i])
                    currentSum += A[i]
                    F(i+1, current, A) // call with selected
                    current.remove(A[i])
                    currentSum -= A[i]
                    F(i+1, current, A) // call with rejecting
                } 
            2. print any one subsequence whose sum is K
                F(i, current, currentSum, A, K){
                    if (i>= A.size()){
                        if(currentSum == K){
                            print(current) // got a subsequence
                            return true
                        }
                        return false
                    }

                    current.add(A[i])
                    currentSum += A[i]
                    if(F(i+1, current, A) == true) return true  // return form here only if allready printed no need to check further
                    current.remove(A[i])
                    currentSum -= A[i]
                    if(F(i+1, current, A) == true) return true 

                    return false
                } 
            3. Count the Subsequences with sum = K
                F(i, currentSum, A, K){
                    if (i>= A.size()){
                        if(currentSum == K){
                            return 1
                        }
                        return 0
                    }

                    // approrah 1
                    currentSum += A[i]
                    left = F(i+1, current, A)
                    currentSum -= A[i]
                    right = F(i+1, current, A)
                    return left + right

                    // approach 2
                    count = 0
                    currentSum += A[i]
                    count += F(i+1, current, A)
                    currentSum -= A[i]
                    count += F(i+1, current, A)

                    return count
                } 
        # Merge Sort
            - divide and merge
            - divide the array recursively untill its length is 1
            - Merge the Left and Right half send it to privious

            merge(a, l, mid, r){
                leftSize = mid - l + 1
                rightSize = r - mid

                // Copy data to the temporary arrays
                for (i = 0 to leftSize - 1){
                    leftArray[i] = a[l + i]
                }
                for (j = 0 to rightSize - 1){
                    rightArray[j] = a[mid + 1 + j]
                }

                // Merge the temporary arrays back into the original array a
                i = 0  // Initial index for leftArray
                j = 0  // Initial index for rightArray
                k = l  // Initial index for merged subarray

                while i < leftSize and j < rightSize:
                    if leftArray[i] <= rightArray[j]:
                        a[k] = leftArray[i]
                        i = i + 1
                    else:
                        a[k] = rightArray[j]
                        j = j + 1
                    end if
                    k = k + 1
                end while

                // Copy any remaining elements from leftArray (if any)
                while i < leftSize:
                    a[k] = leftArray[i]
                    i = i + 1
                    k = k + 1
                end while

                // Copy any remaining elements from rightArray (if any)
                while j < rightSize:
                    a[k] = rightArray[j]
                    j = j + 1
                    k = k + 1
                end while
            }
            merge_sort(a, l, r) {
                if(l>=r){
                    return
                }

                mid = L+R/2
                merge_sort(a, l, mid)
                merge_sort(a, mid+1, r)
                merge(a, l, mid, r)      //merge(a, l, mid, mid+1, r)
            }
        # Quick Sort
            - Pick the Pivot element and place them in its correct position
            - Smaller on left, Larger on Right

            place(arr, l, r){
                pivot = arr[l]

                i=l
                j= r
                while(i<j){
                    while(arr[i]<=pivot && i<r){
                        i++
                    }

                    while(arr[j]>=pivot && i<l){
                        j--
                    }
                    if(i<j){
                        swap(arr[i], arr[j])
                    }
                }

                swap(arr[l], arr[j])
            }

            QS(arr, l, r){
                if(l<r){
                    PI = place(arr, l, r)
                    QS(arr, l, PI-1)
                    QS(arr, PI+1, r)
                }
            }
        # Combination Sum I
            - I can Peek the i Multiple times until arr[i] <= targert
            - base case
                if(i == n || targer == 0){
                    if(target == 0){
                        ans.add(ds)
                    }
                    return
                }
            
            f(i, arr, target, ans, ds){
                n = ds.size()
                if(i == n || target == 0){
                    if(target == 0){
                        ans.add(ds)
                    }
                    return
                }

                if(arr[i]<=target){
                    ds.add(arr[i])
                    f(i, arr, target-arr[i], ans, ds)
                    ds.pop()
                }

                f(i+1, arr, target, ans, ds)
            }
        # Combination Sum II
            // Approach 1 
                1. for order and Duplicate 
                    we can store the and in Ordered Hashset
                    then convert it to array[array]
            // Approach 2
                + I can Select the Subsequences
                + Sort the array first for Order
                + To Avoid Duplicate subsequences
                    I am not Peeking same element again
                1. CHECKING i -> N-1
                
                f(i, target, arr, ans, ds){
                    if(target == 0){
                        ans.add(ds)
                        return
                    }

                    for ind i->N-1{
                        if(ind > i && arr[i] == arr[i-1]){
                            continue
                        }
                        if(arr[i]> target){
                            break
                        }

                        ds.add(arr[i])
                        f(i+1, target-arr[i], arr, ans, ds)
                        ds.pop()
                    }
                }
        # Subset Sum I 
            f(i, sum, arr, ans){
                if(i == arr.size()){
                    ans.add(sum)
                    return
                }

                f(i+1, sum+arr[i], arr, ans)
                f(i+1, sum, arr, ans)
            } 
        # Subset Sum II   
            f(ind, arr, ds, ans){
                ans.add(ds)
                for(i as ind -> n-1){
                    if(i!=ind && arr[i] == arr[i-1]){
                        continue
                    }
                    ds.add(arr[i])
                    f(ind+1, arr, ds, ans)
                    ds.pop()
                }
            }
        # Print all Permutations of String/array I
            f(ds, nums, ans, freq){
                if(ds.size() == nums.size()){
                    ans.add(ds)
                    return
                }

                for(i 0->n-1){
                    if(freq[i] == 0){
                        ds.add(num[i])
                        freq[i]=1
                        f(ds, nums, ans, freq)
                        freq[i] = 0
                        ds.pop()
                    }
                }
            }
        # Print all Permutations of String/array II
            f(arr, ind, ans){
                if(ind == arr.size()){
                    ans.add(arr)
                    return
                }

                for(i as ind -> n-1){
                    swap(arr[ind], arr[i])
                    f(arr, ind+1, ans)
                    swap(arr[ind], arr[i])
                }
            }
        # N-Queens
            isSafe(row, col, board, n){
                TR = row
                TC = col
                while(TR >=0 && TC>=0 ){
                    if(board[TR][TC] == 'Q'){
                        return false
                    }
                    TR--
                    TC--
                }

                 TR = row
                TC = col
                while(TR >=0 && TC>=0 ){
                    if(board[TR][TC] == 'Q'){
                        return false
                    }
                    TR--
                    TC--
                }

                TC = col
                while(TC>=0 ){
                    if(board[row][TC] == 'Q'){
                        return false
                    }
                    TC--
                }

                TR = row
                TC = col
                while(TR < n && TC>=0 ){
                    if(board[TR][TC] == 'Q'){
                        return false
                    }
                    TR++
                    TC--
                }
            }

            NQ(col, board, ans, N){
                if(col == N){
                    ans.add(board)
                    return
                }

                for(row 0->N-1){
                    if(isSafe(row, col, board, N)){
                        board[row][col] = 'Q'
                        NQ(col+1, board, ans, N)
                        board[row][col] = '.'
                    }
                }
            }
        # Sudoko Solver
            solve(board){
                for(i 0->9){
                    for(j 0->9){
                        if(board[i][j] == '.'){
                            for(d 1->9){
                                if(isValid(i, j, d, board)){
                                    board[i][j] = d
                                    if(solve(board)){
                                        return true
                                    }else{
                                        board[i][j] = '.'
                                    }
                                }
                            }
                            return false
                        }
                    }
                }

                return true
            }

            isValid(r, c, d, board){
                for(i 0->8){
                    if(board[r][i] == d){
                        return false
                    }
                    if(board[i][c] == d){
                        return false
                    }
                    if(board[3*(r/3) + i/3][3*(c/3) + i%3] == d){
                        return false
                    }
                }
            }
        # M-Coloring Problem
            isSafe(node, color, graph, m, n, C){
                if(k 0->n-1){
                    if(k!=node && graph[k][node] == 1 && color[k] = col){
                        return false
                    }
                }
                return true
            }
            sovle(node, color, m, n, graph){
                if(node == N){
                    return true
                }
                for(i 1->M){
                    if(isSafe(node, color, graph, N, i)){
                        color[node] = i
                        if(solve(node+1, color, m, n, graph)){
                            return true
                        }
                        color[node] = 0
                    }
                }

                return false
            }
        # Palindrome Partitioning
            F(ind, s, path, res){
                if(ind == s.size()){
                    res.add(path)
                    return true
                }
                for(i ind->N-1){
                    if(IsPalindrome(s, ind, i+1)){
                        path.add(s.substring(ind, i+1))
                        F(i+1, s, path, res)
                        path.pop()
                    }
                }
            }

            IsPalindrome(s, L, R){
                while(L<=R){
                    if(s[L] != s[R]){
                        return false
                    }
                    return true
                }
            }
        # Rate in Maze
            F(r, c, arr, n, ans, move, vis){
                if(r==n-1 && c==n-1){
                    ans.add(move)
                    return
                }

                // DLRU

                // D
                if(r+1<n && !vis[r+1][c] && arr[r+1][c]==1){
                    vis[r+1][c] =1
                    solve(r+1, c, arr, n, ans, move+"D", vis)
                    vis[r+1][c] =0
                }
                //L
                if(c-1>=0 && !vis[r][c-1] && arr[r][c-1] == 1){
                    vis[r][c-1] =1
                    sovle(r,c-1, arr, n, ans, move+"L", vis)
                    vis[r][c-1] =0
                }
                //R
                if(c+1<N && !vis[r][c+1] && arr[r][c+1] == 1){
                    vis[r][c+1] =1
                    sovle(r,c+1, arr, n, ans, move+"R", vis)
                    vis[r][c+1] =0
                }
                //U
                if(r-1>=0 && !vis[r-1][c] && arr[r-1][c] == 1){
                    vis[r-1][c] =1
                    sovle(r-1,c, arr, n, ans, move+"U", vis)
                    vis[r-1][c] =0
                }
            }
        # Kth Permutations
            F(n, k){
                fact =1
                num.add(1)
                for (i as i->n-1){
                    fact = fact*i
                    nums.add(i+1)
                }

                ans = ""
                k = k-1
                while(true){
                    ans = ans + num[k/fact]
                    num.remove(k/fact)

                    if(num.size() == 0){
                        break
                    }

                    k = k % fact
                    fact = fact /num.size()
                }
            }
        # Count Inversion in array
            1. The idea is to modify the merge sort algorithm to count inversions while sorting the array.
            2. During the merge step, if an element from the right half is smaller than an element from the left half, it means there are inversions (because elements in the left half are greater but appear before elements in the right half).
            3. The count of such inversions is the number of remaining elements in the left half since all of these elements form inversions with the current element from the right half.
        # Subsequence vs Subset vs Permutation vs Combination
            # Subsequence
            | **Aspect**             | **Subsequence**                                          | **Subset**                                             |
            |-------------------------|---------------------------------------------------------|--------------------------------------------------------|
            | **Order**               | Respects the order of elements in the original array.   | Order doesnt matter.                                   |
            | **Recursive Calls**     | Always makes two recursive calls (include/exclude).     | Uses a loop to iterate over remaining elements.        |
            | **Duplicate Avoidance** | Not applicable (duplicates are natural).                | Avoids duplicates explicitly (by skipping elements).   |
            | **Base Case**           | Reaches the end of the array (`idx == nums.size()`).    | No explicit base case; result is updated iteratively.  |
## DP ##
    1. DP 1: One Dimensional
        # Nth Fibonacci Number
        # Dp Basics 
            - Optimal Approach
            - Overlapping Subproblems
            - Top Down Approach
                Recursive
                Memoization
            - Bottom Up Approach
                Iterative
                    Tabulation
                    Speace Optimization
        # Climbing Stairs
            if(n <= 1){
                return 1
            }
            Ways(n) = Ways(n-1) + Ways(n-2)
        # Find the Minimum No of Perfect Squares To Get sum = N
            Recursive Step
                - For each i, where i^2 <= N, Subtract i^2 from N and solve n-i^2.
                - Keep track of the minimum count among all possibilities.
            Base Cases:
                - if N = 0, return 0 (no number Reuqired)
                - if n<0, return INT_MAX, representing invalid State.
        # Question
            Q1. Stairs
                if(n <= 1){
                    return 1
                }
                Ways(n) = Ways(n-1) + Ways(n-2)
            Q2. Fibonacci Number
            Q3. Minimum Number of Squares
            "Q1. Maximum Sum Value"
                Core Idea:
                    We want to maximize the value step-by-step
                        First, maximize A[i]*B
                        then, add A[j] * C j>=i
                        fianlly, add A[K] * D K>=j
            "Q2. Max Product Subarray"
                Key Observations
                    1. Handling Negative Numbers:
                        - Multiplying a negative number with a large positive number reduces the product.
                            + -2 * 100 = -200
                        - However, multiplying a negative number with a small negative number can result in a larger positive product.
                            -3 < -2
                            + -2 * -3 = 6
                        - This leads us to track both the maximum product so far (maxProduct) and the minimum product so far (minProduct) for each element.
                    2. Key Variables:
                        - maxProduct: Tracks the maximum product subarray ending at the current index.
                        - minProduct: Tracks the minimum product subarray ending at the current index (important because multiplying two negatives can yield a positive).
                        - result: Tracks the global maximum product found so far.
                    3. Dynamic Nature of the Problem:
                        - At every index i, you have three options for the maximum/minimum product ending at i:
                            + The current element A[i] itself.
                            + The product of A[i] and maxProduct (extending the positive product so far).
                            + The product of A[i] and minProduct (extending the negative product so far).
                    4. Swapping maxProduct and minProduct:
                        - If the current number is negative, swap the roles of maxProduct and minProduct, as multiplying by a negative number flips their significance.
                Algorithm:
                    1. Initialize:
                        - maxProduct, minProduct, and result to the first element of the array, A[0].
                    2. Traverse the array starting from the second element:
                        - If A[i] < 0, swap maxProduct and minProduct.
                        - Update maxProduct to be the maximum of:
                            + A[i] (start a new subarray).
                            + maxProduct * A[i] (extend the previous positive product).
                        - Update minProduct to be the minimum of:
                            + A[i] (start a new subarray).
                            + minProduct * A[i] (extend the previous negative product).
                    3. Update result to track the maximum product found so far.
                        Return result.
    2. DP 2: Two Dimensional
        # Find Max Sum Without Selecting Adjacent Elements (House Robber)
            - Either Take current and Current - 2
            - Or Take Current - 1
            int maxRob(int index, vector<int>& nums, vector<int>& dp) {
                if(index == 0){
                    return nums[0]
                }
                if (index < 0) return 0;

                if (dp[index] != -1) return dp[index];

                // Rob the current house or skip it
                int take = nums[index] + maxRob(index - 2, nums, dp);
                int non_take = 0 + maxRob(index - 1, nums, dp);
                dp[index] = max(take, non_take);
                return dp[index];
            }
        # Find the all Possible Ways to travel from (0,0), (n-1, M-1)
            int uniquePathsMemo(int m, int n, int i, int j, vector<vector<int>>& dp) {
                // Base case: If we reach the bottom-right cell
                if (i == m - 1 && j == n - 1) return 1;
                // If we go out of bounds
                if (i >= m || j >= n) return 0;
                // If the result is already computed
                if (dp[i][j] != -1) return dp[i][j];

                // Recursively calculate unique paths by moving right and down
                return dp[i][j] = uniquePathsMemo(m, n, i + 1, j, dp) + uniquePathsMemo(m, n, i, j + 1, dp);
            }
        # Find the Count of N digit no with digit sum = S
            N =  No of Digits
            S = Required sum
            Digits  = [0-9]

            findWays(N, S, Digit){
                if(S == 0){
                    return 1
                }
                if(N <= 0){
                    return 0
                }
                ways = 0
                for(int i = 0; i < 10; i++){
                    way += findWays(N-1, S-i, Digit)
                }

                return ways
            }
        # Catalan Numbers
            - The Catalan numbers are a sequence of positive integers that appear in various counting problems in combinatorics. They are named after the Belgian mathematician Eugène Charles Catalan.
            - the Nth Catalan No. denoted as Cn = (2n)!/(n!*(n+1)!)
            - First Few Catalan Numbers
                C0 = 1, C1 = 1, C2=2, C3=5, C4=14, C5=42, C6=132, C7=429, C8=1430, C9=4862 ....
            - Combinatorial Applications
                Catalan numbers solve many counting problems, including:
                1. Binary Search Trees (BSTs): The number of unique BSTs that can be formed with n nodes.
                2. Parentheses Combinations: The number of ways to correctly match n pairs of parentheses.
                3. Triangulations: The number of ways to triangulate a convex n+2-gon.
            - Recursive Formula
                Catalan numbers can be calculated recursively as : 
                    Cn = Sumation i=0 to N-1 where Ci. Cn-i-1
                    C0 = 1
                    C1 = 1
        # Find the Count of Unique Bst with N distinct Nodes
            - find the Nth Catalan Number
            f(n){
                if(n<=1){
                    return 1
                }

                result = 0
                for(i as 0 -> N-1){
                    result += f(i) * f(N-1-i)
                }
                return result;
            }
        # Question
            Q1. Unique Paths in a Grid
            Q2. Max Sum Without Adjacent Elements
            Q3. N digit numbers
            Q4. Unique Binary Search Trees II
            "Q1. Min Sum Path in Matrix"
                F(M, N, Grid){
                    if(m == 0, n == 0){
                        return grid[0][0]
                    }

                    if(n<0 || m<0){
                        return INT_MAX
                    }
                    up = F(m-1, n, grid)
                    left = F(m, n-1, grid)

                    return  Grid[m][n] + min(up, left)
                }
            "Q2. Min Sum Path in Triangle"
                F(i, j triangle){
                    if (j < 0 || j >= triangle[i].size()) {
                        return INT_MAX; // Return a large value so invalid paths are not chosen
                    }
                    
                    if (i == triangle.size() - 1){
                        return triangle[i][j];
                    } 

                    down = F(i+1, j, triangle)
                    diag = F(i+1, j+1, triangle)

                    return triangle[i][j] + min(down, diag);
                }
            "Q3. Intersecting Chords in a Circle"
                - Chords 
                    + A chord of a circle is a straight line segment whose endpoints both lie on the circumference of the circle
                - The problem asks us to calculate the number of ways to draw A chords in a circle with 2*A points such that no two chords intersect.
                - This problem is related to Catalan numbers, which count the number of ways to arrange certain structures (e.g., parenthesis combinations, binary trees, or non-intersecting chords in a circle).
            "Q4. Max Rectangle in Binary Matrix"
                Key Observations
                    1. Treat each row of the binary matrix as a histogram.
                    2. Calculate the maximum area rectangle for each histogram row, using a stack-based method to
                        calculate the largest rectangle in a histogram efficiently.
                    3. Accumulate the heights of the histograms as you move row by row
                        If A[i][j]=1: Add 1 to the height above.
                        If A[i][j]=0: Reset the height to 0.
                This reduces the problem to solving N instances of the largest rectangle in a histogram, where N is the number of rows.

                # Approach
                    -  we can Determine the Height of each column for each row so can Treat the Every row as a histogram and find the largest Rectangle in Histogram
                    1. Traverse the Matrix the top to bottom (Columnwise)
                    2. initialize col_height=0 for each columnwise iteration 
                        if value is 1
                            increament the col_height 
                            mark current height = current_height
                        else 
                            col_height = 0;
                            current height = 0
                    3. traverse the each row and find the largest Rectangle in Histogram
                    4. return Max of each row 
    3. DP 3: Knapsack
        # Check Subset Sum = K
        # Knapsack Problem
            Given N Objects With their Values VI (profit/loss) and their weight WI. 
            A Bag with Capacity W that can be used to carry some Objects such that 
                Total sum of Objects weights <= W and Sum of Values in the Bag is maximum.
        # Fractional Knapsack
            Select items in Descending order wrt H[i]/W[i] till complete Capacity is used (Greedy)
            - Max perWeight Value first
            - Sort items by value-to-weight ratio
            
            Function fractionalKnapsack(W, items)
                Sort items by value-to-weight ratio in descending order

                maxValue = 0.0  // Initialize maximum value achievable

                For each item in items
                    If W == 0
                        Break  // Knapsack is full, stop the loop

                    If item.weight <= W
                        // If the entire item can fit in the knapsack
                        W = W - item.weight  // Decrease knapsack capacity
                        maxValue = maxValue + item.value  // Add full value of the item
                    Else
                        // Take the fraction of the item that fits
                        maxValue = maxValue + (item.value * (W / item.weight))
                        W = 0  // Knapsack is now full

                Return maxValue  // Return the maximum value
        # 0-1 Knapsack
        # Unbounded Knapsack
        # Question
            Q1. Fractional Knapsack
            Q2. 0-1 Knapsack
            Q3. Unbounded Knapsack
            "Q1. Buying Candies"
                The "Buying Candies" problem is a variation of the 0/1 Knapsack Problem where:
                    The weight corresponds to the cost of the candy packet (C[i]).
                    The value corresponds to the total sweetness of the candy packet (A[i] * B[i]).
                    The capacity of the knapsack corresponds to the total nibbles available (D).
                    Unlike the fractional knapsack, you can only take complete packets.
                # Approach
                    1. Base Case:
                        If index == N (no more packets left), return 0.
                        If nibbles == 0 (no nibbles left to spend), return 0.
                    2. Recursive Case:
                        We have two choices:
                            Exclude the current packet: Move to the next packet without reducing nibbles.
                            Include the current packet (only if C[index] <= nibbles): Add the sweetness from this packet to the result of the remaining nibbles.
            "Q2. Tushars Birthday Party"
                1. Subproblem Definition: Define dp[j] as the minimum cost to exactly satisfy an eating capacity of j.
                2. Base Case:
                    dp[0] = 0: No cost is required to satisfy an eating capacity of 0.
                3. Recurrence Relation: To satisfy an eating capacity of j, for each dish:
                    If the dish has a filling capacity B[k], consider using this dish.
                    Add the cost C[k] and solve for the remaining capacity j - B[k].
                    The recurrence is : 
                        dp[j] = min(dp[j], dp[j - B[k]] + C[k])
                    where B[k] <= j.

                4. Final Answer: For each friend with an eating capacity A[i], look up dp[A[i]] to find the minimum cost to satisfy them. Sum these costs for all friends.

                Explanation
                    1. DP Array Initialization:
                        dp[j] stores the minimum cost to satisfy a capacity of j.
                        Initialized with INT_MAX (unreachable state).
                    2. Filling DP Array:
                        For every capacity j from 1 to maxCapacity
                            Iterate through all dishes.
                            If a dish can be used (B[k] <= j), calculate the cost of using this dish : 
                                The cost includes the cost of satisfying the remaining capacity (j - B[k]).
                    3. Total Cost Calculation:
                        After filling the dp array, iterate through all friends capacities in A.
                        Sum up the costs for their respective capacities using dp.
            "Q3. Ways to send the signal"
                - The problem involves finding the number of ways to arrange a sequence of laser lights such that no two consecutive lights are on. Each laser light can either be on (O) or off (X).
                Rules
                    Two consecutive lights cannot be on because this would signal danger to aliens.
                    For A laser lights, we need to count all the possible safe arrangements.
                    The result should be returned as ans mod(1e9+7), as the total number of arrangements can be very large.
                Example 1: 
                For A=2, there are two laser lights. The valid arrangements are:
                    O X: First light is on, second is off.
                    X O: First light is off, second is on.
                    X X: Both lights are off.
                Invalid arrangement:
                    O O: Both lights are on, violates the rule.
                Output: 3.

                # Approach
                1. Define the State
                Let:
                    dp[i] represent the total number of valid arrangements for a sequence of i lights, where no two consecutive lights are on
                2. Base Cases
                    dp[1]=2: For a single light, the valid arrangements are O (on) and X (off).
                    dp[2]=3: For two lights, the valid arrangements are OX, XO, and XX.
                3. Recursive Relation
                    To ensure no two consecutive lights are on:
                    1. If the ith light is off, then the first i-1 lights can have any valid arrangement (dp[i−1]).
                    2. If the ith light is on, the i-1 light must be off, leaving the first i-2 lights to have any valid arrangement (dp[i−2]).
                    dp[i] = dp[i−1] + dp[i−2]
    4. DP 4: Applications of Knapsack
        # Rod Cutting
            # Choices 
                1. non take 
                    ind+1, length
                2. Take
                    ind, length - ind+1
            # 1. Define the Problem
                Let: A[i] represent the price of a rod piece of size i+1.
                The goal is to maximize the value of a rod of length N.
            # 2. Recursive State
            Define a recursive function:
                maxProfit(ind, length):
                    ind: The current piece size (0-based index).
                    length: The remaining rod length to be considered.
                    Return the maximum profit achievable using rod pieces from ind to N-1 for a total length of length.
            # 3. Choices
            At every step:
                1. Take the current piece (ind + 1):
                    Deduct the size of the piece from the remaining length.
                    Add the price of the piece to the total profit.
                2. Skip the current piece:
                    Move to the next piece size without reducing the remaining length.
                Thus, the recurrence relation is:
                maxProfit(ind,length)=max(A[ind]+maxProfit(ind,length−(ind+1)),maxProfit(ind+1,length))
            # 4. Base Cases
                If length=0: No rod left to cut, profit = 0.
                If ind=N: No pieces left to consider, profit = 0.
            # 5. Memoization
                To avoid redundant computations, store the result of each state in a dp table:
                    dp[ind][length]: Maximum profit for using pieces from ind to N-1 for a rod of length.
        # Coin Change Permutation
        # Coin Chage Combination
        # 0-1 Knapsack II
        # Question
            "Q1. Cutting a Rod"
                # Choices 
                    1. non take 
                        ind+1, length
                    2. Take
                        ind, length - ind+1
            "Q2. Coin Sum Infinite"
                # Choices
                    1. nontake
                        ind+1, sum
                    2. take
                        ind, sum-A[ind]
            "Q3. 0-1 Knapsack II"
                # choice
                    ind + 1, capacity
                    A[ind] + ind + 1, capacity-B[ind]
           " Q1. Distinct Subsequences"
                // Recursive Choices
                if (A[i] == B[j]) {
                    // Two options: Use A[i] or skip it
                    dp[i][j] = countSubsequences(i + 1, j + 1, A, B, dp) // Match A[i] with B[j]
                            + countSubsequences(i + 1, j, A, B, dp);   // Skip A[i]
                } else {
                    // Skip A[i] if characters don't match
                    dp[i][j] = countSubsequences(i + 1, j, A, B, dp);
                }
            Q2. Length of Longest Fibonacci Subsequence
            Q3. Lets Party
    5. DP Extra
        # Dp Introduction
        # Introduction
            ## HOW TO IDENTIFY WHTHER IS ITS SOLVED BY DP OR GREEDY ## 
            ## SubSequence VS SubSet VS Combinations VS Permutations ## 
            - Those who cannot remember the Past
                Condemned to repeat it
            1. Tabulation  -> Bottom Up
            2. Memoization -> Top Down

            Memoization -> Tabulation -> Space Optimization

            + overlapping Subproblems
                Memoization
            + 3 Steps to Apply Memoization
                1. Declare Dp Data Structure
                2. Store the Ans to Map
                3. Check the Current "Call" is Solved Priviously
            + 3 Steps to find the Recursion Relation
                1. Try to represent the Problem in terms of index
                2. Do all Possible Stuff on That Index according to Problem Statement
                3. Situation
                    Count all ways -> Sum of stum
                    find Min -> min of all ans
            + 3 Steps to Memoixezation -> Tabulation
                1. Declare the Base Case
                2. Express all State in For Loop
                3. copy Recurrence and Write
            + Space Optimization
                if there is a Prev row & prev col
                    we can space optimize it           
        # Fibonacci
            # Memoization
                f(n, dp){
                    if(n <= 1){
                        return n
                    }

                    if(dp[n] != -1){
                        return dp[n]
                    }

                    return dp[n] = f(n-1, dp) + f(n-2, dp)
                }
            # Tabulation
                f(n){
                    dp[n+1];
                    dp[0] = 0, dp[1] = 1

                    for(i as 2 -> N){
                        dp[i] = dp[i-1] + dp[i-2]
                    }

                    return dp[n]
                }
            # space Optimization
                f(n){
                    if(n<=1){
                        return n
                    }
                    prev2 = 0
                    perv1 = 1

                    for(i 2 -> N){
                         
                    }
                }
        # Climbing Stairs
            - same as fibonacci 
                - Memoization
                - Tabulation
                - Space Optimization
            // recursion
            f(n){
                if(n == 0){
                    return 1
                }
                if(n == 1){
                    return 1
                }
                left = f(n-1)
                right = f(n-2)
                return left + right
            }
        # Frog Jump
            // Memoization
                f(i, arr, dp){
                    if (i == 0) return 0;

                    if(dp[i] != -1) return dp[i]

                    onestep = f(i-1, arr, dp) + abs(arr[i] - arr[i-1])

                    twostep = INT_MAX
                    if(i>1) twostep = f(i-2, arr, dp) + abs(arr[i] - arr[i-2])

                    return dp[i] = min (one, twostep)
                }
            // Tabulation
                f(n){
                    dp[n];
                    dp[0] = 0

                    for(i 1 -> N){
                        onestep = dp[i-1] + abs(arr[i] - arr[i-1])

                        twostep = INT_MAX
                        if(i>1) twostep = dp[i-2] + abs(arr[i] - arr[i-2])

                        dp[i] = min (one, twostep)
                    }

                    return dp[n]
                }

            // space Optimization
                f(n){
                    prev2 = 0
                    prev1 = 0

                    for(i 1 -> N){
                        onestep = prev1 + abs(arr[i] - arr[i-1])

                        twostep = INT_MAX
                        if(i>1) twostep = prev2 + abs(arr[i] - arr[i-2])

                        prev2 = prev1
                        prev1 = min(one, twostep)
                    }

                    return prev1
                }
        # Frog Jump With K distance
        # Maximum Sum of Non-Adjacent Elements I (House Robber)
        # Maximum Sum of Non-Adjacent Elements II (House Robber II)

        # 2D DP
        # Ninja's Training
        # Total Unique Path from (0,0) to (m-1,n-1)
        # Total Unique Path from (0,0) to (m-1,n-1) With Obstacle
        # Min Path Sum in a Grid
        # Triangle
        # Minimum & Maximum Falling path sum
        # Cherry Pickup II - Ninja and his Friends (3D DP)

        # DP ON SubSeqence
        # Subset Sum Equal to Target
        # Partition Equal Subset Sum
        # Partition A Set Into Two Subsets With Minimum Absolute Sum Difference | S1-s2 = D
        # Counts Subsets with Sum K
        # Count Partitions with Given Difference
        # 0/1 Knapsack Problem ## IMP ##
        # Minimum Coins
        # Target Sum (Asign Signs [+ -]) | s1-s2 = Target
        # Coin Change II
        # Unbounded Knapsack
        # Rod Cutting Problem | infinite supply of N rods with price same as unbounded kanpsack

        # DP on Strings
        # Longest Common Subsequence ## VVIP ##
        # Print Longest Common Subsequence ## VVIP ##
        # Longest common Substring
        # Longest Palindromic Subsequence | Longest Common Subsequence(s1, rev(s1))
        # Minimum Insertions to Make String Palindrome| N - Longest Palindromic Subsequence(s)
        # Minimum Insertions/Deletions to Convert String A to String B | N - LCS(s1, s2) + M - LCS(s1, s2)
        # Shortest Common Supersequence | L = N - LCS(s1, s2) + M - LCS(s1, s2) + LCS(s1, s2)
        # Distinct Subsequences (String Matching)
        # Edit Distance
        # Wildcard Matching (? *)

        # Dp ON Stocks
        # Best Time to Buy and Sell Stock
        # Buy and Sell Stock II ## VVIP ##
        # Buy and Sell Stock III
        # Buy and Sell Stock IV
        # Buy and Sell Stocks With Cooldown
        # Buy and Sell Stocks With Transaction Fee

        # DP ON Longest Increasing Subsequence
        # Longest Increasing Subsequence
        # Printing Longest Increasing Subsequence
        # Longest Increasing Subsequence | Binary Search
        # Largest Divisible Subset
        # Longest String Chain
        # Longest Bitonic Subsequence
        # Number of Longest Increasing Subsequences

        # MCM (Matrix Chain Multiplication) | Partition DP
        # MCM (Matrix Chain Multiplication) | Partition DP
        # Matrix Chain Multiplication | Recursive | Memoization
        # Matrix Chain Multiplication | Tabulation
        # Minimum Cost to Cut the Stick
## Graphs ##
    1. Graphs 1: Introduction, DFS & Cycle Detection
        # Introduction to Graph
            Types of Graph
                1. Directed / Undirected
                2. Connected / Disconnected
                3. Weighted / Unweighted
                4. Cyclic / Acyclic
                5. Degree (Undirected) / Indegree / Outdegree
            Simple Graph    
                A Connected Graph Without Self Loop & Multiedges
        # Adjacency Matrix
            1. Determine the number of nodes N (it is the maximum node index in the edge list).
            2. Create an N*N matrix initialized to 0.
            3. Iterate through the edge list and populate the adjacency matrix.
        # Adjacency List
            1. Initialize an empty list of vectors (or map of vectors) to store neighbors for each node.
            2. Traverse the edge list:
                Add u''s adjacency list.
                For undirected graphs, add v''s adjacency list as well.
        # DFS Traversal
            Steps to Perform DFS:
                1. Start from the source node: Begin at a selected node, mark it as visited.
                2. Explore all adjacent vertices: For each unvisited adjacent vertex, recursively apply DFS.
                3. Backtrack: Once all adjacent vertices of a node are visited, backtrack and continue the process for other unvisited nodes.
        # Check DAG has a Cycle or NOt
            1. Use a DFS traversal to explore all nodes.
            2. For each node :
                If the node is not visited, perform a DFS traversal.
                During the DFS traversal, mark the node as part of the recursion stack (path[i] = 1).
                If we encounter a node that is already in the recursion stack (path[neighbor] == 1), it indicates a cycle.
                After processing all the adjacent nodes of the current node, mark it as fully processed (visited[i] = 2).
        # Question
            "Q1. Path in Directed Graph"
                Find the path is present or not between 1 to A
                Do DFS Traversal on 1 
                Check if A is visited then path is present otherwise not present

            "Q2. Cycle in Directed Graph"
            "Q1. First Depth First Search"
            "Q2. Maximum Depth"
                Steps
                1. Using Array B and C Create Adjacency List
                2. Using BFS finding the Level and its nodes in that Level
                3. Traversing the Each Query and answer
    2. Graphs 2: BFS & Matrix Questions
        # BFS
            1. Initialization:
                - Create a queue and add the starting node.
                - Create a visited array (or set) to mark nodes that have already been visited to avoid revisiting them.
            2. Traversal
                - While the queue is not empty : 
                    - Dequeue a node from the front of the queue
                    - Process the node (e.g., print or store it).
                    - For each unvisited neighbor of the current node :
                        + Mark it as visited.
                        + Enqueue it to visit later.
            3. End : 
                - Continue the process until the queue is empty.
        # Rotten Oranges
            1. Initialize a queue to store the all rotten oranges value = 2 T = 0.
            2. do BFS traversal
            3. pop current orange and 
                PUSH all adjacency Fresh oranges to queue with T + 1
            4. check all fresh orange and get max ans 
            5. return ans
        # Flipkart Delivery Optimisation
             You are given a 2D matrix A of size NXM representing the map, 
             where each cell is marked with either a 0 or a 1. Here, a 0 denotes a locality, and a 1 signifies a warehouse
             The objective is to calculate a new 2D matrix of the same dimensions as A.
             In this new matrix, the value of each cell will represent the minimum distance to the nearest warehouse. For the purpose of distance calculation, you are allowed to move to any of the eight adjacent cells directly surrounding a given cell.

             - We can find the min distance Using BFS Starting from each warehouse initial distance = 0
             - in Every level Distance will increament by one
        # Number of Islands
            1. Traverse the Whole Matrix 
            2. Do BFS on every Unvisited Land Cell (value = 1 and visited = false)
            3. every time of BFS increament the count by 1
            4. return the count 
            
            for(i as 0 -> N-1 ){
                for(j as 0 -> M-1){
                }
            }
        # Shortest Distance in a maze
        # Question
            Q1. Rotten Oranges
            Q2. Number of islands
            Q3. Another BFS
            Q4. Shortest Distance in a Maze
            Q1. Valid Path
            Q2. Capture Regions on Board
            Q3. Black Shapes
            Q4. Knight On Chess Board
    3. Graphs 3: MST (Prims Algo.) & Dijkstra Algo
        # MST
            A tree in which we have N nodes and N-1 edges & all nodes are reachable from each other.
            MST (Minimum Spanning Tree) 
                is the tree with the minimum possible sum of all the edges in the Spanning Tree.
            Prim''s Algorithm
            Krushkal''s Algorithm

            Tree constructed from a connected Weighted Graph
            S.t. the sum of of weights of selected edges is min

            Algorithm
                Prim''s Algorithm
                Krushkal''s Algorithm
        # Prim's Algorithm
            Start with any node a the root node and 
            keep on adding the other nodes with minimum weight

            1. Initialize Priority Queue and Visited Array
                - Start with a priority queue (pq) initialized with {0, 0}:
                    0: Weight of the edge (initially 0 for the starting node).
                    0: Starting node.
                - Create a vis array of size V, initialized to 0 (indicating all nodes are unvisited).
            2. Process Nodes Using the Priority Queue
                - Repeat until the pq becomes empty:
                    Extract the smallest weight edge using pq.top() and remove it from the queue with pq.pop().
                    Retrieve the node and its associated weight from the extracted edge.
            3. Skip Already Visited Nodes
                - If the node has already been visited (vis[node] == 1), skip further processing to avoid cycles.
            4. Add Edge to MST
                - Mark the node as visited (vis[node] = 1) and add its weight (wt) to the MSTs cumulative weight sum.
            5. Process Adjacent Nodes
                For each neighbor (adjNode) of the current node:
                    Retrieve the edge weight (edW) between node and adjNode.
                    If adjNode has not been visited (vis[adjNode] == 0), push the edge {edW, adjNode} into the priority queue.
            6. Return Total Weigh
                Once all nodes ha
        # Dijkstra's Algorithm
            Dijkstra''s Algorithm is a greedy algorithm used to find the shortest paths from a source vertex to all other vertices in a weighted graph. It works for non-negative edge weights and is commonly implemented using a priority queue (min-heap) for efficiency.

            Algorithm Steps
                1. Initialize Distances:
                    Create a distance array (dist) initialized to infinity (INT_MAX), except for the source vertex, which is set to 0.
                2. Use a Min-Heap:
                    Store pairs {distance, vertex} in a priority queue, starting with {0, source}.
                3. Relax Edges:
                    For the vertex with the smallest known distance (extracted from the priority queue), update the distances to its neighbors if a shorter path is found.
                4. Avoid Revisits:
                    Use a visited set or only process unvisited vertices to avoid unnecessary calculations.
                5. Repeat:
                    Continue until the priority queue is empty.
        # Question
            Q1. Commutable Islands
            Q2. Dijkstra
            Q3. Construction Cost
            Q1. Damaged Roads
            Q2. Edge in MST
    4. Topological Sort & Interview Problems
        # Course Schedule I
            If Cycle is Present then False otherwise True
        # Topological Sort / Order
            Linear Odering of Nodes such that if there is an edge from I -> J then I should be present before J

            1. Select All nodes with Indegree 0 and store in a array/set/queue
            2. Select any one node from array, print it (as Output)
            3. Decrease Indegree of all adjacent nodes by 1
                if Updated indegree is = 0 insert in queue
            4. Repeat from step 2 until queue is empty
        # Minimum jumps to reach end
            - Q. Given an array nums, where each element represents the maximum number of steps you can jump forward from that position, find the minimum number of jumps required to reach the last index. Assume you can always reach the last index.
            - we can check the ranges
            - Focus on Farthest from current Range
                1. initialize 
                    jumps = 0; L=R=0;
                2. while(R<N-1){
                    farthest = 0
                    for (ind L->R){
                        farthest = max(ind + arr[ind] , farthest)
                    }

                    L=R+1
                    R = farthest
                    jumps++
                }
                3. return jumps
        # Max profit from stock prices | Buy and Sell Stock II ## VVIP ##
            1. At any day ind, you decide whether to buy, sell, or do nothing.
            2. Use a binary state buy :
                buy = 0: You are allowed to buy the stock.
                buy = 1: You are allowed to sell the stock.
            3. Use recursion to explore all possible decisions and calculate the maximum profit.
        # Question
            Q1. Possibility of Finishing
            Q2. Topological Sort
            Q3. Best Time to Buy and Sell Stocks II
            Q1. Perfect Numbers
            Q2. Ways to Decode
            Q3. Largest Distance between nodes of a Tree
            Q4. Flip Array
    5. Graphs Extra
        # Minimum Spanning tree / Disjoint set and Problems
        # Other Algo

        # Introduction to Graph
        # Introduction to Graph
        # Graph Representation
        # BFS
        # DFS

        # Problems on BFS and DFS
        # Number of Provinces
        # Number of Distinct Islands [dfs multisource]
        # Flood Fill Algorithm
        # Rotten Oranges
        # Detect Cycle in an Undirected Graph (using BFS)
        # Detect Cycle in an Undirected Graph (using DFS)
        # Distance of nearest cell having 1
        # Surrounded Regions
        # Number of Enclaves
        # Number of Distinct Islands | Constructive Thinking + DFS
        # Bipartite Graph BFS
        # Bipartite Graph DFS
        # Detect cycle in a directed graph using DFS
        # Find Eventual Safe States | Find Safe Nodes

        # Topological Sort & Problems
        # Topological Sort Algorithm
        # Kahn's Algorithm | Topological Sort Algorithm | BFS
        # Detect a Cycle in Directed Graph | Topological Sort | Kahn's Algorithm | BFS
        # Course Schedule I and II | Pre-requisite Tasks | Topological Sort
        # Find Eventual Safe States - BFS - Topological Sort
        # Alien Dictionary - Topological Sort

        # Shortest Path Algorithms and Problems
        # Shortest Path in Directed Acyclic Graph - Topological Sort
        # Shortest Path in Undirected Graph with Unit Weights
        # Word Ladder - I | Shortest Paths
        # Word Ladder - II | Shortest Paths
        # Word Ladder - II | Optimized approach
        # Dijkstra's Algorithm - Using Priority Queue - C++ and Java - Part 1
        # Dijkstra's Algorithm - Using Set - Part 2
        # Dijkstra's Algorithm - Why PQ and not Q, Intuition, Time Complexity Derivation - Part 3
        # Print Shortest Path - Dijkstra’s Algorithm
        # Shortest Distance in a Binary Maze
        # Path With Minimum Effort
        # Cheapest Flights Within K Stops
        # Minimum Multiplications to Reach End
        # Number of Ways to Arrive at Destination
        # Bellman Ford Algorithm
            - Relax All the Edges N-1 times sequentially
            - Relax
                if(dist[u]+wt < dist[v])
                    dist[v] = dist[u]+wt
            - Why N-1 times?
                Since in a Graph of N nodes,in Worst Case there can be N-1 edges to Reach from any node to any other node.
                therefore we need to relax all the edges N-1 times.
                Try drawing a graph which Takes  more than N-1 edges for any Path. it is impossible.
            - How to Detect the Negative Cycle
                on Nth iteration, the ralaxation will be done and if the distance of any node changes then it means there is a negative cycle.  
        # Floyd Warshall Algorithm
            - From Every Source
            - multisource Shortest Path
            - detect Negative Cycle
            - go Via Every Vertex/Node
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
            - How to Detect the Negative Cycle
                if(cost[i][i]  < 0) return true;
        # Find the City With the Smallest Number of Neighbours at a Threshold Distance

        # Minimum Spanning tree / Disjoint set and Problems
        # Minimum Spanning Tree - Theory
            A tree in which we have N nodes and N-1 edges & all nodes are reachable from each other.
            MST (Minimum Spanning Tree) 
                is the tree with the minimum possible sum of all the edges in the Spanning Tree.
            Prim''s Algorithm
            Krushkal''s Algorithm
        # Prim's Algorithm - Minimum Spanning Tree
            Start with any node a the root node and 
            keep on adding the other nodes with minimum weight

            1. Initialize Priority Queue and Visited Array
                - Start with a priority queue (pq) initialized with {0, 0}:
                    0: Weight of the edge (initially 0 for the starting node).
                    0: Starting node.
                - Create a vis array of size V, initialized to 0 (indicating all nodes are unvisited).
            2. Process Nodes Using the Priority Queue
                - Repeat until the pq becomes empty:
                    Extract the smallest weight edge using pq.top() and remove it from the queue with pq.pop().
                    Retrieve the node and its associated weight from the extracted edge.
            3. Skip Already Visited Nodes
                - If the node has already been visited (vis[node] == 1), skip further processing to avoid cycles.
            4. Add Edge to MST
                - Mark the node as visited (vis[node] = 1) and add its weight (wt) to the MSTs cumulative weight sum.
            5. Process Adjacent Nodes
                For each neighbor (adjNode) of the current node:
                    Retrieve the edge weight (edW) between node and adjNode.
                    If adjNode has not been visited (vis[adjNode] == 0), push the edge {edW, adjNode} into the priority queue.
            6. Return Total Weigh
                Once all nodes have been processed, return the accumulated sum as the total weight of the MST.

        # Disjoint Set | Union by Rank | Union by Size | Path Compression
            - Why
                - Dynamic Graph
                - Check U & V is Reachable in Constant time
            - methods
                - FindParrent(node)
                - unionByRank(node1, node2)
                - unionBySize(node1, node2)
            - Union
                1. find the Ultimate Parrent of U & V
                    PU and PV
                2. find the rank/size of PU & PV
                3. compare the Smaller rank/size to Larger rank/size of PU & PV
            - isInSameComponent(u, v)
                if both having same parent then they are in same component
            - Find Parrent
            - Path Compression
            - Why Connect Smaller to Larger
        # Kruskal's Algorithm - Minimum Spanning Tree
            - Sort all the edges according to weight
            - use Disjoint Set to Create the MST Graph
            - if U & V are not in same component 
                then do Union of U & V and add in Mst
        # Number of Provinces - Disjoint Set
        # Number of Operations to Make Network Connected
        # Accounts Merge - DSU
        # Number of Islands - II - Online Queries - DSU
        # Making a Large Island - DSU
        # Most Stones Removed with Same Row or Column - DSU
        # Strongly Connected Components - Kosaraju's Algorithm
            1. Sort all the Vertex according to Finishing time
            2. Reverse the Graph
            3. do DFS
        # Bridges in Graph - Using Tarjan's Algorithm of time in and low time
        # Articulation Point in Graph