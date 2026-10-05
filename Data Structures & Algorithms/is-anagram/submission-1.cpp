class Solution {
public:
    bool isAnagram(string s, string t) {
    if (s.length() != t.length()) return false;

      std::unordered_map<char, int> char_index;
      
      for (char& c : s) {
        char_index[c]++;
      }

      for (char& c : t) {
        if (char_index[c] == 0) {
          return false;  
        }
          char_index[c] -= 1;

      }
      return true;
    }
};
