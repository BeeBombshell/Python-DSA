"""
Quick sort is a divide and conquer algorithm
Steps:
1. We first select an element randomly which we call pivot element. We can choose any element as pivot element.
   But for consistency and performce purposes we select middle element of array as the pivot element.
2. Then we move all the elments lower than pivot to the left and higher than pivot to the right to the pivot
3. Then we recursively apply the above 2 steps seperately to each of the sub-arrays of 
   element smaller and larger than last pivot
3. Then we recursively apply the above 2 steps seperately to each of the sub-arrays of 
   element smaller and larger than last pivot
   
   
"""


		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int st=1;int sp=n/2;
		for(int i=1;i<=n;i++) {
			for(int j=1;j<=sp;j++) {
				if(i==n/2+1) {
					System.out.print("* ");
				}
				else {
					System.out.print("  ");
				}
			}
			for(int j=1;j<=st;j++) {
				System.out.print("* ");
			}
			if(i<=n/2) {
				st++;
			}
			else {
				st--;
			}
			System.out.println();
		}
		
	}

