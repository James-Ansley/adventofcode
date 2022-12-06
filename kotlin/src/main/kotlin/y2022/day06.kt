package y2022

import read

fun main() {
    val data = read("y2022/day06")
    val fours = data.windowed(4).map { it.toSet() }
    val fourteens = data.windowed(14).map { it.toSet() }

    println(fours.indexOfFirst { it.size == 4 } + 4)
    println(fourteens.indexOfFirst { it.size == 14 } + 14)
}
