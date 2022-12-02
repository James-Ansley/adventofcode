package y2022

import read

fun main() {
    val data = read("y2022/day01")
        .split("\n\n")
        .map { it.lines() }
        .map { pack -> pack.map { it.toInt() } }
        .map { it.sum() }
        .sortedDescending()

    println(data[0])
    println(data.take(3).sum())
}
