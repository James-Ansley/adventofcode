package y2022

import read
import transpose

fun main() {
    val (crateData, moveData) = read("y2022/day05").split("\n\n")

    val width = crateData.lines().maxOf { it.length }
    val crates = crateData.lines()
        .dropLast(1)
        .reversed()
        .map { it.padEnd(width, ' ') }
        .map { it.slice(1 until it.length step 4) }
        .map { it.toList() }
        .transpose()
        .map { it.filter { char -> !char.isWhitespace() } }

    val moveRegex = "move (\\d+) from (\\d+) to (\\d+)".toRegex()
    val moves = moveRegex.findAll(moveData)
        .map { it.groupValues.drop(1) }
        .map { vals -> vals.map { it.toInt() } }
        .map { (amt, from, to) -> Triple(amt, from - 1, to - 1) }

    val crateMover9000 = crates.map { it.toMutableList() }.toMutableList()
    val crateMover9001 = crates.map { it.toMutableList() }.toMutableList()

    for ((amt, from, to) in moves) {
        val toMoveSingle = crateMover9000[from].takeLast(amt).reversed()
        crateMover9000[to].addAll(toMoveSingle)
        crateMover9000[from] = crateMover9000[from].dropLast(amt).toMutableList()

        val toMoveMany = crateMover9001[from].takeLast(amt)
        crateMover9001[to].addAll(toMoveMany)
        crateMover9001[from] = crateMover9001[from].dropLast(amt).toMutableList()
    }

    println(crateMover9000.map { it.last() }.joinToString(""))
    println(crateMover9001.map { it.last() }.joinToString(""))
}