class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        if (s.equals(t)) return true;
        
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            Integer count = map.get(s.charAt(i));
            if (Objects.isNull(count)) {
                map.put(s.charAt(i), 1);
            }
            else {
                map.put(s.charAt(i), count + 1);
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
