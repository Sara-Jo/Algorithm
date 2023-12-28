/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    let totalTank = 0
    let currentTank = 0
    let start = 0

    for (let i = 0; i < gas.length; i++) {
        const netCost = gas[i] - cost[i] 
        totalTank += netCost 
        currentTank += netCost
        if (currentTank < 0) {
            start = i + 1
            currentTank = 0
        }
    }
    return totalTank < 0 ? -1 : start
};
