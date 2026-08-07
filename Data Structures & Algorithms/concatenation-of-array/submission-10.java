class Solution {
    public int[] getConcatenation(int[] nums) {
        if (nums == null || nums.length == 0) {
            return null;
        }
        int[] concat = new int[nums.length * 2];
        for (int i = 0; i < nums.length; i++) {
            concat[i] = nums[i];
            concat[i + nums.length] = nums[i];
        }
        return concat;
    }
}