class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> results;
        int n = nums.size();
        for(int i = 0; i < n; i++){
            int products = 1;
            for(int j = 0; j < n; j++){
                if(j == i) continue;
                products *= nums[j];
            }

            results.push_back(products);
        }

        return results;
    }
};
