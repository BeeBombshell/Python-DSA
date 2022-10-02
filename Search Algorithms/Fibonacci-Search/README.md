<h1>Fibonacci Search</h1>

<h4>
    The Fibonacci search method, just like the Binary search method, is a comparison-based searching algorithm that is based on the divide and conquer technique. This search method works on an array that is sorted in the non-decreasing order.
</h4>
<br>
<h3> Algorithm </h3>
<hr>

<h4>
  We carry out the Fibonacci search using the following steps:

  1. To begin, we find a Fibonacci number that is greater than or equal to the size of the given array in which we have to search the key. Formally, we can say that if the size of the array is n then we must find a Fibonacci number F_{k} such that F_{k} \geq n.
   
  2. The next step is to compute F_{k-1}, F_{k-2}, the offset, and the index value. The index is computed using the offset, n, and F_{k-2}.
   
  3. Here, we compare the key with the element at index in the array. This comparison will give us one of the following three outcomes:
     1. If the key and array element at index are equal then the key is at position index in the given array. We return it and stop.
     2. If the key is less than the array element at index index, then we search the key in the left sub-tree to F_{k-2}.
     3. If the given key is greater than the array element at index, then we search the right sub-tree to F_{k-2}.
   
  4. If the key is not found, repeat step 1 to step 5 as long as F_{k-2} \geq 0 i.e., we have a Fibonacci number that is greater than the length of the array n.
</h4>
