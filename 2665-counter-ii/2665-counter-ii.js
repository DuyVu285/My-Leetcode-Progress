/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let numVal = init;
    return {
        increment: () => {
            numVal = numVal + 1;
            return numVal;
        },
        reset: () => {
            numVal = init;
            return numVal;
        },
        decrement: () => {
            numVal = numVal - 1;
            return numVal;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */