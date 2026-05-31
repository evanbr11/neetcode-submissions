class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> distinct = new HashSet<>(
            Arrays.stream(nums).boxed().collect(Collectors.toList()));
        for (int n : nums) {
            if(!distinct.remove(n)) return true;
        }
        return false;
    }
}