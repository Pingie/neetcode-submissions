#define ii pair<int, int>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
       unordered_map<int, int> mp;
       for(auto x: nums){
        mp[x]++;
       } 
       priority_queue<ii> q;
       for(auto it: mp){
        q.push({it.second, it.first});
       }
       vector<int> results;
       while(k){
        ii top = q.top(); q.pop();
        results.push_back(top.second);
        k--;
       }
       return results;
    }
};
