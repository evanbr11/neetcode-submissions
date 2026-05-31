class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> distinct = new HashSet<>();
        for (int n : nums) {
            if(!distinct.add(n)) return true;
        }
        return false;
    }
}