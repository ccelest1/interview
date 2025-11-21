function maxSubarraySum(nums) {
    if (nums.length === 0) {
        return 0;
    }

    // Initialize the variables
    let maxCurrent = nums[0];
    let maxGlobal = nums[0];

    // Iterate through the array
    for (let i = 1; i < nums.length; i++) {
        maxCurrent = Math.max(nums[i], maxCurrent + nums[i]);
        if (maxCurrent > maxGlobal) {
            maxGlobal = maxCurrent;
        }
    }

    return maxGlobal;
}
