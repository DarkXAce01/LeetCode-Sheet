// class Solution {
// public:
//     int search(vector<int>& nums, int target) {
//         int ans;
//         int len = nums.size();
//         int beg = 0;
//         int end = len-1;
//         while(beg<=end){
//             int mid = beg + (end - beg)/2;
//             if(nums[mid] == target){
//                 ans = mid;
//             }
//             else if(nums[mid]>target){
//                 end = mid-1;
//             }
//             else if(nums[mid]<target){
//                 beg = mid+1;
//             }
//             else{
//                 ans = -1;
//             }
//         }
//         return ans;
//     }
// };
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low=0;
        int high=nums.size()-1;
        while(low<=high){
            int mid = low+(high-low)/2;
            if(nums[mid]==target){
                return mid;
            }
            else if(nums[mid]<target){
                low = mid+1;
            }
            else{
                high = mid-1;
            }
        }
        return -1;
    }
};