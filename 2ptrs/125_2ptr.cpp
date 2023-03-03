class Solution {
public:
    bool isPalindrome(string s) {
        /**
            1\ String processing;
            2\ Check palindrome with two pointers.
        */
        string str = "";
        for (int i=0; i<s.length(); i++) {
            if (iswalnum(s[i])) {
                if (isalpha(s[i]) && s[i]<='Z') {
                    s[i] = s[i] - 'A' + 'a';
                }
                str += s[i];
                // cout << str << endl;
            }
        }

        if (str.length()==0) return true;

        int high = str.length()-1;
        int low = 0;

        while (high > low) {
            if (str[high] != str[low]) 
                return false;
            --high;
            ++low;
        }

        return true;
    }
};