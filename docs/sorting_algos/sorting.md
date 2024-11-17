
# Common Sorting Algorithms

Sorting algorithms are used to rearrange elements in a list in a specific order, typically ascending or descending. Here are some of the most common types:

## 1. Bubble Sort

Bubble Sort is a simple comparison-based algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

- **Time Complexity**: O(n²)
- **Best Use Case**: Small lists or when the list is almost sorted.

## 2. Selection Sort

Selection Sort divides the list into a sorted and an unsorted part. It repeatedly selects the smallest (or largest, depending on the order) element from the unsorted part and moves it to the end of the sorted part.

- **Time Complexity**: O(n²)
- **Best Use Case**: Small lists, or when memory writes are a concern, as it performs minimal swaps.

## 3. Insertion Sort

Insertion Sort builds the sorted list one element at a time by repeatedly picking the next element from the unsorted list and inserting it in its correct position in the sorted part.

- **Time Complexity**: O(n²)
- **Best Use Case**: Small lists or lists that are already mostly sorted.

## 4. Merge Sort

Merge Sort is a divide-and-conquer algorithm. It divides the list into two halves, recursively sorts each half, and then merges the two sorted halves back together.

- **Time Complexity**: O(n log n)
- **Best Use Case**: Large lists, especially when a stable sort is needed.

## 5. Quick Sort

Quick Sort is a divide-and-conquer algorithm that selects a "pivot" element and partitions the list around the pivot, so elements less than the pivot are on the left and elements greater are on the right. It then recursively sorts the sublists.

- **Time Complexity**: O(n log n) on average, O(n²) in the worst case
- **Best Use Case**: Large lists, as it’s generally faster than Merge Sort, though it’s not stable.

## 6. Heap Sort

Heap Sort is a comparison-based algorithm that uses a binary heap data structure. The list is first turned into a max heap, then the largest element is repeatedly removed from the heap and added to the sorted part of the list.

- **Time Complexity**: O(n log n)
- **Best Use Case**: Large lists where stability is not required.

## 7. Counting Sort

Counting Sort is a non-comparative algorithm. It works by counting the occurrences of each unique element, then uses this information to place each element in the correct position in the sorted list. This algorithm works best when the range of numbers (k) is small.

- **Time Complexity**: O(n + k)
- **Best Use Case**: Lists with a limited range of integers.

## 8. Radix Sort

Radix Sort is a non-comparative algorithm that sorts numbers by processing individual digits. It starts with the least significant digit and moves to the most significant, using a stable sort (like Counting Sort) for each digit position.

- **Time Complexity**: O(d * (n + k)), where `d` is the number of digits
- **Best Use Case**: Large lists of integers with a known digit range.

## 9. Bucket Sort

Bucket Sort is a distribution-based algorithm. It works by dividing the elements into several "buckets" and then individually sorting each bucket, typically using another algorithm. The buckets are then concatenated to form the sorted list.

- **Time Complexity**: O(n + k) on average
- **Best Use Case**: Uniformly distributed data, typically with floating-point numbers.

## 10. Shell Sort

Shell Sort is an extension of Insertion Sort. It sorts elements that are far apart and gradually reduces the gap between elements to be compared, effectively creating a more efficient version of Insertion Sort.

- **Time Complexity**: O(n log n) in the best cases, O(n²) in the worst cases
- **Best Use Case**: Medium-sized lists where other algorithms might be inefficient.

---

Each of these sorting algorithms has unique properties that make it suitable for specific types of data and use cases. Understanding their characteristics and performance can help you choose the right one for your needs.

