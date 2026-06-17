class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        Map<Character, Long> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if (!map.containsKey(currentChar)) {
                map.put(currentChar, s.chars().filter(c -> c == currentChar).count());
            }
        }

        for (int i = 0; i < t.length(); i++) {
            char currentChar = t.charAt(i);
            if (!map.containsKey(currentChar)) {
                return false;
            }
            if (
                map.get(currentChar) != 
                t.chars().filter(c -> c == currentChar).count()
                ) {
                    return false;
                }
        }
        return true;
    }
}
