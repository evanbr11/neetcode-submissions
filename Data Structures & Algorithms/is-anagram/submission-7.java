class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        Map<Character, Integer> map = new HashMap<>(26);
        for (char ch = 'a'; ch <= 'z'; ch++) {
            map.put(ch, 0);
        }

        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), map.get(s.charAt(i)) + 1);
            map.put(t.charAt(i), map.get(t.charAt(i)) - 1);
        }
        if (map.values().stream().allMatch(n -> n == 0)) {
            return true;
        }
        return false;
    }
}
