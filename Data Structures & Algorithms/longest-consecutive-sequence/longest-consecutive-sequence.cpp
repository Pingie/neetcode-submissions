class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());

        int longest = 0;
        for(auto x: numSet){
            if(numSet.find(x - 1) == numSet.end()){
                int current = x;
                int streak = 1;

                while(numSet.find(current + 1) != numSet.end()){
                    streak++;
                    current++;
                }

                longest = max(longest, streak);
            }
        }
        return longest;
    }
};
