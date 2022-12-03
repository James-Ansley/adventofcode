package y2022

import readLines

fun main() {
    val data = readLines("y2022/day03")
    val letters = ('a'..'z') + ('A'..'Z')

    val compartments = data
        .map { line -> line.chunked(line.length / 2) }
        .map { compartments -> compartments.map { it.toSet() } }
        .map { (c1, c2) -> (c1 intersect c2).first() }
        .sumOf { letters.indexOf(it) + 1 }

    val groups = data
        .chunked(3)
        .map { group -> group.map { it.toSet() } }
        .map { (g1, g2, g3) -> (g1 intersect g2 intersect g3).first() }
        .sumOf { letters.indexOf(it) + 1 }

    println(compartments)
    println(groups)
}
