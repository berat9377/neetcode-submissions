class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> non_duplicate_set;
        for (int num : nums) {
            if (!non_duplicate_set.insert(num).second){
                return true;
            }
        }
        return false;
    }
};