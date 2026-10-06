class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> num_map;
    int difference, num;

    for (int i = 0; i<nums.size();i++){
      num = nums[i];
      difference = target - num; 

      if (num_map.find(difference) != num_map.end()){
        return vector<int> {num_map[difference], i};
      }

      num_map[num] = i;
    }
    

    }
};
