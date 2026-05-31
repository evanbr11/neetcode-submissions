class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> distinct = new HashSet<>(
            Arrays.stream(nums).boxed().collect(Collectors.toList()));
        System.out.print(distinct);
        return !(distinct.size() == nums.length);
    }
}