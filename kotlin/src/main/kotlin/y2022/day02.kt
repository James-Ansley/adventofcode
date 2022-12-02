package y2022

import readLines

fun main() {
    val data = readLines("y2022/day02")
        .map { it.toCharArray() }
        .map { (p1, _, p2) -> p1 - 'A' to p2 - 'X' }

    val moves = data.map { (p1, p2) -> p1 to (p1 + p2 - 1).mod(3) }

    println(data.sumOf { it.score() })
    println(moves.sumOf { it.score() })
}

private fun Pair<Int, Int>.score(): Int {
    val (p1, p2) = this
    return if ((p1 - 1).mod(3) == p2) {
        p2 + 1
    } else if ((p2 - 1).mod(3) == p1) {
        p2 + 7
    } else {
        p2 + 4
    }
}
