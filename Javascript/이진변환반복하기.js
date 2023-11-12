function binary(n) {
    let answer = ''
    if (n < 2) return String(n)
    while(true) {
        remain = n % 2
        value = (n-remain) / 2
        answer = String(remain) + answer
        if (value === 1 || value === 0) {
            answer = String(value) + answer
            break
        }
        n = value
    }
    return answer
} 

function solution(s) {
    let count = 0
    let times = 0
    while(true) {
        times++;
        const str_l = [...s]
        const str_l_new = str_l.filter(x => x !== "0")
        count += str_l.length - str_l_new.length

        s = binary(str_l_new.length)
        // s = str_l_new.length.toString(2)
        if(s === "1") break
    }
    return [times, count]
}
