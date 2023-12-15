// function g(n) {
//     let result = []
//     for(let i = 1; i<=n; i++){
//         result.push(i)
//     }
//     return result
// }
// console.log(g(4))

// const myObject = {
//     1:12,
//     2:12,
//     3:11,4:17,
//     5:11,6:3
// }
// // 객체의 키 배열을 가져옴
// const keys = Object.keys(myObject);

// // 키 배열을 값에 따라 오름차순으로 정렬
// const sortedKeys = keys
// .sort((a, b) => myObject[a] - myObject[b])
// .map(x => Number(x));

// console.log(sortedKeys); // 정렬된 키 배열 출력

const grid = [[1,2,2,2],[1,2,1,1],[1,2,2,1],[3,2,1,1]]
console.log(grid.slice(0,3).map(x => x.slice(0,3)))

const one = grid.reduce((acc, row)=> acc.concat(row))
console.log(new Set(one))
for(let s of new Set(one)){
    console.log(s)
}