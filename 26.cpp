#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int removeDuplicates(vector<int>& nums) {
    int k = 0;
    unordered_set<int> visitedValues;
    
    for (int i = 0; i < nums.size(); ++i) {
        if (visitedValues.find(nums[i]) == visitedValues.end()) {
            visitedValues.insert(nums[i]);
            nums[k] = nums[i];
            ++k;
        }
    }
    return k;
}

int main() {
    vector<int> nums = {1, 1, 2};
    int k = removeDuplicates(nums);
    
    cout << k << endl;
    for (int i = 0; i < k; ++i) {
        cout << nums[i] << " " << endl;
    }
    cout << endl;
    
    return 0;
}