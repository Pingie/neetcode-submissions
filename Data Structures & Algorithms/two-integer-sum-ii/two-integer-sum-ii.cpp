class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;  
       
        while ( left < right ) {
            int validSum = numbers[ left ] + numbers[ right ]; 

            if ( target == validSum ) {
                return { left + 1 , right + 1 };
            }

            if ( target < validSum ) {
                right--;
            }
            else if ( target > validSum ) {
                left++;
            }
        }
        
        return {};
    }
};
