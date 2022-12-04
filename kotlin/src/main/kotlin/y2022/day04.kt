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
        .map { (a, b, c, d) -> a..b to c..d }

    val contained = matches
        .count { (e1, e2) -> e1.all { e2.contains(it) } || e2.all { e1.contains(it) } }

    val overlap = matches
        .count { (e1, e2) -> max(e1.first, e2.first) <= min(e1.last, e2.last) }

    println(contained)
    println(overlap)
}
