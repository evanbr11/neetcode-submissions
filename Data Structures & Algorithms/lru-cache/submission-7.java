class LRUCache {
    private final int capacity;
    private Map<Integer, Integer> cache;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new LinkedHashMap<>(this.capacity, 0.75f, true) {
            @Override
            protected boolean removeEldestEntry(
                Map.Entry<Integer, Integer> eldest) {
                return size() > LRUCache.this.capacity;
            }
        };
    }
    
    public int get(int key) {
        return this.cache.getOrDefault(key, -1);
    }
    
    public void put(int key, int value) {
        if (this.cache.putIfAbsent(key, value) != null) {
            this.cache.replace(key, value);
        }
    }
}
