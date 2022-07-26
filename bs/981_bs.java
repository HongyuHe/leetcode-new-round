/**
    Really good problem!!! Main takeaways:
        
        1. Read the question F*NG carefully ok?!
        2. binary search on floor key:
            a. stop condition: size == 2 -> check;
            b. including mid in one side;
        3. TreeMap.floorKey();
        4. index = binarSearch(...); if index < 0: insert(key, -index-1);
    
    
    2h 30m
*/


class TimeMap {

    /** Initialize your data structure here. */
    private Map<String, TreeMap<Integer, String>> timeDb; // <key, <timestamp, value>>
    // private Map<String, LinkedList<Object[]>> timeDb; // <key, <timestamp, value>>
    
    public TimeMap() {
        timeDb  = new HashMap<>();
        // isUpdated = false;
    }
    
    public void set(String key, String value, int timeStamp) {
        timeDb.putIfAbsent(key, new TreeMap<Integer, String>( (kv1, kv2) -> kv1 - kv2 ));
        TreeMap<Integer, String> tMap = timeDb.get(key);
        tMap.putIfAbsent(timeStamp, value);
        // isUpdated = true;
        // timeDb.putIfAbsent(key, new LinkedList<Object[]>());
        // LinkedList<Object[]> items = timeDb.get(key);
        // items.add(new Object[] {timeStamp, value});
    }
    
    public String get(String key, int timeStamp) {
        if (key == null) return null;
        
        TreeMap<Integer, String> tMap = timeDb.getOrDefault(key, null);
        if (tMap == null) return null;
        // Map.Entry<Integer, String> lastItem = tMap.lastEntry();
        // if (timeStamp < lastItem.getKey()) return "";
        Integer k = tMap.floorKey(timeStamp);
        if (k == null) return "";
        else return tMap.get(k);
        
//         List<Object[]> items = timeDb.getOrDefault(key, null);
//         if (items == null) return null;
        
//         if (items.size() == 1) 
//             return ((int)items.get(0)[0] <= timeStamp)? (String)items.get(0)[1] : "";

        // "The timestamps for all TimeMap.set operations are strictly increasing." => no need to sort!!!
        // if (isUpdated) { 
        //     Collections.sort(items, (i1, i2) -> (int)i1[0] - (int)i2[0]);
        //     isUpdated = false;
        // }
        
        // String res = binarySearch(items, timeStamp, 0, items.size()-1);
        // int maxIndex = -1;
        // String res = "";
        //  for (Object[] item : items) {
        //      if ((int)item[0] <= timeStamp && (int)item[0] > maxIndex) {
        //          maxIndex = (int)item[0];
        //          res = (String)item[1];
        //      }
        //  }
        // int res = Collections.binarySearch(items, timeStamp, (o1, o2) -> (int)o1[0] - (int)o2[0]);
        // if (res >= 0)
        //     return (String)items.get(res)[1];
        // else if (res == -1)
        //     return "";
        // else
        //     return (String)items.get(-res-1)[1];
    }
    
    // [1,2,3,4,5,7,8,9] 6 10 0
//      [10, 20] 30
    private String binarySearch(List<Object[]> items, int timeStamp, int start, int end) {
        // System.out.println("Search "+timeStamp+" In " + start +" "+end);

        // if (start > end || start < 0 || end >= items.size()) return "";
        
        if (end == start || end - start == 1) {
            if (timeStamp >= (int)items.get(end)[0]) {
                return (String)items.get(end)[1];
            } else if (timeStamp >= (int)items.get(start)[0]) {
                return (String)items.get(start)[1];
            } else {
                return "";
            }
        }
        
        // if (start == end) {
        //     if ((int)items.get(start)[0] <= timeStamp) {
        //         return (String)items.get(start)[1];
        //     } else {
        //         return "";
        //     }
        // }
        
        int mid = (start + end) / 2;
        if ((int)items.get(mid)[0] < timeStamp)
            return binarySearch(items, timeStamp, mid, end); // in this case, we must take `mid` into accout as well
        else if ((int)items.get(mid)[0] > timeStamp)
            return binarySearch(items, timeStamp, start, mid-1);
        else
            return (String)items.get(mid)[1];
    }
    
}
// [2, 10, 14, 20] 15

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */