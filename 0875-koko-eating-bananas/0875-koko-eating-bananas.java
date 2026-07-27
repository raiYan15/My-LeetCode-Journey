class Solution {
    public boolean helper(int[] piles, int k,int h){
        int currentHours = 0;
        for(int i : piles){
            currentHours += (int)Math.ceil(i*1.0/k);
            if(currentHours>h){
                return false;
            }
        }
        return true;
    }

    public int minEatingSpeed(int[] piles, int h) {
        
        int max = Integer.MIN_VALUE;
        
        for(int i : piles){
            max = Math.max(i,max);
        }        

        int left = 1;
        int right = max;

        int ans = max;
        while(left<=right){
            int mid = (left+right)/2;

            if(helper(piles,mid,h)){
                ans = mid;
                right = mid-1;
            }else{
                left = mid+1;
            }
        }

        return ans;
    }
}