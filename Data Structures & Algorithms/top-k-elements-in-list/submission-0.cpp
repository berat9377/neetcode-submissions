class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> frequency_map;

    for(int& num : nums){
      frequency_map[num]++;
    }
    
    int n = nums.size();
    vector<vector<int>> buckets(n+1);

    for (const auto& [key, value] : frequency_map){
        buckets[value].push_back(key);
    }

    vector<int> result;

    for (int i = n;i>=1 && result.size() < k;i--){
      for (int num : buckets[i]){
        result.push_back(num);
        if (result.size() == k) break;
      }
    }

    return result;
    }
};
