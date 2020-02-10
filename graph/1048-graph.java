
/*
    take away:
    - dp
    - stringbuilder efficient string manipulation;

    1. sort by length
    2. bottom up from len == 2
    3. try to delete each char from this word and match with previous len-words
*/

class Solution {
    public int longestStrChain(String[] words) {
        if (words.length == 1)
            return 1;

        Arrays.sort(words, (w1, w2) -> w1.length() - w2.length());

        Map<String, Integer> dp = new HashMap<>();
        int longest = 1;
        for (String word : words) {
            int maxChainLen = 1;
            if (word.length() == 1) {
                dp.put(word, maxChainLen);
                continue;
            }

            StringBuilder wordStr = new StringBuilder(word);
            for (int i = 0; i < word.length(); i++) {
                char c = wordStr.charAt(i);

                wordStr.deleteCharAt(i);
                String predecessor = wordStr.toString();

                maxChainLen = Math.max(maxChainLen, dp.getOrDefault(predecessor, 0) + 1);
                wordStr.insert(i, c);
            }
            dp.put(word, maxChainLen);
            longest = Math.max(longest, maxChainLen);
        }
        return longest;
    }
}