class Solution {
public:
    bool isPalindrome(string s) {
        string res = "";
        for(int i = 0; i < s.size(); i++){
            if(isdigit(s[i]) || isalpha(s[i])) res += tolower(s[i]);
        }
        
        string tmp = res;
        reverse(tmp.begin(), tmp.end());

        return tmp == res;
    }
};
