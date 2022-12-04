package y2022

import read
import kotlin.math.max
import kotlin.math.min

fun main() {
    val re = "(\\d+)-(\\d+),(\\d+)-(\\d+)".toRegex()
    val data = read("y2022/day04")
    val matches = re.findAll(data)
        .map { it.groupValues.drop(1) }
        .map { it.map { e -> e.toInt() } }

    val contained = matches.count { (a, b, c, d) -> a <= c && d <= b || c <= a && b <= d }
    val overlap = matches.count { (a, b, c, d) -> max(a, c) <= min(b, d) }

    println(contained)
    println(overlap)
}
