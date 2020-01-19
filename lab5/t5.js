const m1 = [1, 3, 5];
const m2 = [43, 23, 65, 32];

let func = (arr, ...arrs) =>
    arr.map(
        (val, i) =>
            arrs.reduce(
                (a, arr) => [...a, arr[i]],
                [val]
        )
)

console.log(func(m1.sort(), m2.sort().reverse()));
