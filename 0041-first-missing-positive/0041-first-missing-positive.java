class Solution {
    boolean[] map = new boolean[(int)1e5 + 1];
    public int firstMissingPositive(int[] nums) {
        for(int i : nums){
            if(i<= 0 || i>nums.length){
                continue;
            }

            map[i-1] = true;
        }


        for(int i=0;i<nums.length;i++){
            if(!map[i]){
                return i+1;
            }
        }
        return nums.length+1;
    }
}